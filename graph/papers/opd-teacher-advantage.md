---
id: paper:opd-teacher-advantage
type: paper
title: 'Demystifying On-Policy Distillation: Where Does the Teacher’s Advantage Live?'
authors:
- Yiping Li
- Zhibo Hou
- Fan Zhao
- Zhiyu An
- Wan Du
year: 2026
month: 10
arxiv_id: '2610.19145'
url: https://arxiv.org/abs/2610.19145
methods:
- method:opd
cites:
- paper:opd
tags:
- distillation
- opd
- gotcha
---

# Where the OPD teacher's advantage lives

## Abstract Summary
Controlled token flips at teacher-student disagreements locate the teacher's advantage along student trajectories. Single-token flips are modest. Repeated flips raise accuracy from 28.4% to 74.5% vs teacher 76.9%. Mass- and KL-based selection beat random flips by 15-18pp at similar counts. After OPD, more argmax agreement does not consistently raise accuracy.

## Key Contributions
1. Flip interventions as a KD diagnostic on student-generated traces.
2. Repeated vs single corrections; mass/KL selection vs random.
3. Post-OPD remaining headroom is not just argmax match.

## Empirical Highlights
- Repeated flips 28.4%→74.5% (teacher 76.9%) on selected failed trajectories.
- Mass/KL selection +15-18pp vs random at similar flip counts.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19145`
- Code: `none found` (`code_status: none`).
