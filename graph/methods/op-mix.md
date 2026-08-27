---
id: method:op-mix
type: method
title: "OP-Mix (Optimal Transport Data Mixing)"
category: "data-curriculum"
status: active
papers:
  - paper:op-mix
recipes:
  - recipe:op-mix
claims:
  - benchmark: "Data Mixing Benchmark"
    metric: "representation coverage"
    value: "Wasserstein-optimal distribution coverage"
    baseline: "Heuristic Proportions"
    date: "2026-08-26"
    verified: true
    notes: "Wasserstein distance minimization between pretraining corpus and target evaluation distributions."
tags:
  - pretraining
  - data-curriculum
  - op-mix
---

# OP-Mix (Optimal Transport Data Mixing)

## Method Overview
OP-Mix uses optimal transport (Wasserstein distance) to compute token mixture weights that minimize representation divergence from target evaluation distributions.

## When to Use
- Calibrating pretraining data proportions against target downstream domain benchmarks.
