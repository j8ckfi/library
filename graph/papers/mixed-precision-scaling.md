---
id: paper:mixed-precision-scaling
type: paper
title: Mixed Precision Scaling Laws for Quantized Pretraining
authors:
- Jinuk Kim
- Rajarshi Saha
- Muhammed Fatih Balin
- Youngsuk Park
year: 2026
month: 10
arxiv_id: '2610.17637'
url: https://arxiv.org/abs/2610.17637
methods:
- method:mixed-precision-scaling
cites:
- paper:quartet-ii
tags:
- quantization
- fp4
- scaling-laws
- mixed-precision
---

# Mixed Precision Scaling Laws for Quantized Pretraining

## Abstract Summary
Scaling law for quantized pretraining that separates capacity effects from persistent optimization error in the forward and backward passes. Decomposes existing 4-bit recipes (NVFP4 vs Quartet II) into per-pass components. Forward quantization is more loss-sensitive than backward. Use the law to pick which pass to keep high precision under a compute budget.

## Key Contributions
1. Decomposition of NVFP4 / Quartet II recipes into forward vs backward components on 430M Qwen3 at 12.8B tokens.
2. Law \(L\) with \(\rho_N,\rho_D,\varepsilon_f,\varepsilon_b\); up to \(11\times\) lower held-out MSE than existing quantized-pretrain laws (single-paper).
3. Layer-wise mixed-precision extension; compute-optimal forward/backward NVFP4 fraction vs MXFP8.

## Empirical Highlights
- Backward-only NVFP4: +0.32–0.72% val loss vs BF16; forward-only: +0.94–1.22% (430M Qwen3, 12.8B tokens; Table 1).
- Best uniform FP4 (Quartet II) still leaves a gap to BF16; mixed precision is the paper's recommended close.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17637`
- Code: `none found` (`code_status: none`).
