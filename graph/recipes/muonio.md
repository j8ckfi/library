---
id: recipe:muonio
type: recipe
title: "MuonIO Embedding and LM-Head Updates"
method: method:muonio
task: task:llm-pretraining-optimization
target_hardware: "Muon host that already updates hidden matrices; paper: 60M / 130M / 1B C4"
framework: "PyTorch Muon / Polar Express plus I/O-layer norm-aware steps"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - muonio
  - optimizer
  - muon
---

# MuonIO Embedding and LM-Head Updates

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.02705`). `repo_url: none found`. `code_status: none`.
- Hidden-layer ~7B optimizer stays Muon2. This recipe only replaces AdamW on embeddings and the LM head.

## Quickstart Implementation

```python
from __future__ import annotations

import math


def col_1to2_step(grad: list[list[float]], lr: float) -> list[list[float]]:
    if not grad or not grad[0]:
        raise ValueError("embedding gradient is empty")
    cols = len(grad[0])
    update = [[0.0] * cols for _ in grad]
    for j in range(cols):
        nrm = math.sqrt(sum(row[j] * row[j] for row in grad))
        if nrm == 0.0:
            continue
        scale = lr / nrm
        for i, row in enumerate(grad):
            update[i][j] = -scale * row[j]
    return update


def row_2toinf_step(grad: list[list[float]], lr: float) -> list[list[float]]:
    if not grad or not grad[0]:
        raise ValueError("lm_head gradient is empty")
    update = []
    for row in grad:
        inf = max(abs(x) for x in row)
        if inf == 0.0:
            update.append([0.0] * len(row))
            continue
        update.append([-lr * x / inf for x in row])
    return update
```

Apply `col_1to2_step` to the embedding table and `row_2toinf_step` to the LM head. Keep hidden matrices on Muon2 (or Polar Express).

## Critical Hyperparameters & Tuning Advice
- I/O FLOPs \(7Vd+3V\) vs AdamW \(13Vd\); state \(Vd\) vs \(2Vd\).
- Do not retarget Muon2 from the 60M–1B C4 table.
