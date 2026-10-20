---
id: recipe:framegrpo
type: recipe
title: 'Multi-frame video GRPO'
method: method:framegrpo
task: task:rl-video-mllm
target_hardware: 'Paper: seven video understanding/reasoning benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- framegrpo
---

# Multi-frame video GRPO

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def shared_frames_silent(n_unique_frame_sets: int) -> bool:
    if n_unique_frame_sets < 1:
        raise ValueError('need at least one frame set')
    return n_unique_frame_sets == 1
```

Do not retarget locked SOTA from this recipe.
