---
id: recipe:nemotron-3-super-latentmoe
type: recipe
title: "Nemotron-3 Super Latent MoE Recipe"
method: method:nemotron-3-super-latentmoe
task: task:pretrain-moe-frontier
target_hardware: "32x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - moe
---

# Nemotron-3 Super Latent MoE Recipe

```python
import torch

print("Nemotron-3 Super Latent MoE initialized")
```
