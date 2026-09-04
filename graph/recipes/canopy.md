---
id: recipe:canopy
type: recipe
title: "CANOPY SignalCoverageRL Recipe"
method: method:canopy
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "multi-node H100 (paper: veRL + SGLang + Megatron; n=32 AppWorld groups)"
framework: "PyTorch / veRL / SGLang / Megatron"
repo_url: "https://github.com/AlibabaResearch/SignalCoverageRL"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - canopy
  - agentic
  - outcome-only
---

# CANOPY SignalCoverageRL Recipe

## Hardware & Environment Setup
- Listed code: `https://github.com/AlibabaResearch/SignalCoverageRL`. Paper trains Qwen3-14B with veRL, asynchronous SGLang rollouts, Megatron updates, against a stabilized AppWorld server.
- AppWorld paper config: 90 tasks / 90 steps / batch 90, n=32 (2,880 rollouts/step), 50 turns / 32k train, temperature 0.9, KL β=1e-4, lr 3e-6, one update/step, hardest tier kept. Inference: 100 turns / 61k, T=0.6.

## Quickstart Implementation

```python
import math


def min_group_size(p_min: float, tau: float = 0.8) -> int:
    """First-order n so a hard task with success p_min has coverage >= tau.

    P_sig ≈ 1-(1-p)^n for small p. Treat as a floor against the GPU budget.
    """
    if not 0.0 < p_min < 1.0:
        raise ValueError("p_min must be in (0, 1)")
    if not 0.0 < tau < 1.0:
        raise ValueError("tau must be in (0, 1)")
    return max(2, math.ceil(math.log(1.0 - tau) / math.log(1.0 - p_min)))


def sparse_outcome(passed: int, n_tests: int) -> float:
    """Fully-correct-only reward. Do not use pass-fraction here."""
    if n_tests <= 0:
        return 0.0
    return 1.0 if passed == n_tests else 0.0
```

## Critical Hyperparameters & Tuning Advice
- Size n from a base-policy pilot on the hardest retained tier. Paper AppWorld n=32; SWE n=16.
- One update per rollout batch. Do not split into stale mini-batches.
- Sparse {0,1} fully-correct reward. Pass-fraction is the compensation CANOPY argues you do not need once coverage is restored.
- KL-anchor to the base. Unanchored entropy collapse is the late-training failure mode.
- Host SWE eval harness stays mini-SWE-agent. This recipe trains a policy; it does not replace the harness.
