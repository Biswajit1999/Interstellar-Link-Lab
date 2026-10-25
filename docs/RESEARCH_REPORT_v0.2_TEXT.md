# Interstellar Link Lab — v0.2 scientific report (text extraction)

**Research lead:** Biswajit Jana  
**Source:** 11-page *Interstellar Link Lab Research Report v0.2* prepared for this standalone repository.  
**Status:** Extracted text for accessibility; PDF page layout, equations, tables, and images may not survive extraction. The full PDF remains part of the separate local release bundle. These are illustrative simulation results, not flight or FTL validation.

---

<PARSED TEXT FOR PAGE: 1 / 11>

                                            Interstellar Link Lab
 Release v0.2.0 • Scientific research report and verification addendum • 25 October 2026

 Research lead: Biswajit Jana | Repository target: Biswajit1999/interstellar-link-lab


 Executive summary
 This release is a runnable laboratory for idealized deep-space optical communication, photon-counting PPM,
 predictive-image transport, relativity controls, and symbolic geometry baselines. It adds an independent analytical
 hard-decision PPM detector error model, numerical confidence intervals, and CRC-gated tiled image reconstruction. 60
 local automated tests pass. No real interstellar signal, operational spacecraft terminal, experimental FTL link, or
 physical warp corridor has been demonstrated.


 v0.2.0 experiment results

   Measurement                                      Reproducible seeded result


   Uncoded PPM theory                               Poisson symbol/bit error law incl. random tie breaking


   Synthetic image                                  96 x 96 pixels; 36 separately transmitted 16 x 16 tiles


   Strong, 40 photons/symbol                        36 accepted / 0 failed; 0 errors of 19,840 bits


   Weak, 4 photons/symbol                           9 accepted / 27 fallback; 186 errors of 19,840 bits


   Packet wire size                                 2,480 B, vs monolithic compressed innovation 1,202 B


   Reconstructed RMSE                               Strong: 1.156; weak: 4.588 grayscale levels


   Verification                                     60 tests pass locally in stated environment




 Scientific interpretation
 The exact Poisson model agrees with the seeded Monte Carlo within sampling uncertainty. The tiled receiver preserves
 intact innovations under weak signal conditions, at the cost of substantially larger packet overhead. Each received
 innovation arrives only after conventional optical propagation light-time. The detector, receiver-clock, photon source and
 Earth/Proxima geometry are idealized assumptions, not engineering measurements.


 Reproduction and audit
 Install with pip install -e ".[dev]", run python -m pytest -q, then python scripts/run_demo.py
 --out-dir . and python scripts/run_advanced.py --out-dir .. Results are in results/baselines.json and
 results/advanced.json. Source files, input parameters, and seeds are included in the attached repository ZIP.




Interstellar Link Lab | v0.2.0 simulated research                                                                             1

<PARSED TEXT FOR PAGE: 2 / 11>

 A. Analytical error-rate cross-check
 For M-slot photon-counting PPM, the transmitted slot has Poisson count with mean (s+b) and each of the M-1
 nontransmitted slots has Poisson background with mean b. The hard-decision receiver chooses the greatest count with
 uniform tie breaking. Given transmitted-slot count k, define F(k-1)=Pr[B<k] and f(k)=Pr[B=k] for B~Poisson(b).

 Then Pr(correct | k) = Integral_0^1 [F(k-1)+t f(k)]^(M-1) dt. Averaging over k~Poisson(s+b) gives the uncoded
 symbol-error rate (SER). Under symmetric slot errors the raw BER = SER*M/[2(M-1)]. For b=0, SER=(1-1/M) exp(-s),
 which is tested at several M and s. This is a detector benchmark, not a capacity bound or an operational deep-space
 modem.




 Figure 8. Exact ideal-Poisson SER/BER against independent-symbol Monte Carlo. Only symbol-error observations use 95% Wilson
 confidence intervals; within-symbol bit errors can correlate.




Interstellar Link Lab | v0.2.0 simulated research                                                                              2

