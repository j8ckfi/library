---
id: recipe:flashnext-rl
type: recipe
title: 'Flash-Next 8xB200 RL freeze set'
method: method:flashnext-rl
task: task:frontier-rl-posttrain-stack
target_hardware: '1x 8xB200 plus three inference nodes; 131K context SWE RL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- flashnext-rl
---

# Flash-Next 8xB200 RL freeze set

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

FROZEN = ('embed', 'layer0', 'layer1', 'ngram', 'indexer', 'mtp')

def is_frozen(name: str) -> bool:
    return any(name.startswith(p) for p in FROZEN)
```

Do not retarget locked SOTA from this recipe.
