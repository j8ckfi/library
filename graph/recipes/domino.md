---
id: recipe:domino
type: recipe
title: DoMINO (Decomposable Multi-Scale Iterative Neural Operator) Recipe
method: method:domino
task: task:operator-industrial-mesh
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+ / NVIDIA PhysicsNeMo
repo_url: none found
pip_dependencies:
- torch>=2.5.0
- torch-geometric>=2.5.0
tags:
- scientific-ml
- neural-operator
- domino
- point-cloud
- physicsnemo
---

# DoMINO Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Implementation: `none found` (NVIDIA PhysicsNeMo ecosystem).

## Hyperparameters & Optimization
- Loss: Subdomain Boundary and Interior Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine decay.
