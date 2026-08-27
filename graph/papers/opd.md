---
id: paper:opd
type: paper
title: "OPD: On-Policy Distillation with Generalized Divergence for Language Models"
authors:
  - "THU-NLP Team"
year: 2026
month: 4
arxiv_id: "2604.13016"
url: "https://arxiv.org/abs/2604.13016"
methods:
  - method:opd
cites:
  - paper:gkd
tags:
  - post-training
  - distillation
  - on-policy
  - opd
---

# OPD: On-Policy Distillation with Generalized Divergence for Language Models

## Abstract Summary
OPD (On-Policy Distillation) formalizes generalized divergence matching for distilling reasoning and generation capabilities from frontier teachers into small student models, establishing the 2026 default distillation framework.

## Key Contributions
1. **Generalized Divergence Formulation**: Unifies forward, reverse, and Jensen-Shannon on-policy distillation objectives.
2. **Student Rollout Optimization**: Eliminates teacher exposure bias by optimizing student-generated token trajectories.

## Open Source Repository
- Implementation: `https://github.com/thunlp/OPD`
