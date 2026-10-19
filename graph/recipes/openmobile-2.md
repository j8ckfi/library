---
id: recipe:openmobile-2
type: recipe
title: 'Scalable mobile-agent environments'
method: method:openmobile-2
task: task:hybrid-computer-use-agent-rl
target_hardware: 'Paper: MobileGym++ / AndroidWorld / MobileWorld'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- openmobile-2
---

# Scalable mobile-agent environments

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def reward_done(success: bool) -> float:
    return 1.0 if success else 0.0
```

Do not retarget locked SOTA from this recipe.
