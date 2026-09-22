---
id: recipe:critical-state-rl
type: recipe
title: "Critical-State RL Occurrence Diagnostic"
method: method:critical-state-rl
task: task:agentic-async-rl
target_hardware: "rollout box able to nest-sample actions then resample reward-only continuations at a frozen prefix"
framework: "PyTorch GRPO/bandit host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - critical-state-rl
  - agentic
  - tool-use
---

# Critical-State RL Occurrence Diagnostic

## Hardware & Environment Setup
- No official GitHub as of 2026-09-22 (`arXiv:2609.24985`). `repo_url: none found`. `code_status: none`. Same note as Cal-OPD.
- Async default stays SAO. AppWorld coverage stays CANOPY. Pass@1 stays CISPO. Folding stays FoldGRPO.

## Quickstart Implementation

```python
from __future__ import annotations

from statistics import mean, pvariance


def action_dependent_variance(
    action_means: list[float],
    continuation_vars: list[float],
    n_cont: int,
) -> float:
    """Finite-sampling-corrected Var_a Q(x,a). continuation_vars are per-action sample vars."""
    if len(action_means) < 2:
        return 0.0
    raw = pvariance(action_means)
    noise = mean(continuation_vars) / max(n_cont, 1)
    return max(0.0, raw - noise)


def select_occurrence(scores: dict[str, float]) -> str:
    return max(scores, key=scores.get)
```

Screen candidates for action-sufficiency and reference-policy headroom before ranking on corrected action variance. Train a contextual bandit only on the selected call's tokens.

## Critical Hyperparameters & Tuning Advice
- Re-run the diagnostic per model and task. Gemma miss_func selects recovery; Nemotron miss_func selects the decision before the tool appears.
- Do not treat a mixed-reward group as trainable. Nested resampling can show zero action variance.
- Targeted SFT at the selected turn is not a substitute: miss_func recovery SFT over-fires the tool in the paper.
