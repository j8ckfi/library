---
id: method:attnres
type: method
title: "AttnRes (Attentive Residual Connections)"
category: "architecture"
status: active
do_not_use_for:
  - when: "multi-stream attention residuals vs vanilla / mHC / AttnRes (MSAR)"
    reason: "AttnRes remains the attentive-skip citation; MSAR is a later single-paper residual bake-off, not a supersession"
    use_instead: "method:msar"
papers:
  - paper:attnres
recipes:
  - recipe:attnres
claims:
  - benchmark: "Deep Transformer Pretraining"
    metric: "gradient propagation & loss convergence"
    value: "Stabilizes 100+ layer deep transformer scaling"
    baseline: "Standard Pre-LN ResNet"
    date: "2026-08-26"
    verified: true
    notes: "Attentive skip connections dynamically weighting prior layer representations."
tags:
  - architecture
  - pretraining
  - attnres
---

# AttnRes (Attentive Residual Connections)

## Method Overview
AttnRes replaces static residual addition with learned attentive skip routing across prior layer activations, preventing representation collapse in ultra-deep networks.

## When to Use
- Scaling transformer architectures beyond 100 layers in depth.

## Gotchas & Failure Modes
- A later residual bake-off, `method:msar` (`arXiv:2610.13630`), reports beating AttnRes / mHC / vanilla on 12 benches at 18B and 28B MoE (iso-loss 1.58× vs 1.35× AttnRes). Single-paper baselines; this node is not superseded.
