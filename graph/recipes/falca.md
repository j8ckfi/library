---
id: recipe:falca
type: recipe
title: 'Falsification-aware hierarchical search RL'
method: method:falca
task: task:web-search-agent-rl
target_hardware: 'Paper: five search benchmarks'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- falca
---

# Falsification-aware hierarchical search RL

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def stage_credit(stage_adv, trans_adv, act_adv):
    return stage_adv + trans_adv + act_adv
```

Do not retarget locked SOTA from this recipe.
