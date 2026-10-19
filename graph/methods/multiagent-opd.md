---
id: method:multiagent-opd
type: method
title: 'MultiAgent-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains single-agent matching; MultiAgent-OPD jointly trains a Leader-Searcher-Answerer team'
  use_instead: method:opd
- when: 'whether to use more than one agent (default: do not)'
  reason: 'single-agent-plus-tools remains the orchestration default; this is a team-training recipe'
  use_instead: method:single-agent-plus-tools
assumptions:
- 'Shared-parameter Leader-Searcher-Answerer. Frozen Teacher scores student search/summary tokens; Leader from team success; Answerer from candidate correctness.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:multiagent-opd
recipes:
- recipe:multiagent-opd
claims:
- benchmark: 'Seven datasets, hierarchical search team, macro avg@4'
  metric: 'macro avg@4'
  value: '38.68%; +4.06 vs Prompted Critic; +2.61 vs C-MAS + RL'
  baseline: 'Prompted Critic / C-MAS + RL (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23234'
  notes: 'Does not retarget OPD or single-agent-plus-tools.'
tags:
- distillation
- opd
- multi-agent
- active
---

# MultiAgent-OPD

## Method Overview
MultiAgent-OPD jointly trains a shared-parameter Leader-Searcher-Answerer team: a frozen Teacher trained on Searcher-Answerer correctness scores student search and summary tokens while the Leader learns from team success.

## When to Use
- Hierarchical search teams where a final answer gives only indirect feedback to subagents, and you can train a same-family Teacher first.

## When NOT to Use
Default distill → `method:opd`. Default orchestration → `method:single-agent-plus-tools`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` with a mention on `task:multi-agent-orchestration` (`sota_for: []`). Does **not** replace OPD or single-agent-plus-tools.

## Gotchas & Failure Modes
- Needs a Teacher trained in a Searcher-Answerer workflow first.
- Does not overturn the library's do-not-MAS default.
