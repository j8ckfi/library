---
id: paper:geotransolver
type: paper
title: 'GeoTransolver: Learning Physics on Irregular Domains Using Multi-scale Geometry
  Aware Physics Attention Transformer'
authors:
- Corey Adams
- Rishikesh Ranade
- Ram Cherukuri
- Sanjay Choudhry
year: 2025
month: 12
arxiv_id: '2512.20399'
url: https://arxiv.org/abs/2512.20399
methods:
- method:geotransolver
cites:
- paper:transolver
- paper:gino
tags:
- scientific-ml
- neural-operator
- geotransolver
- physicsnemo
---

# GeoTransolver: Learning Physics on Irregular Domains Using Multi-scale Geometry Aware Physics Attention Transformer

## Abstract Summary
We present GeoTransolver, a multiscale geometry-aware physics attention transformer for Computer Aided Engineering (CAE). GeoTransolver extends the Transolver backbone with GALE (Geometry-Aware Latent Embeddings) attention, which pairs physics-aware self-attention on learned state slices with cross-attention to a shared geometry and global context computed via multi-scale ball queries (inspired by Domino) and reused in every block. Implemented and released in NVIDIA PhysicsNeMo, GeoTransolver persistently projects geometry and global parameters, into physical state spaces to anchor computations to domain structure and operating regimes. We benchmark on DrivAerML, SHIFT-SUV, and SHIFT-Wing against Domino, Transolver (PhysicsNeMo implementation), and literature-reported AB-UPT, evaluating drag/lift R2 and relative L1 errors on field variables. As an additional nonlinear structural mechanics application, we also report Transolver and GeoTransolver results on bumper-beam and full-vehicle Body-in-White (BIW) crash-dynamics benchmarks, evaluating relative L2 trajectory error and probe-level kinematic MSE. GeoTransolver delivers improved accuracy, robustness to geometry and regime shifts, and favorable data efficiency; we include DrivAerML ablations and qualitative contour and design-trend results, advancing operator learning for high-fidelity surrogates on complex, irregular, non-linear domains.

## Key Contributions
- Formulates and evaluates `geotransolver` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `none found`
