---
id: method:delta-learning
type: method
title: "Delta Learning Alignment"
category: "rl-alignment"
status: active
papers:
  - paper:delta-learning
recipes:
  - recipe:delta-learning
claims:
  - benchmark: "Instruction Alignment Benchmarks"
    metric: "win rate vs parameter drift"
    value: "Targeted representation shifts without catastrophic forgetting"
    baseline: "Standard SFT"
    date: "2026-08-26"
    verified: true
    notes: "Directional delta updates in activation space."
tags:
  - post-training
  - alignment
  - delta-learning
---

# Delta Learning Alignment

## Method Overview
Delta Learning formulates instruction alignment as targeted directional updates in activation space, enabling precise behavioral modification without broad parameter drift.

## When to Use
- Fine-tuning base models for specific compliance or safety behaviors without degrading base capabilities.
