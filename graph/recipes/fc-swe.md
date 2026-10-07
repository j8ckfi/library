---
id: recipe:fc-swe
type: recipe
title: "FC-SWE Failure-Conditioned Recovery"
method: method:fc-swe
task: task:swe-agent-category-expert-rl
target_hardware: "SWE-agent RL box; paper: SWE-bench Verified 500, Qwen3.5-4B"
framework: "PyTorch SWE-agent RL host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - fc-swe
---

# FC-SWE Failure-Conditioned Recovery

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def recovery_context(failed_patch: str, verifier_feedback: str) -> str:
    if not failed_patch.strip():
        raise ValueError("failed patch is empty")
    if not verifier_feedback.strip():
        raise ValueError("verifier feedback is empty")
    return failed_patch + "\n" + verifier_feedback
```

Reuse failed patch + verifier feedback. 41.7 / 52.8 / 70.7 vs GRPO 38.9 / 48.5 / 67.3. Do not retarget Category-Aware SWE Experts.
