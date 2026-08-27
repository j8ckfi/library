---
id: method:bpco
type: method
title: "BPCO (Best Practice Critic Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:token-level-critic-rl
supersedes: []
papers:
  - paper:bpco
recipes:
  - recipe:bpco
claims:
  - benchmark: "Mathematical Reasoning (40.3K dataset, 1.5B to 30B-A3B MoE) & Rubric Tasks"
    metric: "accuracy & sample efficiency (1 response/prompt)"
    value: "Matches or exceeds multi-sample GRPO baselines while sampling 1 response per prompt"
    baseline: "Standard PPO Critic / Group-Relative GRPO (G=8)"
    date: "2026-08-27"
    verified: true
    notes: "DPPO probability clipping + reward-bounded value predictions + Monte Carlo targets + unnormalized advantages + length-adaptive GAE + privileged critic inputs."
tags:
  - rl-alignment
  - actor-critic
  - token-level-advantage
  - bpco
  - sota
---

# BPCO (Best Practice Critic Optimization)

## Method Overview
BPCO stabilizes single-rollout actor-critic reinforcement learning for language models through five synergistic design principles:
1. **Divergence PPO (DPPO)**: Bounds token policy probability shift $|\pi_\theta(y_t \mid s_t) - \mu(y_t \mid s_t)| \le \epsilon$ instead of standard ratio-based clipping.
2. **Reward-Bounded Value Head**: Restricts critic predictions to the valid domain of the reward function (e.g. $[R_{\min}, R_{\max}]$ via sigmoid or clamping).
3. **Monte Carlo Value Targets**: Updates the critic directly on observed terminal returns rather than noisy bootstrapped TD targets.
4. **Unnormalized Policy Advantages**: Preserves raw advantage magnitudes instead of forcing batch-wise unit-variance normalization.
5. **Length-Adaptive GAE**: Scales the GAE discount parameter according to generated sequence length.
6. **Privileged Critic Inputs**: Conditions the training-only value model on prompt rubrics and reference solutions that are withheld from the policy.

## When to Use
- When training budgets or memory constraints prevent sampling large groups of rollouts per prompt (e.g., $G \ge 8$).
- When fine-grained token-level credit assignment is needed rather than uniform sequence-level advantages.

## Relation to Existing SOTA
- Does not replace `method:cispo` or `method:sapo` as the multi-sample group RL defaults, but provides the primary single-sample token-level critic baseline.
