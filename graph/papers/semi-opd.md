---
id: paper:semi-opd
type: paper
title: "When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better"
authors:
  - "Siyan Zhao"
  - "Yonggan Fu"
  - "Jindong Jiang"
  - "Shih-Yang Liu"
  - "Song Bian"
  - "Byung-Kwan Lee"
  - "Sharath Turuvekere Sreenivas"
  - "Wenliang Dai"
  - "Hanrong Ye"
  - "Aditya Grover"
  - "Pavlo Molchanov"
year: 2026
month: 10
arxiv_id: "2610.11291"
url: "https://arxiv.org/abs/2610.11291"
methods:
  - method:semi-opd
cites:
  - paper:opd
  - paper:on-policy-or-off-policy
tags:
  - post-training
  - distillation
  - opd
  - semi-opd
  - offline-rollout
---

# When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better

## Abstract Summary
Live on-policy sampling is not always the right OPD rollout. Semi-OPD distills on offline rollouts from the *initial* student. Across 17 teacher-student pairs (1.5B–235B), Semi-OPD beats live OPD in 14 cases, up to +13.6% accuracy and 11.4× training speedup. Live OPD wins only when initial teacher–student output-token overlap is already high. A training agent should check overlap before paying for on-policy rollouts. No official GitHub as of 2026-10-09.

## Key Contributions
1. Semi-OPD: freeze initial-student rollouts; distill on that offline prefix set.
2. 14/17 pairs beat live OPD; up to +13.6% and 11.4× wall-clock.
3. Route by initial output-token overlap: high overlap → live OPD; otherwise Semi-OPD.

## Empirical Highlights
- 17 pairs, 1.5B–235B: Semi-OPD wins 14.
- Up to +13.6% accuracy and 11.4× training speedup vs live OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11291`
- Code: none found as of 2026-10-09 (`code_status: none`).
