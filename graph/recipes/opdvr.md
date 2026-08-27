---
id: recipe:opdvr
type: recipe
title: "OPDVR On-Policy Distillation with Verifiable Reward Recipe"
method: method:opdvr
task: task:distill-reasoner-verifier
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / verl"
repo_url: "https://github.com/LeapLabTHU/OPDVR"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
  - "verl>=0.2.0"
tags:
  - recipe
  - distillation
  - rlvr
  - opdvr
---

# OPDVR On-Policy Distillation with Verifiable Reward Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with `verl` and `vLLM` rollout acceleration.

## Quickstart Code

```python
import torch

def compute_opdvr_reward(
    student_log_probs: torch.Tensor,
    teacher_log_probs: torch.Tensor,
    is_correct: torch.Tensor,
) -> torch.Tensor:
    """Computes ReLU-gated token-level rewards for OPDVR.

    Args:
        student_log_probs: Log-probabilities from student policy [B, T].
        teacher_log_probs: Log-probabilities from teacher policy [B, T].
        is_correct: Trajectory verification indicator [B, 1] (True for correct).

    Returns:
        Gated token-level reward tensor [B, T].
    """
    log_ratio = teacher_log_probs - student_log_probs
    correct_reward = torch.relu(log_ratio)
    incorrect_reward = -torch.relu(-log_ratio)
    
    mask = is_correct.unsqueeze(-1).expand_as(log_ratio)
    return torch.where(mask, correct_reward, incorrect_reward)
```

## Critical Configuration Options
- `CORRECTNESS_GATED`: `True` to enable ReLU-gated OPDVR.
- `GRPO_SCALED`: `True` for Group Relative Policy Distillation (GRPD).
- `LOG_PROB_TOP_K`: `0` for sampled-token OPD.
