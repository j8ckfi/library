---
id: recipe:softwaregym
type: recipe
title: SoftwareGym Synthesized GUI Env Factory
method: method:softwaregym
task: task:hybrid-computer-use-agent-rl
target_hardware: CUA training host plus synthesized GUI sandboxes
framework: GUI env factory + CUA trainer
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- softwaregym
---

# SoftwareGym Synthesized GUI Env Factory

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def env_reliable(gui_pass_rate: float, min_pass: float = 0.9) -> bool:
    if not 0.0 <= gui_pass_rate <= 1.0:
        raise ValueError("pass rate must be in [0, 1]")
    return gui_pass_rate >= min_pass
```

Repair until the GUI checker passes. Do not retarget Claude computer-use.
