---
id: recipe:ffno
type: recipe
title: Factorized Fourier Neural Operator (F-FNO) Recipe
method: method:ffno
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090 or 1x A100
framework: PyTorch 2.5+
repo_url: https://github.com/alasdairtran/fourierflow
pip_dependencies:
- torch>=2.5.0
- numpy>=1.26.0
- hydra-core>=1.3.0
tags:
- scientific-ml
- neural-operator
- spectral
- ffno
---

# Factorized Fourier Neural Operator (F-FNO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/alasdairtran/fourierflow`.
- Data: 2D/3D Navier-Stokes turbulence datasets.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine schedule, weight_decay=1e-4.
