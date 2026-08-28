---
id: recipe:geotransolver
type: recipe
title: GeoTransolver (Geometry-Aware Physics Attention) Recipe
method: method:geotransolver
task: task:operator-industrial-mesh
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+ / NVIDIA PhysicsNeMo
repo_url: none found
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
tags:
- scientific-ml
- neural-operator
- geotransolver
- physicsnemo
---

# GeoTransolver Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Implementation: `none found` (Referenced in NVIDIA PhysicsNeMo docs).

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine learning rate decay.
