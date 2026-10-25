# Original investigator research brief

> Historical project requirements preserved from the research planning conversation. The `<<< PASTE ... >>>` placeholder is part of the original prompt. This text is a requirements document, not experimental evidence. The project itself remains standalone and independent of Moving Observer.

---

I want you to act as my principal research physicist, numerical-relativity
researcher, quantum-information scientist, optical-communications engineer,
scientific software architect, statistician, and critical peer reviewer.

AUTHOR / RESEARCH CONTEXT
=========================

I am Biswajit Jana (GitHub: Biswajit1999).

My existing project is "The Moving Observer". Its research style is important:
it uses explicit coordinate/reference frames, reproducible calculations,
astrometric propagation, Gaia data, uncertainty propagation, sensitivity
analysis, numerical validation, interactive 3D visualisation, first-
post-Newtonian modelling where appropriate, and very careful statements about
what a model can and cannot establish.

The new project must follow the same scientific philosophy.

PROJECT WORKING TITLE
=====================

Causal Frontier
A Reproducible Search for Information Transfer Beyond the Light Cone

Optional research-module name:

Moving Observer: Causal Corridor (MOCC)

I have pasted below a deep-research report that defines the scientific basis
for the project.

<<< PASTE THE COMPLETE DEEP-RESEARCH REPORT HERE >>>


MISSION
=======

Build a research-grade, open, reproducible project investigating this question:

    Given a newly and randomly selected message X at transmitter event A,
    is there any physically admissible mechanism by which a receiver at a
    spacelike-separated event B can obtain statistically significant mutual
    information I(X;Y) > 0 before an ordinary light signal from A could
    arrive?

Do NOT assume faster-than-light communication exists.

Do NOT attempt to prove my preferred idea.

Attempt to falsify every candidate, including our own.

The project must remain scientifically valuable if every FTL candidate fails.

The final project should contain three major scientific branches:

1. CAUSAL FRONTIER
   Fundamental relativity, light cones, observer transformations,
   no-signalling and causality tests.

2. CAUSAL CORRIDOR
   General-relativistic inverse design of warp/hyperwave/wormhole-inspired
   communication geometries, including complete stress-energy analysis.

3. PHOTON FRONTIER
   A physically realistic, near-light-speed interstellar optical
   communications system using high-photon-information-efficiency
   modulation, coding, single-photon detection and predictive AI.

NON-NEGOTIABLE SCIENTIFIC RULE
==============================

The project must define FTL communication operationally.

Let X be a freshly generated random transmitted message and Y_< be everything
the distant receiver can observe before the normal light-cone arrival time.

The primary FTL statistic is

    I_pre = I(X ; Y_<).

A candidate is NOT FTL merely because:

- a pulse peak appears early;
- phase velocity exceeds c;
- group velocity exceeds c;
- two quantum measurements are correlated;
- an entangled state collapses;
- a coordinate velocity exceeds c;
- a metric has a parameter labelled "warp speed";
- a simulation visually reaches the receiver early;
- information was pre-shared at the receiver;
- post-selection reveals a correlation later.

For an FTL claim, a newly selected message must be recoverable before the
ordinary causal light front.

No component of the software, documentation or UI may display "FTL achieved"
unless this criterion is satisfied and all registered causal-side-channel
tests have also passed.

PHYSICS FOUNDATION
==================

Implement special relativity from first principles.

Use

    ds² = -c²dt² + dx² + dy² + dz²

and classify intervals as timelike, null or spacelike.

Implement Lorentz transformations:

    gamma = 1/sqrt(1-v²/c²)

    x' = gamma(x-vt)

    t' = gamma(t-vx/c²)

For a hypothetical signal speed u > c over distance L, calculate

    Δt' = gamma L (1/u - v/c²)

and demonstrate numerically and visually that Δt' becomes negative for

    v > c²/u.

Implement a tachyonic-antitelephone / return-signal simulator.

Do not treat reversed coordinate ordering as an implementation detail.
Causality analysis is a first-class component.

