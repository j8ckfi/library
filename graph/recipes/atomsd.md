---
id: recipe:atomsd
type: recipe
title: 'Procedural-atom self-distill for agents'
method: method:atomsd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: LLM agent tasks vs reward and distillation baselines'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- atomsd
---

# Procedural-atom self-distill for agents

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def atom_keys() -> tuple[str, ...]:
    return ('intent', 'when', 'do', 'avoid')
```

Do not retarget locked SOTA from this recipe.
