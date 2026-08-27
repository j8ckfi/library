---
id: paper:opd2
type: paper
title: "OPD2: Multi-Teacher On-Policy Distillation at Scale"
authors:
  - "NAVER AI Lab Team"
year: 2026
month: 7
arxiv_id: "2607.15161"
url: "https://arxiv.org/abs/2607.15161"
methods:
  - method:opd2
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd2
---

# OPD2: Multi-Teacher On-Policy Distillation at Scale

## Abstract Summary
OPD2 extends on-policy distillation to heterogeneous multi-teacher ensembles, dynamically routing student tokens to domain-specialist teachers (math, coding, reasoning).

## Key Contributions
1. **Dynamic Teacher Routing**: Adaptive weighting across specialized teacher models during student rollouts.
2. **Ensemble Knowledge Transfer**: Combines strengths of multiple specialized frontier models into a single compact student.

## Open Source Repository
- Implementation: `https://github.com/naver-ai/opd2` (claimed)