QUANTUM NO-SIGNALLING MODULE
============================

Implement a Bell-pair simulation.

For

    |Phi+> = (|00> + |11>)/sqrt(2)

show that Bob's reduced density matrix is

    rho_B = I/2

before receiving Alice's classical result.

Implement general no-signalling checks:

    sum_a P(a,b|x,y)

must not depend on Alice's setting x, and the corresponding Alice marginal
must not depend on Bob's setting.

Generate a random Alice message X and attempt to infer X using only Bob's
local data.

Show numerically that

    I(X;Y_Bob) ~= 0

before classical communication.

Then show Bell correlations after the records are compared.

This module is a calibration test: our framework must correctly reject
quantum nonlocality as FTL communication.

INFORMATION-THEORY CORE
=======================

Implement

    I(X;Y) = sum p(x,y) log2[p(x,y)/(p(x)p(y))].

Include:

- entropy;
- conditional entropy;
- channel capacity;
- BER;
- symbol error rate;
- confidence intervals;
- permutation tests;
- Monte Carlo null tests;
- false-discovery correction where multiple hypotheses are tested.

The program must identify the ordinary light arrival time t_c.

Divide observations into

    Y_< = Y(t < t_c)

and

    Y_>= = Y(t >= t_c).

The pre-lightcone result must never use samples from Y_>=.

GENERAL RELATIVITY ENGINE
=========================

Implement a transparent GR pipeline capable of taking a metric

    g_mu_nu(x)

and calculating or numerically evaluating:

    inverse metric g^mu_nu
    Christoffel symbols
    Riemann tensor
    Ricci tensor
    Ricci scalar
    Einstein tensor
    stress-energy tensor

using

    G_mu_nu + Lambda g_mu_nu
      = (8 pi G / c^4) T_mu_nu.

Where symbolic calculation becomes impractical, use numerical/autodiff
methods, but cross-check simple metrics symbolically.

Validation metrics MUST include:

1. Minkowski spacetime:
       R_mu_nu_rho_sigma = 0

2. Schwarzschild exterior:
       G_mu_nu = 0

3. selected known cosmological or analytic metric:
       compare against analytic results

4. independent implementation comparison where possible.

Never trust a single symbolic or numerical pipeline without cross-validation.

STRESS-ENERGY ANALYSIS
======================

Given a desired metric, calculate

    T_required = c^4/(8 pi G) * (G + Lambda g).

For arbitrary observer four-velocity u^mu calculate:

    rho = T_mu_nu u^mu u^nu.

Evaluate:

- Null Energy Condition;
- Weak Energy Condition;
- Strong Energy Condition;
- Dominant Energy Condition;
- averaged null energy where applicable;
- observer dependence;
- energy density extrema;
- pressure eigenvalues;
- momentum flux;
- anisotropic stress.

Do NOT evaluate the WEC for only one favoured observer and call it satisfied.

Sample physically allowed timelike observers systematically.

Implement null-vector optimisation for NEC minima.

Where feasible use GPU acceleration.

CURVATURE AND VALIDITY
======================

Calculate curvature invariants including at least the Kretschmann scalar

    K = R_abcd R^abcd.

Track the minimum proper length scale in every geometry.

Define the Planck length

    l_P = sqrt(hbar G/c^3).

Flag results whenever characteristic scale approaches the Planck regime.

A Planck-scale classical-GR result must be labelled:

    "classical GR extrapolation; quantum-gravity reliability unknown"

and never "physically feasible".

WARP METRIC BENCHMARK
=====================

Implement the Alcubierre metric as a benchmark:

    ds² =
      -c²dt²
      + [dx - v_s f(r_s) dt]²
      + dy² + dz².

Use multiple smooth shape functions f(r).

Reproduce known qualitative stress-energy and energy-condition behaviour.

Then reproduce, as accurately as possible from the literature:

- Alcubierre;
- Bobrick-Martire classes where computationally practical;
- Lentz-type claims where sufficient equations are available;
- Hyperwave / microscopic warp communication.

