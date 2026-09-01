---
id: recipe:nora
type: recipe
title: "NoRA Normalized LoRA Recipe"
method: method:nora
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA GPU 24GB+"
framework: "PyTorch / HuggingFace PEFT fork"
repo_url: "https://github.com/Joluck/NoRA"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - peft
  - lora
  - nora
---

# NoRA Normalized LoRA Recipe

## Hardware & Environment Setup
- Install the PEFT fork (replaces the environment `peft` package):

```bash
git clone https://github.com/Joluck/NoRA.git
cd NoRA/peft
pip install .
```

## Quickstart Implementation

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=8,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    use_nora=True,
)
model = get_peft_model(base_model, config)
```

Init-only variant: `use_nora="init"`. BIMI: `init_lora_weights="bimi"` (columns already unit-norm). Rank-dimension column norms of `lora_A` are the constraint; set `lora_alpha=r`.

## Critical Hyperparameters & Tuning Advice
- `lora_alpha = r` so scaling is 1 after unit-column $A$.
- `use_nora=True` for per-forward normalization; `"init"` if the forward cannot change.
- RLVR: enable the same flag on the PeRL / PEFT adapter path. Do not swap in PiSSA/MiLoRA for RLVR.
- Quality-default 24GB LoRA without an RLVR-stability requirement remains vanilla LoRA + rsLoRA + LR sweep.
