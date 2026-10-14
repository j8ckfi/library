---
id: paper:justopd
type: paper
title: 'JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models'
authors:
- Zikun Zhang
- Jiayuan Sheng
- David D. Yao
- Wenpin Tang
year: 2026
month: 10
arxiv_id: '2610.17397'
url: https://arxiv.org/abs/2610.17397
methods:
- method:justopd
cites:
- paper:a2d
- paper:opd
- paper:semicat
tags:
- distillation
- diffusion-lm
- opd
---

# JustOPD

## Abstract Summary
On-policy distillation from an AR teacher onto a discrete diffusion LM (Dream-7B student, Qwen3-14B teacher). Not A2D's AR-delta recycle onto a converted dLLM, and not continuous SemiCat pretrain.

## Key Contributions
1. Token-level OPD matching from AR to absorbing/masked dLLM rollouts.
2. Length-conditioned GSM8K / MATH500 deltas (JSD).
3. No public code as of 2026-10-14.

## Empirical Highlights
- L=256 GSM8K 77.03→81.80, MATH500 31.80→39.60 (single-paper).
- L=512 GSM8K 78.77→84.45.
- L=1024 MATH500 36.80→48.00 (JSD).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17397`
- Code: `none found` (`code_status: none`).
