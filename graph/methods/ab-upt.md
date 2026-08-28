---
id: method:ab-upt
type: method
title: AB-UPT (Anchored-Branched Universal Physics Transformer)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:ab-upt
recipes:
- recipe:ab-upt
claims:
- benchmark: AhmedML / DrivAerML Automotive Aerodynamics
  metric: relative L2 error (surface & volume pressure/velocity)
  value: 2.07 rel L2 on AhmedML volume pressure (vs Transolver-3 2.16)
  baseline: UPT / GINO / MeshGraphNet
  date: '2026-08-28'
  verified: true
  notes: Anchored-Branched UPT with separate geometry, surface, and volume branches;
    CAD-only inference capability. Uses LION optimizer in some configs.
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- ab-upt
---

# AB-UPT (Anchored-Branched Universal Physics Transformer)

## Method Overview
AB-UPT scales neural CFD surrogates for full-scale automotive aerodynamics:
1. **Branch Decomposition**: Splits representations into dedicated geometry, surface field, and volume field branches.
2. **Anchor Attention**: Anchors cross-attention queries to surface mesh coordinates to decouple CAD geometric inference from volumetric mesh generation.
3. **CAD-Only Inference**: Evaluates aerodynamic performance directly from raw CAD surface geometries without computing volumetric CFD meshes.

## When to Use
- Primary industrial alternative to Transolver-3; competitive on volumetric AhmedML fields (2.07 rel L2 volume pressure).
