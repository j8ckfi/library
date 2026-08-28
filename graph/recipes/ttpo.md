---
id: recipe:ttpo
type: recipe
title: "TTPO (Test-Time Policy Optimization) Implementation Recipe"
method: method:ttpo
task: task:label-free-test-time-reasoner
target_hardware: "1x NVIDIA H100 80GB (or 1x RTX 4090 24GB for small models)"
framework: "PyTorch 2.5+ / vLLM / HuggingFace Transformers"
repo_url: "https://github.com/ZJU-REAL/TTPO"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
  - "accelerate>=1.2.0"
tags:
  - recipe
  - test-time-training
  - reasoning
  - ttpo
---

# TTPO (Test-Time Policy Optimization) Implementation Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA H100 80GB for test-time batch rollouts, or RTX 4090 24GB for <=3B parameter models.
- Framework: PyTorch 2.5+ with vLLM acceleration.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F
from collections import Counter

def compute_ttpo_loss(
    model,
    prompt_ids: torch.Tensor,
    rollout_ids: list[torch.Tensor],
    parsed_answers: list[str],
    entropy_threshold: float = 0.5,
) -> torch.Tensor:
    """Computes asymmetric TTPO loss (OPSD on agreeing rollouts + Grouped RL on disagreeing rollouts).

    Args:
        model: Policy language model being adapted at test time.
        prompt_ids: Token IDs of the input problem prompt.
        rollout_ids: List of sampled token ID tensors for G rollouts.
        parsed_answers: List of canonical extracted answers for each rollout.
        entropy_threshold: Threshold for confident token filtering.

    Returns:
        Scalar loss tensor for test-time gradient step.
    """
    valid_answers = [ans for ans in parsed_answers if ans is not None]
    if not valid_answers:
        return torch.tensor(0.0, requires_grad=True, device=prompt_ids.device)

    vote_counts = Counter(valid_answers)
    pseudo_answer, count = vote_counts.most_common(1)[0]
    
    agree_indices = [i for i, ans in enumerate(parsed_answers) if ans == pseudo_answer]
    disagree_indices = [i for i, ans in enumerate(parsed_answers) if ans != pseudo_answer and ans is not None]

    total_loss = torch.tensor(0.0, device=prompt_ids.device)
    
    # 1. Distillation on agreeing rollouts (OPSD branch)
    if agree_indices:
        best_agree_idx = max(agree_indices, key=lambda idx: len(rollout_ids[idx]))
        agree_seq = rollout_ids[best_agree_idx]
        logits = model(agree_seq.unsqueeze(0)).logits[:, :-1, :]
        targets = agree_seq[1:]
        opsd_loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        total_loss = total_loss + opsd_loss

    # 2. Grouped RL penalty on disagreeing rollouts (RL branch)
    if disagree_indices:
        rl_penalty = torch.tensor(0.0, device=prompt_ids.device)
        for d_idx in disagree_indices:
            disagree_seq = rollout_ids[d_idx]
            logits = model(disagree_seq.unsqueeze(0)).logits[:, :-1, :]
            targets = disagree_seq[1:]
            log_probs = F.log_softmax(logits, dim=-1)
            token_log_probs = log_probs.gather(2, targets.unsqueeze(0).unsqueeze(2)).squeeze(2)
            # Penalize confident erroneous tokens
            confident_mask = token_log_probs.exp() > entropy_threshold
            if confident_mask.any():
                rl_penalty = rl_penalty + token_log_probs[confident_mask].mean()
        total_loss = total_loss + (rl_penalty / len(disagree_indices))

    return total_loss
```

## Critical Hyperparameters & Tuning Advice
- **Rollouts Per Problem ($G$)**: 8 to 16 for robust majority-voting consensus.
- **Learning Rate**: 1e-6 to 5e-6 (low LR for test-time stability).
- **Adaptation Steps**: 1 to 3 optimization steps per test prompt.
