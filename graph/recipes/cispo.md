---
id: recipe:cispo
type: recipe
title: "CISPO Dense Reasoning RL Recipe"
method: method:cispo
task: task:math-code-rl-dense
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / MiniMax-M1"
repo_url: "https://github.com/MiniMax-AI/MiniMax-M1"
pip_dependencies:
  - "torch>=2.5.0"
  - "vllm>=0.7.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - rl-alignment
  - cispo
---

# CISPO Dense Reasoning RL Recipe

```python
import torch

print("CISPO MiniMax-M1 / ScaleRL reasoning RL recipe loaded")
```
