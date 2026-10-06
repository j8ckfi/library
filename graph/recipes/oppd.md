---
id: recipe:oppd
type: recipe
title: "OPPD Sequence-Level Power Distillation"
method: method:oppd
task: task:student-distillation
target_hardware: "SMC + frozen teacher box; paper: math then HumanEval transfer"
framework: "PyTorch; official OPPD"
repo_url: "https://github.com/ArminAzizi98/OPPD"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - oppd
  - distillation
---

# OPPD Sequence-Level Power Distillation

## Hardware & Environment Setup
- Official: `https://github.com/ArminAzizi98/OPPD`. `code_status: released` as of 2026-10-06.
- Token-level matching stays OPD.

## Quickstart Implementation

```python
from __future__ import annotations

def power_weight(logp: float, exponent: float) -> float:
    if exponent < 1:
        raise ValueError("power exponent must be >= 1")
    return exponent * logp
```

Clone OPPD. Student proposes; weight complete answers by the frozen teacher's power distribution; MLE with those weights. Do not decode 64 candidates at serving.

## Critical Hyperparameters & Tuning Advice
- MATH500 +23.0 vs untrained. Vs GRPO +3.8 MATH500. Do not retarget OPD.
