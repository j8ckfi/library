---
id: paper:ask-to-distill
type: paper
title: 'Ask to Distill: Learning to Synthesize Data for On-Policy Distillation'
authors:
- 'Jiashuo Sun'
- 'Hao Zhang'
- 'Xueqiang Xu'
- 'Heng Wang'
- 'Yixuan Xie'
- 'Pengcheng Jiang'
- 'Zhenrui Yue'
- 'Jiajun Fan'
- 'Peiran Li'
- 'Ge Liu'
- 'Shaowen Wang'
- 'Jiawei Han'
year: 2026
month: 10
arxiv_id: '2610.27450'
url: https://arxiv.org/abs/2610.27450
methods:
- method:ask-to-distill
cites:
- paper:opd
tags:
- distillation
- opd
- synthetic-data
- active
---

# Ask to Distill

## Abstract Summary
Ask-to-Distill optimizes a student-initialized question synthesizer with a distributional surrogate from a frozen student-teacher pair (disagreement plus teacher mass on the student support), then runs ordinary OPD on the prompt-only bank.

## Key Contributions
1. Answer-free synthesizer reward for OPD prompt banks.

## Empirical Highlights
- Beats unoptimized student prompts and KL-filtered real questions; matches or exceeds real-bank OPD in evaluated settings.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27450`
- Code: `https://github.com/GasolSun36/Ask_to_Distill` (`code_status: released`).
