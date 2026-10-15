---
id: method:actionopd
type: method
title: ActionOPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation
  reason: OPD remains token-prob matching; ActionOPD aligns semantic actions without teacher logp
  use_instead: method:opd
- when: outcome-only AppWorld coverage / anti-drift
  reason: CANOPY remains sparse-outcome agent RL
  use_instead: method:canopy
assumptions:
- Semantic actions as the distill unit. Black-box teacher samples; student is rewarded for action agreement.
- Paper: Qwen3-4B/8B, two teachers, four OOD tool-use benches. Code thu-nics/ActionOPD released.
last_reviewed: '2026-10-15'
papers:
- paper:actionopd
recipes:
- recipe:actionopd
claims:
- benchmark: Qwen3-4B/8B tool-use OOD (four benches); tau2-bench vs offline / token OPD
  metric: average OOD accuracy
  value: +3.3-6.9pp across four OOD benches; competitive with offline distill and token-level OPD on tau2-bench
  baseline: offline imitation and token-level OPD (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19820
  notes: Does not retarget OPD or CANOPY.
tags:
- distillation
- opd
- agents
- active
---

# ActionOPD

## Method Overview
Align the student's action-level decisions with a teacher at student-encountered states. Sample actions from both, reward semantic agreement, and optimize with policy gradients. No teacher token probabilities and no shared tokenizer.

## When to Use
- Distilling a tool-use agent from a black-box teacher that does not share a tokenizer.

## When NOT to Use
Token matching with a same-tokenizer teacher → `method:opd`. Sparse-outcome AppWorld RL → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`) with a mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace OPD.

## Gotchas & Failure Modes
- Self-ActionOPD (same-model teacher plus privileged context) is an extra setting, not VISTA.
