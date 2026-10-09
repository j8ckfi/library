---
id: paper:delta-mopd
type: paper
title: "Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts"
authors:
  - "Hejian Sang"
  - "Zhengze Zhou"
  - "Shayan Mohajer Hamidi"
  - "Xiaomin Li"
  - "Rohit Jain"
  - "Alborz Geramifard"
year: 2026
month: 10
arxiv_id: "2610.10460"
url: "https://arxiv.org/abs/2610.10460"
methods:
  - method:delta-mopd
cites:
  - paper:open-mopd
  - paper:opd
tags:
  - post-training
  - distillation
  - mopd
  - delta-mopd
---

# Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts

## Abstract Summary
MOPD usually copies each teacher's endpoint policy, which mixes post-training change with preferences inherited from that teacher's base. Inherited base pull can exceed the post-training shift and distort composition. Δ-MOPD transfers each teacher's teacher-minus-base logit shift, re-anchored at the student's frozen initialization. Holds teacher selection fixed and compares to endpoint supervision in common-domain composition and routed-domain distillation. Beside Open-MOPD. No official GitHub as of 2026-10-09.

## Key Contributions
1. Endpoint MOPD mixes inherited base pull with the post-training shift.
2. Δ-MOPD: teacher-minus-base logit shift re-anchored at the student init.
3. Same teacher selection; shift targets improve composition geometry vs endpoint copy.

## Empirical Highlights
- Inherited base pull can exceed the post-training shift and inflate teacher-term norm / target-student KL.
- Shift targets help common-domain composition and phased routed-domain distillation.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.10460`
- Code: none found as of 2026-10-09 (`code_status: none`).
