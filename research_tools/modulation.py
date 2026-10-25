"""An independently runnable reference model for photon-counting modulation.

Uncoded, independent Poisson slot counts with ML slot selection and uniform
tie-breaking. Results are idealized, not a CCSDS modem, flight link, or FTL.
Research lead: Biswajit Jana. Apache-2.0.
"""
from dataclasses import dataclass
from math import comb, exp, isfinite, log2, sqrt

C = 299792458.0
LIGHT_YEAR_M = 9.4607304725808e15


def _check(value, name):
    if not isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and nonnegative")


def ppm_ser(M, signal, background):
    """Exact hard-decision M-PPM symbol-error probability (random ties).

    On slot: Poisson(signal + background). Other slots: Poisson(background).
    For a particular on-slot count k, the correct-decision probability is
    integral_0^1 (P(B<k)+t P(B=k))^(M-1) dt.
    Numerical summation is restricted to means <=200.
    """
    if type(M) is not int or M < 2 or M & (M-1):
        raise ValueError("M must be a power of two >=2")
    _check(signal, "signal")
    _check(background, "background")
    if signal+background > 200:
        raise ValueError("Poisson mean beyond validated range")
    if signal == 0:
        return 1-1/M
    if background == 0:
        return (1-1/M)*exp(-signal)
    total = signal+background
    cutoff = int(total + 15*sqrt(total+1) + 30)
    p_on = exp(-total)
    p_off = exp(-background)
    f_less = 0.
    correct = 0.
    for k in range(cutoff+1):
        conditional = sum(comb(M-1, j)*f_less**(M-1-j)*p_off**j/(j+1)
                          for j in range(M))
        correct += p_on*conditional
        if k < cutoff:
            f_less += p_off
            p_on *= total/(k+1)
            p_off *= background/(k+1)
    return max(0., min(1., 1-correct))


def symmetric_hard_information(M, ser):
    """MI bits/symbol of equiprobable M-ary symmetric hard-output channel."""
    if not 0 <= ser <= 1:
        raise ValueError("SER must lie in [0,1]")
    correct = 1-ser
    incorrect = ser/(M-1)
    return max(0., log2(M)
               + (correct*log2(correct) if correct else 0)
               + ((M-1)*incorrect*log2(incorrect) if incorrect else 0))


def _binary_entropy(p):
    return -p*log2(p)-(1-p)*log2(1-p) if 0 < p < 1 else 0.


def _poisson_cdf(k, mean):
    if k < 0:
        return 0.
    term = exp(-mean)
    total = term
    for n in range(1,k+1):
        term *= mean/n
        total += term
    return min(1., max(0., total))


@dataclass(frozen=True)
class Link:
    signal_counts_per_s: float
    noise_counts_per_s: float
    slot_s: float
    distance_m: float
    peak_to_average_limit: float = 128.

    def __post_init__(self):
        for key in ("signal_counts_per_s", "noise_counts_per_s", "slot_s",
                    "distance_m", "peak_to_average_limit"):
            _check(getattr(self, key), key)
        if min(self.slot_s, self.distance_m) == 0 or self.peak_to_average_limit < 1:
            raise ValueError("positive duration/distance and peak ratio >=1 required")


def ppm(M, link, payload_bits=8192):
    """M-PPM: fixed average signal photon-rate budget, ideal one-slot pulse.

    Signal photons/frame = rate * M * slot duration, noise/slot = noise-rate
    * slot duration. Peak/average intensity ratio is M, not free gain.
    Information rate is only the ideal symmetric *hard-decision* MI rate.
    """
    if type(payload_bits) is not int or payload_bits <= 0:
        raise ValueError("payload_bits must be positive")
    if M > link.peak_to_average_limit:
        return dict(modulation="PPM", M=M, feasible=False, peak_ratio=M)
    frame = M*link.slot_s
    s = link.signal_counts_per_s*frame
    b = link.noise_counts_per_s*link.slot_s
    error = ppm_ser(M,s,b)
    information = symmetric_hard_information(M,error)
    rate = information/frame
    t_light = link.distance_m/C
    return dict(modulation="PPM", M=M, feasible=True, peak_ratio=M,
                signal_per_symbol=s, noise_per_slot=b, ser=error,
                raw_rate_bps=log2(M)/frame, hard_mi_rate_bps=rate,
                light_time_s=t_light,
                optimistic_complete_message_s=t_light+payload_bits/rate if rate else None)


def ook(link, payload_bits=8192):
    """OOK binary, equiprobable bits; ideal threshold based on Poisson counts.

    On-slot signal mean = 2 * average signal rate * duration; off-slot mean=0.
    Threshold maximizes equiprobable-input hard-decision MI, no FEC claim.
    """
    if type(payload_bits) is not int or payload_bits <= 0:
        raise ValueError("payload_bits must be positive")
    if link.peak_to_average_limit < 2:
        return dict(modulation="OOK", feasible=False, peak_ratio=2)
    s = 2*link.signal_counts_per_s*link.slot_s
    b = link.noise_counts_per_s*link.slot_s
    if s+b > 200:
        raise ValueError("Poisson mean beyond validated range")
    best = (float("-inf"), 0, 0., 0.)
    for threshold in range(1, int(s+b+12*sqrt(s+b+1)+20)+1):
        false_alarm = 1-_poisson_cdf(threshold-1,b)
        miss = _poisson_cdf(threshold-1,s+b)
        p_out = (false_alarm+1-miss)/2
        information = (_binary_entropy(p_out)
                       -(_binary_entropy(false_alarm)+_binary_entropy(miss))/2)
        if information > best[0]:
            best = (information, threshold, false_alarm, miss)
    info, threshold, false_alarm, miss = best
    rate = max(0., info)/link.slot_s
    t_light = link.distance_m/C
    return dict(modulation="OOK", feasible=True, peak_ratio=2,
                threshold=threshold, false_alarm=false_alarm, miss=miss,
                raw_rate_bps=1/link.slot_s, hard_mi_rate_bps=rate,
                light_time_s=t_light,
                optimistic_complete_message_s=t_light+payload_bits/rate if rate else None)


def trade_study(link, orders=(2,4,8,16,32,64,128)):
    return [ppm(M,link) for M in orders]+[ook(link)]


if __name__ == "__main__":
    import json
    cases = {
       "photon_starved": Link(200.,20.,0.002,4.24*LIGHT_YEAR_M),
       "brighter_link": Link(2000.,100.,0.0005,4.24*LIGHT_YEAR_M)
    }
    print(json.dumps({n:trade_study(c) for n,c in cases.items()}, indent=2))
