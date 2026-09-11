---
id: recipe:nsd
type: recipe
title: "NSD Negative Self-Distillation"
method: method:nsd
task: task:privileged-teacher-opsd
target_hardware: "8x A100 80GB (paper; 2x minimum)"
framework: "PyTorch 2.8 / vLLM 0.11 / verl (in-repo) / Ray 2.55"
repo_url: "https://github.com/Prongcan/NSD"
pip_dependencies:
  - "torch==2.8.0"
  - "vllm==0.11.0"
  - "ray==2.55.1"
  - "transformers==4.57.6"
  - "flash-attn==2.8.3"
tags:
  - recipe
  - nsd
  - opsd
  - distillation
---

# NSD Negative Self-Distillation

## Hardware & Environment Setup
- Official train/eval: `https://github.com/Prongcan/NSD` (in-repo verl; do not swap a stock verl).
- Collection (exact slug): `https://huggingface.co/collections/PassionPrc/nsd-negative-self-distillation` — PassionPrc/NSD-Qwen3-1.7B, PassionPrc/NSD-Qwen3-4B, PassionPrc/NSD-Qwen3-8B.
- Install: `cd verl && pip install -e .`. CUDA 12.9. Loss: `verl/verl/trainer/distillation/losses.py` (`divergence_gated`, `divergence_gated_log`, `divergence_gated_sigmoid`).
- Train: `scripts/4B_NSD/` (PG `*_pg_*`; supervised `*_supervised_*`; default online: `run_online_nsd_sol_aware_supervised.sh`). Eval: `scripts/eval/` (AIME / HMMT / MATH-500).
- Privileged-teacher first hop stays VISTA. Pass@1 stays CISPO. Distill matching stays OPD.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def nsd_loss(
    student_logp: torch.Tensor,
    ref_logp: torch.Tensor,
    attack_logp: torch.Tensor,
    alpha: float = 0.01,
    beta: float = 1.0,
) -> torch.Tensor:
    """KL-anchor to the reference plus divergence-gated unlikelihood vs the negative teacher."""
    student_p = student_logp.exp()
    ref_p = ref_logp.exp()
    atk_p = attack_logp.exp()
    kl = F.kl_div(student_logp, ref_p, reduction="none", log_target=False)
    gate = torch.relu(atk_p - ref_p)
    unlikelihood = -torch.log1p(-student_p.clamp(max=1 - 1e-6))
    return (beta * kl + alpha * gate.detach() * unlikelihood).sum()
```

## Critical Hyperparameters & Tuning Advice
- Paper default: online negative-condition generation, no gold. α=0.01, two epochs on Qwen3-1.7B/4B/8B.
- Variants in-repo: question-only, sol-aware, wiki-irrelevant, sol-aware online. Default is online.
- Do not drop the KL term; unlikelihood without an anchor unlearns language.
