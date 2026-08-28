---
id: recipe:ab-upt
type: recipe
title: AB-UPT (Anchored-Branched Universal Physics Transformer) Recipe
method: method:ab-upt
task: task:operator-industrial-mesh
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+
repo_url: https://github.com/Emmi-AI/AB-UPT
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
- lion-pytorch>=0.1.2
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- ab-upt
---

# AB-UPT Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB) or H100.
- Repository: `https://github.com/Emmi-AI/AB-UPT`.
- Datasets: AhmedML, DrivAerML CAD surface and volumetric flow fields.

## Hyperparameters & Optimization
- Loss: Relative L2 on surface and volume predictions.
- Optimizer: LION (or AdamW), lr=1e-4 to 1e-3, cosine schedule.
