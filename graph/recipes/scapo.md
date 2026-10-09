---
id: recipe:scapo
type: recipe
title: "SCAPO Semifactual Token Credit"
method: method:scapo
task: task:math-code-rl-dense
target_hardware: "GRPO-family host; paper: Qwen3 1.7B/4B math RLVR"
framework: "PyTorch GRPO host; official SCAPO"
repo_url: "https://github.com/DtYXs/SCAPO"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - scapo
---

# SCAPO Semifactual Token Credit

## Hardware & Environment Setup
- Official: `https://github.com/DtYXs/SCAPO`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def stability_scale(drift: float, cap: float = 1.0) -> float:
    if cap <= 0:
        raise ValueError("cap must be positive")
    if drift < 0:
        raise ValueError("drift must be non-negative")
    return cap / (cap + drift)
```

Rescale GRPO token credit by semifactual stability. Do not retarget CISPO.