<PARSED TEXT FOR PAGE: 3 / 11>

 B. Packet-tiled image reconstruction
 The sender and receiver share a synthetic prior and a motion prediction. The sender quantizes each 16 x 16 pixel
 innovation, compresses it with zlib, and transmits a tile header plus CRC-32. Good packets update only their tiles; failed
 packets leave those pixels at their prior model prediction. Headers are validated but the simulator assumes perfect slot
 and tile framing. CRC detects errors rather than correcting them. The tiled approach increases payload size in this
 demonstration.




 Figure 7. Sender image, premessage shared prediction, strong-link decoded state and weak-link local packet fallbacks. No precognition
 or faster-than-light information transfer is implied.




Interstellar Link Lab | v0.2.0 simulated research                                                                                        3

<PARSED TEXT FOR PAGE: 4 / 11>

 C. Research maturity and blocked gates
 Passed: 60 reproducible local tests covering established mathematical baselines, idealized photon-channel modeling,
 Poisson analytic/Monte Carlo agreement, and synthetic tiled reconstruction.

 Blocked: frozen Gaia/JPL state vectors and covariance; actual point-ahead, pointing jitter, turbulence and stellar
 background; peak-power transmitter feasibility; optical acquisition, clock recovery, validated framing, FEC and ARQ;
 test-bench measurements; independent GR tensor validation across additional metrics; any physical source for a
 speculative spacetime corridor.


 Future experiments and publication priorities
 1. Implement source-frozen astrometry and ephemeris ingestion, exact reception epochs, uncertainty propagation, and
 physical point-ahead vectors for Earth-Proxima targets.

 2. Validate a detector- and pointing-aware photon budget against experimentally published optical link data and
 reproducible Monte Carlo detector models.

 3. Add real framing, packet reliability, synchronization acquisition and documented forward-error correction. Compare
 with standards-conformant reference implementations.

 4. Run a laboratory photon attenuation/PPM experiment with traceable time stamps, pulse calibrations, and measured
 noise processes.

 5. Independently replicate published GR geometry calculations with complete stress-energy and causal-global checks
 before attempting any new spacetime model.


 Prior work and project citation
 The following appended pages preserve the original v0.1.0 foundational research report for provenance. They refer to the
 earlier 37-test baseline and six figures; this cover and the v0.2.0 JSON/README supersede those counts. The standing
 scientific limitations and primary references are maintained in the source repository.

 Cite: Biswajit Jana (2026), Interstellar Link Lab: Photon-efficient links and relativistic causality, software release v0.2.0.
 Intended repository: github.com/Biswajit1999/interstellar-link-lab (not yet published).




Interstellar Link Lab | v0.2.0 simulated research                                                                                 4

<PARSED TEXT FOR PAGE: 5 / 11>

 INTERSTELLAR LINK LAB
 Photon-efficient interstellar links, predictive imaging and relativistic
 causality

 Scientific research programme: Causal Frontier | Research lead: Biswajit Jana | 25 October 2026




 INITIAL SCIENTIFIC REPORT — EXECUTED SIMULATION BASELINE

 This report describes a real, versioned Python research implementation with 37 passing local
 automated tests and six regenerated figures. Calculations are idealized and synthetic. No
 faster-than-light message, physical warp geometry, mission hardware or observed Proxima data is
 demonstrated.



 Executive summary
 The package integrates an ideal circular-aperture interstellar laser-link budget, direct
 photon-counting pulse-position modulation, predictive remote-image reconstruction, quantum
 no-signalling controls, Lorentz geometry and symbolic GR validation. All tests and figures can be
 reproduced locally from fixed seeds. Hardware-in-loop, astrometric data provenance, standards
 coding, quantitative uncertainty and independent GR reproduction are next milestones.



 Three independently useful research programmes
   Branch                        Status                         v0.1.0 deliverable


   Photon Frontier               Established physics +          Airy link, uncoded PPM, seeded synthetic predictive image
                                 exploratory engineering        channel


   Causal Frontier               Established causality          Lorentz invariance, Bell reduced state, MI permutation tests
                                 controls


   Causal Corridor               GR baseline; speculative       Minkowski and Schwarzschild vacuum Einstein tensor
                                 beyond                         checks




 Central scientific distinction: a pre-shared predictive model can reduce transmitted entropy but cannot reveal fresh
 random information before a physical signal arrives. An early arrival relative to a background reference metric is not
 automatically a local FTL signal.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                                1