Do not silently alter published equations.

For each published model create a provenance document containing:

- exact source;
- equation numbers;
- assumptions;
- units;
- our implementation;
- numerical validation;
- deviations from the original paper.

HYPERWAVE REPRODUCTION
======================

Because the Hyperwave literature is particularly close to the project idea,
treat it as a major replication study.

Test separately:

- claimed total energy scaling;
- local energy density;
- wall thickness;
- curvature;
- Planck-scale sensitivity;
- complete stress-energy tensor;
- NEC/WEC/ANEC;
- quantum energy inequality estimates;
- acceleration/deceleration assumptions;
- particle capture and emission;
- controllability of the leading edge;
- requirement for a pre-established tube;
- information capacity;
- reset/reinitialisation requirements;
- causality under two-way operation.

Do not equate a small integrated negative energy with physical feasibility.

CAUSAL CORRIDOR MODEL
=====================

Develop a new exploratory MODEL, not an initially claimed discovery.

Use moving endpoint worldlines

    z_Earth^mu(tau_E)
    z_Target^mu(tau_T).

Start with Alpha/Proxima Centauri as the target.

Use astrometric data with explicit epoch and provenance.

Construct the moving line/corridor

    x_c(s,t)
      = (1-s)x_E(t) + s x_T(t),
      0 <= s <= 1.

Define perpendicular distance r_perp to this corridor.

Explore smooth corridor functions such as

    F(r) =
      0.5 [1 - tanh((r-R)/Delta)].

Explore shift-vector constructions in 3+1 form:

    ds² =
      -alpha² c² dt²
      + gamma_ij
        (dx^i + beta^i dt)
        (dx^j + beta^j dt).

Do NOT assume this construction is physical.

Calculate the required Einstein tensor and T_mu_nu.

Search the parameter space for candidates that minimise a cost functional
such as

    J =
      w_t * arrival_time
      + w_E * absolute_stress_energy
      + w_K * curvature
      + w_N * energy_condition_violation
      + w_Q * quantum_inequality_penalty
      + w_C * causality_penalty.

Avoid cancellation tricks by calculating both

    integral rho dV

and

    integral |rho| dV.

Report both.

INVERSE SOURCE DESIGN
=====================

This is one of the most important original research directions.

Instead of only asking what metric we want, ask whether known physical
stress-energy sources can approximate the required tensor.

Construct basis/model sources where theoretically appropriate:

- electromagnetic fields;
- conducting plasma;
- scalar fields;
- idealised fluids;
- anisotropic fluids;
- Casimir-like stress tensors;
- other well-defined sources from the literature.

Represent

    T_candidate =
      sum_i a_i T_i

where physically meaningful.

Minimise

    L_T =
      integral w(x)
      ||T_candidate - T_required||² d^4x

subject to all physical constraints of the candidate fields.

Do not allow arbitrary independent tensor components if the corresponding
matter model cannot generate them.

A low total-energy scalar mismatch is not enough.
Compare the full tensor.

CASIMIR / NEGATIVE ENERGY MODULE
================================

Implement the ideal parallel-plate benchmark

    E/A = -pi² hbar c / (720 a³)

and

    P = -pi² hbar c / (240 a⁴).

Then make absolutely clear that this does not prove arbitrary exotic
stress-energy can be created.

Where literature permits, compare:

    T_Casimir^mu_nu

against

    T_required^mu_nu.

Quantify tensor mismatch.

Implement quantum-energy-inequality estimates only within their domains of
validity.

State those domains explicitly.

GEODESIC ENGINE
===============

Integrate

    d²x^mu/dlambda²
      + Gamma^mu_ab
        dx^a/dlambda
        dx^b/dlambda
      = 0.

For photons enforce/check

    g_mu_nu k^mu k^nu = 0.

Monitor numerical constraint violation.

Use adaptive integration and at least one independent cross-check.

Calculate:

    t_background
    t_candidate
    Delta_t_gain = t_background - t_candidate.

