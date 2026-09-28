---
id: recipe:mopd-router
type: recipe
title: "MOPD-Router ExpertAlign Token Routing"
method: method:mopd-router
task: task:student-distillation
target_hardware: "multi-GPU verl box; paper: Qwen3-1.7B/4B students, three Qwen3-4B teachers, prompt 2048 / response 16384"
framework: "PyTorch / verl (G-OPD stack) / vLLM"
repo_url: "https://github.com/TURLEing/MOPD-Router"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - mopd-router
  - distillation
  - multi-teacher
  - on-policy
---

# MOPD-Router ExpertAlign Token Routing

## Hardware & Environment Setup
- Official: `https://github.com/TURLEing/MOPD-Router`. `verl/`, `benchmarks/`, `run.sh`. `code_status: released`.
- Multi-teacher default stays Open-MOPD. Single-teacher stays OPD.

```bash
git clone https://github.com/TURLEing/MOPD-Router.git && cd MOPD-Router
cd verl
USE_MEGATRON=0 bash scripts/install_vllm_sglang_mcore.sh
python -m pip install -e '.[vllm,math]'
cd ..
export MATH_TEACHER_MODEL=Keven16/Qwen3-4B-Non-Thinking-RL-Math-Step500
export CODE_TEACHER_MODEL=Keven16/Qwen3-4B-Non-Thinking-RL-Code-Step300
export INSTRUCT_FOLLOWING_TEACHER_MODEL=TianzeTurle/Qwen3-4B-RL-IF-Step500
TEACHER_SIGNAL_AGGREGATION=delta DELTA_ROUTER_WEIGHTING=cosine bash run.sh
```

## Quickstart Implementation

```python
from __future__ import annotations

from math import sqrt


def _dot(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must be aligned")
    return sum(x * y for x, y in zip(a, b))


def _norm(a: list[float]) -> float:
    return sqrt(_dot(a, a))


def expert_align_weights(
    expertise: list[list[float]],
    teaching: list[list[float]],
    delta: float = 1e-6,
) -> list[float]:
    n = len(expertise)
    if n == 0 or n != len(teaching):
        raise ValueError("expertise and teaching must be non-empty and aligned")
    scores = [0.0] * n
    retained: list[int] = []
    for i, (e_vec, d_vec) in enumerate(zip(expertise, teaching)):
        if len(e_vec) != len(d_vec) or not e_vec:
            raise ValueError("per-teacher vectors must be non-empty and same width")
        align = _dot(e_vec, d_vec)
        e_n = _norm(e_vec)
        d_n = _norm(d_vec)
        if e_n < 1e-12 or d_n < 1e-12:
            cosine = 0.0
        else:
            cosine = max(align / (e_n * d_n), 0.0)
        scores[i] = cosine
        if align > delta:
            retained.append(i)
    if not retained:
        return [0.0] * n
    mass = sum(scores[i] for i in retained)
    if mass <= 0.0:
        w = 1.0 / len(retained)
        return [w if i in retained else 0.0 for i in range(n)]
    return [scores[i] / mass if i in retained else 0.0 for i in range(n)]
```

Build `expertise` as \(\log p^i-\log p^{\mathrm{base}}\) and `teaching` as \(\log p^i-\log p^S\) on the student's top-16. Weight per-teacher sampled-token advantages with the returned \(w_{i,t}\). Empty retained set skips the token.

## Critical Hyperparameters & Tuning Advice
- Paper: 3 epochs, batch 1024, LR \(1\times 10^{-5}\) constant, PPO clip 0.2, KL off, thinking off, ExpertAlign \(k=16\), \(\delta=10^{-6}\).
- Same-size: `STUDENT_MODEL=Qwen/Qwen3-4B`. Mean baseline: `TEACHER_SIGNAL_AGGREGATION=mean`. Domain hard-route: `ENTROPY_AWARE_ROUTER=false` plus `extra_info.opd_teacher`.
- Do not retarget Open-MOPD from the +5.88 / +3.95 overall-Avg. lifts.
