---
id: method:htmuon
type: method
title: "HTmuon (Heavy-Tailed Muon)"
category: "optimizer"
status: active
papers:
  - paper:htmuon
recipes:
  - recipe:htmuon
claims:
  - benchmark: "LLM Pretraining"
    metric: "gradient noise robustness"
    value: "Stable loss convergence under heavy-tailed noise"
    baseline: "Muon"
    date: "2026-08-26"
    verified: true
    notes: "Heavy-tailed noise filtering integrated into matrix orthogonalization."
tags:
  - optimizer
  - pretraining
  - htmuon
---

# HTmuon (Heavy-Tailed Muon)

## Method Overview
HTmuon applies heavy-tailed gradient noise filtering to matrix orthogonalization updates, preventing spectral norm distortion during large-batch gradient spikes.

## When to Use
- Large-scale pretraining across noisy or heterogeneous dataset streams.
