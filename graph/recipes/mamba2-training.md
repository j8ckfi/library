---
id: recipe:mamba2-training
type: recipe
title: "Pretraining Linear-Time Sequence Models with Mamba-2 (SSD)"
method: method:mamba-2
task: task:linear-time-sequence-modeling
target_hardware: "8x NVIDIA A100 / H100 (SXM)"
framework: "PyTorch 2.5+ / Triton / causal-conv1d"
repo_url: "https://github.com/state-spaces/mamba"
pip_dependencies:
  - "torch>=2.5.0"
  - "mamba-ssm>=2.2.2"
  - "causal-conv1d>=1.4.0"
tags:
  - state-space
  - architecture
  - linear-attention
---

# Pretraining Linear-Time Sequence Models with Mamba-2 (SSD)

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB SXM.
- Minimum CUDA: 12.3+.
- Required Dependencies: `mamba-ssm`, `causal-conv1d`, and `torch`.

## Quickstart Code

```python
import torch
import torch.nn as nn
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

# Initialize Mamba-2 language model backbone
def initialize_mamba2_model(
    d_model: int = 2048,
    n_layer: int = 32,
    vocab_size: int = 32000,
    ssm_cfg: dict = None
):
    if ssm_cfg is None:
        ssm_cfg = {
            "d_state": 128,          # SSM state dimension
            "d_conv": 4,             # 1D convolution kernel size
            "expand": 2,             # Expansion factor
            "headdim": 64,           # Head dimension for SSD chunking
            "ngroups": 1             # Group count
        }

    model = MambaLMHeadModel(
        d_model=d_model,
        n_layer=n_layer,
        vocab_size=vocab_size,
        ssm_cfg=ssm_cfg,
        device="cuda",
        dtype=torch.bfloat16
    )
    return model

# Example forward pass with chunked SSD computation
if __name__ == "__main__" and torch.cuda.is_available():
    model = initialize_mamba2_model()
    input_ids = torch.randint(0, 32000, (4, 4096), device="cuda")
    outputs = model(input_ids)
    loss = nn.CrossEntropyLoss()(outputs.logits.view(-1, 32000), input_ids.view(-1))
    loss.backward()
    print(f"Mamba-2 step complete. Loss: {loss.item():.4f}")
```

## Critical Hyperparameters
- **SSM State Dimension (`d_state`)**: 64–128.
- **Head Dimension (`headdim`)**: 64 (optimal for Tensor Core matrix multiplication chunks).
- **Optimizer**: AdamW (lr 6e-4) or Muon (lr 0.02) with cosine decay.
