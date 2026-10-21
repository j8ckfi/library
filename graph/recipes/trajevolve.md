---
id: recipe:trajevolve
type: recipe
title: 'Hindsight trajectory evolution plus necessity labels'
method: method:trajevolve
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: two long-horizon datasets; NeurIPS 2026'
framework: PyTorch
repo_url: https://github.com/wenyiwy99/TrajEvolve
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- trajevolve
---

# Hindsight trajectory evolution plus necessity labels

## Hardware & Environment Setup
- Official: `https://github.com/wenyiwy99/TrajEvolve`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def necessary(with_step: bool, without_step: bool) -> int:
    return int(with_step and not without_step)
```

Do not retarget locked SOTA from this recipe.
