---
id: paper:projected-distillation
type: paper
title: 'Projected Distillation: On Learning to Solve Hard Problems from Close, Correct Targets'
authors:
- 'Shripad V. Deshmukh'
- 'Christian Bock'
- 'Kangrui Ruan'
- 'Abhijeet Awasthi'
- 'Vijay Lingam'
- 'Rein Houthooft'
- 'Manish Prajapat'
year: 2026
month: 10
arxiv_id: '2610.27467'
url: https://arxiv.org/abs/2610.27467
methods:
- method:projected-distillation
cites:
- paper:opd
tags:
- distillation
- opd
- active
---

# Projected Distillation

## Abstract Summary
Projected distillation minimally edits failed student attempts into correct targets and contrastively prefers those corrections, so hard problems still get near-on-policy signal when every rollout fails.

## Key Contributions
1. On-policyness as a continuum; linear vs quadratic regret in edit size.

## Empirical Highlights
- Best specialization-retention AUC on 8/9 cells vs GRPO and OPD; gold solutions drop retention 0.916→0.744.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27467`
- Code: `none found` (`code_status: none`).
