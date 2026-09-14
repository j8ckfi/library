---
id: recipe:tiny-aya-l2-thinker
type: recipe
title: "Tiny Aya L2-Thinker Mix"
method: method:tiny-aya-l2-thinker
task: task:multilingual-l2-reasoning-sft
target_hardware: "3.35B SFT box (released weights; train recipe is paper-only)"
framework: "Transformers / Cohere2"
repo_url: none found
code_status: partial
pip_dependencies:
  - "transformers"
  - "huggingface_hub"
tags:
  - recipe
  - multilingual
  - l2-reasoning
  - aya
---

# Tiny Aya L2-Thinker Mix

## Hardware & Environment Setup
- Weights: `https://huggingface.co/CohereLabs/tiny-aya-l2-thinker`
- English sibling: `https://huggingface.co/CohereLabs/tiny-aya-en-thinker`
- Base: `https://huggingface.co/CohereLabs/tiny-aya-base-32K`
- Data: `https://huggingface.co/datasets/CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning`
- No official train GitHub as of 2026-09-14. Instruct default stays OLMo-3. Pass@1 stays CISPO.

## Quickstart Implementation

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

name = "CohereLabs/tiny-aya-l2-thinker"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name, device_map="auto")
prompt = "Solve in the language of the question: 15 の 12% はいくつですか。"
out = model.generate(**tok(prompt, return_tensors="pt").to(model.device), max_new_tokens=256)
print(tok.decode(out[0], skip_special_tokens=True))
```

Mix to reproduce (paper): English reasoning backbone + multilingual reasoning traces in a language subset + multilingual non-reasoning for held-out L2 transfer. Schedule jointly; do not drop NR.

## Critical Hyperparameters & Tuning Advice
- Optimize L2 rate and task accuracy together. Do not chase PolyMath against Qwen3.5-4B.
- For held-out languages, coverage in NR matters more than extra MR languages of the same family.
