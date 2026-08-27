---
id: recipe:scaleq-158
type: recipe
title: "ScaleQ-1.58 Post-Training Ternarization Recipe"
method: method:scaleq-158
task: task:post-training-ternary-quantization
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100 80GB)"
framework: "PyTorch 2.5+ / BitTern"
repo_url: "https://github.com/IntelChina-AI/BitTern"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - quantization
  - ternary
  - scaleq-158
---

# ScaleQ-1.58 Post-Training Ternarization Recipe

```python
import torch

print("ScaleQ-1.58 post-training ternarization pipeline loaded")
```
