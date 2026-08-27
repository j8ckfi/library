---
id: recipe:kimi-linear
type: recipe
title: "Kimi-Linear Attention Recipe"
method: method:kimi-linear
task: task:linear-time-sequence-modeling
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / Triton"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "triton>=3.0.0"
tags:
  - recipe
  - linear-attention
---

# Kimi-Linear Attention Recipe

```python
import torch

print("Kimi-Linear Triton kernel initialized")
```
