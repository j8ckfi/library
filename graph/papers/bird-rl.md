---
id: paper:bird-rl
type: paper
title: 'BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments'
authors:
- 'Ge Qu'
- 'Jinyang Li'
- 'Xiaohan Xu'
- 'Xiaolong Li'
- 'Bowen Qin'
- 'Nan Huo'
- 'Ziwei Tang'
- 'Chenhao Ma'
year: 2026
month: 10
arxiv_id: '2610.29426'
url: https://arxiv.org/abs/2610.29426
methods:
- method:bird-rl
cites:
- paper:sao
tags:
- agentic-rl
- sql
- active
---

# BIRD-RL

## Abstract Summary
BIRD-RL trains SQL/data-centric agents with a four-stage curriculum and trajectory-scoped persistent execution so database replicas can be reused without contaminating other rollouts.

## Key Contributions
1. BIRD-RL as an active plug-in on `task:agentic-async-rl`.

## Empirical Highlights
- 7B 44.40% / 14B 48.00% vs Claude-Opus-4.6 Agent 48.20%; 12.8x spatial RL efficiency vs per-rollout containers. Does not retarget `method:sao`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29426`
- Code: `https://github.com/bird-bench/BIRD-RL` (`code_status: released`).
