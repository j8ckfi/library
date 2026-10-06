---
id: method:sf-mopd
type: method
title: "SF-MOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the multi-teacher student-distillation default"
    reason: "Open-MOPD remains token-share / gap-aware budget; SF-MOPD is slow/fast EMA coupling for capability preservation"
    use_instead: "method:open-mopd"
  - when: "token-level ExpertAlign routing over unlabeled multi-teacher pools"
    reason: "MOPD-Router routes the pool; SF-MOPD does not replace routing"
    use_instead: "method:mopd-router"
  - when: "domain-feedback-scale calibration of labeled MOPD advantages"
    reason: "DN-MOPD rescales log-ratio spread; SF-MOPD is an EMA student pair"
    use_instead: "method:dn-mopd"
  - when: "multi-teacher OPD subspace protection / task cycling"
    reason: "PMOPD projects interfering updates; SF-MOPD is slow/fast coupling"
    use_instead: "method:pmopd"
assumptions:
  - "Labeled multi-teacher OPD host. Fast student takes each teacher update; slow student is an EMA of the fast student and is the deployable checkpoint."
  - "Paper: Qwen3-VL-8B/4B/2B Instruct All Avg. Paper Open-MOPD 64.2 is not the library 83.4% bake-off."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:rethink-mopd
  - paper:sf-mopd
recipes:
  - recipe:sf-mopd
claims:
  - benchmark: "Qwen3-VL-8B-Instruct All Avg"
    metric: "All Avg"
    value: "67.7"
    baseline: "MOPD 65.5 / Open-MOPD 64.2 / VAD-MOPD 63.6"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02324"
    notes: "Table 1. Not a library Open-MOPD 83.4% headroom-recovery retarget."
  - benchmark: "Qwen3-VL-4B-Instruct All Avg"
    metric: "All Avg"
    value: "64.8"
    baseline: "MOPD 63.6 / Instruct init 63.7"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02324"
    notes: "Table 1."
  - benchmark: "Qwen3-VL-2B-Instruct All Avg"
    metric: "All Avg"
    value: "54.2"
    baseline: "MOPD 53.3"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02324"
    notes: "Table 1."
tags:
  - post-training
  - distillation
  - multi-teacher
  - sf-mopd
  - active
---

# SF-MOPD

## Method Overview
MOPD updates one student toward several specialists and the student walks off its initialization. SF-MOPD keeps two copies: a fast student that takes the teacher token update, and a slow EMA of that student. The slow copy is the capability reference and the weights you deploy. Open-MOPD still owns token-share / gap-aware budget.

## When to Use
- Multi-teacher OPD where general capabilities drop as specialist teachers pull the student.

## When NOT to Use
- Multi-teacher default → `method:open-mopd`. Unlabeled token routing → `method:mopd-router`. Labeled log-ratio scale → `method:dn-mopd`. Subspace protection → `method:pmopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside Open-MOPD (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Open-MOPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Paper Open-MOPD 64.2 All Avg is not the library 83.4% headroom-recovery bake-off.
