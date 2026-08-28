---
id: recipe:rno
type: recipe
title: Recurrent Neural Operators (RNO) Recipe
method: method:rno
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090 or A100
framework: PyTorch 2.5+
repo_url: https://github.com/ZaijunYe/RNO
pip_dependencies:
- torch>=2.5.0
- scipy>=1.13.0
- numpy>=1.26.0
tags:
- scientific-ml
- neural-operator
- rno
- recurrent
---

# Recurrent Neural Operators (RNO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/ZaijunYe/RNO`.
- Data: Long-horizon Navier-Stokes and Kuramoto-Sivashinsky trajectories.

## Hyperparameters & Optimization
- Loss: Multi-step unrolled Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine decay.
