---
id: method:mupace
type: method
title: 'MuPACE'
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-adapter quality LoRA / rsLoRA + LR sweep rather than a meta-learned Muon step-size'
  reason: 'Quality default remains vanilla LoRA + rsLoRA + LR sweep; MuPACE meta-learns a global Muon step size'
  use_instead: method:lr-matters-lora
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains pretrain; MuPACE paces Muon only for LoRA FT'
  use_instead: method:muon2
assumptions:
- 'Leave Muon direction untouched; a small recurrent policy emits bounded adjustments to an analytic LR schedule.'
- 'Paper: 64 LoRA FT problems; meta-train on <=16-layer models, transfer to Qwen3-32B / Qwen3.8-27B. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:mupace
recipes:
- recipe:mupace
claims:
- benchmark: '64 LoRA fine-tuning problems; transfer to Qwen3-32B / Qwen3.8-27B'
  metric: 'win rate vs shared-default fixed schedules; competitiveness vs per-task tuned peaks'
  value: 'beats a strong shared-default schedule on 64-78% of problems and matches per-task tuned peaks; one-shot transfer from 16-layer meta-train to 64-layer models'
  baseline: 'fixed Muon LR schedules at a shared default and per-task tuned peaks'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28072'
  notes: 'Does not supersede vanilla LoRA + rsLoRA + LR sweep.'
tags:
- peft
- lora
- muon
- schedule
- active
---

# MuPACE

## Method Overview
MuPACE meta-learns only Muon's global step size for LoRA. A recurrent policy, trained across a distribution of fine-tunes, conditions on the observed trajectory and adjusts an interpretable analytic schedule.

## When to Use
- Muon+LoRA when retuning a schedule per model/task/rank is the bottleneck.

## When NOT to Use
Quality LoRA default → `method:lr-matters-lora`. ~7B pretrain → `method:muon2`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:lr-matters-lora`.

## Gotchas & Failure Modes
- Meta-train distribution matters; it is not a 24GB quality-default replacement.
- Direction stays Muon; only the scalar pace is learned.
