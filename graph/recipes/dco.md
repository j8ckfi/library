---
id: recipe:dco
type: recipe
title: "DCO Layer-Selective Instruct Fine-Tune"
method: method:dco
task: task:instruct-sft-alignment
target_hardware: "8x NVIDIA H200 (paper); 8x GPU LLaMA-Factory freeze for the zh-en demo"
framework: "PyTorch / LLaMA-Factory freeze SFT"
repo_url: "https://github.com/CONE-MT/DCO"
pip_dependencies:
  - "torch>=2.5.0"
  - "llamafactory"
  - "deepspeed"
  - "transformers"
tags:
  - recipe
  - dco
  - sft
  - lst
---

# DCO Layer-Selective Instruct Fine-Tune

## Hardware & Environment Setup
- Official repo: `https://github.com/CONE-MT/DCO` (confirmed 2026-09-16). Weights: `https://huggingface.co/collections/LLaMAX/dco`.
- Install LLaMA-Factory, then run two-stage freeze SFT (`finetuning_type: freeze`). Demo: `dco/qwen3_en_zh.sh` on `LLaMAX/bilingual_zh_en`. General launcher: `specialist_distillation/multilingualism/lst_scripts/submit_lst.sh` (`--bottom-layers 4 --top-layers 16`).
- Instruct default stays OLMo-3 Dolci. LoRA quality stays vanilla LoRA + rsLoRA + LR sweep. This recipe only picks which layers move under a drift budget.

## Quickstart Implementation

```python
from __future__ import annotations


def lst_freeze_spec(bottom: int, top: int, stage: int) -> dict[str, object]:
    """LLaMA-Factory freeze: negative N trains the first N layers; positive N the last N."""
    if stage == 1:
        return {
            "finetuning_type": "freeze",
            "freeze_trainable_layers": -bottom,
            "freeze_trainable_modules": "all",
        }
    if stage == 2:
        return {
            "finetuning_type": "freeze",
            "freeze_trainable_layers": top,
            "freeze_trainable_modules": "all",
        }
    raise ValueError(f"stage must be 1 or 2, got {stage}")


def directional_efficiency(delta_task: float, kl: float) -> float:
    """Paper's empirical η = ΔTask / sqrt(KL) at matched drift."""
    if kl <= 0:
        raise ValueError("KL must be positive to compare directions")
    return delta_task / (kl ** 0.5)
```

Two-stage train (from the repo scripts):

```bash
git clone https://github.com/CONE-MT/DCO
# After LlamaFactory is installed and bilingual_zh_en is registered:
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
  bash dco/qwen3_en_zh.sh bilingual_zh_en 4 8 1 /path/to/Qwen3-8B 42 2048 4
```

Defaults: stage-1 first 4 layers, stage-2 last 8, 1 epoch, lr `5e-5`, seed 42. Paper translation probe also reports b4t12 / b4t16. Keep `lm_head` / embeddings frozen unless you are measuring that ablation.

## Critical Hyperparameters & Tuning Advice
- Sweep split families (b4t8, b4t12, b4t16) at matched anchored KL, not matched step count. Low-drift $\to$ split; larger budget $\to$ contiguous bottom blocks can win accuracy at worse efficiency.
- QA-only data is allowed; keep the instruct chat template so inference still emits CoT.
- Do not treat LST as a LoRA replacement. Do not retarget CISPO for the later RL pass; DCO is the SFT init.
