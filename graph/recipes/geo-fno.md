---
id: recipe:geo-fno
type: recipe
title: Geo-FNO (Fourier Neural Operator on General Geometries) Recipe
method: method:geo-fno
task: task:operator-industrial-mesh
target_hardware: 1x NVIDIA RTX 4090 or 1x A100
framework: PyTorch 2.5+ / NeuralOperator
repo_url: https://github.com/neuraloperator/Geo-FNO
pip_dependencies:
- torch>=2.5.0
- neuraloperator>=1.0.0
- scipy>=1.13.0
tags:
- scientific-ml
- neural-operator
- geo-fno
- mesh-pde
---

# Geo-FNO Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/neuraloperator/Geo-FNO`.
- Data: Airfoil surface meshes and elasticity geometry benchmarks.

## Hyperparameters & Optimization
- Loss: Relative L2 loss on deformed mesh coordinates.
- Optimizer: AdamW, lr=1e-3, weight_decay=1e-4.
