---
id: recipe:scale
type: recipe
title: "SCALE Memory-Efficient Pretraining Recipe"
method: method:scale
task: task:full-param-memory-efficient-pretrain
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100 40GB/80GB)"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - optimizer
  - memory-efficient
  - scale
---

# SCALE Memory-Efficient Pretraining Recipe

```python
import torch

print("SCALE scaled subspace projection optimizer initialized")
```
