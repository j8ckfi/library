---
id: paper:soloq
type: paper
title: 'SoloQ: Calibration-Free Quantization for Diffusion Language Models'
authors:
- Donghyun Lee
- Arkapravo Ghosh
- Varun Manjunath
- Bumjoon Kyle Rhee
- Hyunho Kook
- Shiting Xiao
- Youngeun Kim
- Priyadarshini Panda
year: 2026
month: 10
arxiv_id: '2610.07121'
url: https://arxiv.org/abs/2610.07121
methods:
- method:soloq
cites:
- paper:quartet-ii
- paper:kbbq
- paper:a2d
tags:
- quantization
- dllm
- nvfp4
- soloq
---

# SoloQ: Calibration-Free Quantization for Diffusion Language Models

## Abstract Summary
dLLM activations shift across masks and denoising steps, so calibration-based PTQ is brittle. SoloQ maps weights and activations into a normalized rotated basis (structured K-RPBH plus a rescaling correction) with a predictable marginal, so codebooks and NVFP4 need no data. Block-diffusion gets commit-time KV quantization that leaves the active block in higher precision.

## Key Contributions
1. Calibration-free rotation+rescale PTQ for dLLMs.
2. NVFP4 and distribution-matched codebooks from the post-rotation law.
3. Commit-time KV quant for block-diffusion; up to 2.61× / 2.24× mem / speed.

## Empirical Highlights
- See `method:soloq` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07121`
- Code: `https://github.com/Intelligent-Computing-Lab-Panda/SoloQ` (`code_status: announced`).
