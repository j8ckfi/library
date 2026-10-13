---
id: recipe:saver
type: recipe
title: SAVER Dense-to-Sparse Video RL
method: method:saver
task: task:rl-video-mllm
target_hardware: 'Paper: Qwen3.5 0.8B/2B/4B; 1,250 Time-R1 examples'
framework: PyTorch video RL; official SAVER
repo_url: https://github.com/lmsdss/SAVER
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- saver
---

# SAVER Dense-to-Sparse Video RL

## Hardware & Environment Setup
- Official: `https://github.com/lmsdss/SAVER`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def gate_reference(dense_r: float, sparse_r: float) -> bool:
    return dense_r > sparse_r
```

Infer on sparse frames only. Do not retarget OraRL.
