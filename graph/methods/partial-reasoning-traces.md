---
id: method:partial-reasoning-traces
type: method
title: "Partial Reasoning Traces"
category: "data-curriculum"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the open instruct / chat SFT stack"
    reason: "Trace truncation is a data-shaping plug-in; OLMo-3 Dolci remains the open instruct default"
    use_instead: "method:olmo-3"
  - when: "industrial multi-stage SFT"
    reason: "Nemotron-Cascade 2 remains the industrial instruct alt"
    use_instead: "method:nemotron-cascade-2"
  - when: "labeled Pass@1 RLVR algorithm"
    reason: "CISPO remains Pass@1; this paper only notes that truncation also helps RL hosts"
    use_instead: "method:cispo"
assumptions:
  - "Post-train on pre-collected reasoning trajectories (SFT primary; RL / on-policy distillation hosts also benefit). EMNLP 2026 Findings."
  - "Code: naver-ai/revisiting-trace."
last_reviewed: "2026-09-11"
papers:
  - paper:partial-reasoning-traces
recipes:
  - recipe:partial-reasoning-traces
claims:
  - benchmark: "Reasoning-trace SFT, full vs partial / truncated trajectories"
    metric: "SFT benefit of complete traces"
    value: "full traces give only limited benefit; partial traces remain effective under heavy truncation"
    baseline: "complete long CoT trajectories as the SFT target"
    date: "2026-09-11"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.07103"
    notes: "EMNLP 2026 Findings. Attention + token-removal: intermediate tokens contribute minimally. Also helps RL and on-policy distillation hosts. Not an OLMo-3 replacement."
tags:
  - post-training
  - sft
  - reasoning
  - data-recipe
  - active
---

# Partial Reasoning Traces

## Method Overview
Do not dump complete long CoT as the SFT target. Keep endpoints (question + late / answer-side tokens); drop or truncate the redundant middle. Attention maps and token-removal ablations say intermediate tokens add little. Models fill missing steps from internal knowledge when endpoints are known. The same shaping helps RL and on-policy distillation, not only SFT.

Active SFT-data plug-in. OLMo-3 / Nemotron-Cascade 2 stay the instruct defaults.

## When to Use
- Reasoner SFT (or RL / OPD) on long pre-collected traces. Prefer curated / partial traces.

## When NOT to Use
- Instruct stack pick → `method:olmo-3` / `method:nemotron-cascade-2`. Pass@1 algorithm → `method:cispo`.

## Relation to Existing SOTA
- Active on `task:instruct-sft-alignment` with a mention on math reasoner SFT (`task:math-code-rl-dense`). Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- Truncation is a data choice, not a new loss. Do not skip OLMo-3 mix quality.
- Paper does not license deleting gold answers; it licenses deleting the *middle*.
