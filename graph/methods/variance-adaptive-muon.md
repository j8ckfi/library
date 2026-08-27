---
id: method:variance-adaptive-muon
type: method
title: "Variance-Adaptive Muon"
category: "optimizer"
status: active
papers:
  - paper:variance-adaptive-muon
recipes:
  - recipe:variance-adaptive-muon
claims:
  - benchmark: "Multimodal & Non-Stationary Pretraining"
    metric: "loss stability"
    value: "Prevents loss spikes across data phase transitions"
    baseline: "Muon"
    date: "2026-08-26"
    verified: true
    notes: "Adaptive variance tracking integrated into orthogonal momentum steps."
tags:
  - optimizer
  - pretraining
  - variance-adaptive-muon
---

# Variance-Adaptive Muon

## Method Overview
Variance-Adaptive Muon tracks running second-moment gradient variances across weight matrices to dynamically adjust orthogonalization update steps during curriculum transitions.

## When to Use
- Pretraining runs with scheduled curriculum phase shifts or multimodal token mixing.
