---
id: recipe:u-opsd
type: recipe
title: "u-OPSD (Unsupervised On-Policy Self-Distillation) Recipe"
method: method:u-opsd
task: task:label-free-reasoner-posttrain
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / vLLM / HuggingFace Transformers"
repo_url: "https://github.com/williamium3000/u-opsd"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
  - "accelerate>=1.2.0"
  - "datasets>=3.0.0"
tags:
  - recipe
  - distillation
  - post-training
  - label-free
  - u-opsd
---

# u-OPSD (Unsupervised On-Policy Self-Distillation) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with vLLM generation backend.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F
from collections import Counter

def compute_u_opsd_loss(
    student_model,
    prompt_tokens: torch.Tensor,
    rollout_tokens: list[torch.Tensor],
    parsed_answers: list[str],
    consistency_threshold: float = 0.5,
) -> torch.Tensor:
    """Computes unsupervised on-policy self-distillation loss (u-OPSD).

    Args:
        student_model: The policy network being post-trained.
        prompt_tokens: Problem prompt token IDs [prompt_len].
        rollout_tokens: List of G sampled output sequences.
        parsed_answers: List of G extracted answers.
        consistency_threshold: Minimum consensus fraction (default 0.5).

    Returns:
        Scalar forward KL divergence loss over disagreeing rollouts.
    """
    valid_pairs = [(r, a) for r, a in zip(rollout_tokens, parsed_answers) if a is not None]
    if not valid_pairs:
        return torch.tensor(0.0, requires_grad=True, device=prompt_tokens.device)

    answers = [a for _, a in valid_pairs]
    counts = Counter(answers)
    best_ans, max_count = counts.most_common(1)[0]

    # Verify self-consistency confidence threshold
    if (max_count / len(rollout_tokens)) < consistency_threshold:
        return torch.tensor(0.0, requires_grad=True, device=prompt_tokens.device)

    agreeing = [r for r, a in valid_pairs if a == best_ans]
    disagreeing = [r for r, a in valid_pairs if a != best_ans]

    if not agreeing or not disagreeing:
        return torch.tensor(0.0, requires_grad=True, device=prompt_tokens.device)

    # Pick longest agreeing rollout as pseudo-solution
    pseudo_solution = max(agreeing, key=lambda x: len(x))

    total_loss = torch.tensor(0.0, device=prompt_tokens.device)
    for disagree_rollout in disagreeing:
        # Construct teacher context (prompt + pseudo_solution + disagree prefix)
        teacher_input = torch.cat([prompt_tokens, pseudo_solution, disagree_rollout])
        student_input = torch.cat([prompt_tokens, disagree_rollout])

        with torch.no_grad():
            teacher_logits = student_model(teacher_input.unsqueeze(0)).logits[0, -len(disagree_rollout):, :]
            teacher_probs = F.softmax(teacher_logits, dim=-1)

        student_logits = student_model(student_input.unsqueeze(0)).logits[0, -len(disagree_rollout):, :]
        student_log_probs = F.log_softmax(student_logits, dim=-1)

        # Forward KL: D_KL(teacher || student)
        kl = F.kl_div(student_log_probs, teacher_probs, reduction="batchmean")
        total_loss = total_loss + kl

    return total_loss / len(disagreeing)
```

## Critical Hyperparameters & Tuning Advice
- **Group Rollout Size ($G$)**: 8 to 16 rollouts per prompt.
- **Self-Consistency Threshold ($\tau$)**: 0.5 (absolute majority).
- **Divergence Metric**: Forward KL ($\beta=0$) with pointwise token clipping.
