"""Two-axis active-optics beam-steering control experiment.

A Gauss-Markov pointing disturbance is sensed with noise. A PI controller
requests a fast-steering-mirror angle with finite bandwidth and saturation.
Recorded rms residual and a Gaussian-equivalent optical overlap fraction
are compared with open-loop pointing using the *same* disturbances.

This is a dimensioned control baseline, not a real FSM/CCD transfer function,
an Airy diffraction calculation, or a spacecraft pointing demonstration.
Research lead: Biswajit Jana.
"""
from dataclasses import dataclass,asdict
from random import Random
from math import exp, hypot, isfinite, sqrt, pi
import json

@dataclass(frozen=True)
class Control:
    dt_s: float = .005
    actuator_tau_s: float = .035
    disturbance_memory: float = .995
    disturbance_drive_sigma_rad: float = 9e-8
    measurement_sigma_rad: float = 2e-8
    kp: float = 1.1
    ki_per_s: float = 7.0
    stroke_rad: float = 6e-6
    wavelength_m: float = 1064e-9
    transmit_aperture_m: float = 1.0
    steps: int = 12000
    warmup_steps: int = 2000

    def __post_init__(self):
        for k,v in asdict(self).items():
            if k in ("steps","warmup_steps"): continue
            if not isfinite(v) or v<0:
                raise ValueError(f"{k}: finite nonnegative required")
        if not (self.dt_s>0 and self.actuator_tau_s>0 and
                0<=self.disturbance_memory<1 and self.stroke_rad>0 and
                self.transmit_aperture_m>0 and self.wavelength_m>0 and
                type(self.steps) is int and self.steps>=100 and
                type(self.warmup_steps) is int and 0<=self.warmup_steps<self.steps):
            raise ValueError("invalid controller or sample count")

def clamp(v,limit):
    return max(-limit,min(limit,v))

def run(cfg=Control(),seed=17):
    """No command feedforward: both loops reject identical random disturbances."""
    rng=Random(seed)
    alpha=1-exp(-cfg.dt_s/cfg.actuator_tau_s)
    axes=[{"dist":0.0,"act":0.0,"integral":0.0} for _ in range(2)]
    sum_open=sum_closed=0.0
    cap_open=cap_closed=0.0
    n=cfg.steps-cfg.warmup_steps
    angular_radius=2*cfg.wavelength_m/(pi*cfg.transmit_aperture_m)
    for step in range(cfg.steps):
        open_squared=closed_squared=0.0
        for ax in axes:
            ax["dist"]=cfg.disturbance_memory*ax["dist"]+rng.gauss(
                0,cfg.disturbance_drive_sigma_rad)
            residual=ax["dist"]-ax["act"]
            measure=residual+rng.gauss(0,cfg.measurement_sigma_rad)
            if cfg.ki_per_s:
                ax["integral"]=clamp(ax["integral"]+cfg.dt_s*measure,
                                      cfg.stroke_rad/cfg.ki_per_s)
            command=clamp(cfg.kp*measure+cfg.ki_per_s*ax["integral"],
                          cfg.stroke_rad)
            ax["act"]+=alpha*(command-ax["act"])
            open_squared+=ax["dist"]**2
            closed_squared+=(ax["dist"]-ax["act"])**2
        if step>=cfg.warmup_steps:
            sum_open+=open_squared;sum_closed+=closed_squared
            cap_open+=exp(-2*open_squared/angular_radius**2)
            cap_closed+=exp(-2*closed_squared/angular_radius**2)
    return {
        "input":asdict(cfg),"seed":seed,"samples":n,
        "open_rms_rad":sqrt(sum_open/(2*n)),
        "closed_rms_rad":sqrt(sum_closed/(2*n)),
        "rms_reduction_fraction":1-sqrt(sum_closed/max(1e-99,sum_open)),
        "avg_open_gaussian_overlap":cap_open/n,
        "avg_closed_gaussian_overlap":cap_closed/n,
        "angle_model":"Gaussian-equivalent optical intensity; not Airy.",
        "status":"Seeded 2-axis simulation, no optical hardware validation."
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