Do not call Delta_t_gain "FTL" unless the complete operational information
criterion is also satisfied.

GLOBAL CAUSALITY
================

For every candidate with apparent superluminal capability:

- transform between moving observers;
- construct return-message cases;
- search for closed timelike/causal curves;
- test whether receiver-before-transmitter configurations are possible;
- evaluate global hyperbolicity where computationally possible;
- detect horizons;
- distinguish coordinate artifacts from invariant causal structure.

A candidate that achieves lower one-way arrival time but enables a causal
loop must be explicitly labelled.

PROXIMA / MOVING OBSERVER CONNECTION
====================================

Use the Moving Observer philosophy directly.

Model:

- present Earth/Solar System position;
- Alpha/Proxima barycentric motion;
- target uncertainty;
- stellar relative velocity;
- closest-approach epoch;
- changing endpoint distance;
- light-cone propagation between moving endpoints.

Reproduce a conventional no-FTL baseline first.

Calculate current and closest-approach one-way and round-trip light times.

Then compare every candidate to exactly the same moving-endpoint baseline.

Do not treat target distance as static if the simulation runs over long
times.

PRACTICAL INTERSTELLAR COMMUNICATION BRANCH
===========================================

Build a physically realistic optical link model independent of the
speculative GR work.

Include:

    diffraction
    wavelength
    transmitting aperture
    receiving aperture
    transmit power
    pointing error
    optical throughput
    detector efficiency
    stellar background
    zodiacal background
    dark counts
    clock/timing error
    atmospheric transmission where relevant.

Use

    theta ~= 1.22 lambda / D_t

as a simple Airy-scale benchmark but implement the proper Airy intensity
distribution for detailed calculations.

Photon energy:

    E_gamma = hc/lambda.

Detected photon rate:

    Ndot =
      eta_detector * P_received / E_gamma.

Implement:

- M-ary pulse-position modulation;
- large M;
- realistic background;
- erasures;
- Reed-Solomon baseline;
- LDPC/SCPPM-style options where implementable;
- photon-counting detection;
- coding gain;
- bits per received photon;
- bits per incident photon;
- bandwidth;
- average and peak power.

Include the Gordon-Holevo pure-loss benchmark where appropriate.

Compare conventional direct detection with advanced/quantum receiver
literature without claiming unavailable hardware performance.

PREDICTIVE TWIN COMMUNICATION
=============================

Develop a practical AI communications protocol for large propagation delays.

Both sides maintain an identical predictive model.

At time t predict:

    s_hat_t = f_theta(history).

Transmit only innovation:

    e_t = s_t - s_hat_t.

Quantify:

    H(S)
    H(S | S_hat)
    compression ratio
    prediction error
    resynchronisation cost
    robustness to model drift.

Investigate agent-to-agent communication where each endpoint contains a
local autonomous AI capable of answering predictable queries without waiting
for Earth.

Be scientifically explicit:

    Predictive Twin Communication reduces transmitted information and
    perceived interaction delay.

It does NOT transmit newly created information faster than light.

AI / OPTIMISATION
=================

Use AI only where scientifically justified.

Potential jobs:

- surrogate modelling of expensive GR calculations;
- Bayesian optimisation;
- differentiable metric optimisation;
- symbolic equation verification;
- anomaly detection;
- parameter sweeps;
- uncertainty propagation;
- literature mapping;
- predictive-twin compression.

Do NOT use an AI-generated metric without independently calculating its
Einstein tensor and physical constraints.

An attractive neural-network output is not physics.

MONTE CARLO AND UNCERTAINTY
===========================

Every result must distinguish:

- numerical uncertainty;
- observational uncertainty;
- parameter uncertainty;
- model uncertainty;
- omitted physics.

Use reproducible random seeds.

Use convergence studies.

Do not report false precision.

Where possible use correlated astrometric covariance rather than independent
errors.

PARAMETER SWEEPS
================

At minimum explore characteristic radius logarithmically from approximately:

    1e-35 m to 1e3 m

while flagging quantum-gravity regimes.

