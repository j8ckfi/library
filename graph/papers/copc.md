---
id: paper:copc
type: paper
title: "COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning"
authors:
  - "Zicheng Hu"
  - "Zhijian Zhou"
  - "Xuan Zhang"
  - "Yuchen Liu"
  - "Cheng Chen"
  - "Yuan Li"
  - "Qi Gu"
  - "Yan Feng"
  - "Hongyan Hao"
  - "Chao Qu"
year: 2026
month: 10
arxiv_id: "2610.09597"
url: "https://arxiv.org/abs/2610.09597"
methods:
  - method:copc
cites:
  - paper:sao
tags:
  - post-training
  - async-rl
  - off-policy
  - copc
---

# COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning

## Abstract Summary
Async RL trains on stale trajectories. Policy-side IS correction alone is not enough: advantages also inherit mismatch from behavior-policy continuations (advantage staleness). COPC is an actor-critic method that couples token-level ratio masking with two-sided clipped-ratio weighting of TD residuals. Highest reported tool-integrated math and search among the paper's async baselines; stable at 64-step staleness; 1.7x step-time vs synchronous PPO. Beside SAO.

## Key Contributions
1. Advantage staleness: behavior-policy continuations bias advantages even after actor IS correction.
2. Couple policy-weight masking with two-sided clipped-ratio TD residual weighting.
3. Joint HP sweeps: one correction parameter can reverse the effect of the other.

## Empirical Highlights
- Highest reported tool-integrated math and search vs the paper's strongest async baselines.
- Gains persist at 64-step policy staleness. Search stays stable while most async baselines collapse late.
- Minimal step-time overhead vs async PPO; 1.7x step-time vs synchronous PPO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.09597`
- Code: none found as of 2026-10-09 (`code_status: none`).
