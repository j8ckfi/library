---
id: paper:dfr
type: paper
title: 'Distribution-Based Regularization for Reward Fine-Tuning Diffusion and Flow Models'
authors:
- 'Romeo Passaro'
- 'Jeongjae Lee'
- 'Jong Chul Ye'
- 'Michael M. Bronstein'
- 'Yoshua Bengio'
- 'Alexander Tong'
- 'Danyal Rehman'
year: 2026
month: 10
arxiv_id: '2610.24897'
url: https://arxiv.org/abs/2610.24897
methods:
- method:dfr
cites:
- paper:diffusion-opsd
- paper:self-opd
tags:
- diffusion
- reward-ft
- active
---

# DFR

## Abstract Summary
Reverse-KL reward FT of diffusion/flow is an l2 velocity penalty that does not act on the generated distribution. DFR adds MMD / Frechet / DreamSim distributional rewards. On SD3.5-M, up to +29% diversity and -12% drift at matched reward, 36-41x faster than Flow-GRPO.

## Key Contributions
1. Distributional functional rewards as the regularizer for reward FT.

## Empirical Highlights
- DFR-MMD GenEval 0.95 at +7% time vs RAM with +9% diversity.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24897`
- Code: `none found` (`code_status: none`).
