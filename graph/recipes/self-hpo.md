---
id: recipe:self-hpo
type: recipe
title: 'Alternating harness-policy optimization'
method: method:self-hpo
task: task:agent-harness-runtime
target_hardware: 'Paper: Qwen3.5-35B-A3B coding agents'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- self-hpo
---

# Alternating harness-policy optimization

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def next_stage(stage: str) -> str:
    if stage == 'H':
        return 'P'
    if stage == 'P':
        return 'H'
    raise ValueError(stage)
```

Do not retarget locked SOTA from this recipe.
