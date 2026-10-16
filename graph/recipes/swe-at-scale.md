---
id: recipe:swe-at-scale
type: recipe
title: 'Issue synthesis from historical fixes'
method: method:swe-at-scale
task: task:coding-agent-rl-environment-construction
target_hardware: 'Paper: diversity up to 200 generations per file'
framework: PyTorch
repo_url: https://github.com/cslsolow/SWE-at-scale
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- swe-at-scale
---

# Issue synthesis from historical fixes

## Hardware & Environment Setup
- Official: `https://github.com/cslsolow/SWE-at-scale`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def invert_fix(before: str, after: str) -> str:
    if not before or not after:
        raise ValueError("both sides of the fix are required")
    return before
```

Do not retarget locked SOTA from this recipe.

