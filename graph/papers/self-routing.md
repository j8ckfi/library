---
id: paper:self-routing
type: paper
title: "From Rollouts to Recipes: Self-Contained Post-Training for LLMs"
authors:
  - "Yifei Li"
  - "Lingling Zhang"
  - "Muye Huang"
  - "Zihan Ma"
  - "Jiashuai Liu"
  - "Jun Liu"
year: 2026
month: 9
arxiv_id: "2609.01422"
url: "https://arxiv.org/abs/2609.01422"
methods:
  - method:self-routing
cites:
  - paper:grpo
  - paper:dapo
  - paper:opsa
tags:
  - post-training
  - rlvr
  - routing
  - self-routing
---

# From Rollouts to Recipes: Self-Contained Post-Training for LLMs

## Abstract Summary
Uniform GRPO or uniform on-policy self-distillation wastes updates: mixed-correctness samples want GRPO, low-accuracy low-confidence samples want dense OPSD, already-solved high-confidence samples want KL regularization, and confident failures want a skip. Self-Routing turns rollout correctness and confidence into a sample-level recipe with no external teacher and no extra sampling. Gains over uniform GRPO / OPSD / fixed mixtures on Qwen3 and Qwen3.5 math. Code planned on ms-swift; not released as of 2026-09-04.

## Key Contributions
1. **Behavior state** from group accuracy $a_x$ (smooth low/mid/high membership) and batch-calibrated token-entropy confidence.
2. **Four recipes**: GRPO, OPSD (same-model answer-conditioned teacher, precomputed), REG (KL to reference), SKIP.
3. **Soft router** from hand-specified scores, then one categorical draw so each sample hits one objective per step.

## Empirical Highlights
- Qwen3-4B six-bench avg: Self-Routing 73.7 vs Naive-GRPO 66.8 vs Naive-OPSD 70.4 vs base 61.0. AIME24 83.6 vs GRPO 74.3 vs OPSD 79.4.
- Qwen3.5-4B avg: 86.6 vs GRPO 79.8 vs OPSD 83.0 vs base 76.8.
- Qwen3-1.7B avg: 53.1 vs GRPO 47.9 vs OPSD 49.8.
- Normalized FLOPs at G=8: Naive-GRPO 64.0, Naive-OPSD 24.0, Self-Routing 34.7. Not a wall-clock win vs OPSD; a selective-allocation win vs all-GRPO.

## Open Source Repository & Resources
- Code planned on ms-swift. Not released as of 2026-09-04. Router scores are §3.4 of the paper (`recipe:self-routing`).
