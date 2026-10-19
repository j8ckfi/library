---
id: paper:opmd
type: paper
title: 'OPMD: On-Policy Mechanism Distillation Beyond Output Supervision'
authors:
- 'Yingdong Shi'
- 'Zhihong Li'
- 'Changming Li'
- 'Jingyi Yu'
- 'Quan Li'
- 'Kan Ren'
year: 2026
month: 10
arxiv_id: '2610.14022'
url: https://arxiv.org/abs/2610.14022
methods:
- method:opmd
cites:
- paper:opd
- paper:ride
tags:
- distillation
- opd
- mechanism
- active
---

# OPMD

## Abstract Summary
On-policy distillation (OPD) improves language-model by supervising a student on prefixes sampled from its own policy, but its supervision remains confined to the output space. Consequently, OPD transfers what a teacher predicts without supervising the intermediate computation that produces those predictions. Simply distilling intermediate representations like representation matching is insufficient since teacher and student representations may differ geometrically, and even well-aligned hidden states need not be usable by the student's subsequent computation. We introduce On-Policy Mechanism Distillation (OPMD), which transfers teacher-derived intermediate computation while explicitly accou

## Key Contributions
1. OPMD first builds a student-compatible teacher that transforms teacher representations into intermediate states the student's downstream layers can use, then internalizes those states from on-policy trajectories.

## Empirical Highlights
- highest average in all three teacher-student settings; generalizes to multi-teacher and cross-family SFT

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14022`
- Code: `none found` (`code_status: none`).
