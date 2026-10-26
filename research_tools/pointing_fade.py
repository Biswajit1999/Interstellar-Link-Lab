"""Ideal Gaussian optical link with packet-correlated pointing fades.

Separate from the circular-pupil Airy link: Gaussian 1/e^2 intensity waist w0,
isotropic 2-D Gaussian angular jitter per axis sigma, and receiver disk radius
a << beam radius. Jitter remains fixed during each uncoded packet.
No source obscuration, background, atmosphere, pointing bias, timing error,
FEC, detector memory, hardware or superluminal transport.
Research lead: Biswajit Jana.
"""
from dataclasses import dataclass
from math import pi, sqrt, exp, expm1, log2, isfinite
from random import Random

C = 299792458.
H = 6.62607015e-34
LY = 9.4607304725808e15

def _positive(x, name):
    if not isfinite(x) or x <= 0:
        raise ValueError(name + " must be finite and positive")

@dataclass(frozen=True)
class GaussianOpticalTerminal:
    distance_m: float = 4.24*LY
    wavelength_m: float = 1064e-9
    tx_waist_radius_m: float = 0.5
    rx_aperture_radius_m: float = 5.
    transmit_average_power_w: float = 10.
    end_to_end_efficiency: float = .2
    pointing_sigma_axis_rad: float = 0.

    def validate(self):
        for name in ("distance_m", "wavelength_m", "tx_waist_radius_m",
                     "rx_aperture_radius_m", "transmit_average_power_w"):
            _positive(getattr(self,name), name)
        if not isfinite(self.end_to_end_efficiency) or not 0 <= self.end_to_end_efficiency <= 1:
            raise ValueError("efficiency not in [0,1]")
        if not isfinite(self.pointing_sigma_axis_rad) or self.pointing_sigma_axis_rad < 0:
            raise ValueError("invalid pointing jitter")
        if self.rx_aperture_radius_m/self.beam_radius_m() >= .01:
            raise ValueError("requires receiver radius <1% Gaussian beam radius")
        return self

    def beam_radius_m(self):
        _positive(self.distance_m,"distance")
        _positive(self.wavelength_m,"wavelength")
        _positive(self.tx_waist_radius_m,"waist")
        zR=pi*self.tx_waist_radius_m**2/self.wavelength_m
        return self.tx_waist_radius_m*sqrt(1+(self.distance_m/zR)**2)

    def divergence_rad_farfield(self):
        return self.wavelength_m/(pi*self.tx_waist_radius_m)

    def mean_fade_gain(self):
        self.validate()
        r=self.distance_m*self.pointing_sigma_axis_rad/self.beam_radius_m()
        return 1/(1+4*r*r)

    def mean_capture_exact_gaussian(self):
        """Exact centered receiver *mean* over zero-mean Gaussian pointing."""
        self.validate()
        r2=self.beam_radius_m()**2+4*(self.distance_m*self.pointing_sigma_axis_rad)**2
        a=self.rx_aperture_radius_m
        return -expm1(-2*a*a/r2)

    def on_axis_capture_small(self):
        self.validate()
        return 2*(self.rx_aperture_radius_m/self.beam_radius_m())**2

    def photons_on_axis_per_s(self):
        self.validate()
        emitted=self.transmit_average_power_w*self.wavelength_m/(H*C)
        return emitted*self.on_axis_capture_small()*self.end_to_end_efficiency

    def photons_mean_per_s(self):
        self.validate()
        emitted=self.transmit_average_power_w*self.wavelength_m/(H*C)
        return emitted*self.mean_capture_exact_gaussian()*self.end_to_end_efficiency

    def gain_shape(self):
        """G=U**(1/k), U~Uniform(0,1); k=w(z)^2/[4(R sigma)^2]."""
        self.validate()
        if self.pointing_sigma_axis_rad==0:
            return float("inf")
        return (self.beam_radius_m()/(2*self.distance_m*self.pointing_sigma_axis_rad))**2

    def draw_gain(self,rng):
        k=self.gain_shape()
        return 1. if k==float("inf") else rng.random()**(1/k)

    def outage(self,threshold):
        if not isfinite(threshold) or not 0 < threshold < 1:
            raise ValueError("threshold must be strictly between zero and one")
        k=self.gain_shape()
        return 0. if k==float("inf") else threshold**k


def zero_background_ppm_ser(M, signal):
    if type(M) is not int or M<2 or M&(M-1):
        raise ValueError("M power of two >=2 required")
    if not isfinite(signal) or signal<0:
        raise ValueError("nonnegative finite signal")
    return (1-1/M)*exp(-signal)


def uncoded_packet_success(M, signal, symbols):
    if type(symbols) is not int or symbols<1:
        raise ValueError("symbols must be positive")
    return (1-zero_background_ppm_ser(M,signal))**symbols


def correlated_packet_success(M,on_axis_signal,symbols,terminal,steps=4096):
    """Simpson quadrature over ONE random pointing gain shared by whole packet."""
    if type(steps) is not int or steps<64 or steps%2:
        raise ValueError("steps must be even and >=64")
    k=terminal.gain_shape()
    if k==float("inf"):
        return uncoded_packet_success(M,on_axis_signal,symbols)
    def f(u):
        return uncoded_packet_success(M,on_axis_signal*u**(1/k),symbols)
    summ=f(0)+f(1)
    for i in range(1,steps):
        summ+=(4 if i%2 else 2)*f(i/steps)
    return summ/(3*steps)


def monte_carlo_correlated_packet(M,symbol_signal,symbols,terminal,n=10000,seed=20261026):
    """Conditional-success Monte Carlo; not sampled detector time tags."""
    if type(n) is not int or n<2:
        raise ValueError("n must be >=2")
    rng=Random(seed)
    p=[uncoded_packet_success(M,symbol_signal*terminal.draw_gain(rng),symbols)
       for _ in range(n)]
    mean=sum(p)/n
    var=sum((v-mean)**2 for v in p)/(n-1)
    return {"expected_success":mean,"standard_error":sqrt(var/n),"trials":n,"seed":seed}


def zero_background_soft_information(M,signal):
    """Ideal full-count Shannon MI, bits/PPM symbol; NOT observed goodput."""
    zero_background_ppm_ser(M,signal)
    return -expm1(-signal)*log2(M)


def study():
    from dataclasses import replace
    ref=GaussianOpticalTerminal()
    rows=[]
    for sigma in (0.,.1,.25,.5,1.,2.):
        t=replace(ref,pointing_sigma_axis_rad=sigma*1e-6)
        # 100s per raw symbol and 16 uncoded symbols: deliberately exaggerated
        # toy timing for isolating a packet-correlated pointing fade.
        s=t.photons_on_axis_per_s()*100
        rows.append({
            "sigma_microrad_per_axis":sigma,
            "divergence_microrad":t.divergence_rad_farfield()*1e6,
            "mean_photons_s":t.photons_mean_per_s(),
            "mean_fade_gain":t.mean_fade_gain(),
            "outage_gain_lt_half":t.outage(.5),
            "packet_success_correlated":correlated_packet_success(8,s,16,t),
            "packet_success_mean_power_shortcut":uncoded_packet_success(8,s*t.mean_fade_gain(),16)
        })
    return {"model":"packet-correlated jitter of ideal Gaussian optical beam",
            "conditions":"8PPM; zero background; no FEC; perfect synchronization; 100 seconds/symbol",
            "parameters":ref.__dict__, "rows":rows,
            "claim":"simulation only, no operational or superluminal link"}

if __name__=="__main__":
    import json
    print(json.dumps(study(),indent=2))
