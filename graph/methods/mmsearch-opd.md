---
id: method:mmsearch-opd
type: method
title: 'MMSearch-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'live-web multi-hop search-agent SFT-RL climbing (text Iris recipe)'
  reason: 'Iris remains text search climbing; MMSearch-OPD is multimodal Refine+OPD'
  use_instead: method:iris
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; MMSearch-OPD is a search curriculum plus decaying OPD'
  use_instead: method:opd
- when: 'outcome-only AppWorld coverage / anti-drift'
  reason: 'CANOPY remains sparse-outcome coverage'
  use_instead: method:canopy
assumptions:
- 'Multimodal search with image evidence and a teacher that can score imperfect trajectories. Paper: Qwen3.5-9B student / 27B SFT teacher.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-16'
papers:
- paper:mmsearch-opd
recipes:
- recipe:mmsearch-opd
claims:
- benchmark: 'seven multimodal search benches (MMSearch / LiveVQA / BrowseComp-VL / MM-BC / MMSearch+ / BC-V3 / VisBrowse), 9B'
  metric: 'average accuracy vs Qwen3.5-9B workflow / DeepVoyager-VL-8B'
  value: '60.2 vs workflow 44.9 (+15.3); vs DeepVoyager-VL-8B +9.6; SFT 57.9 then joint 60.2; highest 7B-9B of compared agents'
  baseline: 'Qwen3.5-9B agentic workflow; DeepVoyager-VL-8B (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22240'
  notes: 'Does not retarget Iris or OPD. No public code as of 2026-10-16.'
tags:
- distillation
- opd
- multimodal
- search
- active
---

# MMSearch-OPD

## Method Overview
Upgrade easy multimodal questions into long-horizon search items, SFT, then jointly optimize outcome RL with token-level OPD on imperfect student traces. The reward gap scales teacher weights; an exponential schedule drops the OPD coefficient.

## When to Use
- Training a multimodal search agent when easy image-question seeds exist but hard multi-hop items do not.

## When NOT to Use
Text search climbing → `method:iris`. Plain matching → `method:opd`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:web-search-agent-rl` with a mention on `task:student-distillation` (`sota_for: []`). Does **not** replace Iris or OPD.

## Gotchas & Failure Modes
- No public trainer as of 2026-10-16.
- 9B still trails Seed2.1-Pro workflow 71.0 on the same table.

