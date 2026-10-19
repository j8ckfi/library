---
id: recipe:gca
type: recipe
title: 'Grounded credit assignment for search agents'
method: method:gca
task: task:web-search-agent-rl
target_hardware: 'Paper: Qwen2.5-3B and Qwen3-30B-A3B Search-R1'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- gca
---

# Grounded credit assignment for search agents

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def grounded_credit(adv: float, retrieved: bool, correct: bool, cap: float = 0.1) -> float:
    delta = 0.0
    if retrieved and not correct:
        delta = -min(cap * abs(adv), abs(adv))
    elif correct and not retrieved:
        delta = -min(cap * abs(adv), abs(adv))
    return adv + delta
```

Do not retarget locked SOTA from this recipe.
