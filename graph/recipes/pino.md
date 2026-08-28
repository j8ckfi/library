---
id: recipe:pino
type: recipe
title: Physics-Informed Neural Operator (PINO) Recipe
method: method:pino
task: task:operator-physics-informed
target_hardware: 1x NVIDIA RTX 4090 or A100
framework: PyTorch 2.5+ / NeuralOperator
repo_url: https://github.com/neuraloperator/physics_informed
pip_dependencies:
- torch>=2.5.0
- neuraloperator>=1.0.0
- sympy>=1.13.0
tags:
- scientific-ml
- neural-operator
- physics-informed
- pino
---

# Physics-Informed Neural Operator (PINO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/neuraloperator/physics_informed`.
- Data: 2D Navier-Stokes and Darcy flow with PDE residual collocation points.

## Hyperparameters & Optimization
- Loss: Combined Data L2 Loss + PDE Residual Loss with fixed weighting.
- Optimizer: AdamW (lr=1e-3) followed by L-BFGS.
