---
id: recipe:nemo-dcr
type: recipe
title: "NeMo-DCR Delta-Compressed Refit"
method: method:nemo-dcr
task: task:frontier-rl-posttrain-stack
target_hardware: "Disaggregated agentic RL at large MoE / 1T; NVIDIA NeMo RL"
framework: "NeMo RL"
repo_url: "https://github.com/NVIDIA-NeMo/RL/pull/2444"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - nemo-dcr
---

# NeMo-DCR Delta-Compressed Refit

## Hardware & Environment Setup
- Official: `https://github.com/NVIDIA-NeMo/RL/pull/2444`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def changed_coords(prev, cur, atol: float = 0.0):
    if prev.shape != cur.shape:
        raise ValueError("weight shapes must match")
    return (prev - cur).abs() > atol
```

Ship only changed BF16 coords (~1%/step). Official: NVIDIA-NeMo/RL PR #2444. Do not retarget Miles.
