# Research programme: deep-space communication and information beyond the light cone
**Research lead:** Biswajit Jana | **Date:** 2026-10-25 | **Status:** active computational research, not a discovery claim

## The two questions that must never be conflated

**P1 — communication engineering:** How many verified *new* bits per second can a transmitter send across a photon-starved space link for a given power, telescope aperture, noise, pointing, clock, delay and reliability budget? This is a tractable engineering research problem with measured precedents.

**P2 — causal physics:** Can a fresh, independently random message X, chosen at emission event A, be inferred from receiver-only observations Y at event B when B is **not in the causal future of A under the actual physical spacetime**? No experimentally validated mechanism currently meets this criterion.

Increasing bit rate cannot make the first bit exceed c. Predictive modelling or pre-shared keys do not transport post-selection innovations early. The quantum no-communication theorem bars using entanglement-only local operations to choose Bob's marginal.

## Verified engineering baselines and constraints

1. NASA/JPL **DSOC**, completed in September 2025, demonstrated 267 Mb/s near 31 million km, and multiple Mbps at Mars-scale distances. Its actual engineering used laser optics and superconducting-nanowire photon counting. These numbers are not directly extrapolatable to 4.24 ly. Sources: [NASA/JPL DSOC](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/) and [2025 NASA retrospective](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/deep-space-optical-communications-dsoc/nasas-deep-space-communications-demo-exceeds-project-expectations/).
2. The peer-reviewed DSOC performance description documents actual flight terminal power/aperture and ground receivers; do not present a 1 kW / 10 m transmitter as the demonstrated DSOC configuration. [IEEE DOI 10.1109/JSTQE.2025.3625968](https://doi.org/10.1109/JSTQE.2025.3625968).
3. **2026 CCSDS standards** supersede older issue numbers: [141.0-B-2 physical layer](https://ccsds.org/publications/sls/entry/4662/) and [142.0-B-2 coding/synchronization](https://ccsds.org/publications/newbooks/). Code in this repository is illustrative and **does not claim interoperability** with those standards.
4. Dacha et al. experimentally report 14.5 bits per *incident* photon (17.8 per *detected* photon), in a specific high-photon-information-efficiency experimental channel; they are not universal data-rate guarantees. [arXiv:2501.13356](https://arxiv.org/abs/2501.13356).
5. Deep-space high-delay delivery calls for store/forward and delay-tolerant methods (LTP, bundle protocols), **not** a round-trip handshake per packet. [RFC 5325](https://www.rfc-editor.org/info/rfc5325/). See also 2026 [CCSDS LTP corrigendum](https://ccsds.org/publications/newbooks/).

## Complete engineering chain and planned tests

| Stage | Physics / software task | Required evidence | Present state |
|---|---|---|---|
| 1. Worldlines | Gaia source, ICRS epoch, radial/3D velocity, JPL receiver ephemeris | Frozen raw data, checksum, frame transform, covariance | Planned; current 4.24-ly reference is static |
| 2. Optical design | Diffraction integral, spectral throughput, transmitter power, obscuration, point-ahead, jitter | Independent analytic limiting cases, optical propagation cross-check | Ideal circular-pupil prototype only |
| 3. Photon detection | Poisson signal/background, dark counts, jitter, dead time, afterpulsing, saturation, realistic filter/window | Empirical detector parameters; Monte Carlo vs analytic controls | Idealized Poisson reference |
| 4. Modulation | OOK, M-PPM, high-efficiency PPM, potential DPSK/coherent modes | SER/BER vs photon budget, rate, peak duty, robustness | **OOK/PPM hard-output comparison implemented** |
| 5. Coding and framing | Synchronization, interleavers, CRC, FEC, erasures, framing overhead | Block-error curves, soft-count decoding, hardware constraints | CRC tile proof of concept in local v0.2 archive; FEC pending |
| 6. Source coding | Prediction from previously shared state; send only fresh residual | Source-mismatch robustness, image RMSE/SSIM, energy-per-delivered-bit | Synthetic predictive imaging in v0.2 viewer |
| 7. Transport | DTN custody/recovery, finite contacts, resource scheduling | Goodput, end-to-end delivery latency, outage tests | Planned |
| 8. Prototype | FPGA/laser EOM or LED, time tagger, photon counter, local clock | Calibrated rates, synchronized blind replay, independent receiver | Not yet built |

## Mathematical performance criteria

Reference geometry: tau = ||r_receiver(t_arrival)-r_sender(t_emission)||/c; solve the implicit retarded-time equation with time-varying source and destination. **Neither 4.24 ly nor a static Euclidean separation is a frozen astrometric result.**

Unobstructed diffraction-coupling baseline: received detected count rate = P_tx * spatial_coupling * total_optical_efficiency * detector_efficiency / (h c / wavelength). Receiver background is a separate Poisson process; neither telescope area alone nor photons/s alone determines delivered throughput.

In M-slot pulse-position modulation, one slot receives a Poisson signal with mean s plus b; all other slots receive background b. For equiprobable symbols and equal background, ML chooses the largest count with uniformly randomized ties. Our analytical exact SER is independent of Monte Carlo. The symmetric hard-decision MI is

    I_hard = log2(M) + (1-e)log2(1-e) + e log2(e/(M-1))

where e is symbol-error probability, terms 0 log 0 are defined as zero. The theoretical rate I_hard/(M*T_slot) is an **ideal discrete-channel information benchmark**, not achieved encoded goodput, nor a capacity for the full soft-count observation. Peak/average intensity ratio is M for single-pulse M-PPM in our reference design; larger M is not free. OOK uses an independently optimized count threshold and peak/average ratio 2.

Trade study: [modulation reference model](../../research_tools/modulation.py), [12 tests](../../research_tools/tests/test_modulation.py), [results](MODULATION_RESULTS.md).

## The separate causality / speculative frontier

**Control mechanisms, known physics:** light-cone classification, seeded randomized classical messaging, pre-lightcone mutual information with permutation controls, Bell-pair reduced-marginal no-signalling, negative controls for data leakage.

**Candidate speculative geometry:** reproduce Pieri's *Hyperwave* proposal (2023/2024) before asserting novelty; derive g_(mu nu), inverse/determinant, connection, curvature, Einstein tensor, induced T_(mu nu), conservation, NEC/WEC for a *sufficiently complete family* of null/timelike directions, source compatibility, horizons and global chronology. Do not infer source realizability from an attractive metric. Key prior work: [Pieri](https://arxiv.org/abs/2311.12069), [Bobrick–Martire](https://arxiv.org/abs/2102.06824), [Santiago–Schuster–Visser](https://arxiv.org/abs/2105.03079).

A background-Minkowski 'early' arrival through a candidate nontrivial metric is NOT automatically outside the candidate metric's actual J+(A). A physical FTL claim must satisfy the stronger intervention and actual-metric causality protocol in [CAUSAL_TEST_PROTOCOL.md](CAUSAL_TEST_PROTOCOL.md).

## Scientific outcomes worth publishing before any FTL result

* A validated public, parameterized, detector-to-packet photon-efficiency/latency landscape, with CCSDS-linked documentation.
* Quantitative Pareto front of transmitted energy, peak power, BER/BLER, delivered bits/s and reliable message delay for deep-space optical channels.
* A reproducible stress-energy and physical-source falsification ledger for selected speculative communication metrics.
* Negative and null results are reportable scientific results, if controls and assumptions are rigorous.

**Publication gate:** do not call a simulated association causal or a hypothetical metric physically realizable without independent checks; list falsified and surviving hypotheses separately. Preserve source provenance and commit dates.
