---
id: method:hp-rlvr
type: method
title: HP-RLVR (Hindsight-Privileged RLVR)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the dense math/code Pass@1 RLVR default
  reason: CISPO remains Pass@1; HP-RLVR is G=1 token credit from causal vs hindsight JSD
  use_instead: method:cispo
- when: branchy RLVR token cost; hindsight-divergence prefix reuse
  reason: HDL reuses prefixes inside a GRPO group; HP-RLVR scores one completed rollout
  use_instead: method:hdl
- when: outcome-only AppWorld coverage / anti-drift
  reason: CANOPY remains sparse-outcome coverage
  use_instead: method:canopy
assumptions:
- Single rollout per prompt. Causal vs hindsight JSD weights a historical reward baseline. No critic, no gold solution.
- Paper: Qwen3-1.7B/4B/8B, 100-step paired GRPO G=8 schedule.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:hp-rlvr
recipes:
- recipe:hp-rlvr
claims:
- benchmark: Qwen3-8B paired 100-step math/code/ALFWorld vs G=8 GRPO
  metric: wall-clock vs GRPO; math Avg@12; ALFWorld zero-gradient share
  value: 1.21x/1.46x/2.30x faster; math 65.73 vs 63.07; ALFWorld GRPO zero-grad 43.2% (4B) / 49.0% (8B) vs none
  baseline: G=8 GRPO at matched prompt and step budget (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.20497
  notes: Distinct from HDL. Does not retarget CISPO. GRPO ahead on 8B code and ALFWorld accuracy.
tags:
- rlvr
- hindsight
- credit-assignment
- active
---

# HP-RLVR (Hindsight-Privileged RLVR)

## Method Overview
Score each eligible token twice: under its causal prefix and under a hindsight context that includes the realized future and verifier feedback. Normalized JSD between those views weights a historical reward baseline, giving bounded token credit on successes and failures from G=1.

## When to Use
- RLVR where G=8 groups go silent and you can afford a second scoring pass on one completed rollout.

## When NOT to Use
Pass@1 default → `method:cispo`. Prefix reuse inside a group → `method:hdl`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`) with a mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- Math favors HP-RLVR; 8B code 38.87 vs GRPO 40.65 and ALFWorld 62.45 vs 65.32 favor GRPO.
- Training responses capped at 1024 tokens; ~42% of 4B GRPO hits the cap.
