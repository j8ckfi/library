---
id: recipe:mintrl
type: recipe
title: "MInTRL Sparse Intervention RLVR"
method: method:mintrl
task: task:math-code-rl-dense
target_hardware: "Qwen3-1.7B/4B RLVR box plus a judge (paper: Qwen3-4B-Instruct-2507)"
framework: "PyTorch RLVR host (GRPO-family) with advantage regression"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - mintrl
  - rlvr
---

# MInTRL Sparse Intervention RLVR

## Hardware & Environment Setup
- No official GitHub as of 2026-09-14 (`arXiv:2609.12419`). `repo_url: none found`.
- Pass@1 algorithm stays CISPO. MoE/VL stays SAPO. Async stays SAO.
- Keep most tokens on-policy. Peak is at a small off-policy fraction.

## Quickstart Implementation

```python
from dataclasses import dataclass

import torch


@dataclass
class Chunk:
    tokens: list[int]
    source: str


def mintrl_rollout(student, judge, prompt: list[int], max_chunks: int) -> list[Chunk]:
    """Keep student chunks; on Revise, splice a short judge suffix and resume."""
    prefix: list[int] = []
    chunks: list[Chunk] = []
    for _ in range(max_chunks):
        cont = student.generate(prompt + prefix)
        decision, err_at = judge.review(prompt + prefix, cont)
        if decision == "keep":
            prefix.extend(cont)
            chunks.append(Chunk(cont, "student"))
        else:
            kept, rewritten = cont[:err_at], judge.rewrite(prompt + prefix + cont[:err_at])
            prefix.extend(kept + rewritten)
            chunks.append(Chunk(kept + rewritten, "judge"))
        if student.done(prefix):
            return chunks
    return chunks


def advantage_regression(logp: torch.Tensor, advantage: torch.Tensor) -> torch.Tensor:
    """Sequence-level regression; skip importance sampling on mixed-policy tokens."""
    return ((-logp.sum() - advantage.detach()) ** 2)
```

## Critical Hyperparameters & Tuning Advice
- Prefer MInTRL-Const when the student is weak. Sweep intervention rate; both 0% and dense edits lose.
- Self-intervention works; Proxy can beat Const in that ablation.
