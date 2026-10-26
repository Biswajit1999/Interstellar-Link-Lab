# Entanglement does not deliver a chosen bit

*Laboratory note · 25 October 2026 · Biswajit Jana*

Consider two stations that have already shared a Bell pair. Earth chooses a measurement setting after the particles are distributed. Could a distant station tell which setting was chosen, without waiting for another signal? This question can be answered without assuming an imperfect detector.

## The state and Bob's measurement

For the Bell state

$$
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt{2}},
\qquad
\rho_{AB}=|\Phi^+\rangle\langle\Phi^+|,
$$

tracing over Alice gives

$$
\rho_B=\operatorname{Tr}_A(\rho_{AB})
=\tfrac12 \begin{pmatrix}1&0\\0&1\end{pmatrix}
=\frac{\mathbb I}{2}.
$$

A change in Alice's *unannounced* measurement basis changes which joint correlations can be uncovered when the records are compared. It does not change Bob's local density matrix. If Alice chooses either Z or X and Bob always measures Z, then

$$
P(B=0\mid A_{\mathrm{basis}}=Z)
=P(B=0\mid A_{\mathrm{basis}}=X)=\tfrac12.
$$

The equality holds for any trace-preserving local operation by Alice when she does not condition Bob's sample on a communicated measurement result.

For projective measurements in the X–Z plane, let the measurement axes make angles $\theta_A$ and $\theta_B$ with Z and code the two outcomes as $a,b\in\{0,1\}$. The ideal Bell-state joint probabilities are

$$
P(a,b\mid\theta_A,\theta_B)
=\frac{1+(-1)^{a+b}\cos(\theta_A-\theta_B)}4.
$$

Bob's marginal is obtained by summing over the *unread* Alice result:

$$
P(b\mid\theta_A,\theta_B)=\sum_{a=0}^1P(a,b\mid\theta_A,\theta_B)=\frac12.
$$

Equal-basis results can be perfectly correlated: for Z/Z, Alice and Bob obtain the same outcome. For X/Z, the four joint outcomes have probability $1/4$ each. These are distinct *joint distributions* with the same Bob-only distribution. Seeing the correlation requires comparing the two records later.

## What is tested

Run the standard-library Python control:

~~~bash
python -m research_tools.quantum_no_signal_lab --pairs 12000 --seed 20261025
python -m unittest discover -s research_tools/tests -v
~~~

The script samples an ideal $|\Phi^+\rangle$ source. In each trial Alice independently chooses Z or X with equal probability; Bob always measures Z. It reports each local outcome frequency, the empirical mutual information between Alice's setting and Bob's outcome, and an IID permutation-null p-value.

Because there are finitely many trials, an empirical mutual-information estimate is usually positive even when the true information is zero. The test therefore checks a *calibrated null* rather than testing whether a computed floating-point value is exactly zero.

The optional positive control

~~~bash
python -m research_tools.quantum_no_signal_lab --pairs 12000 --classical-leak
~~~

deliberately overwrites part of Bob's simulated output with Alice's setting. The resulting dependence is **an ordinary inserted side channel**, not quantum signalling. In a real separated experiment such a channel would have to respect its own propagation delay and be audited explicitly.

The IID permutation calculation assumes independent, exchangeable trials. Detector drift, bursts, after-pulsing, time-tag reuse and nonrandom selection invalidate that simple calibration; real laboratory data would require a preregistered timing protocol and dependence-aware nulls.

## Why this matters for interstellar communication

Sharing $10^{30}$ entangled pairs in advance does not allow Earth to select a fresh 0 or 1 and have Proxima read it from its own detector immediately. Quantum teleportation and related protocols require an additional classical communication resource. The original teleportation proposal explicitly uses classical and EPR channels [1]. Nor does this null result establish a no-go theorem against *all logically conceivable* spacetime models: a speculative curved-spacetime device must be assessed under its actual metric, matter sources and causal structure.

The operational condition for an extraordinary communication claim is a *new randomized message* $X$ and a locally recoverable receiver record $Y$ outside the signal's actual future causal set, with timestamp, hardware and side-channel audits. Correlated detection records alone do not meet that condition.

## What should be plotted

Use paired receiver-only histograms for Alice's Z and X settings. Both should approach 50/50. Separately show the Alice–Bob joint outcomes, for which Z/Z correlations are strong and X/Z correlations vanish. Label the panels **receiver-only** and **joint records compared afterward**: conflating them is the origin of the supposed entanglement communication shortcut.

The companion [interactive calculation](../no-signalling.html) renders these distinctions in the browser without a mathematical typesetting service or external network requests.

## References

1. Bennett, C. H., *et al.*, “Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels,” *Physical Review Letters* **70**, 1895–1899 (1993). [DOI: 10.1103/PhysRevLett.70.1895](https://doi.org/10.1103/PhysRevLett.70.1895).
2. Bennett, C. H., *et al.*, “Remote State Preparation,” *Physical Review Letters* **87**, 077902 (2001). [DOI: 10.1103/PhysRevLett.87.077902](https://doi.org/10.1103/PhysRevLett.87.077902).
3. [GitHub mathematical expressions documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions), for the dollar-delimited mathematical notation used in this note.

*Scope: ideal Born-rule probabilities and seeded numerical simulation. No hardware experiment or FTL transmission is asserted.*
