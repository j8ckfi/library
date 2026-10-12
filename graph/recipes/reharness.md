---
id: recipe:reharness
type: recipe
title: ReHarness Recurrent Continual-Learning Harness
method: method:reharness
task: task:agent-continual-learning
target_hardware: Streaming agent host with a textual harness
framework: agent harness (text state)
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- reharness
---

# ReHarness Recurrent Continual-Learning Harness

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def revise_retrieved(retrieved: list[str], trajectory: str) -> list[str]:
    if not trajectory.strip():
        raise ValueError("ReHarness needs the instance trajectory as feedback")
    return list(retrieved)
```

Rewrite retrieved reflections after the turn. Do not retarget ACLArena.
