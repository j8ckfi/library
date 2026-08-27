---
id: recipe:sapo
type: recipe
title: "SAPO MoE/VL RL Training Recipe"
method: method:sapo
task: task:math-code-rl-moe
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / ms-swift"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "ms-swift>=3.0.0"
tags:
  - recipe
  - rl-alignment
  - sapo
---

# SAPO MoE/VL RL Training Recipe

```python
# Launch SAPO with ms-swift:
# swift rlhf --rlhf_type grpo --loss_type sapo --model Qwen/Qwen2.5-7B-Instruct
print("SAPO ms-swift recipe loaded")
```
