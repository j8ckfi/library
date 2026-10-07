---
id: recipe:triage
type: recipe
title: "TRIAGE Direction-Aware NVFP4 Rebalance"
method: method:triage
task: task:fp4-rl-train-rollout-alignment
target_hardware: "Native NVFP4 RL box; paper: Qwen3-4B / 30B-A3B, B300"
framework: "PyTorch NVFP4 RL host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - triage
---

# TRIAGE Direction-Aware NVFP4 Rebalance

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def amplifying_neg(advantage: float, gap: float) -> bool:
    return advantage < 0.0 and gap < 0.0
```

Rebalance segments where negative advantage and negative gap compound. Up to 2.3× rollout vs BF16. Dual-active with TRACE.
