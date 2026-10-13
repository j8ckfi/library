---
id: recipe:replayssm
type: recipe
title: ReplaySSM SSM Input Cache
method: method:replayssm
task: task:linear-time-sequence-modeling
target_hardware: vLLM Mamba-2 / Gated DeltaNet; paper batch 256 decode
framework: vLLM; official ReplaySSM
repo_url: https://github.com/Johnny-Liou/ReplaySSM
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- replayssm
---

# ReplaySSM SSM Input Cache

## Hardware & Environment Setup
- Official: `https://github.com/Johnny-Liou/ReplaySSM`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def replay_ok(checkpoint_ok: bool, buf_len: int) -> bool:
    if not checkpoint_ok or buf_len < 1:
        raise ValueError("need a checkpoint and a nonempty input buffer")
    return True
```

Cache inputs, not state. Do not retarget Mamba-2.
