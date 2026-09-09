---
id: paper:kbbq
type: paper
title: "KBBQ: A Predictive Noise Law and the Limits of Spectrum Flattening in FP4 Quantization"
authors:
  - "Lexington Whalen"
  - "Yuki Ito"
  - "Ryo Sakamoto"
year: 2026
month: 9
arxiv_id: "2609.08135"
url: "https://arxiv.org/abs/2609.08135"
methods:
  - method:kbbq
cites: []
tags:
  - quantization
  - fp4
  - kbbq
---

# KBBQ: A Predictive Noise Law and the Limits of Spectrum Flattening in FP4 Quantization

## Abstract Summary
A second-order theory of quantization noise in matmul characterizes a format by the variance it assigns each element. Integer quantization recovers existing integer-noise theory; floating-point rounding reduces data dependence to a participation factor κ and a closed-form SNR law, with a tight upper bound κ* attained by a recent SOTA flatten. KBBQ (Kappa-Braked Blockwise Quantization) parameterizes how far a transform approaches that ceiling. At W4A4, across four base models and two FP4 formats, KBBQ outperforms the prior SOTA without extra deployment-time compute. Niche beside Quartet-II / MXFP4 (native FP4 *training*), not a hardware-train default.

## Key Contributions
1. **κ participation factor** and closed-form FP quantization SNR.
2. **κ* bound** no function-preserving linear transform can exceed.
3. **KBBQ**: brake how close a blockwise transform sits to that bound.

## Empirical Highlights
- W4A4: beats prior SOTA on four base models × two FP4 formats, no extra deploy compute.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