<PARSED TEXT FOR PAGE: 6 / 11>

 1. Ideal interstellar photon-link baseline
 An on-axis uniformly illuminated circular transmitter and centered circular receiver are modelled by
 the Airy encircled-energy fraction F(x) = 1 - J0(x)² - J1(x)², where x = pi Dt Dr / (2 lambda R). Received
 optical power is the transmitted power multiplied by this fraction and explicitly specified scalar
 optical/pointing efficiencies. Registered photon counts include detector efficiency and E_photon = hc
 / lambda.


   Input / calculated quantity                         Reference scenario


   Separation / light time                             4.24 light-years / 4.24 Julian years (static illustration)


   Wavelength / power / apertures                      1064 nm / 1000 W average / 10 m transmit / 30 m receive


   Scalar efficiencies                                 optics 50%, pointing 100%, detector 75%


   Ideal geometric diffraction loss                    165.16 dB


   Detected signal photon rate                         61,214 counts/s


   Background + detector dark counts                   110 counts/s (illustrative input)




 Figure 1. Modelled detected photon rate as range changes. Background, pointing distribution, wavefront quality,
 obscuration, star flux and receiver acquisition are not solved.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                        2

<PARSED TEXT FOR PAGE: 7 / 11>

 2. PPM and the rate-consistent optical channel
 Each M-PPM symbol has exactly one excited slot. Independent photon counts follow Poisson statistics,
 with additional signal counts in the pulse slot. A largest-count rule (uniformly randomized tie breaks)
 recovers a raw symbol. The reference modem is uncoded: practical CCSDS framing/FEC, time
 synchronization, peak-power limits and detector dead time remain future work.

 The actual link rate and receiver background are mapped into PPM: symbol duration = 40 detected
 photons / modelled photon rate; mean background per slot = count-background rate x symbol
 duration / 16. This yields about 6.12 kb/s raw modulation bits in the highly optimistic example, not a
 useful throughput guarantee.




 Figure 2. Monte Carlo 16-PPM bit and symbol error fractions versus mean registered signal photons/symbol. At low
 error fractions the finite-sample observation floor is indicated.




 Figure 3. Aperture sensitivity at 4.24 ly for idealized on-axis diffraction, with other inputs frozen.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                        3

<PARSED TEXT FOR PAGE: 8 / 11>

 3. Predictive twin: an image can be compressed, not
 foreknown
 A synthetic 96 x 96 pixel star-field image is pre-shared. Both endpoints predict a shifted next frame;
 the actual new frame contains a fresh bright event and random sensor noise. The sender transmits
 quantized and zlib-compressed residuals over the photon-counting PPM link. Strong-signal reception
 restores the innovation while weak reception corrupts the compressed frame and triggers explicit
 prediction-only fallback.


   Synthetic image diagnostic                              Observed result


   Direct new-frame zlib bytes                             5428


   Innovation zlib bytes                                   1202


   Innovation / direct size                                0.221 x


   Decoded reconstruction RMSE                             1.16 gray levels


   Strong link bit errors / frame valid                    0 / True


   Weak link bit errors / fallback                         372 / True




 Figure 4. Synthetic previous, predicted, new, residual, successfully decoded and weak-link-fallback frames. Not a
 telescope observation; not precognition.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                         4

