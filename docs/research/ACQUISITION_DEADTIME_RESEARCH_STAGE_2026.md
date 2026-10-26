# Correlated optical pointing, stellar continuum and detector-memory experiment

*Interstellar Link Lab · 26 October 2026 · Biswajit Jana*

## The question

Does a photon-counting receiver still recover new data when the transmitter's beam wanders for several packet times, the link repeatedly loses acquisition, the star contributes background photons, and the detector has a finite recovery time?

This computational milestone integrates those effects into a single **synthetic** receiver model. It does not describe any measured interstellar hardware or faster-than-light experiment.

## Transmit and receive chain

1. A fresh 8-byte payload is framed with sequence, length and CRC32.
2. A rate-1/2 terminated educational convolutional code (constraint length 3; octal generators 7 and 5) adds redundancy.
3. The code maps onto 8-position pulse-position modulation (20 ms per slot). Each synthetic frame spans 13.92 seconds.
4. Two-axis angular pointing follows a stationary AR(1) process with eight-frame correlation. The example Gaussian intensity overlap is $g_k=\exp[-\lVert\theta_k\rVert^2/(2\sigma_b^2)]$. This is a proxy, not an Airy diffraction treatment.
5. A pilot-frame state machine requires two consecutive good pointing estimates to acquire lock; lock drops beyond a wider angular threshold. Frames spent acquiring are **erasures**.
6. Signal and background photon events are drawn using independent Poisson arrival processes. A non-paralyzable detector blocks subsequent events during its recovery time; electronic timing jitter is applied to surviving event timestamps.
7. Received slot counts pass through a deliberately *mismatched* Poisson soft LLR demapper and educational Viterbi decoder. A packet counts as successfully received **only if CRC verifies its exact message and sequence**.

The mismatched Poisson decoder does not account for dead-time memory. It is a baseline against which a later memory-aware optimal likelihood should be evaluated.

## Background source and limits

For a generic unresolved blackbody continuum source, $F_\lambda\simeq\pi B_\lambda(T)(R_*/d)^2$, and the receiver mean count rate is approximated by

$$
\dot N_*\simeq\left(\frac{\pi D_r^2}{4}\right)F_\lambda\,\Delta\lambda\,\frac{\lambda}{hc}\,\eta q.
$$

Illustrative choices: 3,000 K; 0.15 solar radii; 4.24 light-years; 10 m receiver; 1064 nm carrier; 0.1 nm rectangular filter; 20% efficiency; and **unmeasured** spatial coupling $q=10^{-5}$. This yields about **1.742 photons/s**, or **0.03484 photon per 20-ms slot**. It is **not a measured Proxima spectrum, observing geometry, or atmospheric/stellar-background calibration**. The nominal signal strength of **five detected photons/on-slot** is a separate receiver-input experimental parameter; it is *not* computed from the earlier 10 W, 1 m telescope link (which had much lower photons/s).

## Synthetic replicated outcomes

Eight independent seeds, 100 scheduled frames per seed and scenario:

| Receiver scenario | Mean CRC-verified payload goodput | SD across independent runs | Mean acquisition duty | CRC-valid / all scheduled frames |
|---|---:|---:|---:|---:|
| Perfect pointing, no background or dead time | **4.592 bits/s** | 0.016 | 100.0% | 99.9% |
| Correlated pointing + reacquisition + stellar proxy | **3.264 bits/s** | 0.517 | 78.6% | 71.0% |
| As above + 16-ms detector dead time | **2.011 bits/s** | 0.362 | 78.6% | 43.8% |
| Severe drift, fivefold stellar proxy, 25-ms dead time | **0.000 bits/s** | 0.000 | 37.1% | 0.0% |

Standard deviations describe **variation between independent runs**, not confidence intervals for a real instrument. Frames within a run share correlated pointing. The zero-goodput severe case is finite-sample evidence for failure under the chosen parameter set, not an impossibility theorem.

## Practical consequence

Mean received optical power alone is not a sufficient predictor of **verified packet goodput** when pointing and acquisition introduce sustained outages. Finite detector dead time produces time-correlated counts; the independent-Poisson receiver likelihood becomes incorrect. These two effects must be modelled together when choosing control loop bandwidth, optical receiver array, readout circuitry and error-control code.

The strongest next physics/engineering experiment is a detector-recovery-aware likelihood (or multi-pixel receiver) jointly evaluated with measured pointing spectral density and a *calibrated* stellar spectrum. The criterion should be CRC-verified information per emitted joule, including pilot overhead and reacquisition time.

## Release and reproducibility

The complete **locally tested** v0.7 release includes the event-level Python simulator, blackbody continuum calculator, 19 new passing unit tests, four seeded eight-run scenarios, numerical JSON, two actual PNG plots, an interactive HTML study and a print-size A1 poster. **The full v0.7 source-and-binary package has not yet been transferred into this GitHub repository.** This note is a transparent interim public research record, not a claim of completed repository migration.

Key assumptions still unimplemented: measured detector afterpulsing; jitter distributions; clock acquisition and carrier ambiguity; non-blackbody stellar spectra; filter angular response; realistic transmitter power/aperture for the specified receiver count rate; atmospheric, turbulence and beam-steering feedback; high-quality CCSDS-compatible coding; epoch-frozen Earth-Proxima ephemerides.

The first-bit and earliest immediate-reply times remain approximately 4.24 and 8.48 years respectively in the illustrative static-light-time model. **No faster-than-light messaging was demonstrated or assumed.**

## Published technical context

- [NASA/JPL: Downlink Receiver Algorithms for Deep Space Optical Communications (NTRS 20210007955)](https://ntrs.nasa.gov/citations/20210007955): pointing fades, photon-counting time tags, detector blocking and clock dynamics.
- [Wang et al., Optics Express (2025), DOI 10.1364/OE.571463](https://doi.org/10.1364/OE.571463): dead time and afterpulsing in PPM counting receivers.
- [Xiang et al., Optics Express (2018), DOI 10.1364/OE.26.002848](https://doi.org/10.1364/OE.26.002848): corrected likelihood with dead time and jitter.
- [CCSDS 142.0-B-2 (March 2026)](https://ccsds.org/publications/newbooks/): coding and synchronisation. The educational convolutional code here is *not* a standards-conformant modem.
