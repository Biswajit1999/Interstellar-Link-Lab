# Photon-counted PPM: soft-decision frame experiment

**Research lead:** Biswajit Jana · **Date:** 25 October 2026  
**Status:** Reproducible synthetic model; not hardware or FTL transmission.

## Question

Under a photon-starved Poisson slot-count channel, how frequently does a CRC-framed fresh message survive PPM signalling, a rate-1/2 convolutional code and a soft-decision Viterbi decoder?

## Forward model

An M-PPM symbol contains one illuminated slot. Conditional photon counts are independent:

`N_active ~ Poisson(s+b)`, and `N_other ~ Poisson(b)`, with s the mean detected signal photons in the active slot, b the background mean per slot. A count array has enough information to construct symbol likelihoods. For b>0 the symbol log-likelihood, up to a constant shared between hypotheses, is `n_j log((s+b)/b)`; bit LLRs compare the sum of likelihoods across labels with bit 0 versus 1.

The prototype terminates a constraint-length-3, rate-1/2 convolutional code with octal generators (7,5), computes soft PPM bit likelihoods and performs Viterbi decoding. A CRC-32 check rejects uncorrected frames. It is **not** a CCSDS standard implementation; perfect slot synchronization is assumed.

## Deterministic synthetic study

- Alphabet sizes: M = 4, 8, 16.
- Illuminated-slot signal photons: 0.5, 1, 2, 3, 4, 6, 8, 12.
- Background: 0.08 expected photons/slot; slot width 100 microseconds.
- Sixty independently seeded message trials at each of 24 parameter combinations; successful outcome is valid decoded CRC.
- At s = 4, **8-PPM: 58/60 valid frames**, 95% Wilson interval **0.886–0.991**; **16-PPM: 44/60**, interval **0.610–0.829**.
- At s = 1, 8-PPM had 0/60 valid frames. Finite trials imply an uncertain nonzero underlying success probability, not proof of impossibility.
- Photon-per-pulse comparisons do not hold fixed average optical transmit power; do not interpret their order as a fixed-energy global optimum.

For a highly optimistic static 4.24-light-year optical geometry, P=1000 W, wavelength=1550 nm, transmit D=10 m, receiver D=30 m and scalar throughput=0.2 produce an **ideal received-photon count rate of about 22,411/s**. Acquisition, pointing, background and detector imperfections are omitted.

## Causal timing

The earliest complete message reception in this reference model obeys:

`t_complete >= t_emit + t_light + N_symbol M T_slot`.

For a receiver moving with constant velocity v relative to its initial displacement r0, the flat-spacetime interception equation is `|r0 + vt| = ct`. A 4.24-ly static distance is **not an epoch-frozen Gaia ephemeris**. This model cannot demonstrate controllable faster-than-light communication, and its predictive-image prior cannot provide unknown new bits before their physical arrival.

## Engineering artifacts

See [hardware and electrical architecture](../../hardware/OPTICAL_ARCHITECTURE.md). The complete local v0.4 release includes editable SVG diagrams, a five-page technical manuscript, a browser experiment viewer, a Python advanced modem package, seeded numerical JSON and 76 locally passing test cases (60 baseline pytest + 16 additional advanced unittest cases). **Those binary/advanced source artifacts are not asserted to be uploaded here until they are independently committed and checked.**

## Next experiment gates

Detector timing/dead time and afterpulsing; background PSD and stellar photon models; acquisition and pointing; code comparison against sourced CCSDS recommendations; fair power and bandwidth accounting; detector-calibrated bench results; measured covariance in Gaia/JPL moving-endpoint propagation; independently audited causal interventions and GR source/energy conditions.
