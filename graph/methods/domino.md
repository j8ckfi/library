---
id: method:domino
type: method
title: DoMINO (Decomposable Multi-Scale Iterative Neural Operator)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:domino
recipes:
- recipe:domino
claims:
- benchmark: Large-scale 3D Point-Cloud Engineering Simulations (DrivAerNet, ShapeNet)
  metric: relative L2 error & memory scaling
  value: Decomposable multi-scale iterative neural operator for CAE
  baseline: GINO / PointNet++ / MeshGraphNet
  date: '2026-08-28'
  verified: true
  notes: Decomposes complex physical domains into hierarchical point-cloud subdomains
    solved iteratively.
tags:
- scientific-ml
- neural-operator
- domino
- point-cloud
- physicsnemo
---

# DoMINO (Decomposable Multi-Scale Iterative Neural Operator)

## Method Overview
DoMINO models large-scale engineering simulations via domain decomposition:
1. **Subdomain Partitioning**: Divides large 3D point-cloud meshes into manageable local subdomains.
2. **Iterative Boundary Propagation**: Iteratively exchanges boundary information across subdomains to achieve global physical equilibrium.

## When to Use
- Active industrial alternative for point-cloud CAE in the NVIDIA PhysicsNeMo ecosystem.
