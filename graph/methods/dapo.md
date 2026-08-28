---
id: method:dapo
type: method
title: "DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)"
category: "rl-alignment"
status: active
superseded_by: method:cispo
sota_for: []
supersedes:
  - method:grpo
papers:
  - paper:dapo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "Long-CoT Mathematical & Code Reasoning"
    metric: "pass@1 accuracy & stability"
    value: "Strictly outperforms vanilla GRPO on dense models"
    baseline: "Vanilla GRPO"
    date: "2025-03"
    verified: true
    notes: "Clip-higher, dynamic sampling, token-level loss, and overlong trace shaping for dense policies."
tags:
  - rl-alignment
  - reasoning
  - dapo
  - long-cot
---

# DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)

## Method Overview
DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization) optimizes long-CoT reasoning rollouts in dense models via Clip-Higher (asymmetric clipping parameter \(\epsilon\)), dynamic sampling of mixed-reward groups, token-level advantage loss, and overlong trace shaping. Remains in the graph as a key systems reference.

## Supersession
- Superseded by `method:cispo` as the dense RL default.
