"""Flat-spacetime pre-lightcone causal controls (not a test of FTL hardware).

A new random bit must not be decodable before its physical signal can arrive.
No mutual-information statistic alone proves an extraordinary causal channel.
Curved geometries require an independent actual-metric causal analysis.
Research lead: Biswajit Jana. Apache-2.0.
"""
from dataclasses import dataclass
from math import hypot, isfinite, log2
from random import Random

C = 299792458.


@dataclass(frozen=True)
class Event:
    t_s: float
    x_m: float
    y_m: float = 0.
    z_m: float = 0.


def interval_c2s2(a: Event, b: Event) -> float:
    """Positive for timelike, zero for null, negative for spacelike."""
    dt = b.t_s - a.t_s
    dx = b.x_m - a.x_m
    dy = b.y_m - a.y_m
    dz = b.z_m - a.z_m
    return (C*dt)**2 - (dx*dx+dy*dy+dz*dz)


def flat_future_causal(a: Event, b: Event) -> bool:
    """Whether b lies in/on a's Minkowski future light cone."""
    dt = b.t_s - a.t_s
    dr = hypot(b.x_m-a.x_m, b.y_m-a.y_m, b.z_m-a.z_m)
    return dt >= 0. and C*dt >= dr


def binary_mutual_information(x, y) -> float:
    """Empirical plug-in mutual information (bits), includes finite-sample bias."""
    x = tuple(x)
    y = tuple(y)
    if not x or len(x) != len(y):
        raise ValueError("nonempty equal-length arrays required")
    if any(v not in (0,1) for v in x+y):
        raise ValueError("data must contain binary values")
    n = len(x)
    tab = [[0,0],[0,0]]
    for a,b in zip(x,y):
        tab[a][b]+=1
    rows = [sum(row) for row in tab]
    cols = [tab[0][i]+tab[1][i] for i in range(2)]
    info = 0.
    for i in range(2):
        for j in range(2):
            num = tab[i][j]
            if num:
                info += (num/n)*log2(num*n/(rows[i]*cols[j]))
    return max(0.,info)


def permutation_p(x, y, draws=199, seed=31) -> dict:
    """Permutation p-value with plus-one correction, exchangeable iid null only.

    Time-correlated experimental data require block/time-preserving surrogates.
    """
    if type(draws) is not int or draws < 1:
        raise ValueError("draws must be a positive integer")
    observed = binary_mutual_information(x,y)
    rnd = Random(seed)
    shuffled = list(y)
    count = 0
    for _ in range(draws):
        rnd.shuffle(shuffled)
        if binary_mutual_information(x,shuffled) >= observed-1e-14:
            count+=1
    return {"empirical_mi_bits":observed, "permutation_p":(count+1)/(draws+1),
            "null_draws":draws}


def synthetic_controls(n=4096, seed=101, draws=199):
    """Declared independent null, post-arrival copy, and forced data-leak checks.

    'Leaked' is an *intentional side-channel simulation*, not FTL evidence.
    The prearrival channel is seeded independent of sender's fresh X.
    """
    if type(n) is not int or n < 200:
        raise ValueError("n must be >=200")
    rng=Random(seed)
    x=[rng.randrange(2) for _ in range(n)]
    y_before=[rng.randrange(2) for _ in range(n)]
    y_after=[bit ^ (1 if rng.random()<0.01 else 0) for bit in x]
    y_leak=[bit ^ (1 if rng.random()<0.05 else 0) for bit in x]
    return {"prearrival_independent":permutation_p(x,y_before,draws,seed+1),
            "postarrival_positive_control":permutation_p(x,y_after,draws,seed+2),
            "intentional_side_channel_positive_control":permutation_p(x,y_leak,draws,seed+3),
            "interpretation":"No physical FTL trial: postarrival and leaked streams are seeded synthetic positive controls"}


if __name__ == "__main__":
    import json
    print(json.dumps(synthetic_controls(),indent=2))
