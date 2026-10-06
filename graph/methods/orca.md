---
id: method:orca
type: method
title: "ORCA"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "ORCA is a temporary spectral regularizer on a Muon-family trainer, not a Muon2 replacement"
    use_instead: "method:muon2"
  - when: "Nyström-sketched SOAP / linear-memory second-order states"
    reason: "ORCA is orthogonality annealing, not a SOAP memory sketch"
    use_instead: "method:clean"
  - when: "per-expert Muon step-size multipliers for MoE"
    reason: "ORCA is a shared spectral schedule, not Compass expert step sizes"
    use_instead: "method:expertmuon-compass"
assumptions:
  - "Host is a Muon-family LLM pretrainer. Paper: LLaMA, Qwen3, and fine-grained MoE, 130M–8B."
  - Apply strong soft-orthogonality early, then remove it. Keeping the constraint for the whole run is not ORCA.
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:orca
recipes:
  - recipe:orca
claims:
  - benchmark: "LLaMA / Qwen3 / fine-grained MoE 130M–8B validation loss vs Muon"
    metric: "final validation loss vs Muon"
    value: "lower than Muon; Muon-relative drop matches or exceeds Muon's drop vs Adam"
    baseline: "Muon / Adam"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06116"
    notes: "Abstract-level claim only. Does not retarget Muon2."
tags:
  - pretraining
  - optimizer
  - orca
  - active
---

# ORCA

## Method Overview
ORCA is a Muon-family add-on: strong soft-orthogonality regularization early in pretraining, then removed (Cooled After). The paper argues persistent spectral constraints raise the attainable loss floor; a temporary constraint keeps a broader spectrum early and lets weights adapt later.

## When to Use
- Muon-family dense or fine-grained-MoE pretrain where you can afford an early orthogonality schedule and will drop it.

## When NOT to Use
- Default ~7B optimizer → `method:muon2`. SOAP linear-memory sketch → `method:clean`. Per-expert Muon steps → `method:expertmuon-compass`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` beside `method:muon2` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Persistent orthogonality for the whole run is not ORCA.
- Do not invent numeric loss tables that are absent from the abstract.
