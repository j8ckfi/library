---
id: recipe:pmopd
type: recipe
title: "PMOPD Subspace-Protected Multi-Teacher OPD"
method: method:pmopd
task: task:student-distillation
target_hardware: "full-parameter multi-teacher OPD box; paper: Qwen2.5-7B and Llama-3.1-8B, Adafactor"
framework: "PyTorch OPD host with Adafactor-style preconditioning"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - pmopd
  - distillation
  - multi-teacher
---

# PMOPD Subspace-Protected Multi-Teacher OPD

## Hardware & Environment Setup
- No official GitHub as of 2026-09-30 (`arXiv:2609.34605`). `repo_url: none found`. `code_status: none`.
- Multi-teacher default stays Open-MOPD. Domain scale calibration stays DN-MOPD.

## Quickstart Implementation

```python
from __future__ import annotations


def project_out(matrix: list[list[float]], bases: list[list[float]]) -> list[list[float]]:
    if not matrix:
        return matrix
    rows = len(matrix)
    cols = len(matrix[0])
    out = [row[:] for row in matrix]
    for basis in bases:
        if len(basis) != rows * cols:
            raise ValueError("basis must match matrix size")
        flat = [out[i][j] for i in range(rows) for j in range(cols)]
        denom = sum(b * b for b in basis)
        if denom <= 0.0:
            continue
        coeff = sum(f * b for f, b in zip(flat, basis)) / denom
        k = 0
        for i in range(rows):
            for j in range(cols):
                out[i][j] -= coeff * basis[k]
                k += 1
    return out


def pmopd_step(
    gradient: list[list[float]],
    preconditioned: list[list[float]],
    protected: list[list[float]],
) -> list[list[float]]:
    g_hat = project_out(gradient, protected)
    # Caller applies Adafactor/Adam to g_hat to obtain `preconditioned`.
    return project_out(preconditioned, protected)
```

After each task block, SVD the cumulative \(\Delta W\) (paper \(K=16\)) and store the leading factors. Rebuild that memory at the start of the next cycle. Probe pairwise conflict before the first cycle; paper order Code→Reason→Math, four cycles.

## Critical Hyperparameters & Tuning Advice
- Dual projection is required under Adafactor. Gradient-only projection is an incomplete ablation.
- Do not accumulate an unbounded archive of old bases.
- Do not retarget library Open-MOPD from 66.97 vs their 63.54 Open-MOPD run.
