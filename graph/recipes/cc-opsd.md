---
id: recipe:cc-opsd
type: recipe
title: Critique-Conditioned Privileged OPSD
method: method:cc-opsd
task: task:privileged-teacher-opsd
target_hardware: Privileged OPSD host with a gold solution
framework: PyTorch OPSD host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cc-opsd
---

# Critique-Conditioned Privileged OPSD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def critique_then_score(critique: str, gold: str) -> str:
    if not critique.strip():
        raise ValueError("CC-OPSD requires a generated critique before scoring")
    if not gold.strip():
        raise ValueError("privileged gold is required")
    return critique
```

Search then score. Do not retarget VISTA.
