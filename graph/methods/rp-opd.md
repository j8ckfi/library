---
id: method:rp-opd
type: method
title: "RP-OPD then RL"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation default"
    reason: "OPD remains matching distillation; RP-OPD is a rubric-privileged warm start then rubric RL"
    use_instead: "method:opd"
  - when: "verifiable math/code OPD then RLVR (not rubric rewards)"
    reason: "OPD-then-RLVR sequences OPD then labeled RLVR; RP-OPD is rubric-privileged then rubric RL"
    use_instead: "method:opd-then-rlvr"
  - when: "no programmatic checker exists and the reward must come from process criteria without a privileged teacher"
    reason: "DRACO is outcome-blind rubric credit; RP-OPD needs a rubric-aware teacher"
    use_instead: "method:draco"
  - when: "learning the rubric itself during RL (vacuous credit)"
    reason: "MetaRubric adapts the rubric; RP-OPD treats the rubric as given privileged context"
    use_instead: "method:metarubric"
assumptions:
  - "A rubric exists and a larger teacher can see it. Student never sees the rubric at train or serve. Stage-2 is rubric-reward RL."
  - "NeurIPS 2026. Paper: Qwen2.5-3B/7B and Llama-3.1-8B on HealthBench / ResearchQA / RubricHub Science."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:rp-opd
recipes:
  - recipe:rp-opd
claims:
  - benchmark: "Qwen2.5-7B HealthBench / ResearchQA / RubricHub Science"
    metric: "rubric score"
    value: "0.673 / 0.797 / 0.829"
    baseline: "SFT+RL 0.607 / 0.721 / 0.815; RL no SFT 0.583 / 0.672 / 0.651"
    date: "2026-10-05"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.02781"
    notes: "NeurIPS 2026. Not a CISPO Pass@1 retarget. Not OPD-then-RLVR (verifiable)."
  - benchmark: "Qwen2.5-3B HealthBench / ResearchQA / RubricHub Science"
    metric: "rubric score"
    value: "0.632 / 0.776 / 0.735"
    baseline: "SFT+RL 0.612 / 0.743 / 0.682"
    date: "2026-10-05"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.02781"
    notes: "Same two-stage recipe."
  - benchmark: "Llama-3.1-8B HealthBench"
    metric: "rubric score"
    value: "0.634"
    baseline: "SFT+RL 0.526"
    date: "2026-10-05"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.02781"
    notes: "Llama-3.1-70B teacher."
tags:
  - post-training
  - distillation
  - rubric
  - rp-opd
  - active
---

# RP-OPD then RL

## Method Overview
Rubric RL assigns one score after the full response. RP-OPD first gives a teacher the rubric as privileged context and trains the student with token-level OPD on student prefixes (student never sees the rubric). Stage two runs rubric-reward RL from that checkpoint past the distillation plateau. OPD-then-RLVR is the verifiable sibling; this is the rubric sibling.

## When to Use
- Open-ended / non-verifiable tasks with an explicit rubric and a teacher that can read it.

## When NOT to Use
- Single-teacher matching → `method:opd`. Verifiable OPD then RLVR → `method:opd-then-rlvr`. Outcome-blind rubric credit with no privileged teacher → `method:draco`. Learning the rubric online → `method:metarubric`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside OPD / OPD-then-RLVR (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD or OPD-then-RLVR.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Rubric-conditioned SFT alone underperforms the RP-OPD warm start on the same teacher.
