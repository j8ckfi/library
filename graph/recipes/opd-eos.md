---
id: recipe:opd-eos
type: recipe
title: "OPD Semantic-Class EOS"
method: method:opd-eos
task: task:student-distillation
target_hardware: "4x GPU Slurm (repo smoke); paper pairs include Qwen3-1.7B/4B and Gemma-3-4B"
framework: "PyTorch 2.8 / vLLM 0.11 / vendored verl"
repo_url: "https://github.com/UNCSciML/opd-eos"
pip_dependencies:
  - "torch==2.8.0"
  - "vllm==0.11.0"
  - "transformers==4.55.4"
  - "ray==2.54.0"
  - "math-verify"
tags:
  - recipe
  - opd
  - eos
  - distillation
---

# OPD Semantic-Class EOS

## Hardware & Environment Setup
- Official code: `https://github.com/UNCSciML/opd-eos`. Heart of the study: `verl/utils/eos_semantics.py`. Shared launcher is sampled-token OPD on DAPO-Math-17k TTRL prompts.
- Host distill algorithm stays OPD. This recipe only changes how terminal tokens are scored.
- Slurm headers request a GPU count only. `DRY_RUN=true bash slurm/submit_ttrl_eos_sweep.sh` prints the plan.

## Quickstart Implementation

```python
from __future__ import annotations

import torch
import torch.nn.functional as F


def semantic_stop_logp(logits: torch.Tensor, eos_ids: list[int]) -> torch.Tensor:
    """Sum teacher/student mass over equivalent EOS ids into one stop action."""
    if not eos_ids:
        raise ValueError("eos_ids must be non-empty")
    log_probs = F.log_softmax(logits, dim=-1)
    stacked = torch.stack([log_probs[..., i] for i in eos_ids], dim=-1)
    return torch.logsumexp(stacked, dim=-1)
```

Condition D in the repo (`train_ttrl_eos_d_semantic_class_200step.sl`) is the fix. Conditions A/B are negative controls (native EOS; two-stop decode without loss change).

## Critical Hyperparameters & Tuning Advice
- Discover terminal ids at submit time. Do not hard-code Qwen vs Llama vs Gemma ids.
- Paper defaults: batch 16, rollout n=4, prompt 1024 + response 7168, lr 1e-6, temperature 1.0, `log_prob_top_k=0`.
- If length still inflates after semantic class, look at the K2-Horizon late-training mode; mismatch is not the only source.
