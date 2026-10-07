---
id: paper:a2d
type: paper
title: "Enhancing Diffusion Language Models with Autoregressive Post-Training Weights"
authors:
  - Yiming Qin
  - Ke Wang
  - Amel Abdelraheem
  - Adam Hazimeh
  - Pascal Frossard
year: 2026
month: 10
arxiv_id: "2610.08108"
url: "https://arxiv.org/abs/2610.08108"
methods:
  - method:a2d
cites:
  - paper:canvasanneal
tags:
  - diffusion
  - dllm
  - post-training
  - a2d
---

# Enhancing Diffusion Language Models with Autoregressive Post-Training Weights

## Abstract Summary
A2D recycles an AR post-training weight delta onto a converted dLLM base. That recycle approaches direct diffusion post-training and composes with it; AR and diffusion deltas are nearly orthogonal. First hop on `task:diffusion-lm-ar-delta-recycle`. Does not replace DiffusionOPSD / Self-OPD / CanvasAnneal.

## Key Contributions
1. **AR post-training delta** added to a converted dLLM.
2. **Approaches direct diffusion PT** and composes with it.
3. **AR / diffusion deltas nearly orthogonal**.

## Empirical Highlights
- Recycle-then-diffusion is available; do not treat as Uno serving.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08108`
- Code: none found as of 2026-10-07 (`code_status: none`).
