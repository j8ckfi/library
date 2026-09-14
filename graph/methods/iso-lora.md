---
id: method:iso-lora
type: method
title: "Iso-LoRA (Rank-Efficient Tangent-Space LoRA)"
category: "peft"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "24GB quality LoRA is the library task"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; Iso-LoRA is an optimizer for rank utilization"
    use_instead: "method:lr-matters-lora"
  - when: "RLVR-stable rank-normalized LoRA A"
    reason: "NoRA normalizes A; Iso-LoRA spectrally couples BA updates"
    use_instead: "method:nora"
  - when: "anisotropic per-rank LR under AdamW"
    reason: "AnLR rescales per-rank LRs; Iso-LoRA changes the descent geometry"
    use_instead: "method:anlr-lora"
  - when: "4-bit PEFT stack"
    reason: "Iso-LoRA is not a quantization recipe"
    use_instead: "method:aqlora-q"
assumptions:
  - "Standard LoRA Delta W = BA. Paper: 0.1B-7B language-model adaptation. Strongest gains at moderate-to-large nominal rank."
  - "No official GitHub as of 2026-09-14."
last_reviewed: "2026-09-14"
papers:
  - paper:iso-lora
recipes:
  - recipe:iso-lora
claims:
  - benchmark: "LLaMA-2-7B GSM8K EM, LoRA rank 128"
    metric: "exact match %"
    value: 61.87
    baseline: "Full FT 59.52 / LoRA-Pro 59.20 / LoRA-Muon 59.12 / LoRA rank 8 45.39"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12123"
    notes: "Iso-LoRA rank 8/32/128 = 54.94/58.12/61.87. AdamW underuses rank; Muon uses more directions. Not a completed supersession of lr-matters-lora."
tags:
  - peft
  - lora
  - optimizer
  - iso-lora
  - active
---

# Iso-LoRA (Rank-Efficient Tangent-Space LoRA)

## Method Overview
Nominal rank is capacity; the optimizer decides utilization. AdamW LoRA updates are often low effective-rank. Iso-LoRA runs spectral descent on the induced weight-space perturbation \(BA\) so singular energy spreads, without changing the LoRA parameterization.

## When to Use
- LoRA ranks where AdamW's update spectrum has already collapsed and raising rank stopped helping.

## When NOT to Use
- 24GB quality protocol → `method:lr-matters-lora`. RLVR-stable A → `method:nora`. Per-rank LR → `method:anlr-lora`. 4-bit → `method:aqlora-q`.

## Relation to Existing SOTA
- Active beside NoRA / AnLR-LoRA on `task:lora-quality-tuning` and `task:parameter-efficient-fine-tuning`. Does **not** supersede `method:lr-matters-lora`.

## Gotchas & Failure Modes
- Gains grow with nominal rank; rank-8 is not the paper's headline.
- No public optimizer implementation as of 2026-09-14.
- Still sweep the global LR; Iso-LoRA is not a substitute for that sweep.
