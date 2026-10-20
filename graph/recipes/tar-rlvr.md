---
id: recipe:tar-rlvr
type: recipe
title: 'Targeted adaptive replay for RLVR diversity'
method: method:tar-rlvr
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen2.5 math RLVR, six benches'
framework: PyTorch
repo_url: https://github.com/wenzhilics/tar
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- tar-rlvr
---

# Targeted adaptive replay for RLVR diversity

## Hardware & Environment Setup
- Official: `https://github.com/wenzhilics/tar`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def should_replay(mode_count: int, on_policy_seen: int) -> bool:
    if mode_count < 0 or on_policy_seen < 0:
        raise ValueError('counts must be >= 0')
    return mode_count > 0 and on_policy_seen == 0
```

Do not retarget locked SOTA from this recipe.
