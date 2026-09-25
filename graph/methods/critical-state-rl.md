---
id: method:critical-state-rl
type: method
title: "Critical-State RL"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains the async-algorithm first hop; Critical-State RL diagnoses which turns to train"
    use_instead: "method:sao"
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains outcome-only coverage; this is a BFCL multi-turn diagnostic"
    use_instead: "method:canopy"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "folding a long tool trajectory into a small active context"
    reason: "FoldGRPO folds context; Critical-State RL selects which call receives gradient"
    use_instead: "method:foldgrpo"
  - when: "structural credit split for tool-call vs natural-language-summary tokens"
    reason: "Critical-State RL selects which turn is trainable; SLCA-GRPO routes tool vs summary advantages"
    use_instead: "task:tool-agent-segment-credit"
assumptions:
  - "Task-defined candidate calls and a local label. Nested sampling at a frozen prefix: sample actions, then resample reward-only continuations."
  - "Paper: Gemma-4-26B-A4B no-think four-cell on BFCL v4 multi_turn; also Nemotron missing-function, logged repeat-call, xLAM/Gemma memory."
  - "No public GitHub as of 2026-09-22. Reimplement the diagnostic; do not invent a SAO replacement."
last_reviewed: "2026-09-22"
papers:
  - paper:critical-state-rl
recipes:
  - recipe:critical-state-rl
claims:
  - benchmark: "BFCL v4 multi_turn miss_func, Gemma-4-26B-A4B no-think, four seeds"
    metric: "accuracy"
    value: "0.283 ± 0.015"
    baseline: "start 0.14; decision-turn alternative 0.095 (−4.5 pp)"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24985"
    notes: "Table 1. Diagnostic selects recovery after the tool becomes available. +14.3 pp. Deterministic nt=1, step 30, 200 paired items."
  - benchmark: "BFCL v4 multi_turn miss_param, same protocol"
    metric: "accuracy"
    value: "0.473 ± 0.010"
    baseline: "start 0.435; recovery alternative 0.445 (+1 pp)"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24985"
    notes: "Diagnostic selects the decision before the missing argument arrives. +3.8 pp. Monte-Carlo RTG 0.45."
tags:
  - post-training
  - agentic
  - tool-use
  - critical-state-rl
  - active
---

# Critical-State RL

## Method Overview
Critical-State RL diagnoses **which multi-turn model call is trainable**, then applies occurrence-local (contextual-bandit) RL only there.

A candidate phase qualifies when (1) the local label mediates action → benchmark return (action-sufficiency), (2) some action's label mean beats the reference policy (headroom), and (3) action-conditioned label means vary under the base policy (trainability). Nested sampling at a fixed prefix draws alternative actions, then holds each action fixed while resampling the continuation, separating \(\operatorname{Var}_a Q(x,a)\) from continuation noise. Mixed-reward GRPO/DAPO groups can be continuation noise (example: clean refusals with std 0.477 and no action difference).

Training applies the RL loss only to the selected call's tokens. Surrounding turns supply context or reward without gradient. SAO remains the async first hop. This is a diagnostic plug-in, not a straggler algorithm.

## When to Use
- Multi-turn tool use where several calls are plausible train targets (before vs after a tool appears; decision vs recovery) and you can nest-sample at a frozen prefix.

## When NOT to Use
- Async stragglers → `method:sao`. AppWorld coverage → `method:canopy`. Pass@1 → `method:cispo`. Trajectory folding → `method:foldgrpo`.

## Relation to Existing SOTA
- Active mention on `task:agentic-async-rl`. Does **not** enter `current_sota`. Does **not** replace `method:sao`, `method:canopy`, `method:cispo`, or `method:foldgrpo`.

## Gotchas & Failure Modes
- No public code as of 2026-09-22. The trainable turn is model- and task-specific: Gemma miss_func trains recovery; Nemotron miss_func trains the decision before tool availability. Do not freeze a role.
- Teacher-forced prefixes can mask recovery-turn trainability. Pooling labels across generated prefixes mixes upstream noise.
- Targeted SFT at the selected turn can over-fire the tool and break required refusals (miss_func recovery SFT −6 pp vs base).
