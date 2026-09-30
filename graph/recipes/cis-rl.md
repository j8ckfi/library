---
id: recipe:cis-rl
type: recipe
title: "CIS Truncated Log-Odds Importance Sampling"
method: method:cis-rl
task: task:math-code-rl-moe
target_hardware: "MoE RLVR box with a separate infer engine (vLLM/SGLang) and train engine (FSDP/Megatron)"
framework: "PyTorch / GRPO-family host"
repo_url: "https://github.com/kzhao5/CIS-RL"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - cis-rl
  - rlvr
  - moe
  - importance-sampling
---

# CIS Truncated Log-Odds Importance Sampling

## Hardware & Environment Setup
- Official: `https://github.com/kzhao5/CIS-RL`. `code_status: released`.
- Pass@1 default stays CISPO. MoE/VL optimizer stays SAPO. Engine stays Miles.

```bash
git clone https://github.com/kzhao5/CIS-RL.git && cd CIS-RL
```

## Quickstart Implementation

```python
from __future__ import annotations


def cis_mismatch_weight(
    p_train: float,
    q_infer: float,
    lam: float = 2.3,
    kappa: float | None = None,
) -> float:
    if lam <= 0.0:
        raise ValueError("lam must be positive")
    if p_train < 0.0 or q_infer <= 0.0:
        raise ValueError("probabilities must be non-negative with q_infer > 0")
    p = min(max(p_train, 1e-12), 1.0 - 1e-12)
    q = min(max(q_infer, 1e-12), 1.0 - 1e-12)
    k = p / q
    cap = 1.0 + lam * (1.0 - p)
    k = min(k, cap)
    if kappa is not None:
        if kappa <= 0.0:
            raise ValueError("kappa must be positive when two-sided")
        floor = max(kappa, 1.0 / cap)
        k = max(k, floor)
    return k
```

Multiply the GRPO-family token surrogate by \(k_{\mathrm{CIS}}\). \(\rho\) (update ratio vs \(\theta_{\mathrm{old}}\)) stays on the usual PPO clip. Default is one-sided (\(\kappa=\mathrm{None}\), \(\lambda=2.3\)).

## Critical Hyperparameters & Tuning Advice
- \(\lambda=2.3\). Two-sided floor \(\kappa=5\times 10^{-3}\) is an ablation (diagnostic 6.01); one-sided is the default.
- Do not cap raw \(k\) at a constant (that is TIS). Do not mask an interval of \(k\) (IcePop).
- Dense policies in the paper look like rounding error; the tail is an MoE routing effect.
