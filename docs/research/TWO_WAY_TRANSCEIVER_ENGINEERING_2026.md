# Two-way interstellar transceiver: optical engineering and FTL falsification

*Research lead: Biswajit Jana · Engineering model v0.6 · 26 October 2026*

The starting question is whether Earth can send a **newly chosen message** to a receiver 4.24 light-years away and receive an immediate reply. For ordinary propagation through flat spacetime, the first transmission takes approximately **4.24 years** and the earliest immediate response takes another **4.24 years** (illustrative fixed separation). **Higher bit rates do not shorten the propagation time.**

The accompanying **12-page PDF** and six large SVG design drawings were generated locally and supplied in the v0.6 download package. The PDF and new SVG binaries/figures are **not yet uploaded to GitHub**; this document reproduces the critical system block diagrams directly using Mermaid, and provides working reference code.

## Both endpoints need transmit AND receive electronics

~~~mermaid
flowchart LR
  subgraph E["EARTH STATION"]
    E1["Optical Tx: PPM + FEC + telescope"] 
    E2["Optical Rx: photon count + FEC"]
  end
  subgraph P["PROXIMA STATION"]
    P1["Optical Rx: photon count + FEC"]
    P2["Optical Tx: PPM + FEC + telescope"]
  end
  E1 -- "Forward photons; approx. 4.24 years" --> P1
  P2 -- "Reply photons; another approx. 4.24 years" --> E2
~~~

This is **two-way communication**, not an FTL circuit. Even if payload transmission took only milliseconds, the ordinary request-to-reply delay is about 8.48 years before processing overhead.

## Proposed transmitter hardware chain

~~~mermaid
flowchart LR
  DATA["Fresh measurement"] --> CRC["Packet + CRC"]
  CRC --> FEC["Error-control encoding"]
  FEC --> PPM["FPGA PPM pulse timing"]
  PPM --> DRIVER["Qualified laser driver with interlock"]
  DRIVER --> LASER["Optical source"]
  LASER --> TELESCOPE["Transmitter pupil + fast steering mirror"]
  CAM["Beacon / guide camera"] --> CONTROL["Pointing controller"]
  CONTROL --> TELESCOPE
  SAFETY["Hardware E-stop, power monitoring"] --> DRIVER
~~~

The laser source and its driver must be selected and qualified for optical power, pulse energy, timing, eye safety, temperature, interlocks and electrical compatibility. Do not treat a firmware GPIO as a replacement for a certified optical safety interlock.

## Receiver hardware chain

~~~mermaid
flowchart LR
  SCOPE["Receiving telescope"] --> FILTER["Spectral filter and coupling"]
  FILTER --> DETECTOR["Vendor-qualified SPAD or SNSPD"]
  DETECTOR --> TDC["Digital event timestamps"]
  CLOCK["Reference oscillator; epoch / sync"] --> TDC
  TDC --> SLOTS["Slot alignment + count statistics"]
  SLOTS --> DECODER["Soft decisions + FEC"]
  DECODER --> CRC["CRC / erasure flag"]
  CRC --> OUT["Verified reconstructed new data"]
~~~

A detector's bias/quench or cryogenic subsystem is **not** specified here. Its event output may require correct LVTTL/LVDS compatibility, vendor termination, ESD controls and time-tagging calibration. We have no physically validated advanced detector PCB.

## A low-voltage timing circuit suitable for *initial* bench validation

Controller 3.3-V GPIO -> 330-ohm resistor -> visible LED -> ground. Across a short air gap, a phototransistor has its emitter at receiver ground and collector at a **sense node pulled up to 3.3 V by 10 kohm**. A suitable 3.3-V Schmitt input timestamps the node. Light pulls the node LOW; invert the bit decision.

Approximate TX LED current for an assumed 2.0-V forward voltage:
\[
I = \frac{3.3\,{\rm V}-2.0\,{\rm V}}{330\,\Omega} \simeq 3.9\,{\rm mA}.
\]
This is a *concept*, not a validated circuit board. Confirm GPIO ratings, LED current, phototransistor pinout, rise/fall time, light levels, wiring and all component datasheets before construction. It is not a single-photon receiver.

