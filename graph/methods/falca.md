---
id: method:falca
type: method
title: 'FALCA'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'train a live-web multi-hop search agent (SFT-RL climbing)'
  reason: 'Iris remains climbing; FALCA is propose-falsify hierarchical credit on deep search'
  use_instead: method:iris
- when: 'evidence-guided step credit for deep-search agents (EG-GRPO)'
  reason: 'EG-GRPO is evidence-claim step reward; FALCA is Searcher-Falsifier RL'
  use_instead: method:eg-grpo
assumptions:
- 'Searcher proposes; independent Falsifiers hunt counterevidence. SFT warmup on falsification traces then agentic RL with hierarchical credit.'
- 'No public GitHub as of 2026-10-21; project page douzj-llm.github.io/FALCA.'
last_reviewed: '2026-10-21'
papers:
- paper:falca
recipes:
- recipe:falca
claims:
- benchmark: 'Five search benchmarks vs backbone and harness ablations'
  metric: 'long-horizon deep-search performance; confirmation-bias / error-accumulation'
  value: 'improves over backbone and harness ablations while reducing confirmation bias via falsification reports'
  baseline: 'backbone and harness ablations without falsifiers / hierarchical credit'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28361'
  notes: 'Does not retarget Iris, GCA, or EG-GRPO.'
tags:
- search-agent
- rlvr
- falsification
- active
---

# FALCA

## Method Overview
FALCA casts deep search as propose-falsify. A Searcher proposes candidates; Falsifiers seek counterevidence and write revision reports. Training mixes SFT on those traces with agentic RL and hierarchical credit over stages, state transitions, and actions.

## When to Use
- Long-horizon search RL where early anchoring and confirmation bias dominate.

## When NOT to Use
SFT-RL climbing → `method:iris`. Evidence-claim credit → `method:eg-grpo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:iris`.

## Gotchas & Failure Modes
- Extra falsifier rollouts add cost.
- Not the Iris SFT-RL climbing recipe.
