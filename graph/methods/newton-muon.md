---
id: method:newton-muon
type: method
title: "Newton-Muon"
category: "optimizer"
status: active
papers:
  - paper:newton-muon
recipes:
  - recipe:newton-muon
claims:
  - benchmark: "Language Model Optimization"
    metric: "step efficiency"
    value: "Second-order curvature-corrected step efficiency"
    baseline: "Muon"
    date: "2026-08-26"
    verified: true
    notes: "Low-rank Hessian curvature corrections added to Newton-Schulz iterations."
tags:
  - optimizer
  - pretraining
  - newton-muon
---

# Newton-Muon

## Method Overview
Newton-Muon incorporates diagonal Hessian curvature estimates into the matrix orthogonalization step, accelerating optimization on ill-conditioned attention projections.

## When to Use
- Training deep models with high attention conditioning ratios.