## Quantitative photon budget: a physically constrained baseline

For an unobscured circular transmitting pupil and a much smaller aperture at the receiver plane of its diffraction pattern, define

\[
z=\frac{\pi D_tD_r}{2\lambda R},\qquad
\eta_{\rm capture}\simeq \frac{z^2}{4},\qquad
N_{\rm detected/s} \simeq \frac{P_t}{hc/\lambda}\,\eta_{\rm capture}\,\eta_{\rm system}.
\]

This is an **ideal small-receiver, far-field** approximation, not a full telescope model. The [reproducible v0.6 source](../../research_tools/interstellar_optical_budget.py) uses a stable fourth-order correction. At 4.24 ly, 1064 nm, 10 W, $D_t=1$ m, $D_r=10$ m and 20% end-to-end efficiency, it predicts **0.363 detected photons/s** in this optimistic idealisation. Real acquisition, jitter, atmospheric and background losses are excluded.

For uncoded M-slot PPM **at zero background**, if a pulse produces a Poisson mean $s$ and a tie is guessed uniformly when no photon is detected, the symbol error probability is exactly

\[
P_{\rm SER}=(1-1/M)e^{-s}.
\]

A coded radio/optical modem with timing uncertainty and background requires much more than this analytic lower-complexity control. The additional [regression tests](../../research_tools/tests/test_interstellar_optical_budget.py) check parameter rejection, aperture scaling, inverse-square distance, zero-background PPM and one-way/round-trip timing.

Run:
~~~bash
python -m research_tools.interstellar_optical_budget
python -m unittest discover -s research_tools/tests -v
~~~

## Investigating genuinely shorter round trips

The [Krasnikov-tube paper](https://arxiv.org/abs/gr-qc/9702049) describes a hypothetical spacetime with an unusually short theoretical round trip when a corridor has been established. It is a **mathematical geometry**, not a buildable receiver or modulator. Such proposals face exotic matter/energy, source, stability, horizon, global causality and chronology constraints. [Alcubierre and Lobo's review](https://arxiv.org/abs/2103.05610) is an appropriate starting point.

A proposed experiment requires (i) a physically consistent source of its candidate metric, (ii) a calculation of $J^+(A)$ under the **actual** metric, (iii) a freshly randomised message $X$ at event A, (iv) receiver-only record Y at event B, (v) measured clock uncertainty and side-channel exclusion, and (vi) replication. The no-signalling theorem rules out encoding a fresh bit into Bob's local marginal using entanglement alone.

### Research gates

1. **Electronic loopback:** measured GPIO-to-photodetector timing, jitter, logic polarity and BER.
2. **Qualified single-photon receiver:** calibrated event arrival statistics, dark/background counts and detector dead-time.
3. **Coded PPM modem:** measured clock acquisition, frame error rate and photon efficiency with uncertainty.
4. **Optical terminal:** pointing-control closure, seeing/background/noise model, epoch-specific trajectory and source geometry.
5. **Speculative spacetime audit:** source equations, stress-energy and global causal structure; no unverified FTL hardware claims.

### Primary standards and experimental work

- [NASA/JPL Deep Space Optical Communications (DSOC)](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/), demonstrated an optical communications system, **not FTL**.
- [CCSDS 141.0-B-2 and 142.0-B-2](https://ccsds.org/view/sls/), physical and coding/synchronisation standards revised March 2026.
- Everett and Roman (1997), [Krasnikov spacetime](https://arxiv.org/abs/gr-qc/9702049), theoretical geometry and energy constraints.
- Alcubierre and Lobo (2021), [Warp drive basics](https://arxiv.org/abs/2103.05610), energy, horizons and causality.

**Project status:** software-level calculations and conceptual electronics only. There is no demonstrated light-speed-limit violation or constructed spacecraft-grade transmitter/receiver.
