---
id: recipe:delora-finetuning
type: recipe
title: "Robust Low-Rank Adaptation with DeLoRA"
method: method:delora
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB)"
framework: "PyTorch 2.5+ / Hugging Face PEFT"
repo_url: "https://github.com/ExplainableML/DeLoRA"
pip_dependencies:
  - "torch>=2.5.0"
  - "peft>=0.10.0"
  - "transformers>=4.48.0"
tags:
  - peft
  - delora
---

# Robust Low-Rank Adaptation with DeLoRA

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 (24GB) or A100 (80GB).
- PEFT Version: `peft` with `DeloraConfig`.

## Quickstart Code

```python
import torch
from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

def setup_delora(model_id: str = "meta-llama/Meta-Llama-3-8B"):
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")
    config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        bias="none",
        task_type="CAUSAL_LM"
    )
    peft_model = get_peft_model(model, config)
    return peft_model
```
