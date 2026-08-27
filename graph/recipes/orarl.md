---
id: recipe:orarl
type: recipe
title: "OraRL Video MLLM Training Recipe"
method: method:orarl
task: task:rl-video-mllm
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / OraRL"
repo_url: "https://github.com/HVision-NKU/OraRL"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
  - "decord>=0.6.0"
tags:
  - recipe
  - video-mllm
  - multimodal-rl
  - orarl
---

# OraRL Video MLLM Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with `decord` video decoding and `vLLM` rollout acceleration.

## Quickstart Code

```python
import torch

def compute_decoupled_orarl_advantages(
    policy_rewards: torch.Tensor,
    oracle_reward: float = 1.0,
) -> tuple[torch.Tensor, float]:
    """Computes decoupled OraRL advantages for on-policy rollouts and oracle target.

    Args:
        policy_rewards: 1D tensor of rewards for on-policy candidate rollouts [N].
        oracle_reward: Ground-truth annotation reward scalar.

    Returns:
        policy_advantages: Normalized advantages for policy rollouts [N].
        oracle_weight: Decoupled weight for detached oracle rollout.
    """
    mean_on_policy = policy_rewards.mean()
    std_on_policy = policy_rewards.std() + 1e-8
    
    # Decoupled on-policy advantage
    policy_advantages = (policy_rewards - mean_on_policy) / std_on_policy
    
    # Gap modulation
    oracle_gap = max(0.0, oracle_reward - mean_on_policy.item())
    oracle_weight = oracle_gap
    
    return policy_advantages, oracle_weight
```

## Critical Configuration Options
- `SIGN_BALANCED_PRUNING`: `True` (prunes group to oracle + balanced sign subsets).
- `DECOUPLED_ORACLE`: `True` (excludes oracle from baseline normalization).
- `DISABLE_COT`: `True` (enables direct non-CoT video perception decoding).
