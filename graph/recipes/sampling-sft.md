---
id: recipe:sampling-sft
type: recipe
title: "Sampling SFT Projection Sampling"
method: method:sampling-sft
task: task:math-code-rl-dense
target_hardware: "H100/H200 SFT box plus base-model likelihoods for MH; paper: Qwen2.5-3B math, Qwen2.5-7B-Instruct chemistry/medical"
framework: "PyTorch SFT host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - sampling-sft
  - sft
  - mcmc
---

# Sampling SFT Projection Sampling

## Hardware & Environment Setup
- No official training GitHub as of 2026-10-03 (`arXiv:2610.02140`). `repo_url: none found`. `code_status: none`. Project: `https://aakaran.github.io/finetuning_with_sampling/`.
- Pass@1 stays CISPO. Privileged-teacher OPSD stays VISTA. Vanilla SFT is not this recipe.

## Quickstart Implementation

```python
from __future__ import annotations

import math
import random


def mh_accept(logp_new: float, logp_old: float, rng: random.Random) -> bool:
    if not math.isfinite(logp_new) or not math.isfinite(logp_old):
        raise ValueError("log-probabilities must be finite")
    if logp_new >= logp_old:
        return True
    return rng.random() < math.exp(logp_new - logp_old)


def project_trace(trace: str, logp_fn, is_correct, rng: random.Random, steps: int = 10) -> str:
    if steps < 1:
        raise ValueError("need at least one MCMC step")
    current = trace
    current_logp = logp_fn(current)
    for _ in range(steps):
        proposal = logp_fn.propose(current)
        if not is_correct(proposal):
            continue
        new_logp = logp_fn(proposal)
        if mh_accept(new_logp, current_logp, rng):
            current = proposal
            current_logp = new_logp
    return current
```

Paper defaults: B=32 blocks, T=1856, N_MCMC=10. After projection, run ordinary SFT. Optional second stage: GRPO on the sampling-SFT checkpoint (Table 1 Sampling SFT+RL).

## Critical Hyperparameters & Tuning Advice
- SFT sweep in the paper: epochs {1,2} (medical extends to {1,2,4,6}), LR {5e-5, 1e-5, 5e-6}, batch {16,32,64}, AdamW cosine, grad clip 1.
- Do not SFT a Qwen-boosted set into Olmo. The chain is model-native.
- Vanilla SFT 0.243 vs GRPO 0.457 on MATH(3,4,5) is why this is not “SFT beats GRPO.”
