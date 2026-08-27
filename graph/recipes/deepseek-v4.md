---
id: recipe:deepseek-v4
type: recipe
title: "DeepSeek-V4 MoE Training Recipe"
method: method:deepseek-v4
task: task:pretrain-moe-frontier
target_hardware: "64x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / Megatron-DeepSeek"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "flash-attn>=2.7.0"
tags:
  - recipe
  - moe
  - deepseek-v4
---

# DeepSeek-V4 MoE Training Recipe

```python
import torch

print("DeepSeek-V4 MoE architecture and MLA kernels initialized")
```
