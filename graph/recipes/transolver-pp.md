---
id: recipe:transolver-pp
type: recipe
title: Transolver++ (Million-Scale Neural PDE Solver) Recipe
method: method:transolver-pp
task: task:operator-industrial-mesh
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+
repo_url: https://github.com/thuml/Transolver
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
- scipy>=1.13.0
tags:
- scientific-ml
- neural-operator
- transformer
- transolver-pp
---

# Transolver++ Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Repository: `https://github.com/thuml/Transolver`.
- Data: DrivAerNet million-scale surface aerodynamic meshes.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine decay, weight_decay=1e-4.
