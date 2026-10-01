---
id: recipe:oasis
type: recipe
title: "OASIS Verified On-Policy Scaffolds"
method: method:oasis
task: task:privileged-teacher-opsd
target_hardware: "OPSD box that can sample K rollouts per problem; paper: Qwen3-1.7B/4B/8B"
framework: "PyTorch OPSD host plus a final-answer verifier"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - oasis
  - distillation
  - self-distillation
---

# OASIS Verified On-Policy Scaffolds

## Hardware & Environment Setup
- No official GitHub as of 2026-10-01 (`arXiv:2609.37915`). `repo_url: none found`. `code_status: none`.
- Privileged-OPSD first hop stays VISTA. Unlabeled math stays u-OPSD.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Rollout:
    tokens: list[int]
    correct: bool


def oasis_pair(rollouts: list[Rollout]) -> tuple[Rollout, Rollout] | None:
    verified = [r for r in rollouts if r.correct and r.tokens]
    if not verified:
        return None
    scaffold = min(verified, key=lambda r: len(r.tokens))
    others = [r for r in rollouts if r is not scaffold and r.tokens]
    if not others:
        return None
    context = next((r for r in others if not r.correct), others[0])
    return scaffold, context
```

Apply the OPSD loss along `scaffold` with teacher context `context`. Skip problems with no verified rollout. Do not condition on a written gold solution.

## Critical Hyperparameters & Tuning Advice
- \(K\) rollouts per problem. Extra generation vs vanilla OPSD is expected.
- Shortest verified scaffold is the paper default.
