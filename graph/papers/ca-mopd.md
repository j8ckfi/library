---
id: paper:ca-mopd
type: paper
title: 'Beyond Policy Discrepancy: Capability-Aware Multi-Teacher On-Policy Distillation'
authors:
- 'Xuanfeng Yang'
- 'Le Gui'
- 'Jiaming Wang'
- 'Xuan Zhang'
year: 2026
month: 10
arxiv_id: '2610.26950'
url: https://arxiv.org/abs/2610.26950
methods:
- method:ca-mopd
cites:
- paper:open-mopd
- paper:opd
tags:
- distillation
- mopd
- active
---

# Beyond Policy Discrepancy

## Abstract Summary
CA-MOPD merges RL specialists then allocates multi-teacher OPD strength from verifier-estimated capability gaps rather than behavioral discrepancy, so a student that already matches a teacher is not over-supervised.

## Key Contributions
1. Capability-gap allocation plus merged specialist initialization for MOPD.

## Empirical Highlights
- Average 32.22 vs naive MOPD / paper Open-MOPD / merged init. Paper Open-MOPD is not the library 83.4% bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.26950`
- Code: `none found` (`code_status: none`).
