---
id: recipe:aide2
type: recipe
title: "AIDE2 Recursive Harness RSI"
method: method:aide2
task: task:agent-harness-runtime
target_hardware: "outer-loop proposer plus inner-loop eval fleet at a fixed per-task dollar budget"
framework: "research-agent tree search (AIDE-style)"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - aide2
  - rsi
  - agent-harness
---

# AIDE2 Recursive Harness RSI

## Hardware & Environment Setup
- No public GitHub as of 2026-09-23 (`arXiv:2609.26457`). `repo_url: none found`. `code_status: none`. Authors Weco AI.
- Production kernel stays omp². Regularized frozen-backbone search stays RRSI. Routing weight post-train stays NeoHorse-1. Harness-behavior SFT stays Harness-Zero.

## Quickstart Implementation

```python
from __future__ import annotations


def accept_rewrite(candidate_grade: float, incumbent_grade: float) -> bool:
    """Keep the rewrite only if private held-out grade improves."""
    return candidate_grade > incumbent_grade


def rsi_step(
    incumbent: str,
    proposed: str,
    grade_fn,
) -> str:
    g_inc = grade_fn(incumbent)
    g_new = grade_fn(proposed)
    if accept_rewrite(g_new, g_inc):
        return proposed
    return incumbent
```

Grade every candidate under the same per-task budget. Inner-loop agents see public task rewards; the outer loop selects on private \(g(a)\). The accepted codebase is the next incumbent.

## Critical Hyperparameters & Tuning Advice
- Decouple \(r^{\mathrm{pub}}\) from \(g\). If the inner agent can see the selection grade, it will optimize the proxy.
- Paper outer loop: Claude Opus 4.7. Inner-loop eval: Gemini 3 Flash. Do not spend extra budget to fake a gain.
- Seven accepted rewrites over 100 nodes is the measured sustained trend, not a one-off patch.
