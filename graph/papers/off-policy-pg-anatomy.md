---
id: paper:off-policy-pg-anatomy
type: paper
title: 'Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines'
authors:
- 'Haoqun Cao'
- 'Yurun Yuan'
- 'Tengyang Xie'
year: 2026
month: 10
arxiv_id: '2610.25725'
url: https://arxiv.org/abs/2610.25725
methods:
- method:cispo
cites:
- paper:minimax-m1
- paper:score-centering-pg
tags:
- rlvr
- gotcha
---

# Off-Policy PG Anatomy

## Abstract Summary
For a general class of off-policy PG updates, consistency (optimum remains a stationary point) requires trajectory-level IS or KL regularization paired with a baseline equal to the optimal soft value. Grouped-mean baselines along the KL route implement pessimism. Trajectory IS suffers the curse of horizon.

## Key Contributions
1. Two consistent off-policy PG routes plus a finite-sample grouped-mean baseline analysis.

## Empirical Highlights
- Does not retarget CISPO. Use with paper:score-centering-pg.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25725`
- Code: `none found` (`code_status: none`).
