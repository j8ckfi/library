---
id: recipe:gino
type: recipe
title: Geometry-Informed Neural Operator (GINO) Recipe
method: method:gino
task: task:operator-industrial-mesh
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+ / NVIDIA PhysicsNeMo
repo_url: https://github.com/neuraloperator/neuraloperator
pip_dependencies:
- torch>=2.5.0
- neuraloperator>=1.0.0
- torch-geometric>=2.5.0
tags:
- scientific-ml
- neural-operator
- gino
- cad-mesh
- aerodynamics
---

# Geometry-Informed Neural Operator (GINO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Repository: `https://github.com/neuraloperator/neuraloperator`.
- Data: Ahmed Body 3D surface and volume velocity/pressure fields.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss on surface pressure and volumetric velocity.
- Optimizer: AdamW, lr=1e-3, cosine scheduler.
