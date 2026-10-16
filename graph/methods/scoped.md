---
id: method:scoped
type: method
title: 'SCOPED'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; SCOPED is multi-expert VLM skill distillation'
  use_instead: method:opd
- when: 'multi-teacher token-share balancing (Open-MOPD)'
  reason: 'Open-MOPD remains labeled multi-teacher text; SCOPED is VLM capability experts'
  use_instead: method:open-mopd
- when: 'contrastive vision OPD for VLMs (positive/negative crops)'
  reason: 'CV-OPD is crop teachers; SCOPED is skill-decoupled experts'
  use_instead: method:cv-opd
assumptions:
- 'Heterogeneous VLM capabilities that conflict under Mix-RL. Paper: Qwen3-VL-8B/4B.'
- 'Code: NEUIR/SCOPED (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:scoped
recipes:
- recipe:scoped
claims:
- benchmark: 'eight multimodal benches (CountBenchQA / PixMo-Count / CC-OCR V2 / ChartQA / VisualPuzzles / We-Math / MUIRBench / MMSI), Qwen3-VL'
  metric: 'macro average vs backbone / Mix-RL'
  value: '8B +5.83 vs backbone; +3.82 vs Mix-RL; 4B +3.90 vs backbone'
  baseline: 'Qwen3-VL backbone; Mix-RL; parameter merging (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22217'
  notes: 'Does not retarget OPD, Open-MOPD, or CV-OPD.'
tags:
- distillation
- opd
- multimodal
- vlm
- active
---

# SCOPED

## Method Overview
Train capability experts independently. Reflect over rewarded vs failed rollouts into explicit skills. Distill skill-conditioned experts into a unified student along student trajectories; drop the skills at deploy.

## When to Use
- Unifying VLM perception / OCR / symbolic / multi-image experts that fight under Mix-RL.

## When NOT to Use
Plain matching → `method:opd`. Text multi-teacher → `method:open-mopd`. Crop contrastive VLM OPD → `method:cv-opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD or Open-MOPD.

## Gotchas & Failure Modes
- Skills must not leak into student inference context.
- Mix-RL can still look fine on average while losing expert-only skills.

