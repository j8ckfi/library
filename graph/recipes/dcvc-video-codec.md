---
id: recipe:dcvc-video-codec
type: recipe
title: "Training Learned Neural Video Codecs with DCVC-DC"
method: method:dcvc-dc
task: task:learned-video-compression
target_hardware: "4x or 8x NVIDIA A100 80GB (SXM)"
framework: "PyTorch 2.5+ / CompressAI / CUDA"
repo_url: "https://github.com/microsoft/DCVC"
pip_dependencies:
  - "torch>=2.5.0"
  - "compressai>=1.2.6"
  - "torchvision>=0.20.0"
tags:
  - video
  - compression
  - neural-codec
  - pytorch
---

# Training Learned Neural Video Codecs with DCVC-DC

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Python Packages: `compressai>=1.2.6`, `torchvision`, `torch`.

## Quickstart Code

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MotionCompensationBlock(nn.Module):
    """Learned optical flow motion estimation and frame warping."""
    def forward(self, ref_frame: torch.Tensor, flow: torch.Tensor) -> torch.Tensor:
        # Spatial grid warping with bilinear interpolation
        B, C, H, W = ref_frame.shape
        grid_y, grid_x = torch.meshgrid(
            torch.linspace(-1, 1, H, device=ref_frame.device),
            torch.linspace(-1, 1, W, device=ref_frame.device),
            indexing="ij"
        )
        grid = torch.stack((grid_x, grid_y), 2).unsqueeze(0).repeat(B, 1, 1, 1)
        vgrid = grid + flow.permute(0, 2, 3, 1)
        return F.grid_sample(ref_frame, vgrid, mode='bilinear', padding_mode='border', align_corners=True)

class DCVCContextualFrameCoder(nn.Module):
    """Dual-context neural video compression block."""
    def __init__(self, lambda_rd: float = 256.0):
        super().__init__()
        self.lambda_rd = lambda_rd
        self.motion_warper = MotionCompensationBlock()
        self.context_encoder = nn.Conv2d(6, 128, kernel_size=5, stride=2, padding=2)
        self.frame_decoder = nn.ConvTranspose2d(128, 3, kernel_size=5, stride=2, padding=2, output_padding=1)

    def forward(self, curr_frame: torch.Tensor, ref_frame: torch.Tensor, flow: torch.Tensor):
        # 1. Warp reference frame to create temporal context
        warped_ref = self.motion_warper(ref_frame, flow)
        
        # 2. Contextual encoding (concatenating current frame with temporal prediction)
        in_feat = torch.cat([curr_frame, warped_ref], dim=1)
        latent_y = self.context_encoder(in_feat)
        
        # 3. Quantization simulation with uniform noise during training
        if self.training:
            y_hat = latent_y + torch.rand_like(latent_y) - 0.5
        else:
            y_hat = torch.round(latent_y)
            
        # 4. Contextual frame reconstruction
        rec_frame = self.frame_decoder(y_hat)
        
        # 5. Rate-Distortion Loss (Distortion MSE + proxy Rate entropy)
        distortion = F.mse_loss(rec_frame, curr_frame)
        rate_proxy = torch.mean(torch.abs(y_hat))  # Simplified entropy proxy for illustration
        
        total_loss = self.lambda_rd * distortion + rate_proxy
        return total_loss, distortion, rec_frame
```

## Critical Hyperparameters
- **Lambda Rate-Distortion Parameter (\(\lambda\))**: Choose \(\lambda \in \{256, 512, 1024, 2048\}\) to train distinct quality operating points on the RD curve.
- **GOP (Group of Pictures) Length**: Train with GOP lengths of 7 to 32 frames using multi-frame progressive unrolling.
