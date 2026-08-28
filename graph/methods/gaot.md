---
id: method:gaot
type: method
title: GAOT (Geometry-Aware Operator Transformer)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:gaot
recipes:
- recipe:gaot
claims:
- benchmark: NASA-CRM / DrivAerML / AhmedML Industrial Benchmarks
  metric: relative L2 error (surface pressure)
  value: 34.00 rel L2 on DrivAerML surface pressure (lost vs Transolver-3 3.71)
  baseline: MeshGraphNet / GINO
  date: '2026-08-28'
  verified: true
  notes: 'Geometry-Aware Operator Transformer. Note: NOT the industrial SOTA default;
    significantly underperforms Transolver-3 on large-scale aerodynamic mesh benchmarks.'
tags:
- scientific-ml
- neural-operator
- transformer
- gaot
---

# GAOT (Geometry-Aware Operator Transformer)

## Method Overview
GAOT equips operator transformers with geometry-aware positional representations:
1. **Domain Geometry Encoding**: Encodes surface curvature, normal vectors, and boundary topology into attention biases.
2. **Cross-Attention Mapping**: Maps boundary conditions and flow parameters across arbitrary domain discretizations.

## When to Use
- Active method for arbitrary geometric domains.
- **Benchmark Reality**: GAOT is NOT the industrial default. In Transolver-3 evaluations, GAOT scored 34.00 relative L2 on DrivAerML surface pressure versus 3.71 for Transolver-3.
