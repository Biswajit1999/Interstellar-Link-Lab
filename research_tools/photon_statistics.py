"""Photon-starved M-PPM laboratory with explicit pointing jitter and backgrounds.

Toy independent Poisson slot-counter receiver and uniform random tie-breaking.
Far-field *Gaussian-equivalent* pointing model, not physical Airy jitter integral.
No atmospheric turbulence, stellar spectral irradiance, coding or flight hardware.
Research lead: Biswajit Jana.
"""
from dataclasses import dataclass,asdict
from math import exp, isfinite, pi, sqrt
from random import Random

def poisson(mean,rng):
    if not isfinite(mean) or mean<0 or mean>25:
        raise ValueError("Poisson means must lie in [0,25] in this exact Knuth sampler")
    limit=exp(-mean); prod=1.0; k=0
    while True:
        k+=1; prod*=rng.random()
        if prod<=limit:
            return k-1

def wilson_interval(success,n,z=1.959963984540054):
    if n<=0 or not 0<=success<=n: raise ValueError("invalid trial counts")
    p=success/n; z2=z*z; d=1+z2/n
    center=(p+z2/(2*n))/d
    half=z*sqrt((p*(1-p)+z2/(4*n))/n)/d
    return (max(0,center-half),min(1,center+half))

@dataclass(frozen=True)
class PPMCase:
    order: int = 8
    signal_photons_pulse: float = 2.
    background_photons_slot: float = .08
    pointing_sigma_rad: float = 0.
    transmitter_aperture_m: float = 1.
    wavelength_m: float = 1064e-9
    def __post_init__(self):
        if type(self.order) is not int or self.order<2 or self.order&(self.order-1):
            raise ValueError("M must be a power of two >=2")
        vals=(self.signal_photons_pulse,self.background_photons_slot,
            self.pointing_sigma_rad,self.transmitter_aperture_m,self.wavelength_m)
        if any(not isfinite(x) for x in vals) or min(vals)<0:
            raise ValueError("nonnegative finite inputs required")
        if self.transmitter_aperture_m<=0 or self.wavelength_m<=0:
            raise ValueError("positive wavelength and aperture")
        if self.signal_photons_pulse+self.background_photons_slot>25 or self.background_photons_slot>25:
            raise ValueError("Poisson mean beyond exact sampler validation")
    @property
    def gaussian_angular_radius(self):
        """Approximate 1/e^2 Gaussian far-field intensity angular radius."""
        return 2*self.wavelength_m/(pi*self.transmitter_aperture_m)

def simulate(case=PPMCase(),symbols=2000,seed=17):
    if type(symbols) is not int or symbols<1:
        raise ValueError("positive integer symbols required")
    rng=Random(seed); errors=0; received_signal_sum=0; photons=0; zero_count=0
    for _ in range(symbols):
        sent=rng.randrange(case.order)
        dx=rng.gauss(0,case.pointing_sigma_rad)
        dy=rng.gauss(0,case.pointing_sigma_rad)
        j2=(dx*dx+dy*dy)/(case.gaussian_angular_radius**2)
        s=case.signal_photons_pulse*exp(-2*j2)
        received_signal_sum+=s
        counts=[poisson(case.background_photons_slot+(s if i==sent else 0),rng)
                for i in range(case.order)]
        max_count=max(counts)
        ties=[i for i,v in enumerate(counts) if v==max_count]
        chosen=ties[rng.randrange(len(ties))]
        errors+=chosen!=sent
        photons+=sum(counts)
        zero_count+=max_count==0
    p=errors/symbols
    return {"input":asdict(case),"seed":seed,"symbols":symbols,
        "symbol_errors":errors,"ser":p,
        "ser_wilson_95":wilson_interval(errors,symbols),
        "avg_signal_mean_after_pointing":received_signal_sum/symbols,
        "avg_total_counts_per_symbol":photons/symbols,
        "empty_slot_groups":zero_count,
        "scope":"Uncoded hard-decision synthetic Poisson model; no demonstrated FTL"}

def ideal_no_background_ser(M,signal):
    if type(M) is not int or M<2 or M&(M-1): raise ValueError("power-of-two order")
    if not isfinite(signal) or signal<0:raise ValueError("signal")
    return (1-1/M)*exp(-signal)

if __name__=="__main__":
    import json
    from dataclasses import replace
    case=PPMCase()
    print(json.dumps({"no_jitter":simulate(case),
                      "with_pointing_jitter":simulate(replace(case,pointing_sigma_rad=2e-7)),
                      "ideal_background_free_SER":ideal_no_background_ser(8,2)},indent=2))
