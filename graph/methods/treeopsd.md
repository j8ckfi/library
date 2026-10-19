---
id: method:treeopsd
type: method
title: 'TreeOPSD'
category: rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'outcome-only long-horizon agent RL with a programmatic checker (CANOPY)'
  reason: 'CANOPY remains coverage/anti-drift; TreeOPSD is critic-free tree posterior self-distill'
  use_instead: method:canopy
- when: 'hindsight-guided tree exploration and turn-level credit (TreeHCA)'
  reason: 'TreeHCA is tree backup; TreeOPSD maps credit to a bounded teacher vs the behavior policy'
  use_instead: method:treehca
assumptions:
- 'Long-horizon agent RL with branched continuations from shared prefixes. Paper: Qwen3-30B-A3B-Thinking-2507 Deep Research.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:treeopsd
recipes:
- recipe:treeopsd
claims:
- benchmark: 'Qwen3-30B-A3B-Thinking-2507 Deep Research vs GRPO'
  metric: 'average accuracy'
  value: '+4.97 vs GRPO'
  baseline: 'GRPO (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23181'
  notes: 'Does not retarget CANOPY or TreeHCA. Critic-free; no external teacher.'
tags:
- agent-rl
- opsd
- tree
- active
---

# TreeOPSD

## Method Overview
TreeOPSD treats each interaction turn as a tree node, branches alternative continuations from shared prefixes, backs up terminal rewards into turn-level credit, and maps each credit to a bounded teacher parameterized by the likelihood ratio versus the frozen behavior policy.

## When to Use
- Long-horizon agent RL where terminal rewards starve turn-level credit and sequential mini-batches go stale, without a critic or external teacher.

## When NOT to Use
Checker coverage / anti-drift → `method:canopy`. Async stragglers → `method:sao`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** replace CANOPY.

## Gotchas & Failure Modes
- Needs branched rollouts from shared prefixes.
- Deep Research +4.97 is not an AppWorld TGC bake-off.
