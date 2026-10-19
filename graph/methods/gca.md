---
id: method:gca
type: method
title: 'GCA'
category: rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'train a live-web multi-hop search agent (SFT-RL climbing)'
  reason: 'Iris remains that first hop; GCA is a Search-R1-style credit split'
  use_instead: method:iris
- when: 'outcome-only long-horizon agent RL (coverage / anti-drift)'
  reason: 'CANOPY remains AppWorld coverage; GCA is search+answer grounding'
  use_instead: method:canopy
assumptions:
- 'Search-R1 / GRPO host with verifiable evidence-retrieval and answer-correctness sub-outcomes. Correction capped at 10% of each token advantage.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:gca
recipes:
- recipe:gca
claims:
- benchmark: 'Seven QA benches vs Search-R1; Bamboogle evidence-supported share of correct answers'
  metric: 'average EM; evidence-supported share'
  value: '+5.7 EM Qwen2.5-3B / +6.3 EM Qwen3-30B-A3B vs Search-R1; evidence-supported share 76.9%→93.4%'
  baseline: 'Search-R1 / GRPO (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23148'
  notes: 'Does not retarget Iris. Search-R1 can raise accuracy while grounding falls (Bamboogle 84.0%→42.9%).'
tags:
- search-agent
- grpo
- credit
- active
---

# GCA

## Method Overview
GCA splits GRPO credit using verifiable sub-outcomes: a wrong answer is blamed more than the search that found the evidence, and a correct answer that bypasses retrievable evidence is credited less. The correction is never negative on evidence-finding search and is capped at 10% of each token's advantage.

## When to Use
- Multi-turn search-agent GRPO where accuracy rises while answers stop being evidence-grounded.

## When NOT to Use
Iris SFT-RL climbing default → `method:iris`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:web-search-agent-rl` (`sota_for: []`). Does **not** replace Iris.

## Gotchas & Failure Modes
- Needs verifiable retrieval and answer checks.
- Cap is 10% of token advantage; it never overrides the outcome signal.
