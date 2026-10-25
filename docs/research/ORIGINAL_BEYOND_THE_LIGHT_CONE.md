# Archive: original deep-research report

> **Historical source material.** Preserved for provenance, not a peer-reviewed result or experimentally confirmed FTL system. Old `cite` and `filecite` markers are inherited from the source conversation and must be reconciled with the independently linked source ledger. Mentions of Moving Observer are historical comparisons; this repository is a separate project.

---

# Beyond the Light Cone: A Research Programme for Interstellar Communication

## Executive finding and connection to Moving Observer

I reviewed this question from two different directions: first as a fundamental-physics problem—*can controllable information arrive outside the ordinary future light cone?*—and second as an engineering problem—*if the light-speed limit survives, what is the closest thing to an optimal interstellar communication system that physics permits?* I also examined the structure of your **Moving Observer** repository so that the proposed project grows naturally from your existing work rather than becoming an unrelated speculative exercise.

Your current research style is unusually well suited to this problem. *Moving Observer* already separates coordinate frames from physical observables, propagates stellar motion, explicitly treats Proxima Centauri, distinguishes path length from observer–target separation, performs weak-field and first-post-Newtonian calculations, uses frozen Gaia data, propagates uncertainty, performs sensitivity tests and—importantly—states what each model *cannot* establish. fileciteturn2file0L2-L2 The accompanying catalogue experiment applies the same discipline: fixed populations, paired controls, correlated uncertainties, explicit thresholds and reproducible numerical tests rather than turning an attractive idea into an unsupported discovery claim. fileciteturn3file0L2-L2

That methodology is precisely what a serious faster-than-light communication project needs.

The central conclusion of the research is:

> **There is currently no experimentally demonstrated carrier, modulation scheme, quantum protocol or electronic system capable of transmitting controllable information faster than \(c\).**

This does **not** mean that every imaginable future theory mathematically forbids effective FTL communication. General relativity contains geometries—warp spacetimes, traversable-wormhole constructions and related solutions—in which the ordinary Minkowski-space distance between two endpoints is no longer the correct measure of causal travel time. Alcubierre's original construction is the famous example, and modern theoretical work continues to investigate such geometries. However, converting those metrics into physical devices runs into severe questions involving stress-energy sourcing, negative-energy restrictions, horizons, stability and causality; a major 2026 analysis specifically warns that several claims of physical warp-drive feasibility arise from misunderstandings or incomplete restrictions. citeturn16search0turn12search0turn12search1

There is, however, one particularly important discovery from this literature search for **your exact idea**. A paper titled *Hyperwave: Hyper-Fast Communication within General Relativity* has already proposed using a microscopic warp structure specifically for faster-than-light communication rather than transporting a spacecraft. Its author proposes a pre-established tube of exotic stress-energy and encoding information in particles released when microscopic warp structures decelerate. Therefore, simply proposing "make the warp bubble tiny and use it only for communication" would **not** be a defensible novelty claim. citeturn11search0turn11search4

That finding actually gives us a better research direction.

The strongest project is not:

> "I have invented faster-than-light communication."

It is:

> **"I have constructed a reproducible computational framework that asks exactly what physical conditions would be required for controllable information to cross a spacelike interval, tests every serious candidate against the same causality and information-theoretic criteria, performs inverse stress-energy design for warp/hyperwave geometries, and establishes quantitatively where known physics stops."**

I would provisionally call this project **Causal Frontier**, with a research branch called **Moving Observer: Causal Corridor**.

That could become a genuinely interesting continuation of your portfolio because it connects the question "what does a moving observer see?" to the much deeper question:

\[
\boxed{\text{What events can a moving observer causally influence?}}
\]

The most useful "Einstein-like" move here is not to assume that \(c\) can be beaten. It is to identify exactly which assumption creates the speed limit, systematically remove assumptions one at a time, and calculate what happens.

### A correction to the Proxima example

There is also an important numerical correction to the example in your question. Proxima Centauri is not expected to reach its closest Solar encounter in the next hundred or thousand years. A 2026 Gaia-based encounter study predicts a minimum Sun–Proxima separation of

\[
d_{\min}=0.9679\pm0.0044\ {\rm pc}
\]

in

\[
26.574\pm0.028\ {\rm kyr},
\]

or roughly **26,600 years from now**. That minimum separation is approximately

\[
0.9679(3.26156)\simeq3.157\ {\rm light\ years}.
\]

The paper treats Proxima as part of the Alpha Centauri triple system for this encounter calculation. citeturn15view0turn15view1

At closest approach, therefore, an ordinary electromagnetic message would still require approximately

\[
t_{\rm one-way}\approx3.16\ {\rm years},
\]

and a request followed immediately by a reply would require at least

\[
t_{\rm RTT}\approx6.31\ {\rm years}.
\]

At today's roughly 4.2-light-year scale, the corresponding round-trip latency is roughly 8.5 years. Better transmitters can increase the number of bits delivered; they cannot reduce that propagation latency if the signal remains confined to the ordinary light cone.

That distinction—**bandwidth versus causal latency**—is the foundation of the entire proposed project.

## The physical barrier we actually have to defeat

### The light cone, not electromagnetic wavelength, is the obstacle

It is tempting to search for another wavelength, particle or modulation method: radio, optical, X-rays, gamma rays, neutrinos, gravitational waves, quantum states and so forth. But wavelength is not the fundamental limitation.

In flat spacetime the invariant interval is

\[
ds^2=-c^2dt^2+dx^2+dy^2+dz^2.
\]

For two events separated by \((\Delta t,\Delta\mathbf{x})\),

\[
\Delta s^2=
|\Delta\mathbf{x}|^2-c^2\Delta t^2.
\]

They are:

\[
\begin{cases}
\Delta s^2<0 & \text{timelike}\\[4pt]
\Delta s^2=0 & \text{null}\\[4pt]
\Delta s^2>0 & \text{spacelike}.
\end{cases}
\]

