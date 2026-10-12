---
id: method:cv-opd
type: method
title: CV-OPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation (text)
  reason: CV-OPD adds a visual contrastive constraint on VLM OPD; OPD remains text matching
  use_instead: method:opd
- when: MLLM privileged OPSD with textual spatial guidance from synthetic scenes
  reason: Where-OPD is privileged spatial hints; CV-OPD is contrastive positive/negative crops
  use_instead: method:where-opd
assumptions:
- VLM OPD where the answer can shortcut past visual evidence. Fine-grained visual benches in the paper.
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:cv-opd
recipes:
- recipe:cv-opd
claims:
- benchmark: Fine-grained visual VLM benchmarks vs vanilla OPD
  metric: visual reasoning vs masked/noised-region shortcut
  value: alleviates the visual shortcut (student still answers when evidence is masked under vanilla OPD)
    and improves visual reasoning vs existing VLMs
  baseline: vanilla OPD (answer-as-hint teacher)
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13264
  notes: Does not retarget OPD or Where-OPD. Abstract does not list a single headline number.
tags:
- post-training
- distillation
- opd
- vlm
- cv-opd
- active
---

# CV-OPD

## Method Overview
Keep the student prefix fixed. Query a positive-crop teacher and a negative-crop teacher. Push the student toward the positive and away from the negative with a margin, but only on tokens the discrepancy gate marks as visual.

## When to Use
- VLM OPD where masking the cited region does not change the student's answer.

## When NOT to Use
Text OPD → `method:opd`. Privileged spatial-hint OPSD → `method:where-opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD or Where-OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Negative crops must be answer-unrelated or the contrast is noise.
- DAG is load-bearing; optimizing every token reintroduces the shortcut.
