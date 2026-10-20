---
id: method:bridged-self-distill
type: method
title: 'Bridged Self-Distillation'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching when token probabilities are available; BSD bridges traces without teacher logp'
  use_instead: method:opd
- when: 'strict 1:1 cross-tokenizer coverage / shared-vocab reverse-KL'
  reason: 'Cross-Tokenizer OPD is the 1:1 first hop'
  use_instead: method:cross-tokenizer-opd
assumptions:
- 'External teacher provides a reasoning trace (shared tokenizer, cross-tokenizer, or closed API). Student is a self-teacher on its own rollouts.'
- 'Code TUMLegalTech/Bridged-Self-Distillation as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:bridged-self-distill
recipes:
- recipe:bridged-self-distill
claims:
- benchmark: 'Shared-tokenizer, cross-tokenizer, and closed-API teacher access'
  metric: 'on-policy learning vs scenario-specific OPD that needs teacher token probabilities'
  value: 'one recipe for trace-only teachers; token-level guidance on student rollouts without teacher logp'
  baseline: 'scenario-specific OPD; RLSD ablations'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26397'
  notes: 'Does not replace OPD or Cross-Tokenizer OPD.'
tags:
- distillation
- opd
- cross-tokenizer
- active
---

# Bridged Self-Distillation

## Method Overview
Bridged Self-Distillation (BSD) conditions a same-model self-teacher on an external teacher's reasoning trace as privileged context, then distills that self-teacher onto the student's own rollouts. Teacher token probabilities are not required.

## When to Use
- Distilling from a cross-tokenizer or API teacher that can write a trace but not logits.

## When NOT to Use
Same-tokenizer logp matching → `method:opd`. Strict 1:1 shared-vocab reverse-KL → `method:cross-tokenizer-opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD or Cross-Tokenizer OPD.

## Gotchas & Failure Modes
- Trace quality is the privileged context.
- Related to ActionOPD (no teacher logp) but BSD is self-teacher bridging.
