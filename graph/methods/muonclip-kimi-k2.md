---
id: method:muonclip-kimi-k2
type: method
title: "MuonClip (Kimi-K2 Optimizer Recipe)"
category: "optimizer"
status: sota
sota_for:
  - task:pretrain-moe-frontier
supersedes:
  - method:muon-scalable
papers:
  - paper:muonclip-kimi-k2
recipes:
  - recipe:muon-pretraining
claims:
  - benchmark: "Trillion-Token MoE Pretraining"
    metric: "gradient stability & throughput"
    value: "Zero loss spikes across trillion-scale runs"
    baseline: "Scalable Muon"
    date: "2025-07"
    verified: true
    notes: "Introduces MuonClip gradient clipping and numerical stabilization for trillion-scale MoE training."
tags:
  - optimizer
  - moe
  - scale-up
---

# MuonClip (Kimi-K2 Optimizer Recipe)

## Method Overview
MuonClip adapts matrix-orthogonalized optimization for trillion-token sparse Mixture-of-Experts (MoE) pretraining, adding adaptive matrix clipping to suppress catastrophic gradient surges in dynamically routed expert projections.

## When to Use
- Pretraining trillion-token MoE models.

## Supersession
- Supersedes `method:muon-scalable` at trillion scale.
