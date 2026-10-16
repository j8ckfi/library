---
id: recipe:waypoint-opd
type: recipe
title: 'Gated endpoint policy-shift OPD'
method: method:waypoint-opd
task: task:student-distillation
target_hardware: 'Paper: Qwen3-4B RL teacher; Qwen3-8B/14B/30B-A3B students'
framework: PyTorch
repo_url: https://github.com/hhhbxloveai/WaypointOPD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- waypoint-opd
---

# Gated endpoint policy-shift OPD

## Hardware & Environment Setup
- Official: `https://github.com/hhhbxloveai/WaypointOPD`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def waypoint_gate(early_shift: float, late_shift: float) -> float:
    if early_shift == 0.0 and late_shift == 0.0:
        return 0.0
    return max(0.0, early_shift * late_shift)
```

Do not retarget locked SOTA from this recipe.

