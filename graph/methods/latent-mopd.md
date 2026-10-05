---
id: method:latent-mopd
type: method
title: "Latent-MOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the multi-teacher student-distillation default"
    reason: "Open-MOPD remains token-share / gap-aware budget; Latent-MOPD adds hidden-state channels"
    use_instead: "method:open-mopd"
  - when: "latent OPD collapse / last-layer crossfade into token OPD"
    reason: "LastOPD is a single-teacher latent-collapse schedule; Latent-MOPD is multi-teacher hidden-state matching"
    use_instead: "method:lastopd"
  - when: "distilling RL gains via representation residuals rather than logits"
    reason: "RIDE extrapolates RL-induced residuals; Latent-MOPD matches specialist hidden states"
    use_instead: "method:ride"
assumptions:
  - "Existing domain specialists; no extra teacher training. Same-family 1.5B last-3 is the main table; cross-family last-1 Linear is the transfer check."
  - "Official code fangzy96/Latent-MOPD released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:latent-mopd
recipes:
  - recipe:latent-mopd
claims:
  - benchmark: "same-family 1.5B last-3 Norm"
    metric: "Norm"
    value: "1.05"
    baseline: "token-only MOPD 0.90 / uniform 0.79 / OPRD-style all layers 0.64"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02381"
    notes: "GYM 52.4 / BBH 66.3 / AIME24 50.8 vs token-only 51.8 / 65.4 / 46.0. Not an Open-MOPD 83.4% bake-off retarget."
  - benchmark: "cross-family last-1 Linear Norm"
    metric: "Norm"
    value: "0.26"
    baseline: "token-only MOPD 0.16"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02381"
    notes: "GYM 34.1 vs token-only 29.2."
tags:
  - post-training
  - distillation
  - multi-teacher
  - latent
  - latent-mopd
  - active
---

# Latent-MOPD

## Method Overview
Token-only MOPD copies specialist next-token distributions. Latent-MOPD also matches the late-layer hidden states those distributions are computed from, using a shared projection when widths differ, domain-grouped updates, and a schedule that fades hidden-state loss into token OPD. The routed specialist is the same channel for both losses. LastOPD is a different (single-teacher collapse) schedule. RIDE extrapolates RL residuals, not specialist states.

## When to Use
- Multi-teacher OPD where specialists' hidden geometry is available and token-only MOPD under-transfers.

## When NOT to Use
- Multi-teacher default → `method:open-mopd`. Single-teacher latent collapse → `method:lastopd`. RL residual extrapolation → `method:ride`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside Open-MOPD (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Open-MOPD.

## Gotchas & Failure Modes
- All-layer OPRD-style (Norm 0.64) is worse than last-3. Late layers are the method.
