# Interstellar Link Lab

## Two-way transmitter / receiver engineering — v0.6

[**Read the full two-way transceiver research note**](docs/research/TWO_WAY_TRANSCEIVER_ENGINEERING_2026.md): Earth/Proxima round-trip propagation, an optical transmitter/receiver chain, reference 3.3-V LED–phototransistor circuit, detector/FPGA electrical interfaces, new interstellar photon-budget Python code and tests, and physically falsifiable rather than asserted FTL hypotheses. Full-resolution engineering SVGs and the 12-page PDF are in the independent v0.6 release download; binary assets are not yet fully on GitHub.

## Illustrated engineering field guide — 26 October 2026

Start with [**From a new bit on Earth to a distant receiver**](docs/research/ILLUSTRATED_FIELD_GUIDE.md). The guide explains, in order, the light-time problem, optical modem, electronic control, a 3.3 V visible-LED timing circuit, photon-counting receiver, coding, image prediction, and the quantum no-signalling test. Four [editable SVG diagrams](docs/figures/) accompany the engineering explanation.

**Status:** the illustrated circuits are conceptual references, not a validated PCB or built high-voltage detector. The companion 15-page PDF and binary rendered figures have been generated separately but are not yet stored as binaries in this GitHub repository. No FTL signal has been demonstrated.


**Photon-efficient interstellar communication · Deep-space optical links · Predictive imaging · Relativistic causality**

**Research lead:** Biswajit Jana · **Stage:** scientific simulation prototype

Interstellar Link Lab is an end-to-end, reproducible research programme for:

- Photon-counting, single-photon-level optical communication and interstellar link budgets.
- Pulse-position modulation (PPM), signal detection, packet integrity and eventually error-correcting codes.
- Predictive image transmission, digital-twin residuals and reconstructed receiver imagery.
- Moving Earth–Proxima Centauri endpoints and rigorous light-time accounting.
- Classical and quantum no-signalling control experiments.
- Exploratory numerical-relativity / spacetime hypotheses, **clearly segregated from validated engineering**.

## Photon Frontier: coded optical receiver, 25 October 2026

A new [research note](docs/research/PHOTON_FRONTIER_V04.md) describes a soft-count M-PPM modem with an illustrative constraint-length-3 convolutional code, Viterbi decoding and CRC-validated fresh messages. The [source](research_tools/advanced/) and [regression tests](research_tools/tests/test_advanced.py) are executable Python, not a claimed flight implementation. The [parameter-study script](scripts/run_optical_modem_study.py) reproduces a 24-condition Monte Carlo sweep. Conditions: 0.08 background photons/slot, 100 μs/slot and 60 independently seeded frames per parameter point.

At four detected signal photons per illuminated slot, **8-PPM accepted 58/60 frames** versus **44/60 for 16-PPM**. This is a variable pulse-photon experiment; average optical power is **not controlled** between configurations. The ideal 4.24-light-year geometric budget assumes a 1 kW transmitter, 10 m transmit aperture, 30 m receiver, 1550 nm light and 20% scalar throughput. It estimates approximately 22,411 detected photons/s **before detailed acquisition, pointing and detector losses**.

- [Open the optical-link calculator](web/link-calculator.html) (offline HTML, editable parameters and explicit assumptions).
- [View the optical transmitter/channel/receiver diagram](hardware/diagrams/optical_system.svg).
- [View the 3.3 V optical timing reference circuit](hardware/diagrams/timing_loopback.svg), which is **not** SPAD electronics.
- [Read the detector/electronics bench specification](hardware/OPTICAL_ARCHITECTURE.md).
- [Read the manuscript and interface writing conventions](docs/WRITING_AND_DESIGN.md).

The complete local v0.4 research package also contains a conventional five-page PDF paper, high-resolution figures, a deeper static analysis viewer, and additional source/tests awaiting verification in this online repository. The presence of documents, simulations, or a plotted photon rate is **not** a demonstration of interstellar hardware, a CCSDS compliant waveform or faster-than-light signalling.

---

## Read and test the quantum no-signalling example

- [**Bell-state calculation with correctly rendered equations**](docs/research/QUANTUM_NO_SIGNALLING.md)
- [**Interactive no-signalling experiment**](docs/no-signalling.html) — offline HTML with seeded Bell-pair sampling, receiver-only statistics and an ordinary side-channel positive control.
- [**Reproducible Python source**](research_tools/quantum_no_signal_lab.py) and [regression tests](research_tools/tests/test_quantum_no_signal_lab.py).

