---
id: method:stable-opd
type: method
title: "Stable-OPD"
category: "distillation"
status: active
papers:
  - paper:stable-opd
recipes:
  - recipe:stable-opd
claims:
  - benchmark: "Large-Scale Distillation"
    metric: "gradient variance"
    value: "Variance-controlled gradient updates"
    baseline: "Standard OPD"
    date: "2026-08-26"
    verified: true
    notes: "Control variates for student sampling distributions."
tags:
  - post-training
  - distillation
  - stable-opd
---

# Stable-OPD

## Method Overview
Stable-OPD develops gradient variance reduction techniques for on-policy student trajectory sampling, enabling stable scaling to large distributed batches.

## When to Use
- Large-scale multi-node student distillation runs.
