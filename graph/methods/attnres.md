---
id: method:attnres
type: method
title: "AttnRes (Attentive Residual Connections)"
category: "architecture"
status: active
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
