---
id: recipe:mxfp4-mi355x
type: recipe
title: "MXFP4 Microscaling Training Recipe"
method: method:mxfp4-mi355x
task: task:fp4-hardware-training
target_hardware: "8x AMD Instinct MI355X / NVIDIA Blackwell"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - quantization
  - fp4
  - mxfp4
---

# MXFP4 Microscaling Training Recipe

```python
import torch

print("MXFP4 microscaling tensor cores initialized")
```
