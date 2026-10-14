---
id: paper:tppo
type: paper
title: 'TPPO: Tracking-Value PPO For Language Model Reasoning'
authors:
- Futing Wang
- Chenxi Li
- Jianhao Yan
- Yun Luo
- Zhi Wang
- Yizhuo Li
- Runzhe Zhan
- Yu Cheng
- Tao Lin
year: 2026
month: 10
arxiv_id: '2610.16794'
url: https://arxiv.org/abs/2610.16794
methods:
- method:tppo
cites:
- paper:bpco
- paper:pact
tags:
- post-training
- actor-critic
- ppo
- value
---

# TPPO

## Abstract Summary
Tracking-Value PPO parameterizes the critic as cumulative log-odds rather than a scalar return. +7.0 / +8.4 vs PPO on Qwen3-4B/8B-Base math. HF Daily 2026-10-14.

## Key Contributions
1. Cumulative log-odds value so the critic tracks token-level odds instead of unbounded returns.
2. Single-sample PPO-family recipe; not group-relative CISPO.
3. Released trainer at LINs-lab/TPPO.

## Empirical Highlights
- Qwen3-4B-Base math 41.6 vs PPO 34.6 (+7.0); Qwen3-8B-Base 45.9 vs 37.5 (+8.4) (single-paper).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.16794`
- Code: `https://github.com/LINs-lab/TPPO` (`code_status: released`).
