# Optical transceiver and causality laboratory — instrument design record 01

**Research lead:** Biswajit Jana  
**Version:** 26 October 2026  
**Status:** model/specification; no constructed or flight-qualified transceiver.

## The physical requirement

Earth chooses a new unpredictable message. A station at interstellar range detects its optical signal, establishes frame synchronization, corrects channel errors, and marks recovered bytes as accepted only after an integrity check. A remote return transmitter performs the same process in reverse.

Measure separately:

1. **First-information arrival time**, defined by the physical propagation and receiver acquisition process.
2. **Verified throughput**, delivered *fresh* goodput, bits per second.
3. **Energy efficiency**, accepted fresh information bits per photon and per emitted joule.
4. **Revisit/reply time**, including geometry, both signal paths, autonomous response delay and optional acknowledgement redundancy.

The standard model has a nonzero lower bound on the first and fourth values imposed by light propagation. Optimizing (2) and (3) **does not** relax this.

## Optical propagation and power accounting

For nominal wavelength λ, range R, output optical power P, transmitter pupil D_t and receiver pupil D_r:

$$
E_{\gamma}=hc/\lambda,\qquad
z=\frac{\pi D_tD_r}{2\lambda R},\qquad
\eta_{\rm cap}\simeq z^2/4-z^4/32.
$$

For an unobstructed circular pupil, this last expression is the leading-order *small receiver* expansion of Airy encircled power with the indicated definition of z. The exact encircled energy is **not** just the small-angle approximation outside its domain; use the full Bessel expression there and add optical obscurations and wavefront errors when appropriate.

$$
\dot N_{\rm signal}\simeq \frac{P}{E_\gamma}\;\eta_{\rm cap}\;\eta_{\rm optics}\eta_{\rm detector}.
$$

A separate engineering model must supply optical spectral transmission, pointing overlap, jitter, background photon rate within the receiver's field of view, detector dark counts, saturation and dead time, receiver timing ambiguity, encoding overhead, and atmospheric losses if applicable.

The current constant-velocity [3D light-time code](../../research_tools/relativistic_geometry.py) is an analytical boundary check, not a Gaia catalogue extraction. The [optical budget](../../research_tools/interstellar_optical_budget.py) and [photon statistics](../../research_tools/photon_statistics.py) are idealized stage-0 models. A dynamic optical model must use the actual pointing vector computed at the future light-intercept point, **not** the instantaneous source-target line of sight.

## Electronics interface-control record

| Channel | Proposed boundary | Minimum calibration | Grounding / hazards |
|---|---|---|---|
| Host payload → FPGA | Versioned packet, length, CRC/FEC configuration | Bit-perfect loopback and deterministic frame capture | Software clock is not an optical pulse clock |
| FPGA → emitter driver | Qualified logic pulse interface | Pulse width, rise/fall time, jitter, peak current/optical energy | Independent hardware interlock and current limit |
| Steering controller → tip-tilt actuator | Vendor-compatible analogue/digital control | Frequency response, saturation, latency, noise, rail behaviour | Mechanical resonances, thermal drift, actuator power |
| Guide detector → pointing estimator | Image coordinates and timestamps | Camera integration time, optical centroid error, reference target | Sensor saturation, background scene, latency |
| Receiving telescope → detector | Filtered optical beam | Throughput, pupil obscuration, spectral response | Eye/laser safety, stray light, temperature |
| Photon sensor → time tagger | Documented ECL/LVDS/TTL/other vendor output | Time-walk, propagation delay, termination, dark/afterpulse rate | ESD, electrical ground reference, detector bias |
| Time tagger → FPGA/CPU | Timestamp packets with clock provenance | Clock drift, lost event flags, time-base calibration | Timing reference must be explicitly recorded |
| Decoder → science archive | Frame validity and erasure masks | FER, accepted bits, packet timestamps, versioned decoder | Predictions must never be mislabelled as observations |

**Prototype A: low-voltage optical loopback.** Start with a 3.3 V-compatible controller, a visible LED and a series resistor, a short enclosed optical path, phototransistor collector load and a suitable digital input. No avalanche bias or high-power optical source is part of the prototype. Confirm actual component specifications before construction.

**Prototype B: calibrated single-photon terminal.** Use vendor-qualified modules for optical source, detector, time tagging and (where necessary) cryogenics. A commercial sensor produces a *timing event*, not an intrinsically error-free packet. Reconstruct information downstream and record uncertainty and loss.

## Why active optics belongs in the communication equation

Narrow beams improve energy concentration but become more sensitive to small angular pointing errors. The candidate engineering control loop is:

1. A guide camera or beacon tracks beam or terminal displacement.
2. A state estimator predicts pointing and clock drift.
3. An electronic controller commands a fast-steering mirror within its bandwidth and travel limit.
4. Residual angular error is measured, logged and coupled back into the photon-link model.

