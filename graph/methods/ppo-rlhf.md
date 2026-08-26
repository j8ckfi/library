---
id: method:ppo-rlhf
type: method
title: "PPO (Proximal Policy Optimization for RLHF)"
category: "rl-alignment"
status: active
superseded_by: method:grpo
sota_for: []
supersedes: []
papers:
  - paper:ppo-paper
recipes: []
claims:
  - benchmark: "InstructGPT / Anthropic HH-RLHF"
    metric: "human preference win rate"
    value: "Baseline reference"
    baseline: "Supervised Fine-Tuning"
    date: "2022-03"
    verified: true
    notes: "Requires maintaining 4 model copies in memory: Actor, Critic, Reference, Reward."
tags:
  - rl-alignment
  - baseline
---

# PPO (Proximal Policy Optimization for RLHF)

## Method Overview
PPO for RLHF adapts continuous actor-critic policy optimization to autoregressive token generation. A learned reward model provides scalar scores, while a dedicated value/critic network estimates Generalized Advantage Estimation (GAE) at each token step. Surrogate policy loss is clipped within a \([1-\epsilon, 1+\epsilon]\) trust region.

## When to Use
- When training with dense, non-verifiable human preferences where fine-grained token-level value estimation is strictly necessary.

## Gotchas & Failure Modes
- Enormous GPU memory footprint (requires concurrent hosting of Actor, Critic, Reference Model, and Reward Model).
- Highly unstable critic training dynamics and hyperparameter sensitivity (GAE \(\lambda\), value loss coefficient).
