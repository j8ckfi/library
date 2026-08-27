---
id: recipe:glm-5
type: recipe
title: "GLM-5 Pretraining Recipe"
method: method:glm-5
task: task:pretrain-moe-frontier
target_hardware: "32x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/zai-org/GLM-5"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - architecture
  - glm-5
---

# GLM-5 Pretraining Recipe

```python
import torch

print("GLM-5 training recipe loaded")
```
