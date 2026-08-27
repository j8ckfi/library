---
id: recipe:aqlora
type: recipe
title: "AQLoRA-Q 4-Bit Training Recipe"
method: method:aqlora-q
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x H100 80GB)"
framework: "PyTorch 2.5+ / AQLoRA"
repo_url: "https://github.com/Romyull-Islam/AQLoRA"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - peft
  - 4bit
  - aqlora
---

# AQLoRA-Q 4-Bit Training Recipe

```python
import torch

print("AQLoRA-Q 4-bit quantized adapter training pipeline initialized")
```
