---
id: method:metarubric
type: method
title: "MetaRubric"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "no programmatic checker exists and the reward must come from process criteria without learning the rubric"
    reason: "DRACO is outcome-blind dynamic rubrics + closed-form step credit; MetaRubric learns the rubric against Vacuous Credit"
    use_instead: "method:draco"
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains coverage; MetaRubric is rubric-judge RL"
    use_instead: "method:canopy"
  - when: "rubric-privileged OPD warm start then rubric RL (teacher sees the rubric)"
    reason: "RP-OPD treats the rubric as given privileged teacher context; MetaRubric adapts the rubric itself"
    use_instead: "method:rp-opd"
assumptions:
  - "Instance-specific rubrics plus an LM judge. Inner GRPO uses min(satisfaction, coverage, evidence). Outer loop revises criteria and weights. Paper: medical text and multimodal benches."
  - "Official code metarubric/metarubric released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:metarubric
recipes:
  - recipe:metarubric
claims:
  - benchmark: "PubMedQA vs static-judge GRPO"
    metric: "accuracy"
    value: "Qwen3-4B 78.40 / Gemma-e2b 72.00"
    baseline: "GRPO 72.40 / 51.60 (+6.00 / +20.40)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02824"
    notes: "Not a CANOPY AppWorld TGC retarget. Not DRACO."
  - benchmark: "HealthBench-Hard vs static-judge GRPO"
    metric: "accuracy"
    value: "Qwen3-4B 13.02 / Qwen3-8B 10.34"
    baseline: "GRPO 10.56 / 7.15 (+2.46 / +3.19)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02824"
    notes: "Same paper tables."
  - benchmark: "MMOral-OPG vs static-judge GRPO"
    metric: "score"
    value: "Qwen3-8B 30.44 / Gemma 35.10"
    baseline: "GRPO 27.35 / 31.28 (+3.09 / +3.82)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02824"
    notes: "Multimodal medical."
tags:
  - post-training
  - rl-alignment
  - rubric
  - metarubric
  - active
---

# MetaRubric

## Method Overview
Static rubric judges can award a criterion when the required evidence is missing. That Vacuous Credit can flip GRPO advantages. MetaRubric's inner loop bounds criterion credit by the min of satisfaction, coverage, and evidential support. The outer loop revises criterion text and group weights from current-policy errors, keeping the original rubric's meaning under each prompt's facts (and a paired counterfactual). DRACO writes rubrics without learning a judge; RP-OPD treats a fixed rubric as privileged teacher context.

## When to Use
- Rubric-based RL where the judge hallucinates credit and you can afford an outer rubric-adaptation loop.

## When NOT to Use
- Outcome-blind rubric credit, no learned judge → `method:draco`. Checker TGC → `method:canopy`. Privileged rubric OPD then RL → `method:rp-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:outcome-only-long-horizon-agent-rl` beside DRACO / CANOPY (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace DRACO or CANOPY.

## Gotchas & Failure Modes
- +6.00 / +20.40 PubMedQA is vs static-judge GRPO, not vs DRACO or CANOPY.
- Counterfactual prompt pairs are part of the method; dropping them is not MetaRubric.
