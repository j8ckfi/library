---
id: recipe:beft
type: recipe
title: "BEFT Binarized PEFT Recipe"
method: method:beft
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 4090 24GB"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - peft
  - binarization
---

# BEFT Binarized PEFT Recipe

```python
import torch

print("BEFT binarized adapter initialized")
```
