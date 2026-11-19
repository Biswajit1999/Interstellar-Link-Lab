"""Flat-spacetime constant-velocity null interception; no FTL or ephemeris claim."""
import numpy as np
C = 299792458.0

def intercept_time(relative_position_m, receiver_velocity_m_s, c=C):
    """Solve |r+v*t|=c*t for earliest positive time."""
    r = np.asarray(relative_position_m, dtype=float)
    v = np.asarray(receiver_velocity_m_s, dtype=float)
    if r.shape != (3,) or v.shape != (3,) or not np.all(np.isfinite(r)) or not np.all(np.isfinite(v)) or not np.isfinite(c) or c <= 0 or np.linalg.norm(v) >= c or np.linalg.norm(r) == 0:
        raise ValueError("require finite 3-vectors, nonzero separation and subluminal receiver")
    a = c*c-np.dot(v,v)
    b = np.dot(r,v)
    d = b*b+a*np.dot(r,r)
    return float(np.dot(r,r)/(np.sqrt(d)-b)) if b < 0 else float((np.sqrt(d)+b)/a)

def point_ahead(relative_position_m, receiver_velocity_m_s, c=C):
    """Emission direction and angle relative to instantaneous line of sight."""
    r = np.asarray(relative_position_m,float)
    v = np.asarray(receiver_velocity_m_s,float)
    t = intercept_time(r,v,c)
    direction = (r+v*t)/(c*t)
    los = r/np.linalg.norm(r)
    angle = np.arccos(np.clip(np.dot(direction,los),-1,1))
    return t, direction, float(angle)

def finite_difference_time_gradient(r,v,step_m=1000.):
    """Sensitivity in s/m; conditional on fixed receiver velocity."""
    r = np.asarray(r,float)
    if step_m <= 0: raise ValueError("step_m must be positive")
    out = []
    for j in range(3):
        d = np.zeros(3)
        d[j] = step_m
        out.append((intercept_time(r+d,v)-intercept_time(r-d,v))/(2*step_m))
    return np.array(out)
