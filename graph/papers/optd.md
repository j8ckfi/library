---
id: paper:optd
type: paper
title: 'On-Policy Transition Distillation'
authors:
- 'Runyang You'
- 'Yongqi Li'
- 'Tiezheng Yu'
- 'Wenjie Li'
year: 2026
month: 10
arxiv_id: '2610.28048'
url: https://arxiv.org/abs/2610.28048
methods:
- method:optd
cites:
- paper:opd
tags:
- distillation
- opd
- active
---

# On-Policy Transition Distillation

## Abstract Summary
OPTD keeps final-layer OPD and also matches teacher/student layer-to-layer log-probability increments on student rollouts after a diagnostic that lower transition KL tracks correctness.

## Key Contributions
1. Depthwise prediction-transition matching on student rollouts.

## Empirical Highlights
- Three-domain gap recovery ~90% vs ~75% for OPD; best or tied-best overall in dual- and three-domain.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28048`
- Code: `none found` (`code_status: none`).
