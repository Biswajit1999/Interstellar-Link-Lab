# A link can look healthy on average and still lose the message

*Photon Frontier · Research note, 26 October 2026 · Biswajit Jana*

## The question

An optical receiver may report a respectable *mean* photon count, yet whole messages may fail because its beam has drifted off target. The angular pointing error may be nearly fixed while an entire packet is being sent. This study tests what happens when we average **packet success probability across pointing states**, instead of calculating packet success once at the average received optical power.

This is a reproducible numerical control and analytical model, not a measured spacecraft link or a new FTL mechanism.

## Optical field and pointing model

The transmitter is an ideal, untruncated TEM00 *Gaussian mode*, with 1/e² intensity waist radius \(w_0\). This is **not the same optical pupil** as the repository's separate uniform-circular-aperture/Airy calculation. At wavelength \(\lambda\), propagation distance \(R\) and Rayleigh range \(z_R=\pi w_0^2/\lambda\), the intensity radius is

\[
w(R)=w_0\sqrt{1+(R/z_R)^2},\qquad
\theta_{\rm divergence}=\frac{\lambda}{\pi w_0}.
\]

The receiving circular aperture has radius \(a\ll w(R)\). Two orthogonal angular pointing errors are independent normal variables, each with standard deviation \(\sigma_\theta\). The offset of the beam axis at the receiver is \(\mathbf{r}=R\boldsymbol{\theta}\). In the small-aperture limit, instantaneous intensity gain is

\[
G=\exp[-2|\mathbf r|^2/w(R)^2],\qquad
\mathbb{E}[G]=\frac{1}{1+4(R\sigma_\theta/w(R))^2}.
\]

The *exact mean* aperture fraction for the convolution of a circular Gaussian beam with centered 2-D Gaussian pointing error is

\[
\overline{\eta}_{\mathrm{cap}} =
1-\exp\left[-\frac{2a^2}{w(R)^2+4(R\sigma_\theta)^2}\right].
\]

The averaged detected photon rate is \( \overline{\dot N} =
[P\lambda/(hc)]\,\eta_{\rm system}\,\overline{\eta}_{\rm cap}\).

These expressions **exclude** optical truncation, spacecraft dynamics, systematic mispointing, wavefront error, pointing-acquisition losses, detector noise, stellar background and weather. The Gaussian waist parameter is not an aperture diameter. The source and its receiver must be qualified separately.

## A message is not an average of its symbols

In ideal zero-background M-slot PPM with a mean \(s\) signal photons in the pulse slot, the exact uncoded hard-decision symbol error probability, with uniform random tie-breaking on empty frames, is

\[
P_{\rm SER}(s)=(1-1/M)e^{-s}.
\]

The probability that all \(n\) *uncoded* symbols are correct in a packet, conditional on one constant pointing gain \(G\), is

\[
P_{\rm packet}(G)=[1-(1-1/M)\exp(-s_0G)]^n.
\]

The correct pointing-averaged probability is \( \mathbb E[P_{\rm packet}(G)]\). The common shortcut \(P_{\rm packet}(\mathbb E[G])\) is generally **not equal** to it. Our code uses deterministic Simpson quadrature over the analytically derived gain distribution and checks it against a seeded, independent random sampling estimate.

At strictly **zero** background and perfect synchronization, the complete photon-count channel conveys ideal mutual information \(I(X;Y)=[1-e^{-s}]\log_2 M\) bits per uniformly chosen PPM symbol. This is an **information-theoretic** number, not reliably delivered coded goodput or spacecraft performance.

## Controlled numerical case

Distance 4.24 ly; wavelength 1064 nm; Gaussian transmitter waist radius 0.5 m; receiver *radius* 5 m; mean emitted optical power 10 W; end-to-end detection throughput 0.2. The far-field Gaussian divergence is 0.677 µrad and zero-pointing-error rate is 0.726 detected photons/s. The Airy-pupil model elsewhere predicts 0.363/s for a **different 1 m circular-pupil assumption**; this is not a discrepancy in a single physical model.

To expose burst losses, the calculation deliberately uses **100 seconds per uncoded 8-PPM symbol**, with **16 symbols per packet**, zero background and a fixed error vector throughout each packet. Such a long symbol is a teaching case, not a proposed modem data rate.

| Pointing sigma *per axis* | Mean detected photons/s | P(gain < 0.5) | Proper packet success | Incorrect mean-only approximation |
|---:|---:|---:|---:|---:|
| 0 µrad | 0.726 | 0.0% | ~100% | ~100% |
| 0.25 µrad | 0.470 | 28.0% | 99.6% | ~100% |
| 0.5 µrad | 0.228 | 72.8% | 76.4% | ~100% |
| **1.0 µrad** | **0.0747** | **92.4%** | **30.5%** | **99.2%** |
| 2.0 µrad | 0.0202 | 98.0% | 8.7% | 14.0% |

The difference is substantial but sensitive to the specific toy packet, timing and background assumptions. It should not be quoted as an operational receiver prediction.

## Reproducing and attempting to falsify the calculation

[Run the standalone Python source](../../research_tools/pointing_fade.py) and [20 independent regression controls](../../research_tools/tests/test_pointing_fade.py):

~~~bash
python -m research_tools.pointing_fade
python -m unittest discover -s research_tools/tests -v
~~~

The tests include independent seeded simulation of the 2-D pointing distribution and outage frequency, exact centered Gaussian aperture convolution, the far-field range-square limit, and numerical-quadrature comparisons. **Passing unit tests is not an independent instrument calibration**.

Next compare the model with actual pointing power spectral densities from an instrument, including thermal drift, actuator saturation and estimator lag. Then put measured background, detector dead time, receiver synchronisation, FEC, packet erasures and clock/telescope availability into one simulated chain.

## Published evidence and open questions

- Zwoliński, Jarzyna & Banaszek, *Optics Express* **26** (2018), [10.1364/OE.26.025827](https://doi.org/10.1364/OE.26.025827): full photocount-pattern decoding under background can have qualitatively different distance scaling than erasure-only decoding. **It does not validate the new pointing simulation**.
- Jarzyna *et al.*, [arXiv:2503.13161](https://arxiv.org/abs/2503.13161) (2025): photon information-efficiency constraints and receiver noise rejection.
- Badas Aldecocea *et al.*, SPIE 2024, [10.1117/12.3021617](https://doi.org/10.1117/12.3021617): wavefront errors and pointing-jitter statistics in free-space optics.
- Xiang *et al.*, *Optics Express* **26** (2018), [10.1364/OE.26.002848](https://doi.org/10.1364/OE.26.002848): dead time and timing jitter change photon-count likelihoods.
- Jiang, Liu & Shen, *Optics Letters* **51** (June 2026), [10.1364/OL.592295](https://doi.org/10.1364/OL.592295): **theoretical** capacity differences for engineered photon correlations, not a demonstrated interstellar source or FTL channel.
- [CCSDS 141.0-B-2](https://ccsds.org/searchpubs/entry/4662/) and [142.0-B-2](https://ccsds.org/publications/newbooks/), March 2026: relevant space optical standards. The models are not claimed compliant.

*Long-term engineering question:* which pointing feedback spectrum, acquisition strategy, optical waveform, coding scheme and receiver background rejection jointly maximise **CRC-verified fresh bits per transmitted joule** at large range? The causal-horizon boundary remains unchanged by better modulation or pointing.
