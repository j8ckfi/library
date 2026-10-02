---
id: recipe:activesaddler
type: recipe
title: "ActiveSaddler Failure-Pattern Curriculum"
method: method:activesaddler
task: task:agent-harness-runtime
target_hardware: "offline harness optimizer with a fixed rollout budget; paper: GAIA2 / Terminal-Bench 2.0"
framework: "Python harness optimizer plus a non-stationary bandit over failure-pattern arms"
repo_url: "https://github.com/microsoft/AutoSaddler"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - activesaddler
  - agent-harness
  - curriculum
---

# ActiveSaddler Failure-Pattern Curriculum

## Hardware & Environment Setup
- Official: `https://github.com/microsoft/AutoSaddler`. `code_status: released`.
- Project: `https://autosaddler-projectpage.github.io/activesaddler/`.
- Kernel stays omp². Frozen-backbone RSI stays RRSI. Recursive rewrite stays AIDE2.

```bash
git clone https://github.com/microsoft/AutoSaddler.git && cd AutoSaddler
```

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Arm:
    pattern: str
    remaining: float
    visits: int = 0


@dataclass
class Curriculum:
    arms: dict[str, Arm] = field(default_factory=dict)
    explore_rate: float = 0.2

    def choose(self, unseen_available: bool, rng_u: float) -> str:
        if not 0.0 <= rng_u < 1.0:
            raise ValueError("rng_u must be in [0, 1)")
        if unseen_available and (not self.arms or rng_u < self.explore_rate):
            return "explore"
        if not self.arms:
            raise ValueError("no failure-pattern arms and no unseen scenarios")
        return max(self.arms.values(), key=lambda a: a.remaining).pattern

    def update(self, pattern: str, remaining: float) -> None:
        if remaining < 0.0:
            raise ValueError("remaining progress must be non-negative")
        arm = self.arms.get(pattern) or Arm(pattern=pattern, remaining=remaining)
        arm.remaining = remaining
        arm.visits += 1
        self.arms[pattern] = arm
```

Keep the harness-update operator \(\mathcal{O}\) unchanged. Cluster diagnosed traces into failure-pattern arms, not category labels and not one arm per scenario.

## Critical Hyperparameters & Tuning Advice
- Gains are vs the same optimizer with a frozen schedule. Do not cite +4.4 / +7.5 as beating omp².
- Does not update model weights.
