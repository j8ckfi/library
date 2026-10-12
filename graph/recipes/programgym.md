---
id: recipe:programgym
type: recipe
title: ProgramGym From-Scratch Reproduction Envs
method: method:programgym
task: task:coding-agent-rl-environment-construction
target_hardware: 'Long-horizon coding-agent host; paper: 1,648 sandboxes'
framework: sandbox env factory + agent SFT
repo_url: announced
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- programgym
---

# ProgramGym From-Scratch Reproduction Envs

## Hardware & Environment Setup
- Official: `announced`.
- `code_status: announced` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def env_ok(build_ok: bool, blackbox_pass: bool) -> bool:
    if not build_ok:
        raise ValueError("sandbox must build before tests")
    return blackbox_pass
```

Repair builds and tests in a loop. Do not retarget CodeMidas.
