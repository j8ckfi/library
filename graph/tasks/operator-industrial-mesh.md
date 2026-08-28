---
id: task:operator-industrial-mesh
type: task
title: Neural Operators for Industrial CAD Meshes & Geometries
domain: scientific-ml
summary: Predicting surface and volumetric aerodynamic physical fields on complex
  3D CAD meshes and unstructured point clouds.
current_sota:
- method: method:transolver-3
  as_of: '2026-08-28'
  benchmark: DrivAerML / AhmedML / NASA-CRM (>160M cells)
  metric: relative L2 error (surface & volume fields)
  value: Default SOTA for Industrial 3D Meshes
  notes: Transolver-3 (2602.04940); physics-attention slices, geometry slice tiling,
    amortized subset training, physical-state cache.
methods:
- method:transolver-3
- method:ab-upt
- method:geotransolver
- method:domino
- method:transolver-pp
- method:transolver
- method:gino
- method:gaot
- method:geo-fno
- method:gnot
- method:upt
- method:lno
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- aerodynamics
- transolver-3
---

# Neural Operators for Industrial CAD Meshes & Geometries

## Problem Definition
Evaluating aerodynamic and physical field distributions (surface pressure, wall shear stress, volume velocity/pressure) over high-fidelity 3D CAD geometries and industrial meshes exceeding 100M cells (e.g., DrivAerML, AhmedML, NASA Common Research Model).

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **Transolver-3** (`method:transolver-3`, 2602.04940, ICML 2026), scaling up to >160M cells with geometry slice tiling, amortized subset training, and physical-state caching.
- **Industrial Alternatives**: **AB-UPT** (`method:ab-upt`, 2502.09692), **GeoTransolver** (`method:geotransolver`, 2512.20399), **DoMINO** (`method:domino`, 2501.13350).
- **Lineage**: **Transolver** (`method:transolver`), **Transolver++** (`method:transolver-pp`), **GINO** (`method:gino`), **GAOT** (`method:gaot` - note: GAOT is not the industrial default and lost on DrivAerML/NASA-CRM benchmarks).
