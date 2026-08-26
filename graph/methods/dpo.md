---
id: method:dpo
type: method
title: "DPO (Direct Preference Optimization)"
category: "rl-alignment"
status: active
superseded_by: method:simpo
sota_for: []
supersedes: []
papers:
  - paper:dpo-paper
recipes: []
claims:
  - benchmark: "Anthropic HH-RLHF & GSM8K"
    metric: "win rate"
    value: "Baseline reference"
    baseline: "PPO RLHF"
    date: "2023-05"
    verified: true
    notes: "Analytically maps Bradley-Terry preference loss to closed-form policy optimization."
tags:
  - rl-alignment
  - baseline
---

# DPO (Direct Preference Optimization)

## Method Overview
DPO reparameterizes the reward model in RLHF to extract the optimal policy in closed form. This allows optimizing paired preference loss directly via binary cross-entropy on policy log-probabilities relative to a frozen reference model \(\pi_{\text{ref}}\), removing the need for online reinforcement learning loops.

## When to Use
- Standard baseline for offline preference alignment where a frozen reference model is available and length bias is mitigated via length-penalized evaluation.

## Gotchas & Failure Modes
- Requires caching or live forward passing of the frozen reference model \(\pi_{\text{ref}}\).
- Vulnerable to length bias, where the optimizer boosts win rates by generating longer outputs.
