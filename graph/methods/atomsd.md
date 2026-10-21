---
id: method:atomsd
type: method
title: 'AtomSD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'programmatic checker AppWorld coverage / anti-drift'
  reason: 'CANOPY remains coverage; AtomSD distills procedural atoms from successful traces'
  use_instead: method:canopy
- when: 'repository-grounded procedural skills before interaction experience'
  reason: 'Code2Skill lifts code units; AtomSD extracts Intent/When/Do/Avoid from successful traces'
  use_instead: method:code2skill
assumptions:
- 'Procedural atoms: Intent, When, Do, Avoid. Atom-conditioned supervision plus task-reward optimization.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:atomsd
recipes:
- recipe:atomsd
claims:
- benchmark: 'LLM agent tasks vs strong reward-based and distillation methods'
  metric: 'average performance vs SOTA baseline'
  value: 'up to +9.31 points over the strongest reported reward-based / distillation baseline'
  baseline: 'strong reward-based and distillation agent methods'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26926'
  notes: 'Does not retarget CANOPY, ACE, or Code2Skill.'
tags:
- agentic
- self-distillation
- procedural
- active
---

# AtomSD

## Method Overview
AtomSD extracts reusable Procedural Atoms (Intent, When, Do, Avoid) from the learner's successful trajectories and distills them back through atom-conditioned supervision plus task-reward optimization.

## When to Use
- Agent RL/distill where bundled skills or raw traces do not reuse across histories.

## When NOT to Use
Checker coverage → `method:canopy`. Repo skills → `method:code2skill`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:canopy`.

## Gotchas & Failure Modes
- Atoms come from successful traces; all-fail pools yield nothing.
- Not a write-time playbook (ACE) or repo skill bank (Code2Skill).
