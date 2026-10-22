---
id: method:normtune
type: method
title: 'NormTune'
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:lora-quality-tuning'
  reason: 'NormTune is an active plug-in; method:lr-matters-lora remains the first hop'
  use_instead: method:lr-matters-lora
assumptions:
- 'PEFT host (LoRA/Bone/MoRA). Adaptive strengthening of low-norm layers. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:normtune
recipes:
- recipe:normtune
claims:
- benchmark: 'AIME 2024 / MATH-500 / GPQA / AIME 2025 vs LoRA, Bone, MoRA'
  metric: 'average accuracy vs host PEFT'
  value: '+24.24 / +11.33 / +16.21 vs LoRA / Bone / MoRA; rank-256 hosts still gain +2.17 / +0.93 / +3.00'
  baseline: 'LoRA; Bone; MoRA'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29134'
  notes: 'Does not retarget method:lr-matters-lora.'
tags:
- peft
- lora
- active
---

# NormTune

## Method Overview
NormTune watches per-layer weight-update norms during PEFT and adaptively strengthens layers that stay far below full-FT update scale, which the paper ties to reasoning-token under-adaptation.

## When to Use
- Reasoning PEFT where LoRA/Bone/MoRA keep Pass@1 well below full FT because some layers barely move.

## When NOT to Use
24GB quality default → `method:lr-matters-lora`. RLVR-stable LoRA candidate → `method:nora`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:lr-matters-lora`.

## Gotchas & Failure Modes
- Does not replace an LR sweep.
- No public code.
