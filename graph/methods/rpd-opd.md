---
id: method:rpd-opd
type: method
title: RPD-OPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: same-tokenizer single-teacher matching distillation from a stronger frozen teacher
  reason: RPD-OPD transfers expert-minus-reference log-ratio residuals; OPD remains absolute teacher matching
  use_instead: method:opd
- when: offline initial-student rollouts instead of live on-policy sampling (Semi-OPD)
  reason: Semi-OPD freezes rollouts; RPD-OPD is a relative-Δπ transfer identity
  use_instead: method:semi-opd
assumptions:
- 'A proxy expert and a proxy reference that share enough behavior to isolate a residual. Paper: any-to-any
  across scale, stage, or generation.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:rpd-opd
recipes:
- recipe:rpd-opd
claims:
- benchmark: OPD relative-Δπ transfer, task-specific FT/RL residuals vs scale-only residuals
  metric: whether the induced on-policy update transfers
  value: task-specific RL/SFT differences transfer; scale-only differences transfer weakly or not at all;
    raw policy distance does not predict transfer
  baseline: absolute-teacher OPD; scale-gap expert-reference pairs
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13205
  notes: Does not retarget OPD. An appropriate reference can rescue otherwise unsuccessful transfer.
tags:
- post-training
- distillation
- opd
- rpd-opd
- active
---

# RPD-OPD

## Method Overview
Score the target on-policy with log π_expert − log π_ref and take a KL-regularized step. Ordinary OPD is expert-only (ref = target or uniform). Pick the reference to cancel shared behavior so the residual is the capability you actually want.

## When to Use
- You have an expert and a reference (same family, different stage) and absolute-teacher OPD is too far or the expert is not strictly stronger.

## When NOT to Use
Strong frozen teacher, same tokenizer → `method:opd`. Frozen initial-student rollouts → `method:semi-opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Do not use a larger same-family base as the expert if the residual is only scale.
- A bad reference leaves the shared mass in the reward and the transfer dies.
