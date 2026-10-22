---
id: paper:teachback
type: paper
title: 'TeachBack: Learning to Teach via Bidirectional Preference Optimization for On-Policy Self-Distillation'
authors:
- 'Linfei Ji'
- 'Jiayun Li'
- 'Haozhao Wang'
- 'Siyu Jiang'
- 'Zehao Wang'
- 'Longtao Xiao'
- 'Yu-Jie Yuan'
- 'Ruixuan Li'
year: 2026
month: 10
arxiv_id: '2610.29167'
url: https://arxiv.org/abs/2610.29167
methods:
- method:teachback
cites:
- paper:vista
- paper:opd
tags:
- opsd
- privileged-teacher
- active
---

# TeachBack

## Abstract Summary
TeachBack trains a shared policy as both privileged Teacher and problem-only Student. Forward preference uses teacher traces for the student; reversed preference uses student behavior to stop the teacher from collapsing into reference-conditioned shortcuts.

## Key Contributions
1. TeachBack as an active plug-in on `task:privileged-teacher-opsd`.

## Empirical Highlights
- consistently improves student performance over existing OPSD methods while keeping teacher accuracy comparable. Does not retarget `method:vista`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29167`
- Code: `none found` (`code_status: none`).
