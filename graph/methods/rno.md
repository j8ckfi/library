---
id: method:rno
type: method
title: Recurrent Neural Operators (RNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:rno
recipes:
- recipe:rno
claims:
- benchmark: Long-horizon chaotic Navier-Stokes / Kuramoto-Sivashinsky
  metric: long-term rollout stability & error growth
  value: Recurrent neural operator baseline for stable long-term rollouts
  baseline: Autoregressive FNO / ResNet
  date: '2026-08-28'
  verified: true
  notes: Integrates recurrent state transitions within spectral operator layers to
    prevent error accumulation.
tags:
- scientific-ml
- neural-operator
- rno
- recurrent
---

# Recurrent Neural Operators (RNO)

## Method Overview
Recurrent Neural Operators (RNO) stabilize long-term autoregressive PDE predictions:
1. **Recurrent Spectral State**: Integrates hidden recurrent memory cells directly into Fourier/spectral layers.
2. **Error Accumulation Suppression**: Mitigates compounding rollout errors over hundreds of timesteps in chaotic systems.

## When to Use
- Active method for long-horizon temporal rollouts of chaotic fluid dynamics.
