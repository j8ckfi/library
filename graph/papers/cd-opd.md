---
id: paper:cd-opd
type: paper
title: 'CD-OPD: Contextual Digest for On-Policy Distillation'
authors:
- 'Mingyuan Li'
- 'Yucheng Li'
- 'Xiaxia Wang'
- 'Gong Cheng'
year: 2026
month: 10
arxiv_id: '2610.25359'
url: https://arxiv.org/abs/2610.25359
methods:
- method:cd-opd
cites:
- paper:opd
- paper:branchopd
tags:
- distillation
- opd
- active
---

# CD-OPD

## Abstract Summary
Teacher takeover can be wrong even when student and teacher are independently correct (Collaboration Failure Rate). CD-OPD inserts a teacher-generated contextual digest of required conditions and prior reasoning, then meta-reweights digest segments. +1.32 to +7.05 pp and CFR -27.4% to -56.4%.

## Key Contributions
1. Digest-structured takeover OPD plus online meta-reweighting.

## Empirical Highlights
- Lengthening takeover does not monotonically reduce CFR.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25359`
- Code: `none found` (`code_status: none`).
