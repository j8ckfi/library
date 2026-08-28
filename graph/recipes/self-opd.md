---
id: recipe:self-opd
type: recipe
title: "Self-OPD (Teacher-Free Flow Matching On-Policy Distillation) Recipe"
method: method:self-opd
task: task:posttrain-diffusion
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / Diffusers"
repo_url: "https://github.com/Shiy-Zhang/Self-OPD"
pip_dependencies:
  - "torch>=2.5.0"
  - "diffusers>=0.31.0"
  - "transformers>=4.48.0"
  - "accelerate>=1.2.0"
tags:
  - recipe
  - flow-matching
  - diffusion
  - self-opd
---

# Self-OPD (Teacher-Free Flow Matching On-Policy Distillation) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with HuggingFace Diffusers.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F

def compute_self_opd_loss(
    velocity_pred: torch.Tensor,
    branch_velocities: torch.Tensor,
    branch_rewards: torch.Tensor,
    ref_reward: torch.Tensor,
    sde_variance_scale: float = 1.0,
) -> torch.Tensor:
    """Computes Self-OPD all-branch pull-push velocity loss for flow matching.

    Args:
        velocity_pred: Predicted velocity field at current state v_theta(x_t, t) [B, C, H, W].
        branch_velocities: Candidate SDE branch velocities [K, B, C, H, W].
        branch_rewards: Terminal rewards for K stochastic branches [K, B].
        ref_reward: Terminal reward for deterministic self-reference rollout [B].
        sde_variance_scale: Normalization factor corresponding to SDE step variance.

    Returns:
        Scalar loss tensor for velocity field update.
    """
    # Calculate self-referenced advantages
    advantages = branch_rewards - ref_reward.unsqueeze(0)  # [K, B]
    
    loss = torch.tensor(0.0, device=velocity_pred.device)
    K = branch_velocities.shape[0]

    for k in range(K):
        adv_k = advantages[k]  # [B]
        v_k = branch_velocities[k]  # [B, C, H, W]
        
        # Velocity error vector
        diff = velocity_pred - v_k
        sq_dist = (diff ** 2).sum(dim=[1, 2, 3])  # [B]
        
        # Direction-aware attenuation: positive advantage pulls, negative advantage pushes
        # Attenuation prevents push from destabilizing dominant high-reward trajectory
        weight = torch.where(adv_k >= 0, adv_k, 0.5 * adv_k)
        
        branch_loss = (weight * sq_dist).mean() / sde_variance_scale
        loss = loss + branch_loss

    return loss / K
```

## Critical Hyperparameters & Tuning Advice
- **Number of SDE Branches ($K$)**: 4 to 8 branches per exploration timestep.
- **SDE Noise Schedule ($\eta$)**: 0.2 to 0.4 for controlled stochastic exploration.
- **Multi-Objective Reward Normalization**: Z-score normalize individual reward components before summation.
