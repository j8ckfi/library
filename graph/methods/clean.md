---
id: method:clean
type: method
title: "Clean"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Clean sketches SOAP memory; Muon2 remains the 7B default and KL-SOAP remains the high-memory second-order hop"
    use_instead: "method:muon2"
  - when: "high-memory full SOAP / KL-SOAP at unconstrained batch"
    reason: "KL-SOAP remains the large-batch second-order hop; Clean is the linear-memory SOAP sketch"
    use_instead: "method:soap-muon-scale"
  - when: "full-param FT ternary one-sparse optimizer state"
    reason: "TACO is FT-axis sparse geometry; Clean is a SOAP Nyström sketch"
    use_instead: "method:taco"
assumptions:
  - "You want SOAP-style curvature without quadratic optimizer-state memory. Paper: LLaMA-1.3B memory numbers; 13B on one 80GB GPU."
  - Q-Clean is the low-precision state variant, not a different algorithm family.
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:clean
recipes:
  - recipe:clean
claims:
  - benchmark: "LLaMA-1.3B optimizer-state memory vs Muon (Q-Clean)"
    metric: "optimizer memory reduction"
    value: ">50% vs Muon"
    baseline: "Muon optimizer state"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04204"
    notes: "Does not retarget Muon2 or KL-SOAP."
  - benchmark: "Clean vs AdamW wall-clock to AdamW final quality"
    metric: "wall-clock reduction"
    value: "26% faster than AdamW to AdamW's final performance"
    baseline: "AdamW"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04204"
    notes: "Smaller optimizer-state footprint than AdamW. 13B on one 80GB GPU."
tags:
  - pretraining
  - optimizer
  - soap
  - clean
  - active
---

# Clean

## Method Overview
Clean Nyström-sketches SOAP's left and right preconditioners so optimizer memory is linear in model dimensions, then puts off-subspace curvature back. Q-Clean compresses those states in low precision.

## When to Use
- SOAP-style second-order LLM pretrain when optimizer-state memory is the constraint (including the paper's 13B / 80GB setting).

## When NOT to Use
- Default 7B optimizer → `method:muon2`. Unconstrained-memory large-batch SOAP → `method:soap-muon-scale`. FT ternary sparse state → `method:taco`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` beside `method:soap` / `method:soap-muon-scale` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2, KL-SOAP, or SCALE.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Q-Clean is a state-precision variant of Clean, not a new first hop.
- Do not treat the 13B/80GB claim as a SCALE or Muon2 retarget.
