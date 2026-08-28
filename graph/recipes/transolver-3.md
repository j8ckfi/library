---
id: recipe:transolver-3
type: recipe
title: Transolver-3 (Industrial-Scale Geometry Solver) Recipe
method: method:transolver-3
task: task:operator-industrial-mesh
target_hardware: 8x NVIDIA H100 80GB (or A100 80GB)
framework: PyTorch 2.5+
repo_url: https://github.com/thuml/Transolver-3
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
- scipy>=1.13.0
- trimesh>=4.4.0
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- aerodynamics
- transolver-3
- sota
---

# Transolver-3 Industrial Mesh Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB (or A100 80GB).
- Repository: `https://github.com/thuml/Transolver-3`.
- Datasets: DrivAerML, AhmedML, NASA-CRM (>160M mesh cells).

## Training Hyperparameters (from Paper Table 9)
- Loss: Relative L2 Loss on surface pressure/shear and volumetric fields.
- Epochs: 500 epochs.
- Optimizer: AdamW.
- Learning Rate: 1e-3 with CosineAnnealingLR.
- Warmup: 5% linear warmup.
- Weight Decay: 0.05.
- Gradient Clipping: 1.0.
- Batch Size: 1.
- Subset Sample Size: 100k points per mesh per step.
- Precision: float16 / bfloat16 mixed precision.
