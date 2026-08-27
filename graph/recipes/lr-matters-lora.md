---
id: recipe:lr-matters-lora
type: recipe
title: "Vanilla LoRA + rsLoRA Quality Recipe"
method: method:lr-matters-lora
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100/H100)"
framework: "PyTorch 2.5+ / PEFT"
repo_url: "https://github.com/yuang-lee/lr-matters-lora"
pip_dependencies:
  - "torch>=2.5.0"
  - "peft>=0.14.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - peft
  - lora
  - rslora
---

# Vanilla LoRA + rsLoRA Quality Recipe

```python
from peft import LoraConfig, get_peft_model

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    use_rslora=True, # Rank-stabilized LoRA scaling
    lora_dropout=0.05,
    bias="none",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)
```
