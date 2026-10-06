---
id: recipe:orca
type: recipe
title: "ORCA Early Orthogonal Regularization"
method: method:orca
task: task:llm-pretraining-optimization
target_hardware: "Muon-family LLM pretrain box; paper: LLaMA/Qwen3/MoE 130M–8B"
framework: "PyTorch Muon-family trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - orca
  - optimizer
---

# ORCA Early Orthogonal Regularization

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.06116`). `repo_url: none found`. `code_status: none`.
- Default ~7B optimizer stays Muon2.

## Quickstart Implementation

```python
from __future__ import annotations

def orca_coeff(step: int, cool_after: int, strength: float) -> float:
    if cool_after <= 0:
        raise ValueError("cool_after must be positive")
    if strength < 0:
        raise ValueError("strength must be non-negative")
    return strength if step < cool_after else 0.0
```

Add `orca_coeff * ||W W^T - I||` (or the paper's soft-orthogonality form) only while the coefficient is nonzero. After `cool_after`, the extra term is gone; the Muon update is unchanged.

## Critical Hyperparameters & Tuning Advice
- Cool the regularizer; do not keep it for the whole run.
- Abstract: lower final val loss than Muon. Do not retarget Muon2.
