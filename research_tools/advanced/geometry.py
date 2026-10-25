"""Flat inertial moving-receiver light-time and ideal diffraction-limited photon budget.

Reference model only: no epoch-frozen astrometry, turbulence, laser pointing,
acquisition losses or non-Poisson detector effects.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite,pi,sqrt,acos
import numpy as np
from scipy.special import j0,j1

C=299792458.0
H=6.62607015e-34
LY=9.4607304725808e15

def moving_light_time(r0_m,receiver_velocity_m_s):
    """Positive root of |r0 + vt| = ct for inertial constant v."""
    r=np.asarray(r0_m,dtype=float)
    v=np.asarray(receiver_velocity_m_s,dtype=float)
    if r.shape!=(3,) or v.shape!=(3,) or not (np.isfinite(r).all() and np.isfinite(v).all()):
        raise ValueError("finite three-dimensional vectors required")
    rr=float(np.dot(r,r))
    vv=float(np.dot(v,v))
    if vv>=C*C:
        raise ValueError("receiver velocity must be subluminal")
    if rr==0:
        return 0.
    rv=float(np.dot(r,v))
    return (rv+sqrt(rv*rv+(C*C-vv)*rr))/(C*C-vv)

def point_ahead_angle_rad(r0_m,receiver_velocity_m_s):
    r=np.asarray(r0_m,dtype=float)
    if r.shape!=(3,) or not np.isfinite(r).all() or np.linalg.norm(r)==0:
        raise ValueError("nonzero finite three-dimensional vector required")
    t=moving_light_time(r,receiver_velocity_m_s)
    target=r+np.asarray(receiver_velocity_m_s,dtype=float)*t
    co=float(np.clip(np.dot(r,target)/(np.linalg.norm(r)*np.linalg.norm(target)),-1,1))
    return float(acos(co))

@dataclass(frozen=True)
class OpticalLink:
    distance_m:float
    wavelength_m:float
    transmit_aperture_m:float
    receive_aperture_m:float
    average_optical_power_w:float
    throughput:float=0.2

    def validate(self):
        vals=(self.distance_m,self.wavelength_m,self.transmit_aperture_m,
              self.receive_aperture_m,self.average_optical_power_w,self.throughput)
        if not all(isfinite(v) for v in vals) or min(vals[:4])<=0 or vals[4]<0 or not 0<=vals[5]<=1:
            raise ValueError("invalid optical link parameters")

    def airy_encircled_fraction(self):
        """Unobscured on-axis circular Airy pattern, no pointing error."""
        self.validate()
        x=pi*self.transmit_aperture_m*self.receive_aperture_m/(2*self.wavelength_m*self.distance_m)
        if x<1e-2:
            return float(x*x/4-x**4/32+5*x**6/2304)
        return float(max(0,min(1,1-j0(x)**2-j1(x)**2)))

    def received_photons_per_s(self):
        self.validate()
        source_rate=self.average_optical_power_w*self.wavelength_m/(H*C)
        return source_rate*self.airy_encircled_fraction()*self.throughput
