---
id: task:operator-grid-pde
type: task
title: Neural Operators for Regular-Grid PDEs
domain: scientific-ml
summary: Learning solution operators for parametric partial differential equations
  discretized on regular Cartesian grids.
current_sota:
- method: method:cvit
  as_of: '2026-08-28'
  benchmark: PDEBench / 2D Darcy Flow / 2D Navier-Stokes
  metric: relative L2 error across variable resolutions
  value: Default SOTA for Regular Grid PDEs
  notes: CViT (2405.13998); continuous vision transformer with coordinate cross-attention.
- method: method:poseidon
  as_of: '2026-08-28'
  benchmark: PDEBench / 2D/3D Multiscale PDEs
  metric: fine-tuned relative L2 error
  value: SOTA Pretrained Foundation Fine-tune
  notes: Poseidon (2405.19101); pre-trained multiscale operator fine-tuned when PDE
    family shifts.
methods:
- method:cvit
- method:poseidon
- method:fno
- method:deeponet
- method:ffno
- method:cno
- method:tante
- method:rno
tags:
- scientific-ml
- neural-operator
- pde
- regular-grid
- cvit
---

# Neural Operators for Regular-Grid PDEs

## Problem Definition
Parametric partial differential equations (PDEs) discretized on regular Cartesian grids, such as 2D/3D Darcy flow, Navier-Stokes fluid dynamics, and wave equations. The goal is learning resolution-invariant solution operators mapping initial/boundary conditions or coefficient fields to solution states.

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **CViT** (`method:cvit`, 2405.13998, ICLR 2025) Continuous Vision Transformer with coordinate embeddings and query-wise cross-attention.
- **Pretrained Foundation Alternative**: **Poseidon** (`method:poseidon`, 2405.19101) fine-tuned for the target PDE family.
- **Baselines**: **FNO** (`method:fno`), **DeepONet** (`method:deeponet`), **CNO** (`method:cno`), **F-FNO** (`method:ffno`).
