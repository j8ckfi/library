---
id: recipe:cal-opd
type: recipe
title: "Cal-OPD Residual Advantage"
method: method:cal-opd
task: task:student-distillation
target_hardware: "8x NVIDIA H20 (paper: 4 student + 4 teacher); H100 is the closest substitute"
framework: "PyTorch / verl"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
  - "verl"
tags:
  - recipe
  - cal-opd
  - distillation
  - on-policy
---

# Cal-OPD Residual Advantage

## Hardware & Environment Setup
- No official GitHub as of 2026-09-21 (`arXiv:2609.21619`). `repo_url: none found`. `code_status: none`.
- Paper implements all methods in verl (Sheng et al.) on 8×H20, 100 steps, 256 trajectories/step, one rollout per question, lr \(1\times 10^{-6}\), train response 16384 / eval 20480.
- Distill default stays OPD. Privileged-teacher adaptation stays VISTA. Retirement stays RetireOPD.

## Quickstart Implementation

```python
from __future__ import annotations


def tsd_bounds(ell_t: float, delta_pos: float, delta_neg: float, lam: float = 5.0) -> tuple[float, float]:
    d_down = max(0.0, -delta_pos, -delta_neg)
    d_up = max(0.0, delta_pos, delta_neg)
    return ell_t - lam * d_down, ell_t + lam * d_up


def cal_opd_advantage(
    ell_t: float,
    ell_s: float,
    delta_pos: float,
    delta_neg: float,
    lam: float = 5.0,
) -> float:
    lo, hi = tsd_bounds(ell_t, delta_pos, delta_neg, lam)
    return max(lo - ell_s, 0.0) - max(ell_s - hi, 0.0)
```

## Critical Hyperparameters & Tuning Advice
- Default probes are positive and negative evaluative feedback, not solution-level privilege. \(C_{\mathrm{sol}}\) over-filters.
- \(\lambda=5\). Larger \(\lambda\) expands the TSD region and drops retained discrepancy toward ~20%.
- Interventions are teacher-only. Do not mix privileged tokens into the student prefix.
- If every token in a sequence has zero calibrated advantage, skip the update.
