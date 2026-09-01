---
id: paper:opsa
type: paper
title: "Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement"
authors:
  - "Yi Ding"
  - "Ruqi Zhang"
year: 2026
month: 8
arxiv_id: "2608.31046"
url: "https://arxiv.org/abs/2608.31046"
methods:
  - method:opsa
cites:
  - paper:opd
  - paper:grpo
  - paper:gkd
tags:
  - post-training
  - on-policy
  - distillation
  - teacher-free
  - opsa
---

# Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement

## Abstract Summary
On-policy distillation asks a teacher to score student-generated prefixes that are off-policy for the teacher. Teacher advantages are often noisy (negative on correct answers, positive on incorrect ones), and the noise rate grows with teacher scale (30.6% at 4B, 50.6% at 235B-A22B). Students improve at a similar rate whether noisy trajectories are kept, dropped, or used alone. Gains concentrate on low-logp student tokens; a fixed negative advantage on those tokens matches teacher-provided advantages. On-Policy Self-Adaptation (OPSA) therefore drops the teacher and assigns entropy-adaptive negative advantages to the lowest-20% logp tokens, suppressing tails and redistributing mass among head tokens.

## Key Contributions
1. **Teacher-noise diagnosis**: Quantifies sign disagreement between OPD advantages and verifiable rewards; noise increases with teacher scale, and the largest teacher is almost uniformly negative.
2. **What OPD actually learns**: Low-logp tokens and negative advantages drive improvement; high-logp tokens and teacher-specific signs do not.
3. **OPSA**: Supervision-free token-level RL with $A_i^{\mathrm{dyn}}=-\frac12-\frac{H_i-H_{\min}}{2(H_{\max}-H_{\min})}$ on the lowest-20% logp tokens. Beats OPD, OPSD, GRPO, and TTRL on math without teacher, reward, or hint.

## Empirical Highlights
- Qwen3-1.7B AIME24 Avg@32: OPSA 48.85 vs base 13.44 (+35.41, 263% relative) vs OPD 32.08 vs GRPO 33.96.
- Qwen3-1.7B three-benchmark average Avg@32 / Pass@32: OPSA 35.83 / 65.56 vs best RL baseline +11.04 / +8.89.
- Qwen3.5-9B AIME24 Avg@32: 76.35 -> 87.81 despite a strong base.
- Trained on DAPO-17k questions only (no labels). Non-thinking unless noted.

## Open Source Repository & Resources
- Code: `https://github.com/DripNowhy/On-Policy-Self-Adaptation` (slime fork)
- Project: `https://dripnowhy.github.io/On-Policy-Self-Adaptation/`
- Checkpoints: Hugging Face collection `Tuwhy/on-policy-self-adaptation`
