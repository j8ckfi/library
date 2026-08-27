---
id: method:cppo
type: method
title: "CPPO (Constrained Proximal Policy Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:cppo
recipes:
  - recipe:cppo
claims:
  - benchmark: "Safe Reasoning & Factuality"
    metric: "constraint adherence"
    value: "Dual Lagrangian constraint satisfaction"
    baseline: "Standard PPO"
    date: "2026-08-26"
    verified: true
    notes: "Adaptive Lagrangian multipliers for safety and factuality constraints."
tags:
  - post-training
  - rl-alignment
  - safety
  - cppo
---

# CPPO (Constrained Proximal Policy Optimization)

## Method Overview
CPPO optimizes reasoning policies under explicit safety and factual consistency constraints using adaptive Lagrangian multipliers.

## When to Use
- Alignment runs requiring strict bounds on hallucination or safety violation rates.
