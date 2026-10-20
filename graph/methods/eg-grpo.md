---
id: method:eg-grpo
type: method
title: 'EG-GRPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'live-web multi-hop search SFT-RL climbing'
  reason: 'Iris remains first hop; EG-GRPO is evidence-guided step credit on synthetic deep-search data'
  use_instead: method:iris
- when: 'grounded search vs answer token credit without evidence annotations'
  reason: 'GCA is the search/answer split'
  use_instead: method:gca
assumptions:
- 'Synthetic deep-search data with evidence claim annotations.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:eg-grpo
recipes:
- recipe:eg-grpo
claims:
- benchmark: 'BrowseComp / BrowseComp-ZH / GAIA / xBenchDS-2505 / xBenchDS-2510'
  metric: 'deep-search accuracy vs trajectory-level GRPO'
  value: 'step-level evidence-guided credit with discounted return and three-level fallback grouping on five deep-search benches'
  baseline: 'trajectory-level GRPO / Search-R1-style outcome RL'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25269'
  notes: 'Needs evidence annotations. Does not replace Iris or GCA.'
tags:
- rl-alignment
- search-agent
- credit
- active
---

# EG-GRPO

## Method Overview
EG-GRPO (Evidence-Guided GRPO) turns synthetic evidence claims into step-level rewards by attributing claims onto the search trajectory, then mixes discounted step advantage with trajectory GRPO and a three-level fallback when groups are silent.

## When to Use
- Training a deep-search agent on synthetic multi-hop data that already has evidence annotations.

## When NOT to Use
Iris live-web climbing → `method:iris`. Search vs answer tokens without evidence labels → `method:gca`.

## Relation to Existing SOTA
Active plug-in on `task:web-search-agent-rl` (`sota_for: []`). Does **not** replace Iris or GCA.

## Gotchas & Failure Modes
- Evidence annotations are the scarce ingredient.
- Open-ended live web may not have them.
