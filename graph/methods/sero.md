---
id: method:sero
type: method
title: 'SERO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'outcome-only AppWorld coverage / anti-drift without an executable oracle'
  reason: 'CANOPY remains sparse-outcome coverage; SERO needs a training-only oracle'
  use_instead: method:canopy
- when: 'state-grounded on-policy distillation for multi-turn agents'
  reason: 'State-OPD matches teacher on student states; SERO executes oracle futures'
  use_instead: method:state-opd
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; SERO is agentic oracle continuation'
  use_instead: method:opd
- when: 'variable environment latency / async stragglers'
  reason: 'SAO remains async RL'
  use_instead: method:sao
assumptions:
- 'Interactive agents with restorable simulator snapshots and a training-only oracle. Paper: Qwen2.5-1.5B/7B ALFWorld/WebShop.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-16'
papers:
- paper:sero
recipes:
- recipe:sero
claims:
- benchmark: 'ALFWorld / WebShop, Qwen2.5-1.5B/7B GraphGPO and HGPO'
  metric: 'ALFWorld seen/unseen success; WebShop score/success'
  value: '1.5B GraphGPO ALFWorld 90.63/88.02→95.83/91.67; WebShop 87.27/77.93→88.90/79.27; 7B unseen +11.20; root-only hurts'
  baseline: 'GraphGPO / HGPO / GiGPO / GRPO (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.19397'
  notes: 'Does not retarget CANOPY or SAO. No public code as of 2026-10-16.'
tags:
- rl-alignment
- agentic
- oracle
- active
---

# SERO

## Method Overview
From a failed on-policy state, restore the env and let an oracle finish. Train on those executable actions with weights equal to the frozen policy's compatibility with the prefix. Keep the base RL estimator; drop the oracle at inference.

## When to Use
- Long-horizon agent RL where failed groups never visit the useful suffix and you have an env snapshot plus a training oracle.

## When NOT to Use
Checker-only coverage → `method:canopy`. Matched-state teacher OPD → `method:state-opd`. Async stragglers → `method:sao`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** replace CANOPY.

## Gotchas & Failure Modes
- Root-only oracle actions decrease ALFWorld; use the full continuation.
- Extra GraphGPO steps close some of the gap but do not match SERO in the paper's budget control.

