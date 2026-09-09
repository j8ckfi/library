---
id: recipe:rlvr-group-correlation
type: recipe
title: "Within-Group Verifier ICC Hygiene"
method: method:rlvr-group-correlation
task: task:math-code-rl-dense
target_hardware: "CPU for ICC; GPU only if regenerating k=8 rollouts (paper: Qwen2.5-1.5B)"
framework: "PyTorch optional / analysis"
repo_url: "https://github.com/ethxin0011/rlvr_group_correlation"
pip_dependencies:
  - "numpy"
tags:
  - recipe
  - rlvr
  - verifier
  - hygiene
---

# Within-Group Verifier ICC Hygiene

## Hardware & Environment Setup
- Official analysis code: `https://github.com/ethxin0011/rlvr_group_correlation`. Pipeline stages live under `src/` (`pilot_gate.py`, `rule_verify.py`, `advantage_replay.py`).
- This is not a trainer. Host Pass@1 stays CISPO. Do not treat k completions as independent verifier trials.

## Quickstart Implementation

```python
from __future__ import annotations


def kish_n_eff(k: float, rho: float) -> float:
    """Design-effect-adjusted size of a k-completion group under exchangeable correlation."""
    rho = max(float(rho), 0.0)
    return float(k) / (1.0 + (float(k) - 1.0) * rho)


def icc_oneway(groups: list[list[float]]) -> float | None:
    """One-way random-effects ICC(1) on per-completion error flags."""
    groups = [g for g in groups if len(g) > 1]
    if len(groups) < 10:
        return None
    n = sum(len(g) for g in groups)
    m = len(groups)
    grand = sum(sum(g) for g in groups) / n
    ssb = sum(len(g) * (sum(g) / len(g) - grand) ** 2 for g in groups)
    ssw = sum(sum((x - sum(g) / len(g)) ** 2 for x in g) for g in groups)
    df_b, df_w = m - 1, n - m
    if df_b <= 0 or df_w <= 0:
        return None
    msb, msw = ssb / df_b, ssw / df_w
    k_bar = (n - sum(len(g) ** 2 for g in groups) / n) / (m - 1)
    denom = msb + (k_bar - 1) * msw
    if denom == 0:
        return 0.0
    icc = (msb - msw) / denom
    return max(-1.0, min(1.0, icc))
```

## Critical Hyperparameters & Tuning Advice
- Paper headline: ρ=0.530 ⇒ n_eff≈1.70 at k=8, not 8 independent scores.
- Keep group integrity: generate all k completions in one call; drop incomplete groups rather than backfill.
- Stratify ICC by answer form. Do not quote a single aggregate verifier error rate as independence.
