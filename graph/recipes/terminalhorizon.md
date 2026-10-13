---
id: recipe:terminalhorizon
type: recipe
title: TerminalHorizon Terminal Data Engine
method: method:terminalhorizon
task: task:coding-agent-rl-environment-construction
target_hardware: 'Paper: SFT Qwen3.5-27B on 2,852 terminal trajectories'
framework: PyTorch SFT; project page only
repo_url: https://zs1314.github.io/TerminalHorizon
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- terminalhorizon
---

# TerminalHorizon Terminal Data Engine

## Hardware & Environment Setup
- Project: `https://zs1314.github.io/TerminalHorizon`.
- `code_status: none` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def rebuild_if_precompleted(done: bool) -> str:
    if done:
        return "rebuild"
    return "keep"
```

Detect pre-completed work before logging a trajectory. Do not retarget CodeMidas.
