---
id: method:empo
type: method
title: 'EMPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:outcome-only-long-horizon-agent-rl'
  reason: 'EMPO is an active plug-in; method:canopy remains the first hop'
  use_instead: method:canopy
assumptions:
- 'Executable effects are identifiable. Compatible with trajectory-level and step-level estimators. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:empo
recipes:
- recipe:empo
claims:
- benchmark: 'ALFWorld, WebShop, Sokoban vs trajectory- and step-level credit hosts'
  metric: 'task success and learning efficiency vs strong multi-turn RL'
  value: 'outperforms strong baselines on all three environments without extra critics or rollouts'
  baseline: 'trajectory-level and step-level multi-turn RL that keep response-specific IS ratios'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29427'
  notes: 'Does not retarget method:canopy.'
tags:
- agent-rl
- credit
- active
---

# EMPO

## Method Overview
EMPO replaces response-specific probability ratios with an effect-level surrogate so distinct text that executes the same action shares credit.

## When to Use
- Multi-turn agents where several phrasings call the same tool and response-level IS splits the credit.

## When NOT to Use
Programmatic-checker coverage → `method:canopy`. Tool vs summary token split → `method:slca-grpo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:canopy`.

## Gotchas & Failure Modes
- No public code.
- Needs an execution-level equivalence (same tool call / same env effect), not paraphrase similarity.
