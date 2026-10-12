---
id: recipe:state-opd
type: recipe
title: State-Grounded Multi-Turn OPD
method: method:state-opd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Multi-turn agent OPD host; paper: ALFWorld / ScienceWorld / WebShop'
framework: PyTorch agent OPD host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- state-opd
---

# State-Grounded Multi-Turn OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def high_entropy_state(response_entropy: float, threshold: float) -> bool:
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    return response_entropy >= threshold
```

Ground the teacher on the interaction state. Do not retarget CANOPY or OPD.
