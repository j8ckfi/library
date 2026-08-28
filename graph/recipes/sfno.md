---
id: recipe:sfno
type: recipe
title: Spherical Fourier Neural Operator (SFNO) Recipe
method: method:sfno
task: task:operator-weather
target_hardware: 1x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+ / torch-harmonics
repo_url: https://github.com/neuraloperator/neuraloperator
pip_dependencies:
- torch>=2.5.0
- torch-harmonics>=0.6.0
- tensorly>=0.8.1
tags:
- scientific-ml
- neural-operator
- spherical
- sfno
- weather
---

# Spherical Fourier Neural Operator (SFNO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA A100 (80GB) or H100.
- Repository: `https://github.com/neuraloperator/neuraloperator`.
- Data: ERA5 atmospheric variables on latitude-longitude spherical grids.

## Hyperparameters & Optimization
- Loss: Area-weighted Relative L2 / L1 Loss on S2.
- Optimizer: AdamW, lr=1e-3, cosine decay with warmup.
