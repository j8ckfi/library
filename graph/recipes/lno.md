---
id: recipe:lno
type: recipe
title: Latent Neural Operator (LNO) Recipe
method: method:lno
task: task:operator-industrial-mesh
target_hardware: 1x NVIDIA RTX 4090
framework: PyTorch 2.5+
repo_url: https://github.com/L-I-M-I-T/LatentNeuralOperator
pip_dependencies:
- torch>=2.5.0
- scipy>=1.13.0
- numpy>=1.26.0
tags:
- scientific-ml
- neural-operator
- lno
- inverse-pde
---

# Latent Neural Operator (LNO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090.
- Repository: `https://github.com/L-I-M-I-T/LatentNeuralOperator`.
- Data: Forward and inverse Darcy, Poisson, and Helmholtz datasets.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, step lr scheduler.
