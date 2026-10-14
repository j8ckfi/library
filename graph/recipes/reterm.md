---
id: recipe:reterm
type: recipe
title: ReTerm recovery-fork GRPO
method: method:reterm
task: task:coding-agent-rl-environment-construction
target_hardware: 'Paper: Qwen3.5-9B ReTerm-GRPO'
framework: PyTorch
repo_url: https://github.com/twothsnd/ReTerm
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- reterm
---

# ReTerm recovery-fork GRPO

## Hardware & Environment Setup
- Official: `https://github.com/twothsnd/ReTerm`.
- `code_status: released` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def fork_from_failure(failed: bool, can_checkpoint: bool) -> bool:
    if not can_checkpoint:
        raise ValueError("need a checkpointable failure state")
    return failed
```

Do not retarget locked SOTA from this recipe.
