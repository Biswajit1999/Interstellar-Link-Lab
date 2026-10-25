# Interstellar Link Lab

**Photon-efficient interstellar communication · Deep-space optical links · Predictive imaging · Relativistic causality**

**Research lead:** Biswajit Jana · **Stage:** scientific simulation prototype

Interstellar Link Lab is an end-to-end, reproducible research programme for:

- Photon-counting, single-photon-level optical communication and interstellar link budgets.
- Pulse-position modulation (PPM), signal detection, packet integrity and eventually error-correcting codes.
- Predictive image transmission, digital-twin residuals and reconstructed receiver imagery.
- Moving Earth–Proxima Centauri endpoints and rigorous light-time accounting.
- Classical and quantum no-signalling control experiments.
- Exploratory numerical-relativity / spacetime hypotheses, **clearly segregated from validated engineering**.

## Research programme — 25 October 2026

The original [*Beyond the Light Cone* research report](docs/research/ORIGINAL_BEYOND_THE_LIGHT_CONE.md) and [original scientific research brief](docs/research/ORIGINAL_RESEARCH_BRIEF.md) are preserved here as historical inputs, separate from the current verified-source research and working code. Earlier source-message citation tokens in those archived documents are **not validated bibliographic citations**.

- [**Sourced scientific programme: optical engineering vs true causal FTL**](docs/research/RESEARCH_PROGRAM_2026.md)
- [**Modulation results: photon-counting OOK and M-ary PPM**](docs/research/MODULATION_RESULTS.md) — [source code](research_tools/modulation.py), [regression tests](research_tools/tests/test_modulation.py), [trade-study plot](figures/modulation_trade_2026.svg)
- [**Causal and speculative GR falsification protocol**](docs/research/CAUSAL_TEST_PROTOCOL.md)

### Current executable reference (standard-library only)

```bash
python -m research_tools.modulation
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
