---
id: method:anlr-lora
type: method
title: "AnLR-LoRA"
category: "peft"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "24GB quality LoRA is the library task"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; AnLR is a per-rank LR plug-in"
    use_instead: "method:lr-matters-lora"
  - when: "RLVR-stable rank-normalized LoRA A"
    reason: "NoRA normalizes A; AnLR rescales per-rank LRs"
    use_instead: "method:nora"
  - when: "4-bit PEFT stack"
    reason: "AnLR is not a quantization recipe"
    use_instead: "method:aqlora-q"
assumptions:
  - "AdamW LoRA. Per-rank factors are mean-normalized inside each module so the global LR is unchanged."
last_reviewed: "2026-09-09"
papers:
  - paper:anlr-lora
recipes:
  - recipe:anlr-lora
claims:
  - benchmark: "Commonsense / NLG / visual instruction-tuning vs uniform-LR LoRA"
    metric: "task scores vs LoRA"
    value: "consistent lift; robust across global LR; transfers to other LoRA variants"
    baseline: "uniform-LR LoRA"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05885"
    notes: "No extra trainable parameters. Not a completed supersession of method:lr-matters-lora."
tags:
  - peft
  - lora
  - anlr-lora
  - active
---

# AnLR-LoRA

## Method Overview
AnLR-LoRA gives each LoRA rank-one component its own effective learning rate from function-space velocity and Adam SNR, then mean-normalizes per module. Active beside NoRA (rank-normalize A) and lr-matters-lora (global LR sweep). Does not replace either.

## When to Use
- Uniform-LR LoRA underuses rank (collapsed singular spectrum).

## When NOT to Use
- 24GB quality protocol → `method:lr-matters-lora`. RLVR-stable A → `method:nora`.

## Relation to Existing SOTA
- Active on `task:lora-quality-tuning` / `task:parameter-efficient-fine-tuning`. Does **not** supersede `method:lr-matters-lora` or `method:nora`.

## Gotchas & Failure Modes
- No official GitHub as of 2026-09-09.
- Still sweep the global LR; AnLR does not replace that sweep.
