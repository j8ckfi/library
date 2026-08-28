---
id: paper:fourcastnet-3
type: paper
title: 'FourCastNet 3: A geometric approach to probabilistic machine-learning weather
  forecasting at scale'
authors:
- Boris Bonev
- Thorsten Kurth
- Ankur Mahesh
- Mauro Bisson
- Jean Kossaifi
- Karthik Kashinath
- Anima Anandkumar
- William D. Collins
- Michael S. Pritchard
- Alexander Keller
year: 2025
month: 7
arxiv_id: '2507.12144'
url: https://arxiv.org/abs/2507.12144
methods:
- method:fourcastnet-3
cites:
- paper:sfno
tags:
- scientific-ml
- neural-operator
- weather-forecasting
- fourcastnet-3
- sota
---

# FourCastNet 3: A geometric approach to probabilistic machine-learning weather forecasting at scale

## Abstract Summary
FourCastNet 3 advances global weather modeling by implementing a scalable, geometric machine learning (ML) approach to probabilistic ensemble forecasting. The approach is designed to respect spherical geometry and to accurately model the spatially correlated probabilistic nature of the problem, resulting in stable spectra and realistic dynamics across multiple scales. FourCastNet 3 delivers forecasting accuracy that surpasses leading conventional ensemble models and rivals the best diffusion-based methods, while producing forecasts 8 to 60 times faster than these approaches. In contrast to other ML approaches, FourCastNet 3 demonstrates excellent probabilistic calibration and retains realistic spectra, even at extended lead times of up to 60 days. All of these advances are realized using a purely convolutional neural network architecture tailored for spherical geometry. Scalable and efficient large-scale training on 1024 GPUs and more is enabled by a novel training paradigm for combined model- and data-parallelism, inspired by domain decomposition methods in classical numerical models. Additionally, FourCastNet 3 enables rapid inference on a single GPU, producing a 60-day global forecast at 0.25°, 6-hourly resolution in under 4 minutes. Its computational efficiency, medium-range probabilistic skill, spectral fidelity, and rollout stability at subseasonal timescales make it a strong candidate for improving meteorological forecasting and early warning systems through large ensemble predictions.

## Key Contributions
- Formulates and evaluates `fourcastnet-3` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `none found`
