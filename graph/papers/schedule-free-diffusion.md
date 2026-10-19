---
id: paper:schedule-free-diffusion
type: paper
title: 'Large Diffusion Models Need More Than EMA'
authors:
- 'Chuyu Hu'
- 'Huanran Chen'
- 'Shitong Shao'
- 'Yinpeng Dong'
year: 2026
month: 10
arxiv_id: '2610.22945'
url: https://arxiv.org/abs/2610.22945
methods:
- method:schedule-free-diffusion
cites:
- paper:representation-guidance
- paper:diffusion-opsd
tags:
- diffusion
- optimizer
- ema
- active
---

# Schedule-Free Diffusion

## Abstract Summary
Large-scale diffusion models are commonly trained with a constant learning rate (LR) and exponential moving average (EMA), despite the strong performance of LR decay and Schedule-Free optimization in training large language models. We study whether EMA is uniquely suited to diffusion training, or whether stronger alternatives have been underexplored. Our theory shows that averaging a constant-step trajectory has an inherent optimization limitation, whereas LR decay and Schedule-Free optimization admit vanishing stationarity guarantees under standard nonconvex assumptions. Empirically, LR decay and EMA provide complementary benefits: combining decay with EMA further improves the standard base

## Key Contributions
1. Schedule-Free (and LR decay) replace or complement EMA on large diffusion models: averaging a constant-step trajectory has an inherent optimization limit, while Schedule-Free reduces parameter variability without freezing late-stage progress.

## Empirical Highlights
- Schedule-Free beats constant-LR EMA across stages; LR decay+EMA is complementary but aggressive decay+EMA weakens continued optimization

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22945`
- Code: `none found` (`code_status: none`).
