---
id: method:transolver-pp
type: method
title: Transolver++ (Million-Scale Neural PDE Solver)
category: neural-operator
status: active
sota_for: []
supersedes: []
superseded_by: method:transolver-3
papers:
- paper:transolver-pp
recipes:
- recipe:transolver-pp
claims:
- benchmark: Million-Scale 3D Aerodynamics / DrivAerNet
  metric: relative L2 surface error
  value: Million-scale geometry neural solver baseline
  baseline: Transolver / GINO
  date: '2026-08-28'
  verified: true
  notes: Scales Physics-Attention to million-scale geometries via hierarchical spatial
    slicing.
tags:
- scientific-ml
- neural-operator
- transformer
- transolver-pp
---

# Transolver++ (Million-Scale Neural PDE Solver)

## Method Overview
Transolver++ scales Physics-Attention to million-scale geometries:
1. **Hierarchical Slicing**: Decomposes large-scale 3D mesh points into multi-scale hierarchical slice tokens.
2. **High-Fidelity Aerodynamics**: Models fine boundary layer variations on million-node vehicle meshes.

## Supersession
- Superseded by `method:transolver-3` (2602.04940) as the industrial CAD default; remains active.
