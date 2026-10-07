---
id: recipe:adam-beta-cubic
type: recipe
title: "Adam Shared-Beta Cubic Rule"
method: method:adam-beta-cubic
task: task:llm-pretraining-optimization
target_hardware: "Adam / AdamW box; paper: 11 workloads, 200-update pilot"
framework: "PyTorch; official cubic-rule repo"
repo_url: "https://github.com/AlbertoFdezHdez/Adam_beta_rule_cubic"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - adam-beta-cubic
---

# Adam Shared-Beta Cubic Rule

## Hardware & Environment Setup
- Official: `https://github.com/AlbertoFdezHdez/Adam_beta_rule_cubic`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def cubic_beta(probe: float, a: float, b: float, c: float, d: float) -> float:
    beta = ((a * probe + b) * probe + c) * probe + d
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must land in (0, 1)")
    return beta
```

Official: AlbertoFdezHdez/Adam_beta_rule_cubic. 200-update pilot + 16 probes at 4 checkpoints. Do not retarget Muon2.
