---
id: recipe:resopd
type: recipe
title: "ResOPD Tail Residualization"
method: method:resopd
task: task:student-distillation
target_hardware: "sparse-payload OPD host (sampled-token or Top-k teacher)"
framework: "PyTorch OPD host"
repo_url: "https://github.com/InternLM/ResOPD"
code_status: announced
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - resopd
  - distillation
---

# ResOPD Tail Residualization

## Hardware & Environment Setup
- Claimed repo: `https://github.com/InternLM/ResOPD`. 404 as of 2026-10-06. `code_status: announced`.
- Distill default stays OPD. Sparse keep-mask stays sparse-opd-supervision.

## Quickstart Implementation

```python
from __future__ import annotations

def tail_mass(top_probs: list[float]) -> float:
    if not top_probs:
        raise ValueError("Top-k payload is empty")
    mass = sum(top_probs)
    if mass < 0 or mass > 1:
        raise ValueError("Top-k probabilities must be in [0, 1] and sum to <= 1")
    return 1.0 - mass
```

Transmit Top-k (or the sampled token) plus `tail_mass`. Backprop the exact tail-event gradient and sample the within-tail residual locally. No extra teacher query.

## Critical Hyperparameters & Tuning Advice
- Abstract: unbiased full-vocab reverse KL under the same sparse payload. Do not retarget OPD.
