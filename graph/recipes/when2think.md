---
id: recipe:when2think
type: recipe
title: "When2Think IDAC Hybrid Reasoning"
method: method:when2think
task: task:math-code-rl-dense
target_hardware: "multi-GPU GRPO-family box for hybrid Think/NoThink math RLVR"
framework: "PyTorch / critic-free GRPO-family host"
repo_url: "https://github.com/JJunShim/When2Think"
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - when2think
  - rlvr
  - hybrid-reasoning
---

# When2Think IDAC Hybrid Reasoning

## Hardware & Environment Setup
- Claimed repo: `https://github.com/JJunShim/When2Think`. README was a stub (`# When2Think`) as of 2026-09-18. `code_status: partial`.
- Host Pass@1 algorithm stays CISPO. This recipe only shapes Think vs NoThink length.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RefStats:
    accuracy: float
    tokens: float


def idac_reward(
    correct: bool,
    tokens: int,
    mode: str,
    ref: RefStats,
    think_bonus: float = 0.1,
    length_coef: float = 0.05,
) -> float:
    """Shape verifier reward with offline accuracy/token references."""
    r = 1.0 if correct else 0.0
    easy = ref.accuracy >= 0.8
    if easy and mode == "think":
        r -= length_coef * max(tokens - ref.tokens, 0) / max(ref.tokens, 1)
    if (not easy) and mode == "think" and correct:
        r += think_bonus
    if (not easy) and mode == "nothink" and not correct:
        r -= think_bonus
    return r


def batch_zscore(advantages: list[float]) -> list[float]:
    n = len(advantages)
    if n == 0:
        return []
    mean = sum(advantages) / n
    var = sum((a - mean) ** 2 for a in advantages) / n
    std = var ** 0.5
    if std < 1e-8:
        return [0.0] * n
    return [(a - mean) / std for a in advantages]
```

## Critical Hyperparameters & Tuning Advice
- Build `RefStats` offline. Do not query a live reference model inside the step.
- Keep the CISPO/GRPO surrogate. IDAC is the reward, not a new clip.
- If almost every prompt is hard, NoThink never wins and you have paid for a router that never routes.
