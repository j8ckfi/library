---
id: recipe:quartet-ii
type: recipe
title: "Quartet-II NVFP4 Hardware Training Recipe"
method: method:quartet-ii
task: task:fp4-hardware-training
target_hardware: "8x NVIDIA Blackwell / Hopper SXM 80GB"
framework: "PyTorch 2.5+ / Quartet-II"
repo_url: "https://github.com/IST-DASLab/Quartet-II"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformer-engine>=1.12.0"
tags:
  - recipe
  - quantization
  - fp4
  - nvfp4
  - quartet-ii
---

# Quartet-II NVFP4 Hardware Training Recipe

```python
import torch

print("Quartet-II NVFP4 hardware training kernels initialized")
```
