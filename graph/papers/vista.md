---
id: paper:vista
type: paper
title: "VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation"
authors:
  - "Zewen Ding"
  - "Zezhong Wu"
  - "Zhou Tao"
  - "Shida Wang"
  - "Shizhuo Hou"
  - "YongXiang Hua"
  - "Haoyu Cao"
  - "Linli Xu"
year: 2026
month: 8
arxiv_id: "2608.28306"
url: "https://arxiv.org/abs/2608.28306"
methods:
  - method:vista
cites:
  - paper:gkd
  - paper:grpo
  - paper:tulu3-rlvr
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - vista
---

# VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation

## Abstract Summary
On-policy self-distillation (OPSD) trains a problem-only student on its own rollouts using dense token-level supervision from a privileged teacher that also sees a gold reference solution. Standard OPSD treats that teacher as a fixed target along the student prefixes. VISTA keeps the OPSD student update and additionally adapts the teacher toward the student, but only on outcome-verified rollouts and only at the top-$k$ token positions with largest teacher-first KL$(P^T \| P^S)$. Student loss is forward KL with stop-grad on the teacher; teacher loss is reverse KL with stop-grad on the student. No extra sampling or separate reward objective is introduced. Inference keeps only the problem-only student.

## Key Contributions
1. **Teacher-superiority diagnosis**: Formalizes that reference conditioning does not guarantee the privileged distribution is a better problem-only target at every prefix, producing reference-specific tokens or suppressed valid student continuations.
2. **Verifier-gated, top-$k$ student-to-teacher adaptation**: Outcome verification selects which rollouts may update the teacher; teacher-first KL selects which positions. Reverse-KL teacher loss is mode-seeking; student OPSD loss is unchanged.
3. **Matched-protocol gains over OPSD and GRPO**: On Qwen3-1.7B/4B/8B instruct, Avg@12 over AIME24/AIME25/HMMT25 is 44.0 / 64.3 / 66.9 versus OPSD 43.4 / 63.6 / 64.8 and GRPO 37.7 / 62.7 / 64.0. Largest gain is +2.1 at 8B. Reverse (fail-only) teacher gate scores 64.5, below OPSD; verified-only scores 66.9. Best $k$ in $\{16, 32\}$.

## Empirical Highlights
- Training: OpenThoughts math, 100 updates, global batch 32, independent LoRA $r=64$ $\alpha=128$, $\eta_S=4\times 10^{-6}$, $\eta_T=3\times 10^{-6}$ ($\lambda=0.75$), clip $\tau=0.05$, 8x H800, verl 0.6.1 / PyTorch 2.8 / vLLM 0.11.0.
- Parent method is vanilla OPSD (Zhao et al., arXiv:2601.18734, Self-distilled reasoner), which is not a first-hop node in this library.

## Open Source Repository
- No official GitHub found as of 2026-08-31. Reimplement on verl following paper Algorithm 1 (`recipe:vista`).
