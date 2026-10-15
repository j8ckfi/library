---
id: method:dt-lora
type: method
title: DT-LoRA (Dynamic Tangent LoRA)
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-adapter quality LoRA / rsLoRA + LR sweep rather than tangent-space branches
  reason: Vanilla LoRA + rsLoRA + LR sweep remains the 24GB quality default
  use_instead: method:lr-matters-lora
- when: two-stage residual-gradient complementary LoRA (ReGRA)
  reason: DT-LoRA is a live tangent branch; ReGRA initializes a second adapter after stage 1
  use_instead: method:regra
- when: stacking independently trained LoRA adapters
  reason: READ owns skill composition
  use_instead: method:read-lora
assumptions:
- Vision / detection LoRA in the paper (VTAB-1K, COCO). Randomized SVD of residual
  gradients.
- GitHub Snipine/DT-LoRA announced (no trainer) as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:dt-lora
recipes:
- recipe:dt-lora
claims:
- benchmark: VTAB-1K; COCO r=16; residual energy outside LoRA tangent
  metric: accuracy / avg; ρ outside tangent
  value: VTAB-1K 76.2 vs LoRA 75.7; COCO r=16 avg 46.6 (+8.2 vs LoRA); ρ 85.4–96.9%
  baseline: LoRA (single-paper; not rsLoRA+LR sweep)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.17730
  notes: Does not supersede vanilla LoRA + rsLoRA + LR sweep.
tags:
- peft
- lora
- tangent-space
- active
---

# DT-LoRA (Dynamic Tangent LoRA)

## Method Overview
Keep a stable LoRA branch. Add a dynamic branch from matrix-free randomized SVD of residual gradients that sit outside the current tangent.

## When to Use
- Residual gradients keep leaving LoRA's tangent and a modest extra branch is acceptable.

## When NOT to Use
24GB quality default → `method:lr-matters-lora`. 4-bit PEFT stack → `method:aqlora-q`. Multi-skill fold → `method:read-lora`.

## Relation to Existing SOTA
Active plug-in on `task:lora-quality-tuning` (`sota_for: []`). Does **not** supersede vanilla LoRA + rsLoRA + LR sweep.

## Gotchas & Failure Modes
- **code: announced** (Snipine/DT-LoRA stub) as of 2026-10-14.
- Vision/detection paper; not an LLM 24GB bake-off vs rsLoRA + LR sweep.
