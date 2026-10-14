---
id: recipe:monarch-muon
type: recipe
title: Monarch-Muon
method: method:monarch-muon
task: task:llm-pretraining-optimization
target_hardware: 'Paper: 257M / 1B MoE quality; 6.89B H100 systems'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- monarch-muon
---

# Monarch-Muon

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def monarch_blocks_ok(n_blocks: int) -> bool:
    if n_blocks < 1:
        raise ValueError("need at least one Monarch block")
    return n_blocks in (1, 2)
```

Do not retarget locked SOTA from this recipe.
