---
id: method:gino
type: method
title: Geometry-Informed Neural Operator (GINO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:gino
recipes:
- recipe:gino
claims:
- benchmark: Ahmed Body 3D Aerodynamics / Surface Pressure
  metric: relative L2 surface error
  value: Hybrid GNO encoder + latent FNO baseline
  baseline: PointNet / MeshGraphNet
  date: '2026-08-28'
  verified: true
  notes: Graph Neural Operator encodes arbitrary surface meshes to regular latent
    grid for FNO processing.
tags:
- scientific-ml
- neural-operator
- gino
- cad-mesh
- aerodynamics
---

# Geometry-Informed Neural Operator (GINO)

## Method Overview
GINO integrates Graph Neural Operators (GNO) with Fourier Neural Operators (FNO) for 3D engineering geometries:
1. **GNO Mesh Encoder**: Projects unstructured boundary/surface mesh point clouds into a regular 3D Cartesian latent grid.
2. **Latent 3D FNO**: Processes volumetric physics with global Fourier neural operator layers.
3. **GNO Query Decoder**: Projects latent grid representations back to arbitrary output surface points.

## When to Use
- Active industrial ancestor for automotive aerodynamics (Ahmed Body) in NVIDIA PhysicsNeMo.
