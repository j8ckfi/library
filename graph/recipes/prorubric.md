---
id: recipe:prorubric
type: recipe
title: ProRubric protocol-level grouping
method: method:prorubric
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: HealthBench 4B/8B rubric RL'
framework: PyTorch
repo_url: https://github.com/Estrellajer/ProRubric
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- prorubric
---

# ProRubric protocol-level grouping

## Hardware & Environment Setup
- Official: `https://github.com/Estrellajer/ProRubric`.
- `code_status: released` as of 2026-10-14.

- HF Daily 2026-10-14.

## Quickstart Implementation

```python
from __future__ import annotations

def protocol_holds(criteria: list[bool]) -> bool:
    if not criteria:
        raise ValueError("empty protocol")
    return all(criteria)
```

Do not retarget locked SOTA from this recipe.
