---
id: recipe:dataflex-rl
type: recipe
title: "DataFlex-RL Uniform GRPO Note"
method: method:dataflex-rl
task: task:math-code-rl-dense
target_hardware: "same as host GRPO (paper: Qwen2.5-7B-Base, 12 seeds)"
framework: "PyTorch / host GRPO"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - dataflex-rl
  - rlvr
---

# DataFlex-RL Uniform GRPO Note

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Treat uniform GRPO as the accuracy control. Host Pass@1 stays CISPO.

## Quickstart Implementation

```python
def paired_delta_ci_excludes_zero(low: float, high: float) -> bool:
    """DataFlex-RL's bar: a data policy must exclude 0 in a paired 95% interval vs uniform."""
    return (low > 0.0) or (high < 0.0)
```

## Critical Hyperparameters & Tuning Advice
- Report a domain-balanced multi-bench average, not a math-only subset.
- 12 matched seeds in the paper's primary table. Do not claim a win from one seed.
