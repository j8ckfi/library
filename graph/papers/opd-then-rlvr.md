---
id: paper:opd-then-rlvr
type: paper
title: "Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR"
authors:
  - "Boyan Li"
  - "Bingsen Chen"
  - "Chenghao Yang"
  - "Ping Nie"
  - "Chen Zhao"
  - "Xi Ye"
year: 2026
month: 9
arxiv_id: "2609.04108"
url: "https://arxiv.org/abs/2609.04108"
methods:
  - method:opd-then-rlvr
cites:
  - paper:opd
  - paper:grpo
tags:
  - post-training
  - distillation
  - rlvr
  - scheduling
  - opd
---

# Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR

## Abstract Summary
OPD and RLVR are often fused inside one PPO step, either as a weighted sum of advantages (KDRL, SRPO, HDPO, KDRL-mask) or as a teacher-modulated rescaling of the RL advantage (TRRD, RLSD). This paper shows a two-stage **OPD-then-RL** schedule — reverse-KL OPD for S steps, then pure GRPO — beats pure OPD, pure GRPO, and those joint fusions on logic and math. OPD expands pass@k coverage of teacher-supported solutions; RL sharpens pass@1 inside that support. Joint updates interfere (sign conflict on OPD-critical parameters). Switch when OPD validation saturates; OPD is a better RL cold start than SFT. Student Qwen3-1.7B-Base, teacher Qwen3-8B non-thinking. Code: `https://github.com/StringNLPLAB/opd-rlvr`.

## Key Contributions
1. **Unified token-level view** of joint OPD+RLVR as mixing $A^{\mathrm{GRPO}}=\hat{A}$ and $A^{\mathrm{OPD}}=d_t$ inside one clipped surrogate.
2. **OPD-then-RL**: $A_t=d_t$ for step $\le S$, else $\hat{A}$. Default $S=60$ of 150/120 total steps.
3. **Mechanism**: sequential decoupling vs joint sign conflict (Table 3 SCR).
4. **Switch rule**: OPD validation score at the cut largely sets post-RL accuracy. OPD cold-start beats SFT-then-GRPO on DeepMath (Table 8).

## Empirical Highlights
- Table 2, Qwen3-1.7B-Base ← Qwen3-8B, pass@1 / pass@32 avg@32. Logic avg: OPD-then-RL 80.6 / 98.3 vs GRPO 49.4 / 68.1 vs OPD 53.9 / 94.9 vs best joint KDRL 62.8 / 92.4 vs KDRL-Annealing 68.9 / 95.4. Up to 26.7 pass@1 over joints on logic.
- Math avg: OPD-then-RL 31.8 / 58.5 vs OPD 31.0 / 55.9 vs GRPO 28.4 / 55.7 vs SRPO 31.6 / 56.5. Lead vs six of nine methods on pass@1; tie with the three strongest (bootstrap).
- 0.6B student logic avg pass@1 70.4 vs GRPO 45.0 vs OPD 48.9 (Table 5).
- Table 8 DeepMath cold start: OPD-only 30.3 → OPD-then-GRPO 31.8 / p@32 51.3→58.5; SFT-only 25.4 → SFT-then-GRPO 26.1 / p@32 56.6→54.1.

## Open Source Repository & Resources
- Code: `https://github.com/StringNLPLAB/opd-rlvr` (veRL). Paper RL stage is GRPO; library Pass@1 default remains CISPO when you leave the paper's trainer.
