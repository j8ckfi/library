---
id: recipe:spikingjelly-snn
type: recipe
title: "Direct Training of Deep Spiking Neural Networks with SpikingJelly"
method: method:surrogate-gradient-snn
task: task:spiking-neural-networks-training
target_hardware: "1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB)"
framework: "PyTorch 2.5+ / SpikingJelly (>=0.0.0.0.14)"
repo_url: "https://github.com/fangwei123456/spikingjelly"
pip_dependencies:
  - "torch>=2.5.0"
  - "spikingjelly>=0.0.0.0.14"
tags:
  - snn
  - neuromorphic
  - spikingjelly
  - surrogate-gradient
---

# Direct Training of Deep Spiking Neural Networks with SpikingJelly

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100 GPU.
- PyTorch & SpikingJelly: `pip install spikingjelly`.

## Quickstart Code

```python
import torch
import torch.nn as nn
from spikingjelly.activation_based import neuron, functional, surrogate, layer

class DeepSpikingNet(nn.Module):
    """Deep Spiking Neural Network trained with multi-step surrogate gradients."""
    def __init__(self, channels: int = 128, num_classes: int = 10, T: int = 4):
        super().__init__()
        self.T = T
        
        # Leaky Integrate-and-Fire neuron with smooth Arctan surrogate gradient
        surrogate_fn = surrogate.ATan(alpha=2.0)
        
        self.conv_net = nn.Sequential(
            layer.Conv2d(3, channels, kernel_size=3, padding=1, bias=False),
            layer.BatchNorm2d(channels),
            neuron.LIFNode(tau=2.0, v_threshold=1.0, surrogate_function=surrogate_fn, step_mode='m'),
            
            layer.MaxPool2d(2, 2),
            
            layer.Conv2d(channels, channels * 2, kernel_size=3, padding=1, bias=False),
            layer.BatchNorm2d(channels * 2),
            neuron.LIFNode(tau=2.0, v_threshold=1.0, surrogate_function=surrogate_fn, step_mode='m'),
            
            layer.AdaptiveAvgPool2d((1, 1)),
            layer.Flatten(),
            layer.Linear(channels * 2, num_classes, bias=False),
            neuron.LIFNode(tau=2.0, v_threshold=1.0, surrogate_function=surrogate_fn, step_mode='m')
        )

    def forward(self, x_seq: torch.Tensor) -> torch.Tensor:
        # x_seq shape: [T, Batch, C, H, W]
        # Multi-step execution over T timesteps
        out_spikes = self.conv_net(x_seq)
        # Average firing rate across timesteps for classification logits
        return out_spikes.mean(dim=0)

def train_snn_step(model, optimizer, criterion, x, y, T=4):
    optimizer.zero_grad()
    # Repeat static image over T timesteps (or use direct DVS event frames)
    x_seq = x.unsqueeze(0).repeat(T, 1, 1, 1, 1)
    
    out = model(x_seq)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()
    
    # CRITICAL: Reset neuron membrane potentials after each batch
    functional.reset_net(model)
    return loss.item()
```

## Critical Hyperparameters
- **Timesteps (\(T\))**: \(T=4\) to \(T=8\) gives high accuracy with minimal temporal latency.
- **Surrogate Function**: `surrogate.ATan(alpha=2.0)` or `surrogate.FastSigmoid()`.
- **Neuron State Reset**: Always invoke `functional.reset_net(model)` after every training/eval step to clear historical membrane potential accumulation.
