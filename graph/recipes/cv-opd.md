---
id: recipe:cv-opd
type: recipe
title: Contrastive Vision On-Policy Distillation
method: method:cv-opd
task: task:student-distillation
target_hardware: VLM OPD host
framework: PyTorch VLM OPD host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cv-opd
---

# Contrastive Vision On-Policy Distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def visual_token(token_discrepancy: float, sample_gate: float, min_d: float) -> bool:
    if min_d < 0:
        raise ValueError("min_d must be non-negative")
    return token_discrepancy >= min_d and sample_gate > 0
```

Contrast crops, gate tokens. Do not retarget OPD.
