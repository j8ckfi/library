---
id: method:rgpo
type: method
title: "RGPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "RGPO is adaptive rationale scaffolding on sparse-reward RLVR; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "sparse local off-policy intervention rather than rationale scaffolding"
    reason: "MInTRL is a sparse-intervention plug-in; RGPO scaffolds ground-truth rationales"
    use_instead: "method:mintrl"
  - when: "Pass@K / coverage / no-backward"
    reason: "ES-reasoning remains Pass@K"
    use_instead: "method:es-reasoning"
assumptions:
  - "Sparse-reward RLVR with access to ground-truth rationales. NeurIPS 2026. Code: VietHoang1512/rgpo (`code_status: released`)."
  - "Pair with paper:ga-grpo for the closed-form guidance weight λ*(T,δ,σ²)."
last_reviewed: "2026-10-07"
papers:
  - paper:rgpo
  - paper:ga-grpo
recipes:
  - recipe:rgpo
claims:
  - benchmark: "Sparse-reward RLVR with adaptive ground-truth rationale scaffolding"
    metric: "rationale-guided policy optimization vs unguided group RL"
    value: "adaptive GT rationale scaffolding (NeurIPS 2026)"
    baseline: "unguided GRPO-family RLVR; LUFFY / ExPO-style fixed guidance"
    date: "2026-10-07"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.07342"
    notes: "Theory sibling paper:ga-grpo (2610.06861) λ*=σ0²/(σ0²+Rmax²δ²T); 31% fewer GPU-h on Qwen2.5-Math-7B-Base. Does not replace CISPO."
tags:
  - post-training
  - rl-alignment
  - guidance
  - rgpo
  - active
---

# RGPO

## Method Overview
Rationale-Guided Policy Optimization adaptively scaffolds ground-truth rationales for sparse-reward RLVR instead of dumping a fixed expert trace. GA-GRPO (`paper:ga-grpo`) is the bias-variance theory of that guidance family.

## When to Use
- Sparse-reward math/code RLVR with GT rationales available, beside MInTRL / LUFFY / ExPO-style methods.

## When NOT to Use
- Pass@1 default → `method:cispo`. Sparse intervention without rationales → `method:mintrl`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: released** VietHoang1512/rgpo as of 2026-10-07.
- GA-GRPO is theory/evidence, not a second trainer.