<PARSED TEXT FOR PAGE: 9 / 11>

 4. Causal controls and relativity
 The interval is ds² = -c²dt² + dx² + dy² + dz². A Lorentz boost preserves intervals and can reverse the
 time ordering of hypothetical spacelike separated events. This is not evidence that such signals exist
 or that a complete causal loop has been realized. The quantum control constructs a Bell pair with
 Bob’s reduced local state I/2; Bob’s unconditioned outcomes cannot reveal Alice’s fresh setting.
 Seeded mutual-information permutation tests quantify finite-sample correlation under a classical null
 and an exact-copy positive control.




 Figure 5. Minkowski light cone and hypothetical 4c arrival, a mathematical counterfactual only. Any genuine
 message must be assessed against physical local cones and verified causality.

 Null diagnostic: Bob-local MI 8.5825e-06 bits, permutation p-value 0.802 (399 permutations). This is a small synthetic
 control, not a rigorous exclusion threshold or experimental quantum evidence.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                              5

<PARSED TEXT FOR PAGE: 10 / 11>

 5. Prediction efficiency and feasibility caveats




 Figure 6. Compressed innovation and raw new-image message size in one fixed-seed synthetic example. Initial
 shared image/model distribution cost is excluded.

 A payload reduction in a shared-model system does not reduce the speed-of-light delay. The sender
 and receiver must already share model state; novel information is conveyed only through the actual
 optical channel. Spaceflight feasibility additionally requires transmit peak power, power/thermal/mass
 budgets, point-ahead and pointing jitter, receiver acquisition, stellar/sky background spectrum,
 coding overhead and long-term detector behavior.



 6. General relativity: established mathematical
 controls
 SymPy independently computes Christoffel symbols, Ricci tensors and Einstein tensors for selected
 analytic metric inputs. Unit tests return zero Einstein tensors for Minkowski and Schwarzschild
 exterior vacuum in geometric units c = G = 1. This validates these mathematical cases only. It does
 not calculate a warp-drive source, energy-condition satisfaction, global causality, traversability, null
 geodesics or engineering feasibility.



 7. Priority scientific backlog
 The project includes 34 research issues grouped into photon channels, astronomy/astrometry,
 information causality, hardware bench, validated GR, published warp/Hyperwave reproduction, future
 exploratory Moving-Observer Causal Corridor, and independent publication audit. Real Gaia and JPL
 inputs are explicitly absent until frozen and checksummed.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                   6

<PARSED TEXT FOR PAGE: 11 / 11>

 8. Release criteria and next experiments
 1. Regenerate results/figures in a clean environment and verify 37 current tests.

 2. Freeze Gaia 6D Proxima astrometry with covariance and JPL Horizons or SPICE ephemerides.

 3. Implement pointing-jitter distributions, stellar and atmospheric background and physical detector
 timing.

 4. Implement standards-aware coding, packet framing, synchronisation, confidence intervals and true
 useful throughput.

 5. Compare calibrated photon-starved optical laboratory measurements with a declared uncertain
 model.

 6. Calibrate strict pre-causal receiver windows, leakage injection, type-I rate and independent
 interventions.

 7. Validate independent numerical GR tensor/geodesic engines and reproduce published work before
 exploratory metrics.



 9. Reproduce the research baseline
 In the package root: create a Python virtual environment; execute pip install -e ".[dev]", python
 -m pytest -q, then python scripts/run_demo.py --out-dir .. Compare generated figures and
 results/baselines.json to this report.



 10. Selected sources
 • NASA/JPL Deep Space Optical Communications — jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/

 • Interstellar probe communications — arxiv.org/abs/1801.07778

 • Photon-starved optical communications — arxiv.org/abs/2501.13356

 • Gaia DR3 data and assumptions — arxiv.org/abs/2208.00211

 • Hyperwave communication geometry prior art — arxiv.org/abs/2311.12069

 • Warp energy-condition discussion — arxiv.org/abs/2105.03079

 • Space communications standards — ccsds.org

 Scientific status: computational foundations only. No observed or engineered
 faster-than-light signal; no verified exotic matter source, physical corridor, or new spacetime
 technology.




INTERSTELLAR LINK LAB | v0.1.0 | 25 OCT 2026                                                                    7