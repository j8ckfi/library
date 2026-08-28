---
id: recipe:transolver
type: recipe
title: Transolver (Physics-Attention PDE Transformer) Recipe
method: method:transolver
task: task:operator-industrial-mesh
target_hardware: 2x NVIDIA A100 (80GB) or RTX 4090
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
- transolver
---

# Transolver Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 2x NVIDIA A100 (80GB).
- Repository: `https://github.com/thuml/Transolver`.
- Data: ShapeNet, Car-Design, 2D/3D irregular PDE meshes.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, weight_decay=1e-4, CosineAnnealingLR.
