---
id: paper:spod
type: paper
title: 'Beyond the Teacher: Understanding and Preserving Distillation Overshoot in Agentic On-Policy Distillation'
authors:
- 'Jike Zhong'
- 'Ming Li'
- 'Yuxiang Lai'
- 'Xi Xiao'
- 'Sheng Zhang'
- 'Ritwick Chaudhry'
- 'Tianle Chen'
- 'Jingyu Xie'
- 'Zheda Mai'
- 'Shao-Yuan Lo'
- 'Konstantinos Psounis'
- 'Yuanyuan Lei'
year: 2026
month: 10
arxiv_id: '2610.25034'
url: https://arxiv.org/abs/2610.25034
methods:
- method:spod
cites:
- paper:opd
tags:
- distillation
- opd
- active
---

# SPOD

## Abstract Summary
In multi-turn agentic OPD a weaker student can beat its teacher mid-training then regress as teacher-disfavored successful choices erode. SPOD masks conflicting teacher supervision on protected successful choices. Up to +15.2 pp vs ordinary OPD and +20.0 vs the teacher.

## Key Contributions
1. Repair-vs-erosion analysis plus success-preserving OPD.

## Empirical Highlights
- ALFWorld Gemma E4B 16.5% → 82.8% peak vs 31B teacher 68.9%, then 73.7% without SPOD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25034`
- Code: `https://github.com/Jike338/SPOD` (`code_status: released`).
