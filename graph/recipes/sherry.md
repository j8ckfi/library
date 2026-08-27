---
id: recipe:sherry
type: recipe
title: "Sherry AngelSlim Quantization Recipe"
method: method:sherry
task: task:1bit-extreme-quantization
target_hardware: "1x NVIDIA RTX 4090 24GB"
framework: "PyTorch 2.5+ / AngelSlim"
repo_url: "https://github.com/Tencent/AngelSlim"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - quantization
  - angelslim
---

# Sherry AngelSlim Quantization Recipe

```python
import torch

print("Sherry AngelSlim low-bit quantization pipeline loaded")
```
