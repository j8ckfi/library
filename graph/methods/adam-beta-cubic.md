---
id: method:adam-beta-cubic
type: method
title: "Adam Shared-Beta Cubic Rule"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "This is an Adam β recipe; Muon2 remains the 7B default"
    use_instead: "method:muon2"
  - when: "default embeddings / lm_head AdamW without a β sweep"
    reason: "AdamW remains the I/O-layer default; this rule only picks shared β"
    use_instead: "method:adamw-optimizer"
assumptions:
  - "Adam / AdamW with shared β1=β2=β. Paper: 200-update pilot, 16 probes at 4 checkpoints, 11 workloads."
  - "Code: AlbertoFdezHdez/Adam_beta_rule_cubic (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:adam-beta-cubic
recipes:
  - recipe:adam-beta-cubic
claims:
  - benchmark: "11-workload Adam shared-β selection"
    metric: "mean relative validation gap vs β=0.95"
    value: "40.7% lower"
    baseline: "constant β=0.95"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08624"
    notes: "32.3% vs best constant β. Does not retarget Muon2 or AdamW as the layer default."
tags:
  - optimizer
  - adam
  - hyperparameters
  - adam-beta-cubic
  - active
---

# Adam Shared-Beta Cubic Rule

## Method Overview
Run a 200-update pilot. Probe gradients at four checkpoints. Fit a cubic rule to pick the shared Adam β (β1=β2=β) instead of defaulting to 0.95.

## When to Use
- Adam / AdamW runs where β is still a free HP and a short pilot is cheaper than a grid.

## When NOT to Use
- ~7B hidden-layer optimizer → `method:muon2`. I/O AdamW without a sweep → `method:adamw-optimizer`.

## Relation to Existing SOTA
- Active HP plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2 or AdamW.

## Gotchas & Failure Modes
- **code: released** AlbertoFdezHdez/Adam_beta_rule_cubic as of 2026-10-07.
- Shared β is the paper's setting; do not copy the cubic onto decoupled β1≠β2 without re-fitting.
