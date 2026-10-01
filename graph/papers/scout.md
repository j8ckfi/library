---
id: paper:scout
type: paper
title: "On the Off-Policy Teacher in On-Policy Distillation"
authors:
  - "Langlin Huang"
  - "Hao Liu"
  - "Mononito Goswami"
  - "Xinyu Li"
  - "Prithwish Jana"
  - "Nikos Kanakaris"
  - "Patrick Blöbaum"
  - "Purak Jain"
year: 2026
month: 9
arxiv_id: "2609.38360"
url: "https://arxiv.org/abs/2609.38360"
methods:
  - method:scout
cites:
  - paper:opd
  - paper:tropd
tags:
  - post-training
  - distillation
  - on-policy
  - scout
---

# On the Off-Policy Teacher in On-Policy Distillation

## Abstract Summary
OPD samples student trajectories and asks a frozen teacher to supervise those prefixes. The trajectories are on-policy for the student and off-policy for the teacher: continuation accuracy falls as student prefixes lengthen, and teacher entropy stays high on student contexts while shrinking on the teacher's own prefixes. SCOUT (Student-COnditioned Updates of the Teacher) keeps the student OPD update and periodically trains the teacher with outcome RL on continuations from student-generated prefixes, then syncs the adapted teacher back. Complementary to student-side gating (TrOPD / SAKI). Across teacher–student pairs, +1.2–2.6 math accuracy over frozen-teacher OPD; code 56.6→59.7. AWS AI Labs / WashU / CMU / Georgia Tech. No public GitHub as of 2026-10-01.

## Key Contributions
1. **Off-policy teacher diagnosis**: teacher continuation from student prefixes degrades with prefix length; entropy gap vs teacher-native prefixes persists.
2. **Teacher-side axis**: adapt the teacher on student prefixes with verifiable-outcome RL rather than only gating a frozen teacher.
3. **Complementary to student-side filters**: sparse teacher updates plus a rising prefix-ratio schedule; a control that updates the teacher without student-prefix conditioning does not match SCOUT.

## Empirical Highlights
- Math: +1.2–2.6 average accuracy over frozen-teacher OPD across three teacher–student configurations.
- Code: 56.6 → 59.7 average. Student-prefix conditioning is load-bearing vs extra teacher RL without it.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.38360`
- Code: none found as of 2026-10-01 (`code_status: none`).
