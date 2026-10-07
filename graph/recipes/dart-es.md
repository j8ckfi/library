---
id: recipe:dart-es
type: recipe
title: "DART-ES Difficulty Reweight and Replay"
method: method:dart-es
task: task:passk-reasoning-coverage
target_hardware: "ES LLM fine-tune box; official DART-ES"
framework: "PyTorch ES host; official DART-ES"
repo_url: "https://github.com/szs777/DART-ES-Code"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - dart-es
---

# DART-ES Difficulty Reweight and Replay

## Hardware & Environment Setup
- Official: `https://github.com/szs777/DART-ES-Code`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def difficulty_weight(pass_rate: float, floor: float = 0.05) -> float:
    if not 0.0 <= pass_rate <= 1.0:
        raise ValueError("pass_rate must be in [0, 1]")
    return 1.0 / max(pass_rate, floor)
```

Official: szs777/DART-ES-Code. Reweight hard prompts and replay them. Do not retarget ES-reasoning.
