# First engineering result: photon-counting OOK versus M-PPM
**Date:** 2026-10-25 | **Status:** deterministic numerical analysis; idealized model, not a hardware measurement.

## Fixed-input synthetic design studies

All rates below are **ideal hard-decision mutual-information benchmarks**, not implemented FEC throughput or actual spacecraft telemetry. Independent binary OOK uses a threshold selected to maximize hard-output information under equiprobable input bits. Independent M-PPM uses exact Poisson symbol-error probabilities with random tie-breaking; a raw PPM frame contains log2(M) uncoded bits. Results use fixed **average detected** signal count rate, a fixed **noise** rate and slot clock. Mean photons per PPM symbol = detected signal counts/s * M * slot seconds; all detected signal energy is concentrated in one pulse. The peak/average intensity ratio required is therefore M.

| Illustrative parameter | Photon-starved | Brighter link |
|---|---:|---:|
| Detected signal photons/s | 200 | 2,000 |
| Background + dark counts/s | 20 | 100 |
| Slot duration | 2 ms | 0.5 ms |
| Max peak/average intensity | 128 | 128 |
| Nominal distance | 4.24 ly | 4.24 ly |

### Analytic hard-output information rate (bits/s)

| Modulation | Photon-starved | Brighter |
|---|---:|---:|
| 2-PPM | 54.79 | 618.34 |
| 4-PPM | 134.17 | 916.82 |
| 8-PPM | 159.74 | 747.27 |
| 16-PPM | 123.22 | 500.00 |
| 32-PPM | 78.12 | 312.50 |
| 64-PPM | 46.87 | 187.50 |
| 128-PPM | 27.34 | 109.38 |
| **Binary OOK** | **136.62** | **1155.66** |

**Interpretation:** In the photon-starved example, 8-PPM gives the highest modeled hard-output information benchmark among evaluated options (159.74 bit/s), but its uncoded symbol error is about 5.25%; it **cannot** be advertised as a reliable 160-bits/s working system without specified FEC. In the brighter case, threshold-optimized binary OOK gives the highest benchmark under the chosen fixed slot clock. This does not generalize to an overall optimal deep-space modulation; its specific clock, peak power, noise and receiver model matter.

All cases have the same idealized light-flight reference of about **133,804,224 seconds** (4.24 Julian years). Full-message completion is never modeled earlier than that. An 8192-bit message would have an *optimistic information-theoretic* additional serialization time of ~51.28 seconds using photon-starved 8-PPM or ~59.96 seconds using OOK; no synchronization, pointing acquisition, coding/frame overhead, retransmission or interruptions are included.

## Why high M can fail

Increasing M improves uncoded bits per chosen pulse, and concentrates a fixed average photon rate into a higher-energy pulse. But a complete frame occupies M slots; hence fewer frames per second, increased peak intensity and potential detector/transmitter constraints. Background counts can create wrong maxima. This is a trade-off, not monotonically increasing efficiency.

These calculations compare **hard output** (best/threshold decisions) and therefore discard potential information in the complete count vectors. Soft-count decoding can perform differently and is a necessary next step. Choosing OOK/PPM must also account for clock recovery, burst duty, extinction ratio, peak optical amplifier limits, coding and link availability.

## Mathematical validation and limits

* If signal=0, equiprobable M-PPM receiver guesses a random symbol: SER=1-1/M, hard MI=0.
* If background=0, SER=(1-1/M) exp(-mean signal photons/symbol).
* For equal-background noise slots, a uniform tie-breaking ML decision induces a symmetric hard M-ary channel.
* For binary OOK, optimize the integer photon threshold; model false-alarm and miss probabilities independently.
* Each reported *complete* message has propagation delay plus serialization time. The theoretical hard-output MI is not necessarily an achieved reliable code rate.
* Poisson mean values above 200 counts/slot or pulse are excluded by the current numerical contract. Saturation, shot-to-shot source variation, detector dead time and finite peak pulse energy are not solved.

To reproduce, execute from repo root:

```bash
python -m research_tools.modulation
python -m unittest discover -s research_tools/tests -v
```

[View modulation source](../../research_tools/modulation.py) · [View plotted trade study](../../figures/modulation_trade_2026.svg)

### Next controlled experiment

1. Implement Poisson soft-count log-likelihood vectors, not just hard count maxima; compare finite-block FEC performance (e.g., clearly named reference code) against code-independent MI.
2. Sweep peak-to-average intensity and code/block length, BER, BLER, and energy per **correct delivered** information bit.
3. Measure detector dark counts, jitter, background filter acceptance and dead-time effects with a low-power photodiode/photon counter bench and timed acquisition gates.
4. Freeze target and observer ephemerides, covariance and receive-time optical pointing before extrapolating to Proxima.

Reference standards: [CCSDS 141.0-B-2 / 142.0-B-2 (March 2026)](https://ccsds.org/publications/newbooks/), [NASA DSOC](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/), and [high photon-information-efficiency optical experiment](https://arxiv.org/abs/2501.13356). The simulation is NOT a replication of those systems.
