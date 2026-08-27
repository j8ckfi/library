---
id: method:ngn
type: method
title: "NGN (Neuromorphic Gated Networks)"
category: "snn"
status: active
papers:
  - paper:ngn
recipes:
  - recipe:ngn
claims:
  - benchmark: "Event Stream Processing"
    metric: "temporal fidelity & synaptic sparsity"
    value: "Cuts simulated synaptic operations by >50%"
    baseline: "Standard LIF"
    date: "2026-08-26"
    verified: true
    notes: "Event-density neuromorphic gating."
tags:
  - snn
  - neuromorphic
  - ngn
---

# NGN (Neuromorphic Gated Networks)

## Method Overview
NGN dynamically routes continuous temporal streams through sparse spiking sub-networks based on incoming event burstiness.

## When to Use
- Processing high-frequency asynchronous event camera and neuromorphic sensor streams.
