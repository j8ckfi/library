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
do_not_use_for:
  - when: "per-expert Muon step-size multipliers from update–gradient alignment"
    reason: "MuonClip is the Kimi-K2 trillion-scale recipe; ExpertMuon-Compass is a per-expert step multiplier on FineWeb-Edu"
    use_instead: "method:expertmuon-compass"
papers:
  - paper:expertmuon-compass
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
last_reviewed: "2026-10-06"
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
- `method:musec` is an optimizer-level momentum spectral clip (different mechanism). It does not replace MuonClip at trillion MoE scale.
