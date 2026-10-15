---
id: method:regra
type: method
title: ReGRA
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-adapter quality LoRA / rsLoRA + LR sweep rather than staged residual adapters
  reason: Vanilla LoRA + rsLoRA + LR sweep remains the 24GB quality default
  use_instead: method:lr-matters-lora
- when: dynamic tangent LoRA branch via residual-gradient SVD
  reason: DT-LoRA is a live tangent branch; ReGRA is a two-stage complementary adapter
  use_instead: method:dt-lora
assumptions:
- Two sequential LoRA stages at a fixed total rank. Residual gradients after stage 1 initialize stage 2; orthogonality regularizer; both merge at deploy.
- Code Fanyao-Li/ReGRA released as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:regra
recipes:
- recipe:regra
claims:
- benchmark: RoBERTa-base/large GLUE; Llama-3-8B math
  metric: GLUE avg / math accuracy vs LoRA at matched or 2x rank
  value: base 84.74 vs LoRA r=8 83.21 / r=16 83.97; large 88.42 vs 87.73/87.75; Llama-3-8B math 72.14 vs 70.83
  baseline: LoRA r=8 and r=16 (single-paper; not rsLoRA+LR sweep)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19700
  notes: Distinct from DT-LoRA. Does not supersede vanilla LoRA + rsLoRA + LR sweep.
tags:
- peft
- lora
- residual-gradient
- active
---

# ReGRA

## Method Overview
Train a first LoRA, then estimate task gradients on a calibration set and remove their projections onto the stage-1 two-sided subspace. Aggregate residual-gradient directions to initialize a second adapter. An orthogonality regularizer keeps the two updates complementary. Merge both into the base weights at inference.

## When to Use
- Fixed-rank LoRA where extra rank past the top singular components hurts, and you can afford a second stage.

## When NOT to Use
24GB quality default → `method:lr-matters-lora`. Live tangent SVD branch → `method:dt-lora`.

## Relation to Existing SOTA
Active plug-in on `task:lora-quality-tuning` (`sota_for: []`). Does **not** replace vanilla LoRA + rsLoRA + LR sweep.

## Gotchas & Failure Modes
- Diagnostic: rank-16 LoRA, keeping only top singular components won; extra components degraded.
