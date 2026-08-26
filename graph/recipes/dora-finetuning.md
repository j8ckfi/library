---
id: recipe:dora-finetuning
type: recipe
title: "Fine-Tuning Foundation Models with DoRA via Hugging Face PEFT"
method: method:dora
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA A100 80GB or 1x RTX 4090 (24GB)"
framework: "PyTorch 2.5+ / Hugging Face PEFT (>=0.9.0)"
repo_url: "https://github.com/huggingface/peft"
pip_dependencies:
  - "torch>=2.5.0"
  - "peft>=0.9.0"
  - "transformers>=4.48.0"
  - "accelerate>=1.2.0"
tags:
  - peft
  - dora
  - fine-tuning
---

# Fine-Tuning Foundation Models with DoRA via Hugging Face PEFT

## Hardware & Environment Setup
- Target Hardware: 1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB).
- PEFT Version: `peft>=0.9.0` (native `use_dora=True` support).

## Quickstart Code

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType

def setup_dora_model(model_id: str = "meta-llama/Meta-Llama-3-8B"):
    # 1. Load base model in bfloat16
    base_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )

    # 2. Configure DoRA (Weight-Decomposed Low-Rank Adaptation)
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
        use_dora=True               # Enables DoRA magnitude-direction decomposition
    )

    # 3. Wrap model with DoRA adapters
    model = get_peft_model(base_model, peft_config)
    model.print_trainable_parameters()
    return model

# Merge adapters back into base model post-training (zero inference overhead):
def merge_and_export(dora_model):
    merged_model = dora_model.merge_and_unload()
    return merged_model
```

## Critical Hyperparameters
- **Rank (\(r\))**: 16–32 with \(\alpha = 2r\).
- **Target Modules**: Apply across all linear projections (Attention + MLP layers) for full fine-tuning parity.
- **Learning Rate**: 1e-4 to 2e-4 with AdamW.