Explore wall thickness ratios.

Explore effective candidate propagation parameters from subluminal through
formally superluminal values.

Create phase diagrams showing regions classified as:

    ordinary causal
    apparent superluminal
    energy-condition violating
    quantum-inequality problematic
    Planckian/invalid classical regime
    numerical failure
    causal-loop capable
    physically unknown

Never label a region "feasible" merely because the numerical solver returns
a solution.

INTERACTIVE VISUALISATION
=========================

Build an interactive web application inspired by Moving Observer.

Views should include:

1. Light Cone
2. Lorentz Boost
3. Tachyon / Causality Lab
4. Quantum No-Signalling
5. Earth–Proxima
6. Optical Link
7. Warp Metric
8. Stress-Energy
9. Energy Conditions
10. Null Geodesics
11. Causal Corridor
12. Causal Loop Test
13. Parameter Explorer
14. Research Report

Use Three.js or another suitable browser 3D framework.

The visualisation must distinguish physical scale from illustrative scaling.

Any enlarged object, exaggerated wall thickness or distorted axis must be
clearly labelled.

Allow users to toggle:

    background metric
    candidate metric
    light cones
    null geodesics
    timelike observers
    energy density
    NEC violation
    curvature
    horizons
    moving target
    reference frame.

Show numerical values beside every visualisation.

REPRODUCIBILITY
===============

The repository must be reproducible offline after dependencies and frozen
data are installed.

Use pinned dependencies.

Record:

- software versions;
- constants;
- units;
- data sources;
- checksums;
- random seeds;
- source paper versions.

Use SI internally unless there is a compelling reason otherwise.

Create explicit unit tests for dimensional consistency.

Never mix c=1 geometrised units with SI silently.

If a paper uses c=G=1, document the conversion.

SUGGESTED SOFTWARE ARCHITECTURE
===============================

Use Python for scientific computation and TypeScript/JavaScript for the
interactive front end unless a better architecture is justified.

Suggested scientific modules:

    causal_frontier/
        constants.py
        units.py
        spacetime.py
        lorentz.py
        lightcone.py
        information.py
        quantum_nosignalling.py
        optical_link.py
        ppm.py
        coding.py
        proxima.py
        metrics/
            minkowski.py
            schwarzschild.py
            alcubierre.py
            hyperwave.py
            causal_corridor.py
        tensors/
            christoffel.py
            curvature.py
            einstein.py
            stress_energy.py
            energy_conditions.py
        geodesics.py
        causality.py
        inverse_design.py
        quantum_energy.py
        uncertainty.py
        optimisation.py
        validation.py

Suggested front-end structure:

    web/
        light-cone
        moving-observer
        quantum
        proxima
        optical-link
        warp
        stress-energy
        causality
        report

Suggested research documents:

    README.md
    REPORT.md
    THEORY.md
    CAUSALITY.md
    QUANTUM_REPORT.md
    WARP_REPORT.md
    HYPERWAVE_REPLICATION.md
    OPTICAL_LINK_REPORT.md
    PROXIMA_REPORT.md
    EXPERIMENT.md
    LITERATURE_SEARCH.md
    DATA_PROVENANCE.md
    VALIDATION.md
    AUDIT.md
    LIMITATIONS.md
    CITATION.cff

TESTING
=======

Create automated tests for:

- Lorentz invariance of ds²;
- light propagation at c;
- reversed ordering for spacelike-separated hypothetical FTL signals;
- no reversal for timelike signals;
- Bell marginal no-signalling;
- mutual information near zero before the classical channel;
- Minkowski curvature zero;
- Schwarzschild vacuum Einstein tensor;
- tensor symmetry;
- Bianchi-identity consistency where practical;
- geodesic null constraint;
- unit conversion;
- optical diffraction scaling;
- inverse-square/far-field behaviour;
- photon-energy calculation;
- PPM encoding/decoding;
- Monte Carlo reproducibility;
- Proxima propagation;
- causal-loop detection;
- energy-condition optimisation.

