---
id: recipe:diffusion-policy-servo
type: recipe
title: "Visuomotor Servo Control Training with Diffusion Policy"
method: method:diffusion-policy
task: task:visuomotor-servo-control
target_hardware: "1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB)"
framework: "PyTorch 2.5+ / Diffusers / Robomimic"
repo_url: "https://github.com/real-stanford/diffusion_policy"
pip_dependencies:
  - "torch>=2.5.0"
  - "diffusers>=0.30.0"
  - "robomimic>=0.3.0"
  - "torchvision>=0.20.0"
tags:
  - control
  - robotics
  - visuomotor
  - diffusion-policy
---

# Visuomotor Servo Control Training with Diffusion Policy

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100 GPU.
- Robot Interfaces: Franka Emika Panda, ALOHA bimanual teleop, or UR5 servo controllers.
- Python Packages: `diffusers>=0.30.0`, `robomimic`, `torchvision`.

## Quickstart Code

```python
import torch
import torch.nn as nn
from diffusers.schedulers.scheduling_ddim import DDIMScheduler

class Conv1dBlock(nn.Module):
    def __init__(self, inp, out):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv1d(inp, out, kernel_size=5, padding=2),
            nn.Mish(),
            nn.Conv1d(out, out, kernel_size=5, padding=2),
            nn.Mish()
        )
    def forward(self, x):
        return self.block(x)

class ConditionalUnet1D(nn.Module):
    """1D Temporal U-Net for predicting noise in continuous action chunks."""
    def __init__(self, action_dim: int = 7, obs_feature_dim: int = 512, hidden_dim: int = 256):
        super().__init__()
        self.action_proj = nn.Conv1d(action_dim, hidden_dim, kernel_size=1)
        self.obs_proj = nn.Linear(obs_feature_dim, hidden_dim)
        self.time_emb = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.Mish(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.conv_in = Conv1dBlock(hidden_dim, hidden_dim)
        self.conv_out = nn.Conv1d(hidden_dim, action_dim, kernel_size=1)

    def forward(self, noisy_actions: torch.Tensor, timestep: torch.Tensor, obs_features: torch.Tensor):
        # noisy_actions: [B, T_act, action_dim] -> permuted to [B, action_dim, T_act]
        x = self.action_proj(noisy_actions.permute(0, 2, 1))
        t_emb = self.time_emb(timestep.unsqueeze(-1)).unsqueeze(-1)
        o_emb = self.obs_proj(obs_features).unsqueeze(-1)
        
        h = x + t_emb + o_emb
        out = self.conv_in(h)
        noise_pred = self.conv_out(out).permute(0, 2, 1)
        return noise_pred

# Diffusion Policy Training Step
def train_diffusion_step(model, noise_scheduler, vision_encoder, rgb_obs, true_actions, optimizer):
    optimizer.zero_grad()
    B = true_actions.shape[0]
    
    # 1. Encode visual camera frames
    obs_features = vision_encoder(rgb_obs)  # [B, obs_dim]
    
    # 2. Sample random diffusion timesteps
    timesteps = torch.randint(0, noise_scheduler.config.num_train_timesteps, (B,), device=true_actions.device).long()
    
    # 3. Add Gaussian noise to action trajectories
    noise = torch.randn_like(true_actions)
    noisy_actions = noise_scheduler.add_noise(true_actions, noise, timesteps)
    
    # 4. Predict noise with 1D conditional U-Net
    noise_pred = model(noisy_actions, timesteps.float(), obs_features)
    
    # 5. MSE Loss on predicted noise
    loss = nn.functional.mse_loss(noise_pred, noise)
    loss.backward()
    optimizer.step()
    return loss.item()
```

## Critical Hyperparameters
- **Action Chunk Horizon (\(T_{\text{act}}\))**: 16 steps (at 50Hz control = 320ms execution horizon).
- **Observation History (\(T_{\text{obs}}\))**: 2 recent visual/proprioceptive frames.
- **Inference Scheduler**: Use DDIM with 10–16 diffusion steps for low-latency real-time closed-loop control.
