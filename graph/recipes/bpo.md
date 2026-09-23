---
id: recipe:bpo
type: recipe
title: "BPO Critic-Free RLVR Loss"
method: method:bpo
task: task:math-code-rl-dense
target_hardware: "rollout box matching a CISPO/GRPO host; paper: Qwen3-30B-A3B-Base, max response 16384"
framework: "PyTorch GRPO-family host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - bpo
  - rl-alignment
  - math
---

# BPO Critic-Free RLVR Loss

## Hardware & Environment Setup
- No official GitHub as of 2026-09-23 (`arXiv:2609.15987`). `repo_url: none found`. `code_status: none`. Same note as Critical-State RL / Cal-OPD.
- Pass@1 default stays CISPO. MoE/VL stays SAPO. Async stays SAO.

## Quickstart Implementation

```python
from __future__ import annotations


def mismatch_weight(mu_p: float, pi_p: float, eps: float) -> float:
    """Complementary-token mismatch weight ω = (1+ε-μ) / (1+ε-π)."""
    return (1.0 + eps - mu_p) / (1.0 + eps - pi_p)


def bpo_token_coeff(
    advantage: float,
    omega: float,
    cap: float,
    eps_low: float,
    eps_high: float,
) -> float:
    """GRPO-style clip mask on ω, then min(sg(ω), C) * A."""
    if advantage > 0.0 and omega > 1.0 + eps_high:
        return 0.0
    if advantage < 0.0 and omega < 1.0 - eps_low:
        return 0.0
    return advantage * min(omega, cap)
```

Group-normalize rewards into \(\hat{A}\) as in GRPO. Substitute `bpo_token_coeff` for the IS-ratio coefficient. Do not train a critic.

## Critical Hyperparameters & Tuning Advice
- Keep additive smoothing \(\varepsilon\) and cap \(C\). \(\omega\) is not an IS ratio.
- Paper matched setting: 256 prompts, group 16, max 16384, eight optimizer updates per rollout batch, 400 steps on DAPO-Math-17k.
- Do not retarget CISPO from the 50.5% AIME peak.
