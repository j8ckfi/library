---
id: recipe:specialists-learn-faster
type: recipe
title: Specialists Learn Faster Data Order
method: method:specialists-learn-faster
task: task:open-data-recipe
target_hardware: Pretrain host; paper chronological vs shuffled organization
framework: PyTorch pretrain data order; project page only
repo_url: https://horizon-lab.org/specialist/
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- specialists-learn-faster
---

# Specialists Learn Faster Data Order

## Hardware & Environment Setup
- Project: `https://horizon-lab.org/specialist/`.
- `code_status: none` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def order_ok(kind: str) -> str:
    if kind not in {"chrono", "shuffle"}:
        raise ValueError("kind must be chrono or shuffle")
    return kind
```

Chronological specialists. Do not retarget OLMo-3.
