---
id: recipe:eg-grpo
type: recipe
title: 'Evidence-guided deep-search GRPO'
method: method:eg-grpo
task: task:web-search-agent-rl
target_hardware: 'Paper: BrowseComp / GAIA / xBenchDS'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- eg-grpo
---

# Evidence-guided deep-search GRPO

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def evidence_step_reward(new_claims: int) -> int:
    if new_claims < 0:
        raise ValueError('new_claims must be >= 0')
    return new_claims
```

Do not retarget locked SOTA from this recipe.
