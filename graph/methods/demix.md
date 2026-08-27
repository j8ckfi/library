---
id: method:demix
type: method
title: "DeMix (Dynamic Data Mixture Optimization)"
category: "data-curriculum"
status: active
papers:
  - paper:demix
recipes:
  - recipe:demix
claims:
  - benchmark: "Pretraining Data Mixtures"
    metric: "sample efficiency"
    value: "Dynamic domain re-weighting improves loss convergence"
    baseline: "Static Mixture"
    date: "2026-08-26"
    verified: true
    notes: "Monitors validation gradient alignment across domains for online mixture adjustment."
tags:
  - pretraining
  - data-curriculum
  - demix
---

# DeMix (Dynamic Data Mixture Optimization)

## Method Overview
DeMix continuously rebalances domain proportions during pretraining by measuring gradient alignment between running training batches and held-out validation slices of key capability domains.

## When to Use
- Optimizing data mixture ratios during long pretraining runs without manual grid searching.
