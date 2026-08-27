---
id: method:mona
type: method
title: "MONA (Momentum Orthogonalization with Nesterov Acceleration)"
category: "optimizer"
status: active
papers:
  - paper:mona
recipes:
  - recipe:mona
claims:
  - benchmark: "Language Model Pretraining"
    metric: "loss convergence"
    value: "Accelerated early convergence"
    baseline: "Standard Muon"
    date: "2026-08-26"
    verified: true
    notes: "Applies Nesterov lookahead acceleration to orthogonalized momentum buffers."
tags:
  - optimizer
  - pretraining
  - mona
---

# MONA (Momentum Orthogonalization with Nesterov Acceleration)

## Method Overview
MONA combines Nesterov accelerated gradient momentum with matrix orthogonalization, projecting lookahead momentum states through Newton-Schulz iterations.

## When to Use
- Fast-decay pretraining phases where early loss convergence is prioritized.
