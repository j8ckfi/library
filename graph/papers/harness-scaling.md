---
id: paper:harness-scaling
type: paper
title: 'Harness Scaling for Generalizable Agentic Reinforcement Learning'
authors:
- 'Fei Bai'
- 'Huatong Song'
- 'Chuan Hao'
- 'Ran Tao'
- 'Jian Yang'
- 'Bryan Dai'
- 'Wayne Xin Zhao'
- 'Ji-Rong Wen'
year: 2026
month: 10
arxiv_id: '2610.29458'
url: https://arxiv.org/abs/2610.29458
methods:
- method:harness-scaling
cites:
- paper:neohorse-1
tags:
- agentic-rl
- harness
- active
---

# Harness Scaling

## Abstract Summary
Harness Scaling treats harness configuration as a training axis: a factorized space, a compact factorial training subset, and RL that mixes global coverage with controlled per-task variation.

## Key Contributions
1. Harness Scaling as an active plug-in on `task:agentic-rsi-routing-posttrain`.

## Empirical Highlights
- improves unseen white-box configs; transfers to unseen external black-box harnesses better than training on one complex black-box harness. Does not retarget `method:neohorse-1`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29458`
- Code: `none found` (`code_status: none`).
