---
id: recipe:ier-opd
type: recipe
title: "IER-OPD Sparse Token Selection"
method: method:ier-opd
task: task:student-distillation
target_hardware: "slime / SGLang box matching host sampled-token OPD (paper: 4 prompts × 16 responses)"
framework: "PyTorch / slime / TA-OPD"
repo_url: "https://github.com/BruceSheng1202/IER-OPD"
code_status: released
pip_dependencies:
  - "torch==2.9.1"
  - "sglang==0.5.9"
  - "transformers==4.57.1"
tags:
  - recipe
  - ier-opd
  - distillation
  - sparse-supervision
  - opd
---

# IER-OPD Sparse Token Selection

## Hardware & Environment Setup
- Official: `https://github.com/BruceSheng1202/IER-OPD`. Formula in `slime/rollout/ier_opd/ier_metrics.py`; fusion in `slime/rollout/tip_compat.py`.
- Python 3.12. Distill default stays OPD. Usefulness keep-mask stays sparse-opd-supervision. Entropy reweight stays IDA-OPD.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python -m pip install -r requirements/train.txt
python scripts/train.py --profile math_qwen3 --method ier --budget 0.01 --execute
```

`--method tip_ier_and` / `ta_opd_ier_and` fuses usefulness with IER. `--method full --budget 1.0` is the full-OPD control.

## Quickstart Implementation

```python
from __future__ import annotations


def ier_or(rank: float, usefulness: float) -> float:
    return rank + usefulness - rank * usefulness


def ier_and(rank: float, usefulness: float) -> float:
    return rank * usefulness


def keep_under_budget(scores: list[float], budget: float) -> list[bool]:
    n = len(scores)
    if n == 0:
        return []
    k = max(1, int(round(budget * n)))
    order = sorted(range(n), key=lambda i: scores[i], reverse=True)
    mask = [False] * n
    for i in order[:k]:
        mask[i] = True
    return mask
```

## Critical Hyperparameters & Tuning Advice
- Start at budget 0.01 or 0.001. 1%–5% with usefulness+IER often matches full OPD; more tokens can add noise.
- Prefer TIP / TA-OPD fused with IER-AND or IER-OR. Entropy+IER is not a reliable pair in the paper.
- Qwen3 profiles disable thinking unless you are reproducing the thinking-on ablation.
