---
id: recipe:gated-deltanet-2
type: recipe
title: "Gated DeltaNet 2 Training Recipe"
method: method:gated-deltanet-2
task: task:linear-time-sequence-modeling
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / FLA"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - linear-attention
---

# Gated DeltaNet 2 Training Recipe

```python
import torch

print("Gated DeltaNet 2 kernel initialized")
```
