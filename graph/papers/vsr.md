---
id: paper:vsr
type: paper
title: Variance-Optimal State Resampling for Reinforcement Learning with Verifiable Rewards
authors:
- Yibo Wang
- Yuanxin Liu
- Zhaoran Wang
year: 2026
month: 10
arxiv_id: '2610.15888'
url: https://arxiv.org/abs/2610.15888
methods:
- method:vsr
cites:
- paper:minimax-m1
- paper:ngu
- paper:thinkprior
- paper:adastep
tags:
- post-training
- rlvr
- resampling
- neyman
---

# VSR (Variance-driven State Resampling)

## Abstract Summary
Neyman allocation μ(s)∝d(s)σ(s) over a prefix replay buffer for RLVR. Beats GRPO / GiGPO in the paper. Distinct from NGU (keep sampling until ≥1 correct) and ThinkPrior (zero-rollout Beta prior).

## Key Contributions
1. Prefix replay plus Neyman allocation on empirical occupancy and residual variance.
2. Dense-math GRPO host and GiGPO agentic host (BabyAI / Sokoban).
3. Not a prompt-selection prior and not an until-correct sampler.

## Empirical Highlights
- Qwen2.5-7B 37.6 vs GRPO 36.1; Llama-3.2-3B 19.1 vs 15.4 (single-paper).
- GiGPO+VSR Qwen2.5-1.5B BabyAI avg 47.6 vs 30.4; Sokoban 18.8 vs 12.7.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.15888`
- Code: `none found` (`code_status: none`).
