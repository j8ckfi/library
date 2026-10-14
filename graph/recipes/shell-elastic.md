---
id: recipe:shell-elastic
type: recipe
title: ShellElastic nested-width supernet
method: method:shell-elastic
task: task:llm-pretraining-optimization
target_hardware: 'Paper: nested widths 119M–1.69B'
framework: PyTorch
repo_url: https://github.com/jincan333/ShellElastic
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- shell-elastic
---

# ShellElastic nested-width supernet

## Hardware & Environment Setup
- Official: `https://github.com/jincan333/ShellElastic`.
- `code_status: released` as of 2026-10-14.

- HF Daily 2026-10-14.

## Quickstart Implementation

```python
from __future__ import annotations

def nested_widths_ok(widths: list[int]) -> bool:
    if not widths or any(w <= 0 for w in widths):
        raise ValueError("widths must be positive")
    return widths == sorted(widths)
```

Do not retarget locked SOTA from this recipe.
