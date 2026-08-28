---
id: method:geo-fno
type: method
title: Geo-FNO (Fourier Neural Operator on General Geometries)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:geo-fno
recipes:
- recipe:geo-fno
claims:
- benchmark: Airfoil flow / Elasticity on irregular 2D/3D geometries
  metric: relative L2 error
  value: Diffeomorphic coordinate deformation baseline
  baseline: Standard FNO / PointNet
  date: '2026-08-28'
  verified: true
  notes: Maps irregular physical domains to latent Cartesian grids via learned coordinate
    deformations.
tags:
- scientific-ml
- neural-operator
- geo-fno
- mesh-pde
---

# Geo-FNO (Fourier Neural Operator on General Geometries)

## Method Overview
Geo-FNO extends Fourier Neural Operators to irregular physical domains and geometries:
1. **Deformation Mapping**: Learns a diffeomorphic coordinate transformation mapping irregular physical geometries onto a canonical regular latent grid.
2. **Latent Spectral Processing**: Solves the PDE using standard FNO in the canonical latent space.
3. **Inverse Interpolation**: Maps the latent solution back onto the original irregular physical coordinates.

## When to Use
- Active baseline for irregular 2D/3D geometries and airfoil simulations.
