---
id: recipe:clean
type: recipe
title: "Clean Nyström SOAP Preconditioners"
method: method:clean
task: task:llm-pretraining-optimization
target_hardware: "SOAP-family LLM pretrain; paper: LLaMA-1.3B memory / 13B on one 80GB GPU"
framework: "PyTorch SOAP-family trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - clean
  - optimizer
  - soap
---

# Clean Nyström SOAP Preconditioners

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.04204`). `repo_url: none found`. `code_status: none`.
- High-memory SOAP stays KL-SOAP. 7B default stays Muon2.

## Quickstart Implementation

```python
from __future__ import annotations

def nystrom_rank(dim: int, rank: int) -> int:
    if dim <= 0 or rank <= 0:
        raise ValueError("dim and rank must be positive")
    return min(rank, dim)
```

Sketch SOAP's left/right preconditioners at `nystrom_rank`. Reintegrate the off-subspace residual. Q-Clean stores those states in low precision.

## Critical Hyperparameters & Tuning Advice
- Q-Clean: >50% optimizer memory vs Muon on LLaMA-1.3B. Clean: 26% faster wall-clock to AdamW final quality. Do not retarget Muon2.
