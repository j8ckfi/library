---
id: method:dpot
type: method
title: DPOT (Denoising Pre-trained Operator Transformer)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:dpot
recipes:
- recipe:dpot
claims:
- benchmark: PDEBench 1D/2D / Diverse PDE Pre-Training
  metric: relative L2 error in downstream transfer
  value: Auto-regressive denoising pre-training baseline
  baseline: From-scratch FNO / U-Net
  date: '2026-08-28'
  verified: true
  notes: Auto-regressive denoising pre-training objective on large-scale synthetic
    PDE trajectories (ICML 2024).
tags:
- scientific-ml
- neural-operator
- foundation-model
- dpot
---

# DPOT (Denoising Pre-trained Operator Transformer)

## Method Overview
DPOT applies masked denoising pre-training to operator learning:
1. **Denoising Objective**: Adds synthetic noise and masking perturbations to PDE trajectory snapshots during pre-training.
2. **Autoregressive Transformer**: Models cross-timestep physical rollouts via causal operator attention blocks.

## When to Use
- Active foundation ancestor for zero-shot and few-shot PDE transfer.
