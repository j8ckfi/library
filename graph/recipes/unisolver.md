---
id: recipe:unisolver
type: recipe
title: Unisolver (PDE-Conditional Universal Transformer) Recipe
method: method:unisolver
task: task:operator-foundation
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+
repo_url: https://github.com/thuml/Unisolver
pip_dependencies:
- torch>=2.5.0
- transformers>=4.48.0
- einops>=0.8.0
tags:
- scientific-ml
- neural-operator
- foundation-model
- unisolver
- sota
---

# Unisolver Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Repository: `https://github.com/thuml/Unisolver`.
- Data: Multi-PDE corpus across diffusion, wave, advection, and Navier-Stokes equations.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine decay, weight_decay=1e-4.
