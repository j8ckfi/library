---
id: recipe:simpo-alignment
type: recipe
title: "Offline Direct Preference Alignment with SimPO via TRL"
method: method:simpo
task: task:direct-preference-alignment
target_hardware: "1x or 2x NVIDIA A100 / H100 (80GB)"
framework: "PyTorch 2.5+ / Hugging Face TRL / Transformers"
repo_url: "https://github.com/huggingface/trl"
pip_dependencies:
  - "torch>=2.5.0"
  - "trl>=0.14.0"
  - "transformers>=4.48.0"
tags:
  - post-training
  - preference-alignment
  - simpo
---

# Offline Direct Preference Alignment with SimPO via TRL

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA H100 80GB (or 2x A100 80GB with FSDP).
- Software: PyTorch 2.5.0+, Hugging Face TRL 0.14.0+.

## Quickstart Code

```python
from trl import CPOConfig, CPOTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset

# SimPO is executed natively in TRL via CPOTrainer with loss_type="simpo"
def train_simpo():
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    
    training_args = CPOConfig(
        output_dir="./simpo_llama3_output",
        loss_type="simpo",          # Enables SimPO length-normalized margin objective
        beta=2.0,                   # SimPO beta scaling parameter
        simpo_gamma=1.4,            # Target margin gamma
        learning_rate=5e-7,
        lr_scheduler_type="cosine",
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        max_length=2048,
        max_prompt_length=1024,
        bf16=True,
        logging_steps=10
    )

    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="bfloat16", device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # dataset = load_dataset("princeton-nlp/llama3-ultrafeedback-armorm", split="train")

    # trainer = CPOTrainer(
    #     model=model,
    #     args=training_args,
    #     train_dataset=dataset,
    #     tokenizer=tokenizer
    # )
    # trainer.train()

if __name__ == "__main__":
    print("SimPO setup configured.")
```

## Critical Hyperparameters
- **`simpo_gamma` (Target Margin \(\gamma\))**: 1.0 to 1.5 (default: 1.4).
- **`beta` (\(\beta\))**: 2.0 to 2.5.
- **Learning Rate**: 3e-7 to 1e-6 (lower than standard SFT).
