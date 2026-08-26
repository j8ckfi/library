---
id: recipe:qlora-peft
type: recipe
title: "Memory-Efficient 4-bit Fine-Tuning with QLoRA & BitsAndBytes"
method: method:qlora
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 3090 / 4090 (24GB VRAM)"
framework: "PyTorch 2.5+ / bitsandbytes / PEFT"
repo_url: "https://github.com/Artidoro/qlora"
pip_dependencies:
  - "torch>=2.5.0"
  - "bitsandbytes>=0.43.0"
  - "peft>=0.9.0"
  - "transformers>=4.48.0"
tags:
  - peft
  - quantization
  - qlora
  - consumer-gpu
---

# Memory-Efficient 4-bit Fine-Tuning with QLoRA & BitsAndBytes

## Hardware & Environment Setup
- Target Hardware: Single 24GB GPU (RTX 3090/4090/A5000) for models up to 33B.
- Software: `bitsandbytes>=0.43.0`, `peft>=0.9.0`.

## Quickstart Code

```python
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

def setup_qlora_pipeline(model_id: str = "meta-llama/Meta-Llama-3-8B"):
    # 1. Configure 4-bit NormalFloat (NF4) quantization with Double Quantization
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    # 2. Load quantized base model
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto"
    )

    # 3. Freeze base weights and cast layer norms to FP32
    model = prepare_model_for_kbit_training(model)

    # 4. Attach 16-bit LoRA adapter matrices
    peft_config = LoraConfig(
        r=64,
        lora_alpha=16,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )

    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    return model
```

## Critical Hyperparameters
- **Compute Dtype**: Always set `bnb_4bit_compute_dtype=torch.bfloat16` on Ampere/Hopper/Ada GPUs to avoid FP16 underflow.
- **Optimizer**: Use `paged_adamw_8bit` or `paged_adamw_32bit` to prevent OOM errors during gradient accumulation peaks.