An ordinary light signal follows the boundary,

\[
|\Delta\mathbf{x}|=c\Delta t.
\]

To send information "faster than light" in the strong sense you are asking about means deliberately creating a message-dependent effect at a **spacelike-separated event**:

\[
|\Delta\mathbf{x}|>c\Delta t.
\]

Relativistic quantum field theory implements this causal structure through microcausality: observables associated with spacelike-separated local regions commute. Modern work continues to establish the relationship between no-signalling and this microcausal structure. citeturn13search7turn13search3turn13search11

So changing from radio photons to optical photons does not solve the problem.

Neither does changing to another experimentally known messenger. Neutrino time-of-flight measurements are compatible with propagation at \(c\), not controllably above it. citeturn13search1turn13search13 Gravitational waves are not an escape route either: the joint GW170817/GRB 170817A observation constrained their propagation speed relative to light to approximately

\[
-3\times10^{-15}
<
\frac{v_{\rm GW}-c}{c}
<
7\times10^{-16}.
\]

citeturn13search14

This leads to a fundamental design rule:

\[
\boxed{\text{A new carrier is insufficient unless it possesses a new causal propagation law.}}
\]

### Why ordinary FTL immediately creates a causality problem

Suppose Earth transmits a message over distance \(L\) at a hypothetical speed

\[
u>c.
\]

In Earth's frame,

\[
\Delta x=L,\qquad
\Delta t=\frac{L}{u}.
\]

Now consider an observer moving at velocity \(v\). The Lorentz transformation gives

\[
\Delta t'
=
\gamma
\left(
\Delta t-\frac{v\Delta x}{c^2}
\right),
\]

where

\[
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.
\]

Substitution gives

\[
\boxed{
\Delta t'
=
\gamma L
\left(
\frac1u-\frac{v}{c^2}
\right)
}.
\]

Therefore

\[
\Delta t'<0
\]

whenever

\[
\boxed{
v>\frac{c^2}{u}.
}
\]

Take an apparently modest example:

\[
u=4c.
\]

Then the condition is only

\[
v>0.25c.
\]

For an observer moving at \(0.5c\),

\[
\gamma\simeq1.1547,
\]

and

