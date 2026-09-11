---
id: recipe:harness-onpolicy-correction
type: recipe
title: "On-Policy Expert Turn Correction"
method: method:harness-onpolicy-correction
task: task:software-engineering-agent-harness
target_hardware: "LoRA-SFT on ~26B–30B MoE (paper: Qwen3-Coder-30B-A3B, Gemma-4-26B-A4B)"
framework: "PyTorch / PEFT LoRA on the student; expert is inference-only"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "peft"
tags:
  - recipe
  - agent-harness
  - on-policy
  - lora
---

# On-Policy Expert Turn Correction

## Hardware & Environment Setup
- No official GitHub as of 2026-09-11. Algorithm from arXiv:2609.09134.
- SWE harness default stays mini-SWE-agent. Stack stays Miles. RSI post-train stays NeoHorse-1.
- Do **not** LoRA-SFT on full expert trajectories after evolving a model-specific harness.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass
class Turn:
    role: str
    content: str


def first_failing_index(student_turns: list[Turn], checker) -> int:
    for i in range(len(student_turns)):
        if not checker(student_turns[: i + 1]):
            return i
    raise ValueError("no failing turn")


def on_policy_expert_example(
    student_turns: list[Turn],
    expert_rewrite: Turn,
    checker,
) -> list[Turn]:
    """Keep the student's prefix; replace only the failing turn with the expert rewrite."""
    k = first_failing_index(student_turns, checker)
    return student_turns[:k] + [expert_rewrite]
```

## Critical Hyperparameters & Tuning Advice
- Expert sees the student's rollout and rewrites one turn. Do not splice in the expert's full plan.
- Same LoRA-SFT *helps* under an unevolved harness; the regression is post-evolution.
