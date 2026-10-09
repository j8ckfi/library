---
id: paper:klpo
type: paper
title: "On KL-Regularized Policy Optimization"
authors:
  - "Yifan Zhang"
year: 2026
month: 10
arxiv_id: "2610.08963"
url: "https://arxiv.org/abs/2610.08963"
methods:
  - method:klpo
cites:
  - paper:sao
  - paper:bpo
tags:
  - post-training
  - async-rl
  - klpo
---

# On KL-Regularized Policy Optimization

## Abstract Summary
Async RL trains one policy on trajectories from another: stale checkpoints and inference-engine mismatch. Clipping IS ratios biases the update; GRPO-style groups are costly on long episodes. KLPO anchors the KL regularizer at the sampler. The regularized step has a closed-form Gibbs solution; KLPO fits the log-ratio optimality condition by least squares on the sampler's own trajectories, so no importance weights are needed. One rollout per prompt; critic-free. SPPO, GPO, REBEL, and BPO arise as special cases. Code: yifanzhang-pro/KLPO. Beside SAO.

## Key Contributions
1. Sampler-anchored KL regularizer with a closed-form Gibbs improvement step.
2. Least-squares fit on sampler trajectories; no IS weights and no group of responses.
3. Token-level policy mirror descent from terminal returns without a critic, including stochastic tool outputs.

## Empirical Highlights
- Critic-free update that uses one rollout per prompt.
- Independent Monte Carlo KL estimates keep gradients unbiased; top-K / binary KL approximations have an exact gap.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08963`
- Code: `https://github.com/yifanzhang-pro/KLPO` (`code_status: released`).
