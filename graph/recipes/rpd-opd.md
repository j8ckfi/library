---
id: recipe:rpd-opd
type: recipe
title: Relative Policy-Difference OPD Transfer
method: method:rpd-opd
task: task:student-distillation
target_hardware: OPD host with an expert and a reference checkpoint
framework: PyTorch OPD host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- rpd-opd
---

# Relative Policy-Difference OPD Transfer

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def relative_log_ratio(logp_expert: float, logp_ref: float) -> float:
    return logp_expert - logp_ref
```

Transfer the residual, not the expert absolute. Do not retarget OPD.
