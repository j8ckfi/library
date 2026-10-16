---
id: paper:rpo
type: paper
title: 'Routing Policy Optimization for Online Diffusion Reinforcement Learning'
authors:
- Qiuhong Shen
- Yiding Yang
- Yuxin Zhang
- Xinwei Huang
- Minxuan Lin
- Bo Liu
- Hao Kang
- Haotian Yang
- Yizhi Wang
- Chongyang Ma
- Xinchao Wang
year: 2026
month: 10
arxiv_id: '2610.22282'
url: https://arxiv.org/abs/2610.22282
methods:
- method:rpo
cites:
- paper:diffusionart
- paper:mend
tags:
- diffusion
- rl-alignment
- routing
---

# Routing Policy Optimization (RPO)

## Abstract Summary
Score-function diffusion RL usually perturbs the reverse trajectory. RPO instead samples attention routes at a few denoising levels, scores the velocity perturbation against the dense-attention velocity, and uses a two-rollout reward difference. Inference restores dense attention and the original sampler.

## Key Contributions
1. Attention routing as the stochastic exploration action.
2. Shared-prompt two-rollout advantage; learned updates remain after routing is dropped.
3. Text-to-image and text-to-video vs Flow-GRPO-style.

## Empirical Highlights
- Nearly 4x higher training efficiency than Flow-GRPO-style methods at improved generation quality.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22282`
- Project: `https://velox-world.com/rpo`
- Code: `none found` (`code_status: none`). Distinct from skipped root-token RPO 2610.17767.

