---
id: task:operator-fourier-adapt
type: task
title: Parameter-Efficient Fine-Tuning for Fourier Operators
domain: scientific-ml
summary: Adapting pre-trained Fourier and spectral latent neural operators to new
  PDE domains and Reynolds numbers with minimal parameter updates.
current_sota:
- method: method:f-adapter
  as_of: '2026-08-28'
  benchmark: Navier-Stokes Re Transfer / 2D Darcy Transfer
  metric: relative L2 error @ ~2% trainable parameters
  value: Default SOTA Spectral PEFT
  notes: F-Adapter (2509.23173); frequency-adaptive adapter overcoming LoRA depth-amplified
    spectral error floor.
methods:
- method:f-adapter
tags:
- scientific-ml
- neural-operator
- peft
- fourier-adapter
- f-adapter
---

# Parameter-Efficient Fine-Tuning for Fourier Operators

## Problem Definition
Fine-tuning large pre-trained Fourier and spectral neural operators (e.g., FNO, DPOT) on downstream tasks (such as shifted Reynolds numbers, altered boundary conditions, or varied geometries) while updating only a small fraction of parameters without degrading high-frequency spectral accuracy.

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **F-Adapter** (`method:f-adapter`, 2509.23173, NeurIPS 2025).
- **Critical Caution**: Do NOT apply vanilla LoRA to Fourier latent operators; vanilla LoRA causes depth-amplified spectral error floors.