The [two-axis PI control simulator](../../research_tools/pointing_control.py) is deliberately simple: a Gauss–Markov angular disturbance, noisy pointing measurement, finite-actuator time constant and travel saturation. The recorded outputs are RMS angular residual and optical overlap averaged under a **Gaussian-equivalent** beam, not a full Airy-integrated turbulence model. Compare seeded open/closed runs with identical disturbances; then replace the synthetic plant with a calibrated physical transfer function.

To obtain flight-relevant sensitivity, measure the guide sensor transfer function, control law stability margins, vibration PSD, atmospheric/telescope disturbances, thermal drift, pointing knowledge vs pointing control, field alignment and optical beacon acquisition.

## Photon-counting waveforms and receiver decision theory

For M-ary PPM, model independent Poisson slot counts:

$$
N_j\sim \begin{cases}\operatorname{Poisson}(s+b)&j=k_{\rm transmitted}\\
\operatorname{Poisson}(b)&j\ne k_{\rm transmitted}.
\end{cases}
$$

For b>0, the log likelihood under candidate slot k differs between candidates by:

$$
\log L_k = N_k \log\left(\frac{s+b}{b}\right)-s+\text{common offset}.
$$

Therefore hard-decision ML chooses the largest count. A soft decoder instead passes slot evidence (and clock/synchronization uncertainty) to a channel decoder. The project includes a seeded hard-decision simulator and a separate soft-decision/FEC programme. Nonzero background, detector afterpulsing, dead time or timing errors change the effective likelihood model.

For the exact zero-background Poisson toy model, if no signal photon is detected the receiver must guess, giving

$$
P_{\rm symbol\,error}=(1-1/M)e^{-s}.
$$

This is not an experimentally achieved coded rate. Useful reliable throughput requires frames, synchronisation, false alarm monitoring, capacity/finite-blocklength analysis and whole-frame confidence intervals.

## Safety and failure states

The beam source must default to disabled when the clock/timing state is invalid, source power is unverified, steering is unreferenced, a watchdog fails or a safety interlock opens. Real laser controls require applicable safety engineering and hardware independent of software; this document is not a guide to defeating interlocks or building high-power hazardous laser drivers.

If the receiver cannot decode a packet, report **erasure** and preserve the original event timestamps. Never fill a missing astronomy measurement with modelled data and call the resulting image "received".

## FTL physics is a separate theoretical experiment

A future instrument concept cannot begin by drawing a faster laser driver. It begins with an explicit candidate theory.

State the spacetime manifold M, metric g, matter/source model T, observer tetrads, and physically allowed trajectory/field equations. Compute Einstein residuals and local/global causal sets under the **actual** metric, including time-order consistency and geodesic completeness or known singularities where relevant. Validate against Minkowski/Schwarzschild analytic benchmarks before any speculative case.

Two *distinct* extraordinary objectives must be tested. **Shortcut transport:** a physically viable metric and source permit delivery faster than a rigorously defined external/reference null route, perhaps while remaining inside J⁺(A) of the actual metric. **Causal violation:** a freshly selected input X is locally readable at B **outside J⁺(A)** of the actual physical theory. Both require rigorous clocks, interventions, source dynamics and side-channel controls. Beating a Minkowski comparison ray must never be silently promoted into violation of the candidate geometry's own null cone.

Known obstacles to warp/wormhole/corridor approaches include extreme source requirements, exotic-energy properties, stability, self-consistency, physical preparation time, chronology and quantum effects. These are research questions with uncertain answers, not deliverables promised by this repository.

## Research data that future teams must be able to reproduce

Archive: hardware BOM revisions, schematics and PCB manufacturing files (when they exist), spectral/thermal calibration, FPGA bitstream revision, firmware commit, source waveform, random seeds, detector timestamps, environmental telemetry, unit metadata, absolute clock calibration, interlock states, aperture/pupil model, source catalogue epoch and covariance, reconstruction recipe and acceptance thresholds.

The **first meaningful scientific deliverable** is a measured bit/error and photon-counting trace compared with a predictive model over varying laser intensity, pointing disturbance, symbol order and detector background—not a speculative FTL demonstration.

### Reference trail

- NASA/JPL, [Deep Space Optical Communications](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/), completed 2025; flight laser transceiver and Palomar SNSPD receiver.
- CCSDS, [Non-Coherent Optical Communications Physical Layer, CCSDS 141.0-B-2](https://ccsds.org/publications/sls/entry/4662/), March 2026. Conformance is **not** claimed.
- Bennett and colleagues, [quantum teleportation](https://doi.org/10.1103/PhysRevLett.70.1895), Physical Review Letters 70 (1993).
- Everett and Roman, [Krasnikov-type spacetime](https://arxiv.org/abs/gr-qc/9702049), 1997.
- Alcubierre and Lobo, [warp-drive review](https://arxiv.org/abs/2103.05610), 2021.

*Numerical results and the website are works in progress. All experimental/hardware aspects require future independent physical validation.*
