---
id: paper:criticopd
type: paper
title: Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
authors:
- Kaixiang Zhao
- Tianrun Yu
- Shangzhe Li
- Yuxiao Yang
- Amanda Hughes
- Weitong Zhang
- Taylor W. Killian
year: 2026
month: 10
arxiv_id: '2610.20572'
url: https://arxiv.org/abs/2610.20572
methods:
- method:criticopd
cites:
- paper:opd
- paper:cc-opsd
tags:
- distillation
- opd
- critique
---

# CriticOPD

## Abstract Summary
Teacher recoverability fails on incorrect student prefixes. CriticOPD uses error recognition: critique, rewrite, then score the revision with the critique as privileged information while the student trains without it.

## Key Contributions
1. Recoverability failure of teacher OPD on incorrect rollouts.
2. Critique-guided rewrite plus privileged scoring.
3. Qwen3-0.6B/1.7B six-bench math; released trainer.

## Empirical Highlights
- Qwen3-1.7B 50.08→54.65; 0.6B 34.80→38.86 vs OPD.
- AIME24/25/AMC +6.01/+7.36/+6.94 on 1.7B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.20572`
- Code: `https://github.com/kzhao5/CriticOPD` (`code_status: released`).
