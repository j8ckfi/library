---
id: recipe:mcgpo
type: recipe
title: Matched-Context Group Policy Optimization
method: method:mcgpo
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Agent GPO host; paper: ALFWorld / WebShop'
framework: PyTorch GraphGPO-style host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mcgpo
---

# Matched-Context Group Policy Optimization

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def opposite_fold(candidate_fold: int, outcome_fold: int) -> bool:
    return candidate_fold != outcome_fold
```

Do not score a pair with its own terminal. Do not retarget CANOPY.
