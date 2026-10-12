---
id: paper:dualquant
type: paper
title: 'DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs'
authors:
- Mahsa Salmani
- Sayeh Sharify
- Hesham Mostafa
year: 2026
month: 10
arxiv_id: '2610.13767'
url: https://arxiv.org/abs/2610.13767
methods:
- method:dualquant
cites:
- paper:kbbq
- paper:quartet-ii
tags:
- quantization
- ptq
- w4a4
- dualquant
---

# DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs

## Abstract Summary
Activation quantization usually needs calibration. DualQuant minimizes weight-reconstruction MSE with dual scales; the same scales rescale activations before they are quantized. Variable splitting + block coordinate descent, each subproblem closed-form. Unified MX family and NVFP4. Packed W4A4 on 4090 tracks fake-quant accuracy.

## Key Contributions
1. Calibration-free dual-scale W+A PTQ from weight-reconstruction MSE.
2. Formal MX / NV block-format support.
3. Packed W4A4 Llama-3.1-8B on RTX 4090; up to 2.61× memory cut.

## Empirical Highlights
- See `method:dualquant` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13767`
- Code: `none found` (`code_status: none`).
