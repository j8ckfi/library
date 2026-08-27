---
id: method:a2sg
type: method
title: "A2SG (Adaptive Surrogate Gradient)"
category: "snn"
status: sota
sota_for:
  - task:spiking-neural-networks-training
supersedes:
  - method:surrogate-gradient-snn
papers:
  - paper:a2sg
recipes:
  - recipe:a2sg
claims:
  - benchmark: "Direct SNN Backpropagation Suite"
    metric: "gradient stability & dead-neuron avoidance"
    value: "Recommended SNN training surrogate gradient backprop"
    baseline: "Static Surrogate Gradients (FastSigmoid / Arctan)"
    date: "2026-08-26"
    verified: true
    notes: "Adaptive surrogate gradient smoothing for direct backpropagation through time."
tags:
  - snn
  - surrogate-gradients
  - a2sg
  - sota
---

# A2SG (Adaptive Surrogate Gradient)

## Method Overview
A2SG provides an adaptive surrogate gradient formulation that dynamically adjusts smoothing width and steepness throughout training epochs, preventing gradient death in deep spiking layers.

## When to Use
- Recommended gradient backpropagation method for training deep SNNs end-to-end (training method, not neuron architecture default).

## Supersession
- Supersedes static `method:surrogate-gradient-snn` formulations.
