---
id: method:sf-normuon
type: method
title: "SF-NorMuon (Scale-Free Normalized Muon)"
category: "optimizer"
status: active
papers:
  - paper:sf-normuon
recipes:
  - recipe:sf-normuon
claims:
  - benchmark: "Transformer Parameter Scaling"
    metric: "learning rate transferability"
    value: "Scale-free learning rate transfer from 1B to 70B"
    baseline: "Muon"
    date: "2026-08-26"
    verified: true
    notes: "Scale-free parameter update formulation for zero-shot hyperparameter transfer."
tags:
  - optimizer
  - pretraining
  - sf-normuon
---

# SF-NorMuon (Scale-Free Normalized Muon)

## Method Overview
SF-NorMuon introduces normalized scale-free matrix updates that maintain constant spectral energy trajectories across varying model depths and widths, allowing direct learning rate transfer.

## When to Use
- Hyperparameter tuning on small proxy models (e.g. 1B) prior to scaling to 70B+ parameters.
