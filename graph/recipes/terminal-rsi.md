---
id: recipe:terminal-rsi
type: recipe
title: 'RSR plus RPR terminal-agent RSI'
method: method:terminal-rsi
task: task:agent-harness-runtime
target_hardware: 'Paper: Qwen3.8-27B five-stage RSR/RPR'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- terminal-rsi
---

# RSR plus RPR terminal-agent RSI

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def spr(success: bool, partial: float) -> float:
    if partial < 0.0 or partial > 1.0:
        raise ValueError("partial must be in [0, 1]")
    return 1.0 if success else 0.5 * partial
```

Do not retarget locked SOTA from this recipe.

