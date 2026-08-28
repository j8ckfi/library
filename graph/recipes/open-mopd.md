---
id: recipe:open-mopd
type: recipe
title: "Open-MOPD (Multi-Teacher On-Policy Distillation) Recipe"
method: method:open-mopd
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / vLLM / HuggingFace Transformers"
repo_url: "https://github.com/BytedTsinghua-SIA/Open-MOPD"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
  - "accelerate>=1.2.0"
  - "deepspeed>=0.14.0"
tags:
  - recipe
  - distillation
  - multi-teacher
  - open-mopd
---

# Open-MOPD (Multi-Teacher On-Policy Distillation) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with vLLM rollouts and DeepSpeed ZeRO-3.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F

def compute_open_mopd_loss(
    student_model,
    domain_prompts: dict[str, torch.Tensor],
    domain_teachers: dict[str, callable],
    domain_gaps: dict[str, float],
) -> torch.Tensor:
    """Computes balanced multi-teacher on-policy distillation loss (Open-MOPD).

    Args:
        student_model: The generalist student policy being trained.
        domain_prompts: Dict mapping domain name to batch of prompt token IDs.
        domain_teachers: Dict mapping domain name to teacher evaluation callable.
        domain_gaps: Dict tracking real-time student-to-teacher headroom gaps per domain.

    Returns:
        Balanced scalar multi-teacher loss.
    """
    total_loss = torch.tensor(0.0, device=next(student_model.parameters()).device)
    total_gap = sum(domain_gaps.values()) + 1e-6

    for domain, prompts in domain_prompts.items():
        # Dynamic gap-aware weighting
        weight = domain_gaps.get(domain, 1.0) / total_gap
        
        # Student rollout
        with torch.no_grad():
            rollouts = student_model.generate(prompts, max_new_tokens=512)
        
        # Teacher target forward pass
        teacher_fn = domain_teachers[domain]
        teacher_probs = teacher_fn(prompts, rollouts)

        # Student forward pass on rollouts
        student_logits = student_model(rollouts).logits
        student_log_probs = F.log_softmax(student_logits, dim=-1)

        # Token-share balanced KL divergence (normalized per sequence length)
        token_mask = (rollouts != 0).float()
        kl_per_token = F.kl_div(student_log_probs, teacher_probs, reduction='none').sum(dim=-1)
        normalized_domain_loss = (kl_per_token * token_mask).sum() / (token_mask.sum() + 1e-6)

        total_loss = total_loss + weight * normalized_domain_loss

    return total_loss
```

## Critical Hyperparameters & Tuning Advice
- **Dynamic Weighting Update Interval**: Recompute domain headroom gaps every 100 optimization steps.
- **Token-Share Normalization**: Always divide domain KL by total active tokens in that domain batch before aggregation.
- **Rollout Temperature**: 0.7 for diverse exploration across reasoning and instruction domains.
