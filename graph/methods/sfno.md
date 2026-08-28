---
id: method:sfno
type: method
title: Spherical Fourier Neural Operator (SFNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:sfno
recipes:
- recipe:sfno
claims:
- benchmark: ERA5 Shallow Water / Atmospheric Dynamics
  metric: long-term rollout stability & RMSE
  value: Equivariant spherical harmonic operator baseline
  baseline: Planar FNO / ResNet
  date: '2026-08-28'
  verified: true
  notes: Spherical harmonic transform-based spectral operator respecting S2 geometric
    symmetries.
tags:
- scientific-ml
- neural-operator
- spherical
- sfno
- weather
---

# Spherical Fourier Neural Operator (SFNO)

## Method Overview
Spherical Fourier Neural Operator (SFNO) parameterizes PDEs natively on the sphere S2:
1. **Spherical Harmonic Transforms**: Replaces standard FFT with spherical harmonic basis projections to preserve geometric equivariance.
2. **Global Atmospheric Stability**: Prevents coordinate singularity artifacts at poles in global climate and weather forecasting.

## When to Use
- Active baseline for spherical atmospheric dynamics and weather forecasting; superseded by FourCastNet 3 as the 2026 SOTA weather default.
