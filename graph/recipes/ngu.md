---
id: recipe:ngu
type: recipe
title: "Never Give Up Adaptive Sampling"
method: method:ngu
task: task:math-code-rl-dense
target_hardware: "math: ~8x H100 for Deepscaler-scale runs (~120 H100 hours compute-matched); code: 2x8 H100 Manufactoria (~28 hours / 3000 steps)"
framework: "PyTorch / Deepspeed + vLLM async GRPO host"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
  - "vllm"
tags:
  - recipe
  - ngu
  - rlvr
  - adaptive-sampling
---

# Never Give Up Adaptive Sampling

## Hardware & Environment Setup
- No verified GitHub as of 2026-09-16. Paper claims `https://github.com/mnoukhov/never-give-up` (HTTP 404). Blog: `https://mnoukhov.github.io/posts/ngu`. `repo_url: none found`.
- Plug into an existing async GRPO-family loop. Host Pass@1 algorithm stays CISPO. MoE/VL stays SAPO. Async tool stragglers stay SAO.
- Deepscaler paper HPs (Qwen3-4B-Base): KL $\beta=0$, lr $1\times10^{-6}$, $K=16$, $N=8$, async steps 4, clip-higher 0.272, response 8192. NGU $p\in\{0.5,0.75,0.875\}$. GSM8k / Manufactoria used $p=0.95$.

## Quickstart Implementation

```python
from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass
class Sample:
    completion: object
    reward: float
    age: int = 0


@dataclass
class PromptState:
    samples: list[Sample] = field(default_factory=list)
    count: int = 0
    baseline: float = 0.0


def ngu_on_group(
    state: PromptState | None,
    new_samples: list[Sample],
    p_ngu: float,
    max_age: int = 4,
) -> tuple[str, PromptState | None, list[Sample], float]:
    """Return action in {drop, train, retry} plus buffer and GRPO baseline."""
    k = len(new_samples)
    rbar = sum(s.reward for s in new_samples) / max(k, 1)
    kept: list[Sample] = list(new_samples)
    count = k
    if state is not None:
        rbar = (state.baseline * state.count + rbar * k) / (state.count + k)
        count = state.count + k
        kept.extend(s for s in state.samples if s.age <= max_age)
    rewards = [s.reward for s in new_samples]
    if rewards and all(r == 1.0 for r in rewards):
        return "drop", None, kept, rbar
    if any(s.reward > rbar for s in new_samples):
        return "train", None, kept, rbar
    if random.random() < p_ngu:
        nxt = PromptState(samples=kept, count=count, baseline=rbar)
        return "retry", nxt, kept, rbar
    return "drop", None, kept, rbar


def age_samples(samples: list[Sample]) -> None:
    for sample in samples:
        sample.age += 1


def anchor_positive_advantages(rewards: list[float], baseline: float) -> list[float]:
    """Keep positive advantages; rescale remaining negatives so advantages sum to 0."""
    adv = [r - baseline for r in rewards]
    pos = [a for a in adv if a > 0]
    neg_idx = [i for i, a in enumerate(adv) if a <= 0]
    if not pos or not neg_idx:
        return adv
    n_pos, n_neg = len(pos), len(neg_idx)
    target = (n_pos / n_neg) * (1.0 - baseline)
    for i in neg_idx:
        adv[i] = -target
    return adv
```

## Critical Hyperparameters & Tuning Advice
- Start with small $K$ (paper: 4 on GSM8k, 16 on Deepscaler) and $p_{\mathrm{NGU}}$ so expected $K/(1-p)$ covers the hard tail. Raising $p$ trades easy-subset for hard-subset, like raising $K$, without oversampling easy failures as badly.
- Filter loss tokens older than $T=4$ steps. Use the full history, including stale negatives, for the GRPO mean; rescale remaining negatives rather than downsampling to 1:1.
- Do not change the CISPO/SAPO/GRPO loss. If the pool is almost all pass@k=0, NGU will spin on retries; give-up probability $1-p$ exists for that.
