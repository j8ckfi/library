---
id: paper:diffusionart
type: paper
title: 'DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models'
authors:
- Zhenglin Wan
- Jiayu Chen
- Zhengfeiyang Zhang
- Pengfei Zhou
- Wangbo Zhao
- Fangyuan Kong
- Pengfei Wan
- Kun Gai
- Yang You
year: 2026
month: 10
arxiv_id: '2610.12572'
url: https://arxiv.org/abs/2610.12572
methods:
- method:diffusionart
cites:
- paper:mend
- paper:diffusion-opsd
- paper:self-opd
tags:
- diffusion
- post-training
- diffusionart
---

# DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models

## Abstract Summary
Online RL for diffusion is split: reverse-process methods (Flow-GRPO) waste GPU-hrs on poor credit; forward-process NFT is efficient but EMA-unstable. DiffusionART aggregates each prompt's rewards into a shared reverse-process direction (removing a hidden forward-reverse consistency force) and adds a trust-region-masked second update instead of EMA. No differentiable reward. Paper also reports DiffusionART-Pairwise.

## Key Contributions
1. Aggregation-first reward tilting for reverse-process states; cancels NFT-style consistency force by construction.
2. Trust-region-masked restoration without EMA HP search.
3. HunyuanVideo-13B: ~12× fewer GPU-hrs vs DiffusionNFT / Flow-GRPO-Fast at late-stage mean reward.

## Empirical Highlights
- See `method:diffusionart` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12572`
- Code: `https://github.com/vanzll/DiffusionART` (`code_status: released`).
