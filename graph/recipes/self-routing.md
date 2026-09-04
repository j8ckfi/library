---
id: recipe:self-routing
type: recipe
title: "Self-Routing Sample-Level Recipe Router"
method: method:self-routing
task: task:math-code-rl-dense
target_hardware: "8x NVIDIA H100 80GB (host GRPO/OPSD run)"
framework: "PyTorch / ms-swift (planned, not released)"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - self-routing
  - rlvr
---

# Self-Routing Sample-Level Recipe Router

## Hardware & Environment Setup
- ms-swift implementation planned; not released as of 2026-09-04. Add the router on top of an existing GRPO trainer that already samples G rollouts and has gold answers for an OPSD branch.
- Paper membership widths: σ_l = σ_h = 0.18, σ_m = 0.16. Do not retune per dataset unless you have a diagnostic.

## Quickstart Implementation

```python
import math


def accuracy_membership(a: float, sigma_l: float = 0.18, sigma_m: float = 0.16, sigma_h: float = 0.18) -> tuple[float, float, float]:
    l = math.exp(-(a - 0.0) ** 2 / (2 * sigma_l ** 2))
    m = math.exp(-(a - 0.5) ** 2 / (2 * sigma_m ** 2))
    h = math.exp(-(a - 1.0) ** 2 / (2 * sigma_h ** 2))
    z = l + m + h
    return l / z, m / z, h / z


def routing_scores(a: float, c_norm: float, c_high: float, c_low: float, delta_c: float) -> dict[str, float]:
    """Paper §3.4. c_norm, c_high, c_low, delta_c are batch-calibrated confidence features in [0, 1]-ish."""
    l, m, h = accuracy_membership(a)
    return {
        "grpo": m + h * (1.0 - delta_c) + l * (1.0 - c_low) * c_norm,
        "opsd": l * (1.0 - c_low),
        "reg": h * delta_c * c_high,
        "skip": l * c_low * c_norm,
    }
```

## Critical Hyperparameters & Tuning Advice
- One recipe per sample per step. Do not mix GRPO and OPSD on the same prompt in the same update.
- SKIP contributes neither gradient nor denominator.
- Host Pass@1 algorithm stays CISPO. This router does not replace OPSA when there are no answers.