The original archival report's TeX delimiters have been repaired for GitHub's native MathJax. Old, unresolvable chat citations are flagged as unverified, not passed off as scholarly references. The active note cites primary publications.

## Research programme — 25 October 2026

The original [*Beyond the Light Cone* research report](docs/research/ORIGINAL_BEYOND_THE_LIGHT_CONE.md) and [original scientific research brief](docs/research/ORIGINAL_RESEARCH_BRIEF.md) are preserved here as historical inputs, separate from the current verified-source research and working code. Earlier source-message citation tokens in those archived documents are **not validated bibliographic citations**.

- [**Sourced scientific programme: optical engineering vs true causal FTL**](docs/research/RESEARCH_PROGRAM_2026.md)
- [**Modulation results: photon-counting OOK and M-ary PPM**](docs/research/MODULATION_RESULTS.md) — [source code](research_tools/modulation.py), [regression tests](research_tools/tests/test_modulation.py), [trade-study plot](figures/modulation_trade_2026.svg)
- [**Causal and speculative GR falsification protocol**](docs/research/CAUSAL_TEST_PROTOCOL.md) — [executable null/positive/side-channel controls](research_tools/causal_controls.py), [tests](research_tools/tests/test_causal.py)
- [**2026 source verification and hypothesis audit**](docs/research/LITERATURE_AUDIT.md)

### Current executable reference (standard-library only)

```bash
python -m research_tools.modulation
python -m research_tools.causal_controls
python -m unittest discover -s research_tools/tests -v
```

The reference code calculates uncoded M-PPM Poisson SER with random tie-breaking, optimized hard-threshold binary OOK information, peak-to-average pulse-intensity constraints and **light-time-preserving** ideal full-message timing. The reported mutual-information rates are *ideal hard-decision channel benchmarks*, not achieved reliable throughput. A GitHub Actions workflow runs the standalone reference tests.

**Scientific conclusion remains unchanged:** higher information throughput is demonstrably possible, but no verified channel carries freshly chosen information outside the actual physical future light cone. No FTL claim, proprietary device claim or CCSDS compliance claim is made.

**Repository transfer status:** The v0.3 research notes and the standalone modulation reference source/tests are online. The earlier v0.2 viewer and report text are also online. The broader 97-file v0.2 source/reports/figure archive is **not yet fully uploaded**; standalone code here must not be represented as that full source archive.

---

## Scientific viewer

[**Open the complete offline v0.2 experiment viewer**](docs/index.html)  
[**Read the eleven-page report as accessible text**](docs/RESEARCH_REPORT_v0.2_TEXT.md)

The embedded viewer provides the v0.2 synthetic interstellar-link experiment, analytical PPM comparisons, photon-counting models, and illustrative reconstructed images. It is a **static display of already simulated data**, not an online telescope or operational spacecraft link.

## Publication state

**Standalone repository** — no Moving Observer submodules or dependency.

The offline v0.2 viewer and an accessible text extraction of the 11-page research report have been uploaded through the repository's authenticated GitHub connection. **The full v0.2.0 source-code ZIP, numerical source, tests, plots and PDF have NOT yet been uploaded to this GitHub repository.** Their independent local release bundle is being transferred separately. Do not infer that this repository is complete because the viewer is present.

The source archive was locally checked as a 60-test simulation baseline, but GitHub Actions has not yet independently rerun all those tests in this separate repository. The aim is to make the standalone repository reproducible and reviewable end-to-end.

## Scientific safeguards

- The nominal 4.24-light-year reference is an **illustrative static distance**, not an astrometric ephemeris.
- The simulation uses highly idealized optical assumptions; it is **not** flight-qualified.
- A predicted image is not information about a newly observed event until its residual bits physically arrive.
- Neither entanglement-only messaging nor faster-than-light signalling has been demonstrated.
- Novel speculative metric research requires stress-energy, energy-condition, causal and observational validity checks.

## Programme architecture

| Module | Focus |
|---|---|
| Photon Frontier | Deep-space optical links, photon statistics, PPM, channel coding, predictive images |
| Causal Frontier | Light cones, Lorentz transformations, quantum no-signalling, statistical controls |
| Causal Corridor | Established GR baselines and separately labelled speculative metrics |

## Next engineering milestones

Publish complete v0.2.0 source and binary research assets; validate independently in CI; add Gaia-epoch astrometric data and uncertainty; stellar noise and detector effects; CCSDS-inspired coding with sourced implementation tests; physical pointing and acquisition; independent relativity verification.

© 2026 Biswajit Jana. No institution or external partnership is implied.
