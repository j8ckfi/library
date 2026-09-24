---
id: recipe:jitmem
type: recipe
title: "JitMem Read-Time Curator"
method: method:jitmem
task: task:agent-memory
target_hardware: "frozen executor plus a GRPO curator; paper: Qwen3-8B / Gemini-2.5-Pro executors"
framework: "GRPO curator over a raw-trajectory bank"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - jitmem
  - agent-memory
---

# JitMem Read-Time Curator

## Hardware & Environment Setup
- No official GitHub as of 2026-09-24 (`arXiv:2609.27334`). `repo_url: none found`. `code_status: none`.
- Playbook default stays ACE. Repository skills stay Code2Skill. System-One control stays Jev-Mem.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trajectory:
    task: str
    steps: list[str]
    success: bool


@dataclass
class MemoryBank:
    traces: list[Trajectory] = field(default_factory=list)

    def retrieve(self, task: str, k: int = 4) -> list[Trajectory]:
        scored = sorted(
            self.traces,
            key=lambda t: sum(w in t.task.lower() for w in task.lower().split()),
            reverse=True,
        )
        return scored[:k]

    def update(self, traj: Trajectory) -> None:
        if traj.success:
            self.traces.append(traj)


def curator_advantage(rewards: list[float]) -> list[float]:
    if not rewards:
        return []
    mean = sum(rewards) / len(rewards)
    return [r - mean for r in rewards]
```

Keep raw traces. Retrieve, curate for the current task, execute, then store only quality-gated successes. Train the curator with group-relative advantages on immediate task reward.

## Critical Hyperparameters & Tuning Advice
- Do not distill at write time. The same trace must be allowed to yield different payloads.
- Freeze the executor. Immediate reward is the point of read-time curation.
- Untrained read-time curation is already a strong ablation; train only if that baseline is in place.
