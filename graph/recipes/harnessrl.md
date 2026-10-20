---
id: recipe:harnessrl
type: recipe
title: 'Just-in-time rubric training harness'
method: method:harnessrl
task: task:agent-harness-runtime
target_hardware: 'Paper: Rubric-Mix-10k, Qwen3.5-4B/9B'
framework: PyTorch
repo_url: https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/HarnessRL
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- harnessrl
---

# Just-in-time rubric training harness

## Hardware & Environment Setup
- Official: `https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/HarnessRL`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def harness_tuple(prompt: str, guidance: str, criterion: str) -> tuple[str, str, str]:
    if not prompt or not criterion:
        raise ValueError('prompt and criterion required')
    return prompt, guidance, criterion
```

Do not retarget locked SOTA from this recipe.
