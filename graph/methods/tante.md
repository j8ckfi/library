---
id: method:tante
type: method
title: TANTE (Time-Adaptive Neural Taylor Expansion)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:tante
recipes:
- recipe:tante
claims:
- benchmark: Stiff Time-Dependent PDEs / Long-Horizon Rollouts
  metric: relative L2 error & rollout stability
  value: Time-adaptive operator learning via neural Taylor expansion
  baseline: Fixed-step FNO / DeepONet
  date: '2026-08-28'
  verified: true
  notes: Neural Taylor expansion for continuous, adaptive time-stepping during long
    rollout simulation.
tags:
- scientific-ml
- neural-operator
- tante
- time-adaptive
---

# TANTE (Time-Adaptive Neural Taylor Expansion)

## Method Overview
TANTE models time-dependent PDEs with adaptive time-stepping:
1. **Neural Taylor Series**: Represents continuous temporal derivatives via neural Taylor expansion coefficients.
2. **Adaptive Timestep Rollouts**: Dynamically adjusts step size during inference based on local truncation error estimates.

## When to Use
- Active method for stiff time-dependent PDEs and adaptive rollout simulations.
