---
id: method:road-mopd
type: method
title: Road MOPD (Cross-Teacher Guarding)
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: multi-teacher token-share / gap-aware budget rather than conflict guarding
  reason: Open-MOPD remains the multi-teacher matching default
  use_instead: method:open-mopd
- when: same-tokenizer single-teacher matching distillation
  reason: OPD remains single-teacher matching
  use_instead: method:opd
- when: multi-teacher OPD subspace protection / task cycling
  reason: PMOPD projects interfering updates; Road MOPD uses non-routed teachers as critics
  use_instead: method:pmopd
assumptions:
- Domain-routed MOPD with a frozen reference. Non-routed teachers score the same student trajectory.
- Paper: Qwen3-4B / 1.7B; math/code/medical teachers. HF Daily 2026-10-15 top paper.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:road-mopd
recipes:
- recipe:road-mopd
claims:
- benchmark: Qwen3-4B Math x Medical 11-task; high-conflict Medical vs Vanilla MOPD
  metric: All / Medical accuracy
  value: Ours 11-task 47.92 vs ExOPD 45.53; Medical +5.6-8.8pp vs Vanilla MOPD
  baseline: Vanilla MOPD, ExOPD, CaMOPD (single-paper; paper Open-MOPD is not the library 83.4% bake-off)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13521
  notes: Does not retarget Open-MOPD.
tags:
- distillation
- mopd
- multi-teacher
- active
---

# Road MOPD (Cross-Teacher Guarding)

## Method Overview
Keep domain-routed teachers, then put non-routed teachers on the same student trajectory as critics. Token credit strengthens when routed and auxiliary teachers agree relative to a frozen reference, and downweights conflicts. Preventive gradient projection removes update components that fight the auxiliary direction, with a norm-retention cap so the target domain still learns.

## When to Use
- Joint MOPD where medicine (or another style-distant domain) collapses under math/code routing.

## When NOT to Use
Default multi-teacher matching → `method:open-mopd`. Single teacher → `method:opd`. Subspace protection → `method:pmopd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace Open-MOPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- Math x code is low-conflict in the paper; the load-bearing failure is medical joint training.
