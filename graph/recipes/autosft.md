---
id: recipe:autosft
type: recipe
title: 'Multi-action SFT data research agents'
method: method:autosft
task: task:instruct-sft-alignment
target_hardware: 'Paper: retrain-from-base each round; IFEval / MBPP+'
framework: PyTorch
repo_url: https://github.com/Thinking-Space/AutoSFT
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- autosft
---

# Multi-action SFT data research agents

## Hardware & Environment Setup
- Official: `https://github.com/Thinking-Space/AutoSFT`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

ACTIONS = ("proportion", "prune", "repair", "replace", "synthesize")

def valid_action(action: str) -> str:
    if action not in ACTIONS:
        raise ValueError(f"unknown SFT data action: {action}")
    return action
```

Do not retarget locked SOTA from this recipe.

