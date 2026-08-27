---
id: method:sspo
type: method
title: "SSPO (Stabilized Sequence Policy Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:sspo
recipes:
  - recipe:sspo
claims:
  - benchmark: "Long-Horizon Reasoning"
    metric: "gradient stability"
    value: "Variance-reduced sequence importance weighting"
    baseline: "GRPO"
    date: "2026-08-26"
    verified: true
    notes: "Sequence-level clipping on extended rollouts."
tags:
  - post-training
  - rl-alignment
  - sspo
---

# SSPO (Stabilized Sequence Policy Optimization)

## Method Overview
SSPO applies sequence-level clipping and variance-reduced advantage estimates to prevent gradient spikes on reasoning rollouts exceeding 16k tokens.

## When to Use
- Extremely long-trace reasoning optimization where token-level importance ratios diverge.
