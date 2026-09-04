---
id: paper:ida-opd
type: paper
title: "Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation"
authors:
  - "Run Yang"
  - "Runpeng Dai"
  - "Jie Sun"
  - "Jielei Zhang"
  - "Fan Zhou"
  - "Hongtu Zhu"
  - "Peiyi Li"
  - "Longwen Gao"
year: 2026
month: 8
arxiv_id: "2608.29846"
url: "https://arxiv.org/abs/2608.29846"
methods:
  - method:ida-opd
cites:
  - paper:opd
  - paper:ra-opd
  - paper:opsa
tags:
  - post-training
  - distillation
  - on-policy
  - entropy
  - ida-opd
---

# Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation

## Abstract Summary
Sampled-token OPD is cheap (teacher log-prob only on the emitted token) but often has diversity distillation failure: pass@1 rises while pass@k plateaus. First-Order Local Entropy Influence $\mathcal{I}_H(y)=A_y D_y$ predicts the sign of the local entropy change. IDA-OPD keeps entropy-expanding updates and shrinks entropy-contracting advantages by $w_y=|q-p|/(q+p)$, which is small exactly where teacher and student already agree (the region that dominates cumulative entropy drain). No full-vocabulary teacher logits. No public code found as of 2026-09-04.

## Key Contributions
1. **Diversity distillation failure**: sampled-token OPD improves pass@1 while pass@k stalls vs the teacher.
2. **$\mathcal{I}_H(y)=A_y D_y$**: $A_y$ alone does not determine entropy; the student's local probability structure $D_y$ does.
3. **Divergence-adaptive shrinkage**: $\widetilde{A}_y=A_y$ if $\mathcal{I}_H\geq 0$, else $w_y A_y$ with $w_y=|q_y-p_y|/(q_y+p_y)$. Sign-preserving; quadratic attenuation near agreement.

## Empirical Highlights
- Qwen3-8B-Non-Thinking math, pass@16 vs OPD: AIME24 83.3 vs 79.1 (+4.2); AIME25 76.7 vs 70.7 (+6.0); HMMT Feb 56.7 vs 49.5 (+7.2); HMMT Nov 63.3 vs 60.8 (+2.5). Pass@1 broadly maintained or slightly up.
- Qwen3-4B-Non-Thinking math, pass@16 vs OPD: AIME24 83.3 vs 78.7 (+4.6); AIME25 70.0 vs 65.7 (+4.3); HMMT Feb 60.0 vs 51.7 (+8.3).
- Code, Qwen3-4B: MBPP+ pass@1/16 71.6/73.8 vs OPD 69.5/72.9; LiveCodeBench 28.1/55.2 vs 26.8/54.2.
- Matches or exceeds teacher-informed AOPD/EOPD pass@16 without top-K teacher distributions.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-04. Filter is Eqs. 1–4 in the paper (`recipe:ida-opd`).
