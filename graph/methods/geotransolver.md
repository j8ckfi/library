---
id: method:geotransolver
type: method
title: GeoTransolver (Geometry-Aware Physics Attention)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:geotransolver
recipes:
- recipe:geotransolver
claims:
- benchmark: 3D Irregular Domain Aerodynamics / Structural Mechanics
  metric: relative L2 error
  value: Multi-scale geometry-aware physics attention with GALE
  baseline: Transolver / GINO
  date: '2026-08-28'
  verified: true
  notes: Physics-Attention integrated with Geometry-Aware Latent Embedding (GALE)
    within NVIDIA PhysicsNeMo ecosystem.
tags:
- scientific-ml
- neural-operator
- geotransolver
- physicsnemo
---

# GeoTransolver (Geometry-Aware Physics Attention)

## Method Overview
GeoTransolver combines Physics-Attention slicing with multi-scale geometric latent embeddings:
1. **GALE Latent Embedding**: Incorporates Geometry-Aware Latent Embedding (GALE) to encode local multi-scale surface curvature.
2. **Multi-Scale Physics Slices**: Extends Transolver attention across hierarchical geometric levels.

## When to Use
- Active industrial alternative in the NVIDIA PhysicsNeMo ecosystem.
