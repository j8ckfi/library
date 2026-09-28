---
id: recipe:dce-srcl
type: recipe
title: "DCE+SRCL Privileged Co-Evolution"
method: method:dce-srcl
task: task:privileged-teacher-opsd
target_hardware: "LoRA r=128 box matching a privileged-OPSD host; paper: Qwen3-1.7B/4B/8B/14B, 32K eval cap"
framework: "PyTorch privileged-OPSD host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - dce-srcl
  - distillation
  - privileged-teacher
  - opsd
---

# DCE+SRCL Privileged Co-Evolution

## Hardware & Environment Setup
- No official GitHub as of 2026-09-28 (`arXiv:2609.30652`). `repo_url: none found`. `code_status: none`.
- Privileged-OPSD first hop stays VISTA. Do not treat this snippet as a VISTA trainer.

## Quickstart Implementation

```python
from __future__ import annotations


def srcl_accept(
    original_len: int,
    rewrite_len: int,
    naturally_terminated: bool,
    structurally_valid: bool,
    answer_correct: bool,
) -> bool:
    if original_len <= 0 or rewrite_len <= 0:
        return False
    return (
        rewrite_len < original_len
        and naturally_terminated
        and structurally_valid
        and answer_correct
    )


def dce_srcl_loss(
    dce_kl: float,
    srcl_ce: float,
    accepted_tokens: int,
    lambda_g: float,
    lambda_s: float,
) -> float:
    if lambda_g < 0.0 or lambda_s < 0.0:
        raise ValueError("loss weights must be non-negative")
    guidance = lambda_g * dce_kl
    if accepted_tokens <= 0:
        return guidance
    return guidance + lambda_s * srcl_ce
```

Each round: sample a problem-only rollout, score prefixes with a detached gold-conditioned copy of the **current** checkpoint (stop-grad on the teacher), optionally rewrite without gold and keep via `srcl_accept`, then `dce_srcl_loss`. Copy \(\theta_{k+1}\) into both roles before the next round.

## Critical Hyperparameters & Tuning Advice
- Paper Qwen3: AdamW \(5\times 10^{-6}\), LoRA rank 128, \(\lambda_{\mathrm{DCE}}=5\times 10^{4}\), \(\lambda_{\mathrm{SRCL}}=25\) at 8B (12.5 / 35 / 25 at 14B / 4B / 1.7B).
- Forward KL is the main \(\Delta\). Every-round teacher refresh beat frozen, EMA, and periodic in the paper.
- Do not retarget VISTA from 65.97% vs their 30.35% OPSD. Bake on the library VISTA protocol first.