\[
\frac{c\Delta t'}{L}
=
\gamma
\left(
\frac{c}{u}-\frac vc
\right)
=
1.1547(0.25-0.5)
\approx-0.289.
\]

In that inertial frame, reception occurs **before transmission**.

This is not merely a semantic issue about coordinates. Once controllable FTL communication can be performed in suitable relative frames, one can attempt a return message and construct tachyonic-antitelephone-type causal loops. This connection between superluminal signalling and reversed event ordering is a central reason FTL communication is far more profound than making a faster radio transmitter. Work on superluminal propagation in relativistic frameworks consequently has to address global causality, not merely local speed. citeturn11search12turn13search7

This observation gives *Moving Observer* an unusually natural entrance into the problem.

Your next project can literally animate the transformation above:

```text
Earth frame

transmission A ●
               \
                \  hypothetical u > c
                 \
                  ● reception B

light cone:       /
                 /
                /


boosted frame

reception B ●
             \
              \
               ● transmission A

          Δt' < 0
```

The visualisation could let a researcher vary \(u/c\), \(v/c\), distance and return-path assumptions and watch the causal ordering change.

### The correct experimental definition of "FTL"

This project should not define success as a pulse peak apparently arriving early, an entangled correlation appearing instantaneously, or a numerical metric yielding an exotic coordinate velocity.

Define a binary transmitted message

\[
X\in\{0,1\}
\]

and the receiver's observation before the ordinary light-front arrival as \(Y\).

The mutual information is

\[
I(X;Y)
=
\sum_{x,y}
p(x,y)
\log_2
\frac{p(x,y)}
{p(x)p(y)}.
\]

A genuine FTL communication observation requires:

\[
\boxed{
I(X;Y_{\rm pre-lightcone})>0
}
\]

with a statistically significant result and with no causal side channel carrying information from \(X\) to the receiver.

This is much stronger than asking whether two detectors exhibit correlated outputs.

I would make that equation the **central falsification criterion of the entire project**.

## Every serious candidate mechanism

The literature does not give us one promising, overlooked particle that can simply be modulated faster than light. Instead, candidate ideas fall into fundamentally different categories.

| Candidate | What is real today? | FTL controllable information? | Research verdict |
|---|---|---:|---|
| Electromagnetic photons | Mature communications technology | **No** | Engineering baseline |
| Neutrinos | Produced and detected experimentally | **No evidence** | Poor FTL candidate |
| Gravitational waves | Directly detected astrophysically | **No; observed speed is extremely close to \(c\)** | Not an FTL carrier |
| Quantum entanglement | Strongly experimentally established | **No** | Valuable no-signalling control |
| Quantum teleportation | Experimentally demonstrated | **No** without classical communication | Valuable control |
| "Fast-light" / anomalous wave propagation | Wave reshaping phenomena exist | **No demonstrated pre-lightcone information channel** | Must test information front, not peak |
| Tachyons | Mathematical hypothetical particles | **No experimental evidence** | Useful causality simulation |
| Traversable wormholes | Theoretical solutions/models exist | **No engineering route demonstrated** | Deep theoretical candidate |
| Warp spacetime | Valid classes of GR metrics exist | **No physical FTL device demonstrated** | Best speculative modelling target |
| Microscopic "Hyperwave" | Published theoretical proposal | **Unverified** | Closest literature match to your original idea |
| Lorentz-violating/extra-dimensional channels | Model-dependent theoretical possibilities | **No demonstrated communication channel** | Boundary research |

The experimental evidence for Bell nonlocality is very strong. For example, Hensen and collaborators performed a loophole-free Bell test using electron spins separated by 1.3 km. But Bell nonlocality is not the same thing as sending a controllable message outside the light cone. citeturn13search0

### Why quantum entanglement does not solve it

Suppose Alice and Bob share the Bell state

\[
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Bob's reduced state is

\[
\rho_B
=
{\rm Tr}_A
\left(
|\Phi^+\rangle\langle\Phi^+|
\right)
=
\frac{I}{2}.
\]

Alice can choose a measurement basis, but Bob's locally observable probability distribution remains independent of that choice until additional classical information arrives. In general, a bipartite correlation obeys no-signalling when

\[
\sum_a P(a,b|x,y)
\]

is independent of Alice's setting \(x\), and correspondingly Alice's marginal is independent of Bob's setting.

Quantum teleportation is sometimes misunderstood in exactly this context. Relativistic formulations of teleportation explicitly retain a causal classical-communication component; entanglement supplies a resource, but it does not eliminate the classical information transfer. citeturn11search2turn11search12

So a Proxima station stocked in advance with \(10^{30}\) entangled pairs would still not let Earth choose "0" or "1" today and allow Proxima to discover that choice instantaneously.

That negative result should actually be included experimentally in **Causal Frontier**. Simulate an entangled channel and demonstrate

\[
I(X;Y_{\rm Bob})=0
\]

before the classical message arrives.

It becomes the project's first calibration test: the framework must correctly reject something that looks nonlocal but cannot communicate.

### Wormholes are more interesting, but much harder

A traversable wormhole changes the topology/geometry of the path rather than propelling a particle locally past \(c\). This distinction matters.

The Einstein field equations are

\[
\boxed{
G_{\mu\nu}
+
\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
}
\]

The conceptual programme is:

\[
T_{\mu\nu}
\longrightarrow
g_{\mu\nu}
\longrightarrow
\text{causal geodesics}.
\]

A celebrated Gao–Jafferis–Wall construction found that an interaction producing negative average null energy could render an Einstein–Rosen bridge traversable in its theoretical setting. Significantly, the authors explicitly noted that their construction cannot be used to violate causality. citeturn11search1

That is a theme throughout serious wormhole work: making a mathematical throat traversable is not equivalent to obtaining an arbitrary time machine or laboratory communication instrument.

The relevant null-energy condition is

\[
T_{\mu\nu}k^\mu k^\nu\ge0
\]

for every null vector \(k^\mu\).

An averaged version along a null geodesic is approximately

\[
\int_{\gamma}
T_{\mu\nu}
k^\mu k^\nu
d\lambda
\ge0.
\]

Traversability in many constructions requires violating such classical energy conditions. Quantum field theory does permit negative local energy densities, but it constrains their magnitude and duration through quantum energy inequalities rather than offering an unrestricted reservoir of exotic energy. citeturn17search0turn17search11

### Warp geometry is the most useful speculative direction

Alcubierre's idea was fundamentally different from accelerating a particle through local space beyond \(c\). He specified a spacetime metric that contracts and expands geometry so that a region could have an arbitrarily large effective coordinate displacement while objects inside remain locally timelike. The original work already acknowledged that exotic matter would be required. citeturn16search0

A representative form of the metric is

\[
ds^2
=
-c^2dt^2
+
[dx-v_s(t)f(r_s)dt]^2
+
dy^2+dz^2,
\]

where

\[
r_s=
\sqrt{
[x-x_s(t)]^2+y^2+z^2
}
\]

and \(f(r_s)\) is a shape function satisfying approximately

\[
f\rightarrow1
\quad\text{inside the bubble},
\]

\[
f\rightarrow0
\quad\text{outside}.
\]

This gives us something computationally concrete.

Given

\[
g_{\mu\nu}(x^\alpha),
\]

we calculate the Christoffel symbols,

\[
\Gamma^\rho_{\mu\nu}
=
\frac12g^{\rho\sigma}
\left(
\partial_\mu g_{\nu\sigma}
+
\partial_\nu g_{\mu\sigma}
-
\partial_\sigma g_{\mu\nu}
\right),
\]

then curvature,

\[
R^\rho_{\ \sigma\mu\nu},
\]

the Ricci tensor,

\[
R_{\mu\nu},
\]

Ricci scalar,

\[
R,
\]

and Einstein tensor,

\[
G_{\mu\nu}
=
R_{\mu\nu}
-\frac12Rg_{\mu\nu}.
\]

We then invert Einstein's equation:

\[
\boxed{
T_{\mu\nu}^{\rm required}
=
\frac{c^4}{8\pi G}
\left(
G_{\mu\nu}
+\Lambda g_{\mu\nu}
\right).
}
\]

This is the key idea for your project.

Instead of saying:

> "Here is a warp metric, therefore it can be built",

we ask:

> "What exact energy density, pressure, momentum flux, anisotropic stress and spacetime curvature would nature have to provide at every point for this metric to exist?"

That is a much more powerful scientific question.

Modern warp-drive literature is still actively contested. Bobrick and Martire constructed general models including positive-energy **subluminal** spherical warp drives and explored superluminal configurations under quantum-inequality constraints. citeturn16search1turn16search4 Lentz proposed positive-energy hyper-fast soliton solutions sourced in an Einstein–Maxwell–plasma framework. citeturn16search5turn16search8 But Santiago, Schuster and Visser subsequently argued that physically reasonable generic warp drives violate the null energy condition, and recent analyses continue scrutinising these constructions. citeturn12search1turn12search5

A 2026 classification study goes still further, highlighting misconceptions and errors in parts of the contemporary warp-drive literature and deriving additional no-go results. citeturn12search0turn12search4

Therefore this field remains an excellent place for **critical computational research**, but not a place where we should write "physics has solved warp drive".

### The Hyperwave idea is extremely close to what you independently imagined

Lorenzo Pieri's *Hyperwave* proposal deliberately shrinks the warp structure because communication does not need to transport people, spacecraft or even conventional equipment. The paper argues that the total negative-energy requirement falls dramatically in the small-radius limit and suggests a tubular prearranged structure through which microscopic warp configurations could travel; their deceleration would release energetic particles that could represent information. citeturn11search0turn16search12

This is conceptually very close to:

> "Don't send a spacecraft faster than light. Send the smallest possible physical disturbance that represents one bit."

That is an excellent insight—but because it is already in the literature, we need to go one step deeper.

The strongest research question becomes:

\[
\boxed{
\text{Can a microscopic spacetime pulse that represents one bit have a physically realisable }T_{\mu\nu}?
}
\]

And then:

\[
\boxed{
\text{Does it transmit new mutual information outside the background light cone without creating causal inconsistency?}
}
\]

That is where I believe your project can become interesting.

## A new research architecture: Causal Corridor

I would build the project around **three layers**, deliberately separating established physics, speculative physics and practical engineering.

### The fundamental layer: Causal Frontier

The first layer answers only:

> **What would count as evidence for superluminal communication?**

Create two moving observers,

\[
O_A:\quad z_A^\mu(\tau_A)
\]

and

\[
O_B:\quad z_B^\mu(\tau_B).
\]

At transmitter event \(A\), observer \(O_A\) randomly chooses

\[
X\in\{0,1\}.
\]

The receiving observer records all detector output \(Y(t)\).

In the ordinary background metric \(g^{(0)}_{\mu\nu}\), calculate the first possible light arrival,

\[
t_c.
\]

Then divide receiver data into

\[
Y_< =Y(t<t_c)
\]

and

\[
Y_\ge=Y(t\ge t_c).
\]

The primary statistic is

\[
I_< =I(X;Y_<).
\]

The null hypothesis becomes

\[
H_0:
I_<=0.
\]

The extraordinary hypothesis is

\[
H_1:
I_<>0.
\]

This automatically rejects dozens of misleading effects.

A detector pulse that moves earlier because of filter reshaping does not pass unless the transmitted choice can be decoded.

A quantum correlation does not pass unless Bob's local outcomes reveal Alice's choice.

A simulation with an apparent coordinate speed \(>c\) does not pass unless the two message events are spacelike under the baseline metric.

A system using prearranged information at the receiver does not pass because \(Y\) must depend on the **newly and randomly selected** \(X\).

This is the single most important methodological innovation I would put at the centre of the work.

### The speculative layer: metric inverse design

Now define a candidate modified spacetime,

\[
g_{\mu\nu}
=
\eta_{\mu\nu}
+h_{\mu\nu},
\]

where

\[
\eta_{\mu\nu}
\]

is Minkowski spacetime and \(h_{\mu\nu}\) is the engineered perturbation.

Instead of guessing the material, specify a communications objective:

\[
\mathcal{J}
=
w_t\,t_{\rm arrival}
+
w_E\,E_{\rm abs}
+
w_K\,K_{\rm curvature}
+
w_C\,C_{\rm causality}
+
w_Q\,Q_{\rm inequality}.
\]

Here:

\[
E_{\rm abs}
=
\int |\rho|\,dV,
\]

rather than only

\[
\int\rho\,dV,
\]

because positive and negative energy cancellation must not hide enormous local requirements.

A useful maximum-curvature metric might include the Kretschmann scalar

\[
K
=
R_{\alpha\beta\gamma\delta}
R^{\alpha\beta\gamma\delta}.
\]

For each candidate metric, calculate

\[
T_{\mu\nu}
=
\frac{c^4}{8\pi G}G_{\mu\nu}.
\]

Then decompose it for an observer with four-velocity \(u^\mu\).

Energy density:

\[
\rho
=
T_{\mu\nu}u^\mu u^\nu.
\]

Energy flux:

\[
q_\alpha
=
-h_\alpha^{\ \mu}T_{\mu\nu}u^\nu.
\]

Spatial stress:

\[
S_{\alpha\beta}
=
h_\alpha^{\ \mu}
h_\beta^{\ \nu}
T_{\mu\nu}.
\]

Now test whether the required tensor resembles **anything physically producible**.

That distinction is crucial because a metric is not an engineering design.

A symbolic equation saying

\[
G_{\mu\nu}=8\pi GT_{\mu\nu}/c^4
\]

only tells us what matter would be required. It does not show that the required matter exists.

### The candidate I would investigate

Call it the **Moving-Observer Causal Corridor**, or MOCC.

Let Earth and Proxima follow moving endpoint worldlines,

\[
z_E^\mu(\tau_E),
\qquad
z_P^\mu(\tau_P).
\]

Rather than assuming stationary endpoints, use actual astrometric propagation—the direct continuation of *Moving Observer*. Your existing work already emphasises the importance of relative motion and proper frame definitions. fileciteturn2file0L2-L2

Define a world-tube connecting the moving endpoints.

For example,

\[
\mathbf{x}_c(s,t)
=
(1-s)\mathbf{x}_E(t)
+
s\mathbf{x}_P(t),
\qquad
0\le s\le1.
\]

Define perpendicular distance from any point to that instantaneous corridor as

\[
r_\perp(\mathbf{x},t)
=
\left\|
\mathbf{x}
-
\mathbf{x}_c(s_\ast,t)
\right\|.
\]

Then introduce a smooth corridor function

\[
F(r_\perp)
=
\frac12
\left[
1-\tanh
\left(
\frac{r_\perp-R}{\Delta}
\right)
\right],
\]

with radius \(R\) and wall thickness \(\Delta\).

The computer can then explore candidate shift fields,

\[
\boldsymbol{\beta}(\mathbf{x},t)
=
v_{\rm eff}(t)
F(r_\perp)
\,\hat{\mathbf{s}},
\]

in a \(3+1\) metric,

\[
ds^2
=
-\alpha^2 c^2dt^2
+
\gamma_{ij}
(dx^i+\beta^i dt)
(dx^j+\beta^jdt).
\]

We then **do not assume the metric is physical**.

We ask the computer:

\[
\text{What }T_{\mu\nu}\text{ would this corridor require?}
\]

and:

\[
\text{Does any observer measure }\rho<0?
\]

\[
\text{Does }T_{\mu\nu}k^\mu k^\nu<0?
\]

\[
\text{Does ANEC fail?}
\]

\[
\text{Do quantum-energy bounds become catastrophic?}
\]

\[
\text{Does }K\rightarrow l_P^{-4}\text{ anywhere?}
\]

\[
\text{Does a horizon form?}
\]

\[
\text{Can the transmitter actually create/control the leading edge?}
\]

\[
\text{Can two corridors form a closed causal curve?}
\]

That would turn an imaginative idea into a very serious computational experiment.

### The Planck-scale trap

This is particularly important when evaluating the Hyperwave argument.

One can reduce a **total integrated energy** by shrinking the bubble to an extraordinarily small radius. But if the geometry is pushed towards Planckian dimensions,

\[
l_P
=
\sqrt{\frac{\hbar G}{c^3}}
\approx1.616\times10^{-35}\ {\rm m},
\]

then classical general relativity itself is no longer obviously a trustworthy description.

Therefore:

\[
\boxed{
\text{small total energy}
\not\Rightarrow
\text{physically easy geometry}.
}
\]

One might instead obtain very small volume multiplied by fantastically large energy density and curvature.

Earlier quantum-inequality work on the Alcubierre metric found precisely this kind of difficulty, deriving extremely small wall-thickness scales and enormous energetic requirements under its assumptions. citeturn17search2 More recent analyses continue to evaluate warp metrics against quantum-energy restrictions rather than treating local negative energy as freely scalable. citeturn17search8

This is one of the most valuable things your project could test quantitatively.

### Casimir energy is not automatically a warp-drive power supply

The ideal parallel-plate Casimir energy scales as

\[
\frac{E_{\rm Cas}}{A}
=
-\frac{\pi^2\hbar c}{720a^3},
\]

with pressure

\[
P_{\rm Cas}
=
-\frac{\pi^2\hbar c}{240a^4},
\]

where \(a\) is plate separation.

The existence of quantum-vacuum/Casimir effects demonstrates that naïve classical positive-energy assumptions require qualification; it does **not** establish that an arbitrary negative stress-energy tensor can be assembled at macroscopic scale and shaped into a warp metric. Current quantum-energy-inequality research specifically concerns the restrictions on the amount and duration of negative energy. citeturn17search0turn17search1

So our code should never compare only:

\[
E_{\rm needed}
\stackrel{?}{<}
E_{\rm Casimir}.
\]

It needs to compare the **complete tensors**

\[
T_{\mu\nu}^{\rm required}
\quad\text{versus}\quad
T_{\mu\nu}^{\rm candidate}.
\]

A matching scalar energy is insufficient.

This could be a particularly strong contribution because it converts the vague question "is enough negative energy available?" into the much harder and scientifically correct question:

\[
\boxed{
\|T_{\mu\nu}^{\rm required}
-
T_{\mu\nu}^{\rm realisable}\|
\rightarrow0?
}
\]

### AI's real role

AI does not alter the light cone.

But it can perform three legitimate roles.

First, it can search a parameter space of metrics:

\[
\Theta
=
\{
R,\Delta,v_s,
\alpha,\beta^i,
\gamma_{ij},\ldots
\}
\]

and minimise a constrained functional,

\[
\Theta^\ast
=
\arg\min_\Theta \mathcal J(\Theta).
\]

Automatic differentiation and GPU optimisation could search millions of metric variants while imposing Einstein-equation and energy-condition penalties.

Second, symbolic AI can search families of \(T_{\mu\nu}\) produced by known fields—electromagnetic fields, plasmas, scalar fields or quantum-vacuum models—and see how closely those tensors approach the required source.

Third, AI can reduce the *subjective* experience of interstellar latency without changing propagation speed.

Suppose Earth and Proxima maintain predictive digital twins. Instead of repeatedly transmitting full state \(s_t\), each side predicts

\[
\hat{s}_t=f_\theta(s_{<t})
\]

and transmits only innovation,

\[
e_t=s_t-\hat{s}_t.
\]

The information burden is then approximately determined by

\[
H(S_t|\hat S_t)
\]

rather than

\[
H(S_t).
\]

That can reduce communications traffic enormously when both sides share predictive models.

It cannot make a newly chosen bit arrive sooner than the light front—but for an autonomous interstellar civilisation, it could make a multi-year-delay network behave surprisingly coherently.

I would include this as a separate engineering contribution called **Predictive Twin Communication** so that even if the FTL hypothesis fails, the project still produces a genuinely useful communications concept.

## What we could actually build and simulate

The project should deliberately have a **physical branch that can be built with known technology** and a **speculative branch that remains computational until new physics exists**.

### The practical interstellar link

For an actual long-range interstellar system, photons remain the strongest baseline. Interstellar links are profoundly photon-starved, which makes photon information efficiency more relevant than terrestrial-style high spectral efficiency. Work on interstellar downlinks therefore emphasises pulse-position modulation and photon-counting techniques. citeturn11search7turn11search10

A 2025 experiment demonstrated **14.5 information bits per incident photon** at 1550 nm after 87.5 dB attenuation using very-high-order pulse-position modulation, illustrating how much information can be extracted from a photon-starved optical channel. citeturn11search3

This is where a "best modulation technique for Proxima" question becomes technically meaningful.

For \(M\)-ary pulse-position modulation, one pulse occupies one of \(M\) temporal slots:

\[
\text{bits/symbol}
=
\log_2M.
\]

For

\[
M=1024,
\]

that is

\[
10\ {\rm bits/symbol}.
\]

For

\[
M=65536,
\]

it is

\[
16\ {\rm bits/symbol}.
\]

At the quantum-optical level, one useful pure-loss channel capacity expression in terms of mean received photons per mode \(n_s\) is

\[
\frac{C_{\rm GH}}{B}
=
\log_2(1+n_s)
+
n_s
\log_2
\left(
1+\frac1{n_s}
\right),
\]

which illustrates why extremely low photon occupancy can produce high information per photon even though absolute data rates may remain low. Photon-efficient experimental work is now approaching these extreme regimes. citeturn11search3

A practical architecture would therefore resemble:

```text
Scientific data
      ↓
AI predictive/delta encoder
      ↓
source compression
      ↓
error-correcting code
      ↓
high-order PPM mapper
      ↓
FPGA timing engine
      ↓
narrow-linewidth laser
      ↓
electro-optic / pulsed modulator
      ↓
large transmitting aperture
      ↓
===============================
         INTERSTELLAR SPACE
         propagation ≈ c
===============================
      ↓
large receiving telescope
      ↓
ultra-narrow optical filter
      ↓
SNSPD photon detector
      ↓
time-to-digital converter
      ↓
PPM/FEC decoder
      ↓
AI predictive-state reconstruction
      ↓
Recovered information
```

Photon-efficient deep-space communication literature already treats high-order PPM as a natural format in this environment, while experimental quantum-optical receiver research is exploring measurements that outperform simple independent on/off slot detection. citeturn11search10turn11search19

### A simple Proxima-scale link calculation

Consider an illustrative—not mission-approved—system:

\[
\lambda=1\ \mu{\rm m},
\]

\[
D_t=10\ {\rm m},
\]

\[
D_r=30\ {\rm m},
\]

\[
P_t=1\,{\rm kW},
\]

and distance

\[
R\simeq4.24\ {\rm ly}
\simeq4.01\times10^{16}\ {\rm m}.
\]

For a diffraction-limited circular transmitter, the first-null angular scale is approximately

\[
\theta
\simeq
1.22\frac{\lambda}{D_t}.
\]

Thus

\[
\theta
\simeq
1.22\times10^{-7}\ {\rm rad}.
\]

The approximate beam radius at Proxima is then

\[
r_b
\simeq
R\theta
\simeq
4.89\times10^9\ {\rm m}.
\]

If we use a crude uniform-disc geometric estimate for illustration,

\[
\eta_{\rm geo}
\sim
\frac{
\pi(D_r/2)^2
}{
\pi r_b^2
}
\simeq9.4\times10^{-18}.
\]

The received power before optical losses is approximately

\[
P_r
\sim
P_t\eta_{\rm geo}
\simeq
9.4\times10^{-15}\ {\rm W}.
\]

At \(1\,\mu{\rm m}\), photon energy is

\[
E_\gamma
=
\frac{hc}{\lambda}
\simeq
1.99\times10^{-19}\ {\rm J}.
\]

Therefore the idealised incident photon rate is of order

\[
\dot N_\gamma
=
\frac{P_r}{E_\gamma}
\simeq4.7\times10^4\ {\rm photons\,s^{-1}}.
\]

With an illustrative aggregate efficiency of \(20\%\),

\[
\dot N_{\rm det}
\sim9.5\times10^3\ {\rm s^{-1}}.
\]

A real link model must replace this simplified area-ratio estimate with the Airy intensity profile and include pointing loss, atmospheric transmission if applicable, telescope throughput, detector efficiency, stellar background, zodiacal background, interstellar extinction, finite linewidth, clock errors and coding margins. But it demonstrates the correct engineering principle:

\[
\boxed{
D_t,\ D_r,\ P_t,\ \lambda,\ \text{coding}
\quad\text{can improve bit rate tremendously}
}
\]

while

\[
\boxed{
t_{\rm propagation}=\frac Rc
}
\]

does not change.

### Electronics for a terrestrial prototype

A first physical prototype would not attempt warp generation. It would demonstrate the communications and falsification infrastructure.

| Subsystem | Realistic prototype hardware |
|---|---|
| Source | Narrow-linewidth 1064 nm or 1550 nm laser |
| Modulation | Electro-optic modulator or picosecond pulsed source |
| Encoder | FPGA implementing high-order PPM |
| Error correction | LDPC, Reed–Solomon or concatenated PPM coding |
| Timing | GPS-disciplined or optical/atomic-clock-derived reference |
| Transmission | Beam expander and motorised tracking stage |
| Receiver | Telescope plus narrowband optical filtering |
| Photon detector | SNSPD where available; SPAD for lower-cost prototype |
| Timing | Picosecond/nanosecond time-to-digital converter |
| Compute | FPGA plus workstation/GPU |
| Analysis | Python scientific stack and reproducible Monte Carlo pipeline |

That hardware branch would establish your project's **real communications competence** even while the GR branch remains theoretical.

### A second physical experiment: quantum no-signalling

A more ambitious laboratory extension could include:

\[
\text{SPDC entangled-photon source}
\rightarrow
\text{Alice}
+
\text{Bob}.
\]

Alice's settings should come from a fast random source.

Bob's entire time series is recorded independently.

Then deliberately try to classify Alice's randomly chosen setting from Bob's local data before receiving Alice's classical record.

Expected result:

\[
I(X_{\rm Alice};Y_{\rm Bob})\approx0.
\]

After the classical records are compared, Bell correlations appear.

This would give your project a beautiful experimental message:

> "Quantum mechanics gives nonlocal correlations—but our own communication criterion correctly distinguishes correlation from information transfer."

That conclusion is consistent with loophole-free Bell experiments and relativistic no-signalling structure. citeturn13search0turn13search3

### The simulation stack

I would implement the research in progressively harder layers.

The **special-relativity simulator** needs only NumPy/TypeScript and should calculate:

\[
x'=\gamma(x-vt),
\]

\[
t'=\gamma
\left(
t-\frac{vx}{c^2}
\right),
\]

light cones, hypothetical FTL trajectories, return paths and causality inversions.

The **information simulator** generates random transmitted messages, noisy detection records and computes:

\[
I(X;Y),
\]

bit-error rate,

\[
{\rm BER}
=
\frac{N_{\rm errors}}{N_{\rm bits}},
\]

false-positive probability and confidence intervals.

The **optical simulator** handles diffraction, photons, noise and PPM/FEC.

The **GR engine** computes:

\[
g_{\mu\nu},
\quad
g^{\mu\nu},
\quad
\Gamma^\rho_{\mu\nu},
\quad
R^\rho_{\ \sigma\mu\nu},
\quad
R_{\mu\nu},
\quad
R,
\quad
G_{\mu\nu},
\quad
T_{\mu\nu}.
\]

The **energy-condition engine** evaluates NEC/WEC/DEC/SEC across large observer samples rather than checking only one preferred observer. That is especially important because recent warp-drive criticism has emphasised that favourable energy density for one family of observers does not prove the full weak energy condition. citeturn12search1turn16search23

The **geodesic engine** integrates

\[
\frac{d^2x^\mu}{d\lambda^2}
+
\Gamma^\mu_{\alpha\beta}
\frac{dx^\alpha}{d\lambda}
\frac{dx^\beta}{d\lambda}
=
0.
\]

For a null signal,

\[
g_{\mu\nu}
\frac{dx^\mu}{d\lambda}
\frac{dx^\nu}{d\lambda}
=0.
\]

Then the key metric is not "bubble velocity".

It is:

\[
\boxed{
\Delta t_{\rm gain}
=
t_{\rm arrival}^{\rm background}
-
t_{\rm arrival}^{\rm candidate}.
}
\]

And simultaneously:

\[
E_{\rm req},
\quad
\rho_{\min},
\quad
K_{\max},
\quad
{\rm ANEC}_{\min},
\quad
{\rm QEI\ violation},
\quad
{\rm CTC\ flag}.
\]

That gives each candidate a multidimensional feasibility score rather than a sensational yes/no answer.

### Parameter sweeps

For every metric family, sweep logarithmically across:

\[
R
=
10^{-35}
\ {\rm m}
\rightarrow
10^3\ {\rm m},
\]

\[
\Delta/R
=
10^{-6}
\rightarrow1,
\]

and candidate effective speeds such as

\[
v_{\rm eff}/c
=
0.1,\ 0.5,\ 0.99,\ 1.001,\ 1.01,\ 1.1,\ 2,\ 10,\ 10^3.
\]

But any calculation approaching the Planck regime must be clearly flagged:

\[
R\sim l_P
\quad\Rightarrow\quad
\text{classical-GR reliability unknown}.
\]

We should never colour a Planck-scale simulation green and call it "feasible".

### Reproducing the Hyperwave paper should be the first speculative benchmark

Before inventing a new geometry, reproduce the published proposal.

That means:

\[
\text{paper equations}
\rightarrow
\text{independent implementation}
\rightarrow
\text{stress-energy maps}
\rightarrow
\text{geodesics}
\rightarrow
\text{energy-condition tests}
\rightarrow
\text{causal analysis}.
\]

Hyperwave is sufficiently close to your original concept that a rigorous independent reproduction gives us a valuable benchmark. citeturn11search0turn11search4

Then change one assumption at a time.

For example:

\[
\text{static endpoints}
\rightarrow
\text{moving Earth/Alpha Cen endpoints},
\]

\[
\text{scalar total energy}
\rightarrow
\text{full stress-energy matching},
\]

\[
\text{nominal warp velocity}
\rightarrow
\text{mutual-information arrival time},
\]

\[
\text{local energy condition}
\rightarrow
\text{observer-robust NEC/WEC/ANEC},
\]

\[
\text{one-way geometry}
\rightarrow
\text{return-path causality test}.
\]

That is much more likely to yield a defensible research contribution than starting with an arbitrary new metric and declaring it revolutionary.

### What would constitute a genuine breakthrough?

I would pre-register five levels.

| Level | Result | Scientific meaning |
|---|---|---|
| **A** | Better bits/photon or lower-energy interstellar link | Real communications engineering |
| **B** | New mathematical metric with interesting causal properties | Theoretical result |
| **C** | Required \(T_{\mu\nu}\) approximated by known physical fields | Major theoretical advance |
| **D** | Laboratory spacetime/field experiment produces statistically significant pre-lightcone \(I(X;Y)>0\) | Extraordinary new physics |
| **E** | Independent replication and causal-loop analysis survive | Physics-changing discovery |

For Level D, I would demand something like:

\[
I(X;Y_<)>0
\]

with a preregistered analysis,

\[
p\ll 5.7\times10^{-7}
\]

for a nominal five-sigma-scale discovery threshold, independent clocks, blinded message generation, physical isolation of all ordinary channels, independent replication and a systematic-error budget.

Anything weaker remains interesting—but should not be called FTL communication.

That scientific restraint is exactly what makes *Moving Observer* credible, and I would preserve it here. fileciteturn3file0L2-L2

## The research programme I would publish

The resulting paper/project should not be titled "I solved faster-than-light communication".

A stronger title would be:

> **Causal Frontier: A Reproducible Search for Information Transfer Beyond the Light Cone**

with the subtitle:

> **From Moving Observers and Quantum No-Signalling to Warp-Metric Inverse Design and Photon-Efficient Interstellar Links**

The core scientific question would be:

\[
\boxed{
\begin{aligned}
&\text{Given a random information source at event }A,\\
&\text{what physically admissible channel, if any, can create}\\
&I(X;Y)>0\text{ at a spacelike-separated event }B?
\end{aligned}
}
\]

The project then divides possible answers into:

\[
\mathcal C
=
\{
\text{EM},
\text{neutrino},
\text{GW},
\text{quantum},
\text{wormhole},
\text{warp},
\text{modified causality}
\}.
\]

Every candidate passes through the same pipeline:

\[
\boxed{
\text{Carrier/geometry}
\rightarrow
\text{propagation model}
\rightarrow
\text{message encoding}
\rightarrow
\text{receiver}
\rightarrow
I(X;Y)
\rightarrow
\text{causality audit}
}
\]

and, for spacetime-engineering candidates,

\[
\boxed{
g_{\mu\nu}
\rightarrow
G_{\mu\nu}
\rightarrow
T_{\mu\nu}
\rightarrow
\text{energy conditions}
\rightarrow
\text{physical source search}.
}
\]

This creates several publishable questions even if the final answer to FTL is "no".

One is whether any claimed superluminal scheme survives a **common information-theoretic definition of signalling**.

Another is whether microscopic warp communication really reduces the physical burden once **curvature, stress tensor structure and quantum-energy constraints** are included, rather than only total integrated energy. The published Hyperwave proposal makes this particularly timely. citeturn11search0turn17search2

Another is whether moving endpoints materially alter causal-corridor engineering. That is directly connected to your existing relative-motion research. fileciteturn2file0L2-L2

Another is how close a physically realizable stress-energy basis can approximate a desired metric:

\[
T_{\mu\nu}^{\rm candidate}
=
\sum_i a_i T_{\mu\nu}^{(i)},
\]

where \(i\) might represent electromagnetic fields, plasmas, scalar-field models or permitted quantum-vacuum configurations.

Then minimise

\[
\mathcal L_T
=
\int
w(x)
\left\|
T_{\mu\nu}^{\rm candidate}(x)
-
T_{\mu\nu}^{\rm required}(x)
\right\|^2
d^4x.
\]

If the minimum is enormous for every known source family, that is a meaningful negative result.

If an unexpected source family makes

\[
\mathcal L_T
\]

dramatically smaller, that is an interesting result.

If it reaches approximately zero while respecting all relevant physical constraints, *then* things become extraordinary.

The project should include an interactive 3D visualisation in the style of *Moving Observer*:

```text
VIEW: Ordinary light cone

                     future
                       │
                     / │ \
                   /   │   \
                 /     │     \
          c     /      │      \     c
               /       │       \
──────────────●─────────┼──────────── space
            transmit


VIEW: Candidate causal corridor

 Earth ●════════════════════════════● Proxima
       ╲                            ╱
        ╲ ordinary light cone     ╱
         ╲                        ╱

Toggle:
[ background metric ]
[ candidate metric ]
[ stress-energy density ]
[ NEC/WEC violations ]
[ curvature ]
[ null geodesics ]
[ observer frame ]
[ causal-loop test ]
```

Users should be able to change:

\[
R,\Delta,v_{\rm eff},D,
\]

observer velocity,

\[
v_{\rm obs},
\]

and model family, then instantly see:

\[
t_{\rm light},
\quad
t_{\rm candidate},
\quad
E_{\rm req},
\quad
\rho_{\min},
\quad
K_{\max},
\quad
{\rm NEC},
\quad
{\rm ANEC},
\quad
{\rm CTC}.
\]

This would make an abstract GR problem visually understandable while preserving rigorous equations underneath.

### My assessment of the scientific opportunity

The probability that present-day physics contains a simple, overlooked electronic modulation technique that sends messages to Proxima in minutes is extremely low given relativity, quantum-field-theoretic causality, Bell/no-signalling evidence, neutrino measurements and gravitational-wave propagation constraints. citeturn13search0turn13search9turn13search14turn13search7

But the research question is **not worthless**.

It becomes scientifically interesting precisely when framed as a falsifiable search over the boundary between:

\[
\text{nonlocal correlation},
\]

\[
\text{apparent superluminality},
\]

\[
\text{effective geometric shortcuts},
\]

and

\[
\text{actual controllable superluminal information}.
\]

Warp-drive research remains active in 2026, including new classification, energy-condition and observational-signature work, but it remains theoretical rather than an experimentally demonstrated engineering technology. citeturn12search0turn12search7turn12search13

So I would **not** make your project's thesis:

> "Einstein was wrong."

I would make it:

> **"We tried to break the light-cone communication bound as systematically as possible, with modern relativity, quantum information, numerical optimisation, AI and reproducible simulation—and here is exactly what must become physically possible before it can be broken."**

That is a much harder paper to dismiss.

And if some unforeseen feature of a candidate model actually survives all of those tests, you will have found something far more important than an attractive equation.

## Copy-paste prompt to turn this research into the project

The following prompt is designed to be pasted into a new ChatGPT conversation **together with this report**. It deliberately asks the model to behave like a rigorous research collaborator rather than a science-fiction generator.

```text
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
```

The crucial strategic choice is therefore **not** between "accept Einstein" and "challenge Einstein". It is between making an unfalsifiable FTL claim and constructing an experiment that would be capable of proving us wrong either way. The latter is much closer to how Einstein's own breakthroughs worked: identify which assumptions are operational, construct thought experiments that expose contradictions, derive the mathematics, then ask nature to decide. The experimental record so far strongly supports relativistic causal signalling even while allowing striking quantum nonlocal correlations and mathematically exotic spacetime solutions. citeturn13search0turn13search14turn13search7

For your research trajectory, **Causal Frontier / Moving Observer: Causal Corridor** is therefore the direction I would choose: not another "warp drive" demonstration, but a common mathematical, computational and information-theoretic framework for determining whether *anything* has genuinely carried a newly chosen bit outside its ordinary light cone.