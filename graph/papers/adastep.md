---
id: paper:adastep
type: paper
title: "AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning"
authors:
  - "Xin Wang"
  - "Wenhao Wu"
  - "Menghao Zhang"
  - "Zhi Wang"
  - "Kun Shao"
  - "Jian Luan"
year: 2026
month: 10
arxiv_id: "2610.03223"
url: "https://arxiv.org/abs/2610.03223"
methods:
  - method:adastep
cites:
  - paper:slca-grpo
tags:
  - post-training
  - rl-alignment
  - agentic
  - credit-assignment
  - adastep
---

# AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning

## Abstract Summary
GiGPO adds a fixed-weight step-level correction to a trajectory-level group advantage. Those local advantages are noisy: later actions, environment stochasticity, and length can dominate the return. AdaStep treats local weighting as MSE estimation of a latent step advantage and, under a stated sampling assumption, derives a per-state shrinkage coefficient (signal-to-total-variance). No critic, extra rollouts, or extra model inference. Active plug-in beside SLCA-GRPO. No public code as of 2026-10-05.

## Key Contributions
1. **Per-state shrinkage** of the step-level correction onto the trajectory-level advantage.
2. **Critic-free, ~1% extra credit-computation time** on the existing GiGPO grouping.
3. **Δ vs GiGPO, Qwen3-1.7B**: ALFWorld In +2.60, ScienceWorld +9.36. Qwen3-4B ALFWorld In +4.99.

## Empirical Highlights
- Qwen3-4B AdaStep 93.01 / 86.58 / 88.76 / 80.27 / 48.70 vs GiGPO 88.02 / 83.07 / 87.34 / 78.28 / 46.67 (ALFWorld In/Out, WebShop Seen/Unseen, ScienceWorld).
- HGPO is a paper baseline, not a library method.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03223`
- Code: none found as of 2026-10-05 (`code_status: none`).
