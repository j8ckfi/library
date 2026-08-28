---
id: method:transolver-3
type: method
title: Transolver-3 (Industrial-Scale Geometry Solver)
category: neural-operator
status: sota
sota_for:
- task:operator-industrial-mesh
supersedes:
- method:transolver
- method:transolver-pp
papers:
- paper:transolver-3
recipes:
- recipe:transolver-3
claims:
- benchmark: DrivAerML / AhmedML / NASA-CRM (>160M cells)
  metric: relative L2 error (surface & volume fields)
  value: Wins 9/10 relative L2 benchmarks (3.71 surface p on DrivAerML vs GAOT 34.00,
    AB-UPT 4.82)
  baseline: AB-UPT / Transolver++ / GAOT / GINO / MeshGraphNet
  date: '2026-08-28'
  verified: true
  notes: Faster slice/deslice, geometry slice tiling, amortized subset training (100k
    points), physical-state cache. ICML 2026.
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- aerodynamics
- transolver-3
- sota
---

# Transolver-3 (Industrial-Scale Geometry Solver)

## Method Overview
Transolver-3 establishes the state-of-the-art standard for industrial 3D aerodynamic mesh evaluation (>160M cells):
1. **Geometry Slice Tiling**: Optimizes slice/deslice projection routines to process complex CAD point sets with linear compute and constant memory.
2. **Amortized Subset Training**: Randomly samples amortized subsets (100k points per step) from massive 100M+ cell meshes while retaining global physical consistency.
3. **Physical-State Caching**: Reuses intermediate physical slice representations across multi-state iterations.

## When to Use
- Default SOTA method for industrial CAD meshes and vehicle/aerospace CFD surrogates (DrivAerML, AhmedML, NASA-CRM).

## Supersession
- Supersedes `method:transolver` and `method:transolver-pp` as the industrial mesh default (ancestors remain active).
