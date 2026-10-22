---
id: paper:empo
type: paper
title: 'One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents'
authors:
- 'Shaojin Ma'
- 'Ruitao Wang'
- 'Pengyi Li'
- 'Jie Yang'
- 'Liangyu Chen'
- 'Gangyi Zhao'
- 'Hongyao Tang'
- 'Yan Zheng'
year: 2026
month: 10
arxiv_id: '2610.29427'
url: https://arxiv.org/abs/2610.29427
methods:
- method:empo
cites:
- paper:canopy
tags:
- agent-rl
- credit
- active
---

# EMPO

## Abstract Summary
EMPO replaces response-specific probability ratios with an effect-level surrogate so distinct text that executes the same action shares credit.

## Key Contributions
1. EMPO as an active plug-in on `task:outcome-only-long-horizon-agent-rl`.

## Empirical Highlights
- outperforms strong baselines on all three environments without extra critics or rollouts. Does not retarget `method:canopy`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29427`
- Code: `none found` (`code_status: none`).
