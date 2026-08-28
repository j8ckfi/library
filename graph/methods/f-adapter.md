---
id: method:f-adapter
type: method
title: F-Adapter (Frequency-Adaptive Fourier Operator PEFT)
category: neural-operator
status: sota
sota_for:
- task:operator-fourier-adapt
supersedes: []
papers:
- paper:f-adapter
recipes:
- recipe:f-adapter
claims:
- benchmark: Navier-Stokes Re Transfer / 2D Darcy Cross-Coeff PEFT
  metric: relative L2 error vs trainable parameters
  value: SOTA PEFT for Fourier operators with ~2% trainable parameters (NeurIPS 2025)
  baseline: Vanilla LoRA / Prefix Tuning / BitFit
  date: '2026-08-28'
  verified: true
  notes: Identifies depth-amplified spectral error floor in vanilla LoRA; frequency-adaptive
    filtering dynamically adapts spectral weights.
tags:
- scientific-ml
- neural-operator
- peft
- fourier-adapter
- f-adapter
- sota
---

# F-Adapter (Frequency-Adaptive Fourier Operator PEFT)

## Method Overview
F-Adapter enables parameter-efficient fine-tuning for spectral and Fourier neural operators:
1. **Failure Mode of Vanilla LoRA**: Vanilla low-rank adaptation suffers from a depth-amplified spectral error floor when applied to Fourier layers.
2. **Frequency-Adaptive Modulation**: Dynamically modulates spectral frequency bands with lightweight frequency-aware adapter branches updating ~2% of model parameters.

## When to Use
- Default SOTA method for fine-tuning pre-trained Fourier operators (FNO, DPOT) across Reynolds numbers and PDE coefficients.
- **Hard Rule**: Do NOT apply vanilla LoRA to Fourier latent operators.
