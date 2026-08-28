---
id: recipe:fno
type: recipe
title: Fourier Neural Operator (FNO) Recipe
method: method:fno
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090 or 1x A100 (80GB)
framework: PyTorch 2.5+ / NeuralOperator
repo_url: https://github.com/neuraloperator/neuraloperator
pip_dependencies:
- torch>=2.5.0
- neuraloperator>=1.0.0
- tensorly>=0.8.1
tags:
- scientific-ml
- neural-operator
- spectral
- fno
- baseline
---

# Fourier Neural Operator (FNO) Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100 GPU.
- Repository: `https://github.com/neuraloperator/neuraloperator`.
- Benchmark Data: PDEBench, 2D Darcy Flow, 2D Navier-Stokes.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss (`LpLoss(d=2, p=2)`).
- Optimizer: AdamW, lr=1e-3, weight_decay=1e-4, CosineAnnealingLR.
- Modes: 12-16 Fourier modes, width: 32-64 channels.
