---
id: recipe:deeponet
type: recipe
title: DeepONet (Deep Operator Network) Recipe
method: method:deeponet
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090
framework: PyTorch 2.5+ / DeepXDE
repo_url: https://github.com/luluxingbing/deeponet
pip_dependencies:
- torch>=2.5.0
- deepxde>=1.11.0
- numpy>=1.26.0
tags:
- scientific-ml
- neural-operator
- deeponet
- baseline
---

# DeepONet Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090.
- Repository: `https://github.com/luluxingbing/deeponet`.
- Data: ODE/PDE initial conditions and boundary evaluations.

## Hyperparameters & Optimization
- Loss: Mean Squared Error (MSE) / Relative L2.
- Optimizer: Adam (lr=1e-3) followed by L-BFGS fine-tuning.
