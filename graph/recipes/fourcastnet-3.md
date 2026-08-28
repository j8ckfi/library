---
id: recipe:fourcastnet-3
type: recipe
title: FourCastNet 3 (Spherical Weather Neural Operator) Recipe
method: method:fourcastnet-3
task: task:operator-weather
target_hardware: 8x NVIDIA H100 80GB
framework: PyTorch 2.5+ / NVIDIA Earth-2
repo_url: none found
pip_dependencies:
- torch>=2.5.0
- torch-harmonics>=0.6.0
- xarray>=2024.1.0
tags:
- scientific-ml
- neural-operator
- weather-forecasting
- fourcastnet-3
- sota
---

# FourCastNet 3 Weather Forecasting Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB.
- Implementation: `none found` (NVIDIA Earth-2 / Modulus framework).
- Data: ERA5 0.25° global reanalysis (surface and atmospheric pressure levels).

## Hyperparameters & Optimization
- Loss: Latitude-weighted MSE + Ensemble CRPS Loss.
- Optimizer: AdamW, lr=5e-4 with cosine decay and warmup.
