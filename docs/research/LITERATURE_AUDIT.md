# Verified-source ledger and evidence gates (25 October 2026)

This is a **current verification supplement**, not a claim that the historical archived research report's old conversational citation tokens resolve. Research lead: Biswajit Jana. Record exact dates, paper versions and DOI when implementing a model.

| Subject | Verified primary source | Established result | What this repo has **not** verified |
|---|---|---|---|
| Deep-space laser communication | [NASA/JPL DSOC mission](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/), [NASA 18 Sep 2025](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/deep-space-optical-communications-dsoc/nasas-deep-space-communications-demo-exceeds-project-expectations/) | 267 Mb/s at ~31 million km near the experiment's shorter ranges; technology demonstration concluded 2025 | No direct Exo/Proxima operational extrapolation; no match to our illustrative telescope model |
| Peer-reviewed DSOC link physics | [IEEE 10.1109/JSTQE.2025.3625968](https://doi.org/10.1109/JSTQE.2025.3625968) | Real measured optical terminal and link performance and ranging regimes | No independent published-data reprocessing yet |
| CCSDS physical layer | [CCSDS 141.0-B-2](https://ccsds.org/publications/sls/entry/4662/) | **March 2026** non-coherent optical physical-layer standard | No standards-conformant packet generator/modem yet |
| CCSDS optical coding | [CCSDS 142.0-B-2](https://ccsds.org/publications/newbooks/) | **March 2026** non-coherent optical coding/synchronization | No coded link or compliance test; old 142.0-B-1 is superseded |
| Photon information efficiency | [Dacha et al., arXiv:2501.13356](https://arxiv.org/abs/2501.13356) | 14.5 bits/**incident** photon and 17.8 bits/**detected** photon reported for one experimental system | Not a universal bound; not reproduced in our simple hard-decision model |
| Interplanetary transport | [RFC 5325 LTP motivation](https://www.rfc-editor.org/info/rfc5325/) | Long-RTT, outage-tolerant transport cannot assume terrestrial rapid handshakes | No implemented LTP/DTN transport layer |
| Gaia astrometry | [Gaia DR3 archive data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html) | Epoch, reference-frame and correlated astrometric columns have defined semantics | No frozen Proxima source vector, validation checksum or propagated covariance |
| Warp metric taxonomy | [Bobrick–Martire, arXiv:2102.06824](https://arxiv.org/abs/2102.06824) | Some positive-energy subluminal constructions; speculative superluminal classifications | No validated physical FTL device |
| Energy-condition critique | [Santiago, Schuster, Visser, arXiv:2105.03079](https://arxiv.org/abs/2105.03079) | General warp energy-condition restrictions; convenient observer tests are insufficient | No validated source material, energy condition over all observers, or chronology solution |
| Microscopic 'Hyperwave' prior art | [Pieri, arXiv:2311.12069](https://arxiv.org/abs/2311.12069) | Published speculative warp-based *communications*, so 'tiny warp for signals' is not a new idea on its own | No independent replication of Einstein tensor/source and no physical realization |
| No-signalling quantum control | Quantum reduced-state identities and classical channel requirement | Local operations on Alice's half cannot select Bob's unconditioned marginal alone | No spacelike field hardware experiment conducted |

## Minimum evidence levels

1. **Verified published measurement:** Cite instrument, physical range, wavelength, transmitted/received power, BER/BLER, data-rate definition and DOI.
2. **Reproduced numeric science:** Code revision, source input, seed, numerical precision, analytic limiting cases, independent implementations, uncertainty/calibration.
3. **Physically plausible but unvalidated design:** Clearly specified power, peak duty, pointing and receiver environment; published engineering bounds; no unsupported extrapolation.
4. **Speculative actual-metric route:** Full Einstein source analysis, energy conditions and stability plus causal set J_plus(A) in *actual geometry*. Reduced travel time versus flat reference is not identical to causal violation.
5. **Extraordinary measured signalling:** Blinded fresh-message intervention, reliable pre-causal-boundary decoding, anticontamination and independent physical replication. No experiment presently satisfies level 5.

## Novelty opportunities (research questions, not discoveries)

**Engineering — strongest immediate route:** Which photon-efficient waveform/FEC/background-gating choices maximize *confirmed delivered* new science bits per Joule subject to laser peak-power and pointing constraints, and can time-stamped predictive residual tiles outperform conventional compression at the same end-to-end reliability? Compare to measured DSOC engineering, not fictional scenarios.

**Causal statistics:** How often do mutual-information estimators, shared model priors, improper time slicing and clock offsets create apparent prelight correlations? Quantify sensitivity, preregistered false positives and independent reproduction under deliberately contaminated controls.

**Theoretical GR:** Can a previously published proposed micro-warp communication metric be reconstructed in an independent symbolic/numerical solver, with complete source constraints and chronology analysis? A negative physical realizability result is publishable if validation is rigorous.

## Correction policy

If a source is inaccessible, unverified, updated or contradictory, document that status rather than inventing an equation, a value or an experimental result. Revisit this ledger before each release and prior to any public publication.
