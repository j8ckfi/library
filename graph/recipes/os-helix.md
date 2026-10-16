---
id: recipe:os-helix
type: recipe
title: 'Native GUI plus code CUA'
method: method:os-helix
task: task:hybrid-computer-use-agent-rl
target_hardware: 'Paper: OS-Helix-27B / 35B-A3B'
framework: PyTorch
repo_url: https://github.com/os-copilot/OS-Helix
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- os-helix
---

# Native GUI plus code CUA

## Hardware & Environment Setup
- Official: `https://github.com/os-copilot/OS-Helix`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def step_is(logp_tokens: list[float]) -> float:
    if not logp_tokens:
        raise ValueError("action must have tokens")
    return sum(logp_tokens) / float(len(logp_tokens))
```

Do not retarget locked SOTA from this recipe.

