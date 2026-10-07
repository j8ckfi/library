---
id: recipe:privileged-context-drift
type: recipe
title: "Privileged Context Drift Diagnostic"
method: method:privileged-context-drift
task: task:privileged-teacher-opsd
target_hardware: "OPSD diagnostic; no trainer"
framework: "analysis only"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - privileged-context-drift
---

# Privileged Context Drift Diagnostic

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def content_vs_source_kl(kl_content: float, kl_source: float) -> float:
    if kl_source <= 0:
        raise ValueError("source KL must be positive")
    return kl_content / kl_source
```

Evidence card. Content (demo/feedback/rephrase) drives KL 5.1× more than source. Do not train from this node.
