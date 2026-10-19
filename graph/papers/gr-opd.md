---
id: paper:gr-opd
type: paper
title: 'GR-OPD: Group-Relative Sequence Credit for On-Policy Distillation'
authors:
- 'Yushu Wang'
- 'Renkai Yang'
- 'Jingcao Xu'
- 'Zili Geng'
- 'Haihong Tang'
- 'Yaohui Jin'
- 'Hao He'
year: 2026
month: 10
arxiv_id: '2610.23042'
url: https://arxiv.org/abs/2610.23042
methods:
- method:gr-opd
cites:
- paper:opd
tags:
- distillation
- opd
- sequence-credit
- active
---

# GR-OPD

## Abstract Summary
On-policy distillation (OPD) provides token-level teacher feedback, yet common sampled-token updates assign credit locally and omit the effects of earlier actions on subsequent feedback. We introduce \method{} (Group-Relative On-Policy Distillation), which decouples feedback computation from credit assignment by aggregating token feedback into calibrated sequence-level credit. We establish a theoretical basis for this approach by showing that, under ideal on-policy assumptions, broadcasting raw summed feedback to every response token yields an unbiased estimate of the negative gradient of the sequence-level reverse-KL objective. To support effective learning in practice, \method{} discounts 

## Key Contributions
1. GR-OPD aggregates token-level teacher feedback into calibrated sequence-level credit, discounts later feedback under distribution shift, and keeps a controlled fraction of the group mean as collective teacher pressure.

## Empirical Highlights
- wins every setting; +10.9 and +11.5 pp with matched thinking; vanilla OPD collapses on mismatched thinking

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23042`
- Code: `none found` (`code_status: none`).
