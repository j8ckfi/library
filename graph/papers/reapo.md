---
id: paper:reapo
type: paper
title: 'ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning'
authors:
- 'Nghi Dao'
- 'Calder Morton-Ferguson'
- 'Noah Golowich'
- 'Adam Block'
year: 2026
month: 10
arxiv_id: '2610.28770'
url: https://arxiv.org/abs/2610.28770
methods:
- method:reapo
cites:
- paper:minimax-m1
tags:
- rlvr
- exploration
- active
---

# ReAPO

## Abstract Summary
ReAPO treats verified success as an SSP terminal and serializes failed GRPO attempts so a later success is credited without reinforcing the preceding failures.

## Key Contributions
1. ReAPO as an active plug-in on `task:math-code-rl-dense`.

## Empirical Highlights
- beats GRPO and recent retry baselines on first-attempt; Qwen3-0.6B reaches 2x-group / 2x-step GRPO peaks with 39% / 31% fewer generated tokens. Does not retarget `method:cispo`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28770`
- Code: `https://github.com/Nghi-Dao/ReAPO` (`code_status: released`).
