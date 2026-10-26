"""Moving-endpoint special-relativistic light-time, in one inertial frame.

Worldlines: x_E(t)=E0+v_E*t, x_B(t)=B0+v_B*t.
The emission time t0 and processing delay are coordinate times in this frame.
There is no gravitational lensing, acceleration, cosmological motion,
Galactic potential, or superluminal communication in this model.
All vectors are 3D SI coordinates and speeds must be below c.
Research lead: Biswajit Jana.
"""
from dataclasses import dataclass
from math import acos, isfinite, sqrt, pi
from random import Random
from statistics import mean, stdev

C = 299792458.0
LY = 9.4607304725808e15
JULIAN_YEAR = 365.25 * 86400.0

def vec(x):
    if len(x) != 3 or not all(isfinite(v) for v in x):
        raise ValueError("finite length-three vectors required")
    return tuple(float(v) for v in x)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return sqrt(dot(a,a))

def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))

def minus(a,b):
    return tuple(x-y for x,y in zip(a,b))

def scale(a,t):
    return tuple(t*x for x in a)

@dataclass(frozen=True)
class Endpoint:
    position_m: tuple
    velocity_m_s: tuple

    def __post_init__(self):
        vec(self.position_m)
        v=vec(self.velocity_m_s)
        if dot(v,v)>=C*C:
            raise ValueError("inertial endpoints must move slower than c")

    def at(self,t):
        if not isfinite(t):
            raise ValueError("finite time required")
        return plus(self.position_m,scale(self.velocity_m_s,t))

def intercept_delay(source_at_emission,receiver_pos,receiver_velocity):
    """Positive null intercept: |receiver_pos+v*t-source|=c*t.

    receiver_pos is the receiver position *at emission*.
    Both input vectors are three-dimensional. Returns seconds.
    """
    r=minus(vec(receiver_pos),vec(source_at_emission))
    v=vec(receiver_velocity)
    A=C*C-dot(v,v)
    if A<=0: raise ValueError("receiver speed must be subluminal")
    b=dot(r,v)
    return (b+sqrt(b*b+A*dot(r,r)))/A

def travel(a,b,t0=0.0):
    if not isfinite(t0):
        raise ValueError("finite emission epoch required")
    transmit=a.at(t0)
    recv=b.at(t0)
    dt=intercept_delay(transmit,recv,b.velocity_m_s)
    direction=minus(b.at(t0+dt),transmit)
    n=norm(direction)
    direction=(0.,0.,0.) if n==0 else scale(direction,1/n)
    return {"emission_s":t0,"arrival_s":t0+dt,"delay_s":dt,
            "beam_unit_vector":direction,"range_at_emission_m":norm(minus(recv,transmit))}

def round_trip(a,b,emission_s=0.0,processing_s=0.0):
    """Outbound + return after receiver clock's coordinate processing delay."""
    if not isfinite(processing_s) or processing_s<0:
        raise ValueError("nonnegative finite processing delay")
    outbound=travel(a,b,emission_s)
    t_reply=outbound["arrival_s"]+processing_s
    inbound=travel(b,a,t_reply)
    return {"outbound_s":outbound["delay_s"],
            "processing_s":processing_s,"return_s":inbound["delay_s"],
            "total_s":inbound["arrival_s"]-emission_s,
            "outbound":outbound,"return":inbound}

def point_ahead_angle(source,receiver,t0=0.0):
    """Angle between instantaneous LOS and intercept direction, radians."""
    instant=minus(receiver.at(t0),source.at(t0))
    if norm(instant)==0: raise ValueError("coincident endpoints")
    aim=travel(source,receiver,t0)["beam_unit_vector"]
    cosang=dot(instant,aim)/norm(instant)
    return acos(max(-1.,min(1.,cosang)))

def position_uncertainty_mc(a,b,pos_sigma_m=0.0,vel_sigma_m_s=0.0,
                            samples=1000,seed=17):
    """Illustrative isotropic diagonal Gaussian perturbation; NOT Gaia covariance.

    Perturbs receiver initial position and velocity independently.
    Proper astrometric covariance and correlated uncertainties must replace this.
    """
    if type(samples) is not int or samples<2 or any(
        not isfinite(v) or v<0 for v in (pos_sigma_m,vel_sigma_m_s)):
        raise ValueError("invalid uncertainty parameters")
    rng=Random(seed); values=[]
    for _ in range(samples):
        p=tuple(x+rng.gauss(0,pos_sigma_m) for x in b.position_m)
        v=tuple(x+rng.gauss(0,vel_sigma_m_s) for x in b.velocity_m_s)
        if norm(v)>=C: raise ValueError("sampled superluminal endpoint")
        values.append(travel(a,Endpoint(p,v))["delay_s"])
    return {"samples":samples,"mean_s":mean(values),
            "std_s":stdev(values),"min_s":min(values),"max_s":max(values)}

if __name__=="__main__":
    import json
    earth=Endpoint((0.,0.,0.),(0.,0.,0.))
    prox=Endpoint((4.24*LY,0.,0.),(0.,24000.,0.))
    results=round_trip(earth,prox)
    print(json.dumps({"outbound_years":results["outbound_s"]/JULIAN_YEAR,
        "round_trip_years":results["total_s"]/JULIAN_YEAR,
        "point_ahead_arcsec":point_ahead_angle(earth,prox)*180/pi*3600,
        "interpretation":"Illustrative inertial-motion geometry, not measured ephemerides or FTL."},indent=2))
