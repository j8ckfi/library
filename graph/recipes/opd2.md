---
id: recipe:opd2
type: recipe
title: "OPD2 Multi-Teacher Distillation Recipe"
method: method:opd2
task: task:student-distillation
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/naver-ai/opd2"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - distillation
  - opd2
---

# OPD2 Multi-Teacher Distillation Recipe

```python
import torch

print("OPD2 multi-teacher routing initialized")
```
