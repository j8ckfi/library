---
id: method:minpro
type: method
title: "MinPRO (Minimal Policy Relative Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:minpro
recipes:
  - recipe:minpro
claims:
  - benchmark: "Math & Code Reasoning"
    metric: "sample efficiency & memory"
    value: "Eliminates critic network overhead"
    baseline: "PPO"
    date: "2026-08-26"
    verified: true
    notes: "Minimalist relative policy formulation."
tags:
  - post-training
  - rl-alignment
  - minpro
---

# MinPRO (Minimal Policy Relative Optimization)

## Method Overview
MinPRO simplifies relative policy optimization by computing direct relative advantages without auxiliary critic networks or learned reward baselines.

## When to Use
- Memory-constrained reasoning RL where allocating VRAM for a critic model is prohibitive.
