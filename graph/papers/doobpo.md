---
id: paper:doobpo
type: paper
title: 'Doob-Based Generative Policy Optimization'
authors:
- 'Maojiang Su'
- 'Qijie Zhu'
- 'Yu Xiao'
- 'Shuyang Yu'
- 'Minshuo Chen'
- 'Zhaoran Wang'
- 'Han Liu'
year: 2026
month: 10
arxiv_id: '2610.28990'
url: https://arxiv.org/abs/2610.28990
methods:
- method:doobpo
cites:
- paper:diffusion-opsd
tags:
- diffusion
- flow
- active
---

# DoobPO

## Abstract Summary
DoobPO fine-tunes diffusion/flow policies without action likelihoods: a ratio model represents the desired update, then a Doob h-transform distills the ratio-tilted target into the generator as conditional drift.

## Key Contributions
1. DoobPO as an active plug-in on `task:posttrain-diffusion`.

## Empirical Highlights
- separates a lightweight ratio-model improvement from generative distillation via conditional drift matching; NeurIPS 2026. Does not retarget `method:diffusion-opsd`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28990`
- Code: `none found` (`code_status: none`).
