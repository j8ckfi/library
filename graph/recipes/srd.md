---
id: recipe:srd
type: recipe
title: "SRD Hindsight-to-Foresight Distillation"
method: method:srd
task: task:math-code-rl-dense
target_hardware: "GRPO-family host; paper: RLVR groups that can go silent"
framework: "PyTorch RLVR host; official SRD"
repo_url: "https://github.com/SalesforceAIResearch/SRD"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - srd
---

# SRD Hindsight-to-Foresight Distillation

## Hardware & Environment Setup
- Official: `https://github.com/SalesforceAIResearch/SRD`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def silent_group(rewards) -> bool:
    if not rewards:
        raise ValueError("empty group")
    return max(rewards) == min(rewards)
```

When the group is silent, distill hindsight into foresight. Do not retarget CISPO.
