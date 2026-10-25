"""First-order weak-field Shapiro time-delay benchmark.

Coordinate delay is not a physical faster-than-light pathway.
"""
from __future__ import annotations
from math import isfinite,log1p
C=299792458.0
G=6.67430e-11
SUN_MASS_KG=1.98847e30
AU_M=149597870700.0

def shapiro_delay_s(mass_kg,r1_m,r2_m,separation_m):
    if not all(isfinite(z) for z in (mass_kg,r1_m,r2_m,separation_m)) or mass_kg<0 or min(r1_m,r2_m)<=0:
        raise ValueError("finite nonnegative mass and positive radii required")
    if not (abs(r1_m-r2_m)<=separation_m<r1_m+r2_m):
        raise ValueError("invalid endpoint triangle")
    if mass_kg==0 or separation_m==0:
        return 0.
    return (2*G*mass_kg/C**3)*log1p(2*separation_m/(r1_m+r2_m-separation_m))
