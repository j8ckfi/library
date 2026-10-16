---
id: method:waypoint-opd
type: method
title: 'Waypoint-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; Waypoint-OPD gates an RL-induced endpoint policy shift'
  use_instead: method:opd
- when: 'relative policy-difference transfer of OPD (expert-minus-reference log-ratio residuals)'
  reason: 'RPD-OPD is a residual identity, not a mid-run directional gate'
  use_instead: method:rpd-opd
- when: 'AR to discrete-dLLM on-policy distillation'
  reason: 'JustOPD is AR-to-dLLM; Waypoint-OPD is AR student matching of an RL teacher shift'
  use_instead: method:justopd
- when: 'privileged same-size gold teacher OPSD'
  reason: 'VISTA remains scoring-teacher OPSD'
  use_instead: method:vista
assumptions:
- 'RL-trained teacher with at least one intermediate checkpoint from the same run. Paper: Qwen3-4B teachers; Qwen3-8B/14B/30B-A3B students.'
- 'Code: hhhbxloveai/WaypointOPD (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:waypoint-opd
recipes:
- recipe:waypoint-opd
claims:
- benchmark: 'Qwen3-8B/14B/30B-A3B math (AIME24/25/26, HMMT, AMC) and code vs Direct-OPD'
  metric: 'domain-average vs Direct-OPD; 8B math Avg vs no-gate'
  value: 'math +2.18/+1.59/+1.89; code +2.66/+1.52/+1.19; 8B math Avg 56.14 vs no-gate 53.50; highest of six domain-student settings'
  baseline: 'Direct-OPD / OPD2 / endpoint policy-shift (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.21601'
  notes: 'Does not retarget OPD, Open-MOPD, JustOPD, or VISTA. Distinct from RPD-OPD.'
tags:
- distillation
- opd
- policy-shift
- active
---

# Waypoint-OPD

## Method Overview
Reuse the teacher's RL-induced log-probability shift as on-policy student supervision, but gate that endpoint shift by cosine agreement between early and late shifts measured at an intermediate checkpoint on student-visited prefixes.

## When to Use
- Distilling an RL-trained teacher whose mid-run updates may cancel, and you can keep one extra frozen checkpoint.

## When NOT to Use
Plain matching → `method:opd`. Residual expert-minus-reference → `method:rpd-opd`. AR→dLLM → `method:justopd`. Privileged gold teacher → `method:vista`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` with a mention on `task:privileged-teacher-opsd` (`sota_for: []`). Does **not** replace OPD, Open-MOPD, or JustOPD.

## Gotchas & Failure Modes
- Needs a mid-run teacher checkpoint from the same RL job.
- Two HMMT cells lose to Direct-OPD; gains are domain averages, not every bench.

