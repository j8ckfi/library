---
id: recipe:opengcua
type: recipe
title: 'Open generalist CUA stack'
method: method:opengcua
task: task:computer-use-agent
target_hardware: 'Paper: eight models on OSWorld-v2; real macOS harness'
framework: PyTorch
repo_url: https://github.com/Tongyi-MAI/OpenGCUA
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- opengcua
---

# Open generalist CUA stack

## Hardware & Environment Setup
- Official: `https://github.com/Tongyi-MAI/OpenGCUA`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def interface_choice(needs_code: bool) -> str:
    return "code" if needs_code else "gui"
```

Do not retarget locked SOTA from this recipe.

