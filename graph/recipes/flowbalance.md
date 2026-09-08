---
id: recipe:flowbalance
type: recipe
title: "FlowBalance Trajectory-Balance Recipe"
method: method:flowbalance
task: task:math-code-rl-dense
target_hardware: "4x8 GPUs (paper math recipe; vendored verl + vLLM)"
framework: "PyTorch / veRL / vLLM / Ray / FSDP"
repo_url: "https://github.com/alexhuang13/FlowBalance"
pip_dependencies:
  - "torch>=2.5.0"
  - "vllm>=0.7.0"
  - "ray>=2.40.0"
tags:
  - recipe
  - flowbalance
  - rlvr
  - trajectory-balance
---

# FlowBalance Trajectory-Balance Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/alexhuang13/FlowBalance`. Blog: `https://alexhuang13.github.io/FlowBalance-Blog/`. Clone, `pip install -e ./verl`, `python3 scripts/check_environment.py`.
- Paper math recipe: 4 nodes × 8 GPUs, Qwen3-8B, DAPO-17k parquet, AIME24 boxed val, prompt 2048 / response 8192, group $N=8$, train prompt batch 256, 180 steps.
- Code maps $\beta_G$ → `FLOWSD_BETA_Q` and $\eta_A$ → `FLOWSD_ETA_R`. Defaults 1 and 15. Clip $B=4$.
- Host Pass@1 labeled RLVR stays CISPO. This recipe is the FlowBalance energy + profiled TB residual on a GRPO-style group.

## Quickstart Implementation

```python
import torch


def flowbalance_energy(advantage: torch.Tensor, guidance: torch.Tensor, eta_a: float, beta_g: float) -> torch.Tensor:
    """E = eta_A A + beta_G G_H sgn(A). A=0 disables the dense branch."""
    sign = torch.sign(advantage)
    return eta_a * advantage + beta_g * guidance * sign


def profiled_logz(energy: torch.Tensor, log_pi: torch.Tensor, log_pref: torch.Tensor, tau: float) -> torch.Tensor:
    """One stopped log-partition estimate per group. energy/log_pi/log_pref: [N]."""
    implied = energy / tau - (log_pi - log_pref)
    return implied.mean().detach()


def flowbalance_tb_loss(
    energy: torch.Tensor,
    log_pi: torch.Tensor,
    log_pref: torch.Tensor,
    tau: float,
) -> torch.Tensor:
    """Profiled trajectory-balance MSE. Gradients only through log_pi."""
    logz = profiled_logz(energy.detach(), log_pi.detach(), log_pref, tau)
    residual = tau * logz + tau * (log_pi - log_pref) - energy.detach()
    return 0.5 * residual.square().mean()
```

## Critical Hyperparameters & Tuning Advice
- $\eta_A=15$, $\beta_G=1$, clip $B=4$. Do not jump $\beta_G$ to 3; the paper's 8B AIME24/HMMT25 drop.
- Group $N=8$ in the public recipe; analysis quotes $N=32$ for contrast-count theory, not the LLM table.
- Privileged $c$ is train-only. Do not leak it into the deployed policy.
- Does not replace CISPO, OPSA, OPD, VISTA, RISE, or CANOPY.
