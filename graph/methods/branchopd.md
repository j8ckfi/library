---
id: method:branchopd
type: method
title: BranchOPD
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation without branching
  reason: OPD remains the student-distillation default; BranchOPD is a branch-and-resample
    plug-in
  use_instead: method:opd
- when: AppWorld outcome-only coverage / anti-drift
  reason: CANOPY remains checker-protocol agent RL; BranchOPD is OPD with agent PBR
  use_instead: method:canopy
assumptions:
- Teacher OPD host. Branch at uncertain or teacher-disagreement tokens; resample student
  continuations.
- 'Code: chendy25/BranchOPD (code_status: announced; empty stub).'
last_reviewed: '2026-10-13'
papers:
- paper:branchopd
recipes:
- recipe:branchopd
claims:
- benchmark: math avg@16; ALFWorld; WebShop vs vanilla OPD and multi-rollout OPD n=7
  metric: pp over vanilla OPD; student tokens vs n=7
  value: +18.55pp math avg@16; +13.8pp ALFWorld; ~19%/31% fewer student tokens vs
    n=7 on ALFWorld/WebShop
  baseline: vanilla OPD; multi-rollout OPD n=7
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13481
  notes: Does not retarget OPD or CANOPY. PBR is the agent protocol-boundary repair.
tags:
- post-training
- distillation
- opd
- branchopd
- active
---

# BranchOPD

## Method Overview
On a student OPD rollout, branch at tokens where the student is uncertain or disagrees with the teacher. Resample continuations from that prefix. Apply token-level teacher KL on the trunk and the branches. Protocol-boundary repair (PBR) restarts at agent protocol boundaries.

## When to Use
- Teacher OPD where multi-rollout OPD (n=7) is too expensive, or multi-turn agents need protocol-boundary repair.

## When NOT to Use
Default single-teacher matching → `method:opd`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` with a mention on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD or CANOPY.

## Gotchas & Failure Modes
- **code: announced** chendy25/BranchOPD empty stub as of 2026-10-13.
- Token savings are versus n=7 multi-rollout OPD, not versus sparse-OPD token budgets.
- PBR is agent-specific; skip it on single-turn math.
