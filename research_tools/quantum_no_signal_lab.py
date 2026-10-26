"""Monte Carlo Bell-pair measurement control for causal communication studies.

This is an ideal |Phi+> calculation, not a physical FTL experiment.
Measurements are projectors in the X-Z plane (angle from +Z).
Research lead: Biswajit Jana.
"""
import argparse
import json
from math import cos, isfinite, log2, pi
from random import Random


def bell_joint(a, b, theta_alice, theta_bob):
    """P(a,b)=[1+(-1)^(a+b) cos(theta_A-theta_B)]/4."""
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("binary measurement outcomes required")
    if not all(map(isfinite, (theta_alice, theta_bob))):
        raise ValueError("angles must be finite")
    return max(0.0, 0.25 * (1 + (-1)**(a+b) * cos(theta_alice-theta_bob)))


def bob_marginal(theta_alice, theta_bob=0.0):
    """Trace out unread Alice outcomes: Bob is always maximally mixed."""
    return tuple(sum(bell_joint(a,b,theta_alice,theta_bob) for a in (0,1))
                 for b in (0,1))


def information_bits(x, y):
    """Empirical plug-in mutual information; finite-null estimate is not exactly 0."""
    if len(x) != len(y) or not x:
        raise ValueError("nonempty equal-length data needed")
    tab = [[0,0],[0,0]]
    for a,b in zip(x,y):
        if a not in (0,1) or b not in (0,1):
            raise ValueError("binary inputs required")
        tab[a][b] += 1
    n=len(x)
    rows=[sum(r) for r in tab]
    cols=[tab[0][j]+tab[1][j] for j in (0,1)]
    return max(0.0,sum((tab[i][j]/n)*log2(tab[i][j]*n/(rows[i]*cols[j]))
                       for i in (0,1) for j in (0,1) if tab[i][j]))


def permutation_p(x,y,draws=99,seed=101):
    """IID exchangeable-null permutation p-value; not valid for serially dependent logs."""
    if draws < 1:
        raise ValueError("draws must be positive")
    rng=Random(seed)
    sample=list(y)
    observed=information_bits(x,y)
    exceed=0
    for _ in range(draws):
        rng.shuffle(sample)
        exceed += information_bits(x,sample) >= observed-1e-14
    return (exceed+1)/(draws+1)


def experiment(n=12000,seed=20261025,classical_leak=False,draws=99):
    """Random Alice X/Z choices; Bob always measures Z, before any classical data arrives.

    A 30% overwrite of Bob's data with Alice's setting is a deliberately inserted
    ordinary side channel and serves solely as a positive detection control.
    """
    if type(n) is not int or n<100:
        raise ValueError("n must be an integer >=100")
    rng=Random(seed)
    alice_settings=[]
    bob_outcomes=[]
    same=[0,0]
    seen=[0,0]
    zero=[0,0]
    for _ in range(n):
        setting=rng.randrange(2)
        # Sample joint outcomes from the Born-rule categorical distribution.
        r=rng.random()
        cumulative=0.0
        a=b=1
        for ai in (0,1):
            for bi in (0,1):
                cumulative+=bell_joint(ai,bi,setting*pi/2,0.0)
                if r<cumulative:
                    a,b=ai,bi
                    break
            if r<cumulative: break
        if classical_leak and rng.random()<0.30:
            b=setting  # deliberately inserted, non-quantum leakage
        alice_settings.append(setting)
        bob_outcomes.append(b)
        same[setting]+=(a==b)
        seen[setting]+=1
        zero[setting]+=(b==0)
    return {
        "model":"ideal_phi_plus_Alice_Z_or_X_Bob_Z",
        "simulated_pairs":n,
        "seed":seed,
        "Bob_zero_probability_given_Alice_Z":zero[0]/seen[0],
        "Bob_zero_probability_given_Alice_X":zero[1]/seen[1],
        "Born_rule_Bob_marginal":bob_marginal(pi/2),
        "empirical_setting_to_Bob_MI_bits":information_bits(alice_settings,bob_outcomes),
        "iid_permutation_p":permutation_p(alice_settings,bob_outcomes,draws,seed+1),
        "fraction_Alice_Bob_equal_given_Alice_Z":same[0]/seen[0],
        "fraction_Alice_Bob_equal_given_Alice_X":same[1]/seen[1],
        "classical_side_channel_control":classical_leak,
        "interpretation":"Simulation control only; no experiment or superluminal channel."
    }


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pairs",type=int,default=12000)
    p.add_argument("--seed",type=int,default=20261025)
    p.add_argument("--permutations",type=int,default=99)
    p.add_argument("--classical-leak",action="store_true")
    a=p.parse_args()
    print(json.dumps(experiment(a.pairs,a.seed,a.classical_leak,a.permutations),indent=2))