Use analytic benchmarks wherever possible.

PUBLICATION STANDARD
====================

Write the report as though hostile but fair expert reviewers will inspect it.

For every major result include:

    claim
    equation
    assumptions
    numerical method
    validation
    uncertainty
    limitations
    interpretation.

Maintain three labels throughout the project:

    ESTABLISHED PHYSICS
    SPECULATIVE THEORETICAL MODEL
    ORIGINAL EXPLORATORY MODEL.

Never blur them.

Do not claim:

- novelty without literature evidence;
- a warp drive exists;
- negative energy can be engineered at required scale;
- Casimir energy automatically produces warp geometry;
- entanglement sends messages instantaneously;
- a simulation proves nature permits the metric;
- a metric solution proves a source can manufacture it;
- AI has discovered new physics merely because an optimiser found a
  numerical minimum.

NOVELTY STRATEGY
================

Do not make the novelty claim "microscopic warp communication", because a
Hyperwave proposal already exists.

Instead investigate possible contributions such as:

- a universal information-theoretic FTL test based on pre-lightcone mutual
  information;
- observer-robust energy-condition evaluation;
- moving-endpoint causal corridors;
- full stress-energy tensor matching rather than total-energy matching;
- integrated Hyperwave replication and falsification;
- inverse source design;
- Planck-scale validity maps;
- global causality tests for two-way operation;
- comparison of speculative FTL ideas and capacity-optimised ordinary
  interstellar links in one reproducible framework.

Before claiming any of these as novel, perform a serious literature search.

Do not infer novelty simply because keyword searches fail.

DELIVERABLES
============

Build this project iteratively but produce working artefacts, not just a
proposal.

The complete target deliverable is:

1. research-grade repository;
2. equations and derivations;
3. tested scientific Python implementation;
4. frozen Proxima/astrometric input data;
5. interactive 3D visualisation;
6. optical interstellar link simulator;
7. quantum no-signalling simulator;
8. Lorentz/causality simulator;
9. GR metric/stress-energy engine;
10. Alcubierre benchmark;
11. Hyperwave replication;
12. exploratory Moving-Observer Causal Corridor;
13. energy-condition maps;
14. null-geodesic simulator;
15. inverse stress-energy-source optimiser;
16. predictive-twin AI communications experiment;
17. publication-quality figures;
18. CSV/JSON exports;
19. complete validation suite;
20. full technical report;
21. six-page illustrated summary;
22. audit and limitations report;
23. literature-search record;
24. reproducibility instructions.

FIRST TASK
==========

Do not immediately write thousands of lines of code.

First inspect the supplied research report and derive the full scientific
specification.

Produce:

A. the exact research hypothesis;
B. null and alternative hypotheses;
C. the operational definition of FTL information transfer;
D. invariant quantities we will measure;
E. candidate mechanisms;
F. falsification criteria for each mechanism;
G. baseline physical models;
H. required datasets;
I. mathematical derivations;
J. simulation architecture;
K. uncertainty model;
L. validation matrix;
M. repository architecture;
N. interactive-visualisation specification;
O. literature questions that must be resolved before novelty claims;
P. milestone sequence.

Then critically attack the proposal.

Identify any conceptual errors, hidden assumptions, coordinate artifacts,
energy-condition mistakes, causality problems or impossible experiments.

Correct them before implementation.

After that specification is complete, begin implementing the repository from
the foundations upward.

MOST IMPORTANT ATTITUDE
=======================

Think ambitiously but behave scientifically.

The goal is not to make science fiction sound plausible.

The goal is to push established physics as hard as possible, identify the
exact boundary where known physics stops, create the best falsifiable
calculation we can, and make every result independently reproducible.

A negative result is a scientific result.

A physically realistic near-c interstellar communications design is a useful
result.

A new mathematical spacetime is a theoretical result, not automatically an
engineering result.

And a genuine statistically verified pre-lightcone transfer of newly chosen
information would require extraordinary evidence, independent replication
and complete causal-systematics analysis.

Start from first principles.