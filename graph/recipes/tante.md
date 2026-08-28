---
id: recipe:tante
type: recipe
title: TANTE (Time-Adaptive Neural Taylor Expansion) Recipe
method: method:tante
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090
framework: PyTorch 2.5+
repo_url: https://github.com/zwu88/TANTE
pip_dependencies:
- torch>=2.5.0
- scipy>=1.13.0
- numpy>=1.26.0
tags:
- scientific-ml
- neural-operator
- tante
- time-adaptive
---

# TANTE Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090.
- Repository: `https://github.com/zwu88/TANTE`.
- Data: Stiff time-dependent PDE trajectories.

## Hyperparameters & Optimization
- Loss: Multi-order Taylor consistency loss + relative L2.
- Optimizer: AdamW, lr=1e-3, cosine decay.
