---
id: recipe:rc-opd
type: recipe
title: "RC-OPD Root-Cause Guided Distillation"
method: method:rc-opd
task: task:privileged-teacher-opsd
target_hardware: "OPSD box that can diagnose and continue failed traces; paper: Qwen3-1.7B/4B/8B Avg@4"
framework: "PyTorch"
repo_url: "https://github.com/Starrylay/RC-OPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - rc-opd
  - distillation
  - privileged-teacher
---

# RC-OPD Root-Cause Guided Distillation

## Hardware & Environment Setup
- Official: `https://github.com/Starrylay/RC-OPD`. `code_status: released`.
- Privileged-OPSD first hop stays VISTA.

```bash
git clone https://github.com/Starrylay/RC-OPD.git && cd RC-OPD
```

## Quickstart Implementation

```python
from __future__ import annotations


def split_error_prefix(flags: list[bool]) -> tuple[int, int]:
    if not flags:
        raise ValueError("need at least one stage flag (True=valid)")
    for i, ok in enumerate(flags):
        if not ok:
            return i, i
    raise ValueError("no error stage; skip RC-OPD and keep the verified trace")
```

Diagnose the first False stage as the Error Stage. Repair it into an Anchor Stage. Continue the student from that prefix. If the continuation verifies, distill Failure Reason & Goal on the error span and COT-to-Anchor on the valid prefix. Else retry until the repair budget, then fall back to reference-conditioned OPSD.

## Critical Hyperparameters & Tuning Advice
- Table 1 Avg@4 is 44.17 / 66.11 / 66.94 vs OPSD 40.28 / 62.50 / 63.33. Not a VISTA bake-off retarget.
