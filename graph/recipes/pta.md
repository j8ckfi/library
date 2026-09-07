---
id: recipe:pta
type: recipe
title: "PTA Teacher-Committed Tool Rollout Recipe"
method: method:pta
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (32B teacher + 1.7B/2B student, paper: veRL + SGLang)"
framework: "PyTorch / veRL / SGLang"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
  - "sglang>=0.4.0"
tags:
  - recipe
  - pta
  - distillation
  - tool-use
---

# PTA Teacher-Committed Tool Rollout Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-07. Paper inserts teacher verification into veRL + SGLang's chunk-level generation loop.
- Retrieval: Qwen3-1.7B student / Qwen3-32B teacher, prompt 8192, response 16384, batch 32, ≤15 turns, ≤256 chunks/sample, 5 epochs.
- Perception: Qwen3-VL-2B-Thinking / Qwen3-VL-32B-Thinking, prompt=response 8192, batch 32, ≤128 chunks/sample, 1 epoch.
- Host text distill without tools stays `method:opd`. Downstream labeled math RLVR stays CISPO. Async tool RL stays SAO.

## Quickstart Implementation

```python
from typing import Callable


def verify_chunk(teacher_topk: set[int], proposed: list[int], teacher_greedy: list[int]) -> list[int]:
    """Keep a student chunk iff every token is in the teacher's top-K; else teacher greedy."""
    if all(tok in teacher_topk for tok in proposed):
        return proposed
    return teacher_greedy[: len(proposed)]


def pta_rollout(
    propose_chunk: Callable[[list[int], list[int]], list[int]],
    verify: Callable[[list[int], list[int]], list[int]],
    parse_tool: Callable[[list[int]], object | None],
    env_step: Callable[[object], list[int]],
    is_final: Callable[[list[int]], bool],
    is_turn_done: Callable[[list[int]], bool],
    token_budget: int,
) -> list[int]:
    """Student-induced, teacher-committed trajectory. Tools run only after a verified turn."""
    tau: list[int] = []
    while len(tau) < token_budget:
        pending: list[int] = []
        while not is_turn_done(pending):
            proposed = propose_chunk(tau, pending)
            pending.extend(verify(tau, proposed))
        tau.extend(pending)
        call = parse_tool(pending)
        if call is not None:
            tau.extend(env_step(call))
        elif is_final(pending):
            break
    return tau
```

## Critical Hyperparameters & Tuning Advice
- Distill KL only on committed assistant tokens. Do not supervise observations.
- Do not skip in-span tool-call replacement. Buffering alone is not the method.
- Persistent lookahead: treat verified chunks as resumable units; carry unfinished samples across student updates under the **same** teacher. Table 5: +24% throughput vs synchronous.
- After PTA, run the environment's native RL (Search-R1 / DeepEyes) with unrestricted student rollouts. Do not keep the teacher on the tool path at RL time.
