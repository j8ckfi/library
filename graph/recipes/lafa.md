---
id: recipe:lafa
type: recipe
title: 'Blockwise flow LM from an AR init'
method: method:lafa
task: task:continuous-diffusion-lm-pretrain
target_hardware: 'Paper: 0.5B / 7B / 8B, <30B tokens'
framework: PyTorch
repo_url: https://github.com/lafa-gh/large-flow-lms
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- lafa
---

# Blockwise flow LM from an AR init

## Hardware & Environment Setup
- Official: `https://github.com/lafa-gh/large-flow-lms`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def blockwise_flow_tokens(n_blocks: int, block: int) -> int:
    if n_blocks <= 0 or block <= 0:
        raise ValueError('sizes')
    return n_blocks * block
```

Do not retarget locked SOTA from this recipe.
