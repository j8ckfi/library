---
id: recipe:metacurate
type: recipe
title: 'Evolving SWE trajectory filters'
method: method:metacurate
task: task:instruct-sft-alignment
target_hardware: 'Paper: Nemotron v3 SWE SFT'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- metacurate
---

# Evolving SWE trajectory filters

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def revise_filter(agree: bool, rule: str) -> str:
    if agree:
        return rule
    if not rule:
        return 'keep-if-verified'
    return rule
```

Do not retarget locked SOTA from this recipe.
