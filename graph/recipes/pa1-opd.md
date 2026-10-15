---
id: recipe:pa1-opd
type: recipe
title: One-step prefix-augmented OPD for continued pretrain
method: method:pa1-opd
task: task:student-distillation
target_hardware: 'Paper: OLMo2 continued pretrain'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- pa1-opd
---

# One-step prefix-augmented OPD for continued pretrain

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def select_surprisal_roots(surprisal: list[float], keep_frac: float = 0.1) -> list[int]:
    if not surprisal:
        raise ValueError("empty surprisal")
    if not 0.0 < keep_frac <= 1.0:
        raise ValueError("keep_frac must be in (0, 1]")
    k = max(1, int(len(surprisal) * keep_frac))
    ranked = sorted(range(len(surprisal)), key=lambda i: surprisal[i], reverse=True)
    return ranked[:k]
```

Do not retarget locked SOTA from this recipe.
