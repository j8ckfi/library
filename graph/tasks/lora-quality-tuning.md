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
  - method:dt-lora
  - method:lr-matters-lora
  - method:lora-unified-study
  - method:super-tuning
  - method:dora
  - method:delora
  - method:lora
  - method:nora
  - method:anlr-lora
  - method:iso-lora
  - method:read-lora
last_reviewed: '2026-10-14'
redirects:
  - when: "stacking independently trained LoRA adapters / sequential skill add without an inference router"
    to: "task:lora-skill-composition"
  - when: "dynamic tangent LoRA branch via residual-gradient SVD (not rsLoRA + LR sweep)"
    to: "method:dt-lora"
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
- **Active optimizer-shape / effective-rank note**: `method:iso-lora` (`arXiv:2609.12123`). AdamW vs SGD/Muon effective rank. Does not replace the LR-sweep quality default.
- **Not this task (stack independently trained adapters)**: `method:read-lora` on `task:lora-skill-composition` (`arXiv:2609.31600`). Does not retarget the LR-sweep quality default.
- **Optional dynamic-tangent LoRA (not this quality default)**: `method:dt-lora` (`arXiv:2610.17730`). VTAB-1K 76.2 vs LoRA 75.7; COCO r=16 avg 46.6 (+8.2). GitHub Snipine/DT-LoRA announced. Does **not** supersede vanilla LoRA + rsLoRA + LR sweep.
