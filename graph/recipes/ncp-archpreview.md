---
id: recipe:ncp-archpreview
type: recipe
title: "NCP-ArchPreview Latent LM Pretrain"
method: method:ncp-archpreview
task: task:latent-space-lm-pretrain
target_hardware: "8.9B pretrain on 5.73T Dolma-3 (paper cluster); eval on 8 GPU via ncp_olmo_eval"
framework: "PyTorch / vLLM (ncp-archpreview fork) / lmdeploy"
repo_url: "https://github.com/LUMIA-Group/ncp_olmo_eval"
pip_dependencies:
  - "ncp-olmo-eval==0.1.1"
tags:
  - recipe
  - ncp
  - latent-lm
  - pretraining
---

# NCP-ArchPreview Latent LM Pretrain

## Hardware & Environment Setup
- Weights: `https://huggingface.co/collections/ArchSpace-Collection/ncp-archpreview`.
- Eval: `https://github.com/LUMIA-Group/ncp_olmo_eval` (vLLM-only public runtime).
- Serving forks: InternLM/lmdeploy; LuckySJTU vLLM `dev/ncp-archpreview`.
- No official from-scratch trainer. Optimizer default stays Muon2. Data recipe stays OLMo-3 / Dolma-3.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class NcpJointLoss:
    ntp_weight: float = 1.0
    ncp_weight: float = 1.0


def ncp_total_loss(ntp_ce: float, ncp_ce: float, cfg: NcpJointLoss) -> float:
    """Joint next-token and next-concept cross-entropy. Concept logits come from the Concept Module."""
    return cfg.ntp_weight * ntp_ce + cfg.ncp_weight * ncp_ce
```

## Critical Hyperparameters & Tuning Advice
- Paper scale: 8.9B params, 5.73T Dolma-3 tokens. Do not retarget Muon2 or swap the open mix.
- 17M VQ module is the cheap domain-adaptation interface; do not full-FT the backbone for a domain shift if the VQ path is enough.
- DFlash2 concept injection is a drafter add-on (+4.17% MAL), not Uno / Miles.
