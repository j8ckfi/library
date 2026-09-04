---
id: recipe:cliff
type: recipe
title: "Cliff Pitfall-Step Advantage Recipe"
method: method:cliff
task: task:math-code-rl-dense
target_hardware: "8x NVIDIA H100 80GB (host RLVR run + teacher judge)"
framework: "PyTorch / veRL"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - cliff
  - rlvr
  - process-supervision
---

# Cliff Pitfall-Step Advantage Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-04. Plug into a GRPO/DAPO-style veRL trainer. Host algorithm for Pass@1 labeled RLVR stays CISPO.
- Teacher must emit a reference solution and, on failed student rollouts, a Pitfall Step index (sentence or token). If the teacher's own solution fails the verifier, skip Cliff for that group.

## Quickstart Implementation

```python
import torch


def cliff_advantages(
    rewards: torch.Tensor,
    lengths: torch.Tensor,
    pitfall: torch.Tensor,
    lam: float = 0.0,
) -> list[torch.Tensor]:
    """Token advantages from a Pitfall Step. rewards in {0, 1}; pitfall[i] is p(a_i).

    λ=0 is the paper default (no positive credit on the correct prefix of a fail).
    """
    r = rewards.float()
    mu = r.mean()
    sigma = torch.sqrt(mu * (1 - mu)).clamp_min(1e-8)
    a_cor = (1.0 - mu) / sigma
    a_inc = (0.0 - mu) / sigma
    token_as = []
    for i, (rew, n, p) in enumerate(zip(r.tolist(), lengths.tolist(), pitfall.tolist())):
        n_i = int(n)
        p_i = max(0, min(int(p), n_i))
        adv = torch.full((n_i,), a_inc if rew < 0.5 else a_cor)
        if rew < 0.5:
            adv[:p_i] = lam * a_cor
        token_as.append(adv)
    cat = torch.cat(token_as)
    b = cat.mean()
    return [a - b for a in token_as]
```

## Critical Hyperparameters & Tuning Advice
- $\lambda=0$. Do not positively reinforce prefixes of failed rollouts.
- Overlength / truncated rollouts: set $p(a)=0$.
- Fall back to vanilla group-relative advantages when the teacher reference fails the verifier.
- Cliff is a plug-in. It does not replace CISPO, OPD, or VeriGate.
