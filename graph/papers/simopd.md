---
id: paper:simopd
type: paper
title: 'SimOPD: Relational Knowledge Transfer for On-Policy Distillation'
authors:
- 'Kai Tang'
- 'Xing Zheng'
- 'Haobo Wang'
- 'Guangcheng Zhu'
- 'Shenzhi Yang'
- 'Zhengqing Zang'
- 'Yingfan Ma'
- 'Bowen Song'
- 'Weiqiang Wang'
year: 2026
month: 10
arxiv_id: '2610.23306'
url: https://arxiv.org/abs/2610.23306
methods:
- method:simopd
cites:
- paper:opd
- paper:ride
tags:
- distillation
- opd
- similarity
- active
---

# SimOPD

## Abstract Summary
A key challenge in on-policy distillation (OPD) is extracting effective supervision from teacher knowledge. Supervision from token probabilities may underutilize internal knowledge, while direct hidden-state matching forces the student to shift to the teacher's feature space and complicates cross-architecture transfer. Inspired by contrastive learning's use of relationships between instances, we propose \textbf{SimOPD} to transfer teacher internal knowledge through response similarities. Specifically, SimOPD uses paired memory banks of student-generated responses to extract supervision from the teacher's internal representations as similarity distributions. The student then matches these dis

## Key Contributions
1. SimOPD stores student-generated responses in paired memory banks, reads teacher internal representations as similarity distributions, and matches those distributions in the student's own representation space.

## Empirical Highlights
- +2.6 same-arch / +3.1 cross-arch vs strongest baselines

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23306`
- Code: `none found` (`code_status: none`).
