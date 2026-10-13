---
id: recipe:d2r
type: recipe
title: D2R Imagination Rehearsal Steering
method: method:d2r
task: task:continuous-control-world-model
target_hardware: 'Paper: CALVIN 8-task frozen-policy steering'
framework: PyTorch control RL; no public trainer
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- d2r
---

# D2R Imagination Rehearsal Steering

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def freeze_policy(train_policy: bool) -> bool:
    if train_policy:
        raise ValueError("D2R keeps the generalist policy frozen")
    return True
```

Rehearse in the world model. Do not retarget EfficientTDMPC.
