---
id: paper:duoopd
type: paper
title: "DuoOPD: Learning from Joint Teacher–Student Outcomes for Multi-Task On-Policy Distillation"
authors:
  - "Ao Yu"
  - "Weibo Gao"
  - "Heng Zhou"
  - "Linan Yue"
  - "Rui Li"
  - "Suyi Liu"
  - "Yu Yan"
  - "Yizhong Zhang"
  - "Qi Liu"
year: 2026
month: 9
arxiv_id: "2609.33711"
url: "https://arxiv.org/abs/2609.33711"
methods:
  - method:duoopd
cites:
  - paper:opd
  - paper:opdvr
  - paper:open-mopd
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - duoopd
---

# DuoOPD: Learning from Joint Teacher–Student Outcomes for Multi-Task On-Policy Distillation

## Abstract Summary
Single-teacher multi-task OPD ignores who was correct. On average it pushes down even the student's correct answers when the teacher fails; gating by student correctness (OPDVR) fixes the direction but still uses a failing teacher the same way as a succeeding one. DuoOPD lets the student outcome set the sign and the joint teacher–student outcome set the support: teacher-only success uses the teacher's verified answer as scoring context; student-only success uses a within-task shared weight; agreement uses teacher preferences. One four-outcome rule, no task-specific knobs. Mean macro accuracy +2.58 (Qwen3) and +5.98 (Llama) over OPD; also leads on scientific-calculation / IF / code mixtures. Code: `https://github.com/YongYuanDeAo/DuoOPD`.

## Key Contributions
1. **Direction vs support**: student verification sets \(\sigma=2r_S-1\); joint outcome selects teacher context or shared magnitude.
2. **Four-outcome rule** covering \(r_T,r_S\in\{0,1\}^2\) without per-task settings.
3. **Ablation**: outcome-based direction alone stays near OPDVR; teacher references and within-task weight sharing supply most of the gain.

## Empirical Highlights
- Qwen3 / Llama mean macro accuracy +2.58 / +5.98 vs OPD; beats five baselines including gated OPD.
- Positive on both teacher-solved and teacher-failed questions in every domain of the main mixture.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.33711`
- Code: `https://github.com/YongYuanDeAo/DuoOPD` (`code_status: released`).
