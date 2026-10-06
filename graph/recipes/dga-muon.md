---
id: recipe:dga-muon
type: recipe
title: "DGA-Muon Decoupled Geometry-Aligned Scaling"
method: method:dga-muon
task: task:llm-pretraining-optimization
target_hardware: "Muon/NorMuon LLM pretrain box"
framework: "PyTorch Muon-family trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - dga-muon
  - optimizer
---

# DGA-Muon Decoupled Geometry-Aligned Scaling

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.06578`). `repo_url: none found`. `code_status: none`.
- 7B default stays Muon2.

## Quickstart Implementation

```python
from __future__ import annotations

def scale_axis(rows: int, cols: int) -> str:
    if rows <= 0 or cols <= 0:
        raise ValueError("matrix shape must be positive")
    if cols >= rows:
        return "row"
    return "column"
```

Compute second-moment scales on the raw gradient along `scale_axis`. Orthogonalize separately. Clip the scales. Do not derive the scale from the orthogonalized matrix.

## Critical Hyperparameters & Tuning Advice
- Wide: row-wise. Tall: column-wise. Do not retarget Muon2.
