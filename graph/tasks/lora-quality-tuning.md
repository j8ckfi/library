---
id: task:lora-quality-tuning
type: task
title: "LoRA Quality Tuning on Single GPU"
domain: "efficiency"
summary: "Maximizing accuracy and representation retention during single-GPU low-rank adaptation without parameter bloat."
current_sota:
  - method: method:lr-matters-lora
    as_of: "2026-08-26"
    benchmark: "Single GPU PEFT / MMLU / GSM8k"
    metric: "accuracy vs parameter overhead"
    value: "Matches/exceeds DoRA"
    notes: "Vanilla LoRA + rsLoRA + LR sweep (2602.04998, 2601.22708) NOT DoRA."
methods:
  - method:lr-matters-lora
  - method:lora-unified-study
  - method:super-tuning
  - method:dora
  - method:delora
  - method:lora
  - method:nora
  - method:anlr-lora
last_reviewed: "2026-09-09"
tags:
  - efficiency
  - peft
  - lora
  - quality
---

# LoRA Quality Tuning on Single GPU

## SOTA Recommendation (as of 2026-09-01)
- Use **Vanilla LoRA + rsLoRA + LR sweep** (`method:lr-matters-lora`, 2602.04998, 2601.22708) — NOT DoRA. Unchanged.
- **Recommended upgrade candidate** for RLVR-stable adapters: `method:nora` (`arXiv:2608.31036`). Status active; not a first-hop replacement of the LR-sweep quality default.
- **Optional anisotropic per-rank LR**: `method:anlr-lora` (`arXiv:2609.05885`). Active beside NoRA. Does not replace the LR sweep.
