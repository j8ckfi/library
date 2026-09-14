---
id: method:evors
type: method
title: "EvoRS (On-Policy Reward-System Self-Evolution)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "a programmatic checker exists and sparse outcome RL is enough"
    reason: "CANOPY is the checker protocol; EvoRS evolves an open-ended Reward-DAG"
    use_instead: "method:canopy"
  - when: "no checker, but a frozen judge can score dynamic rubrics with closed-form step credit"
    reason: "DRACO is the outcome-blind rubric sibling; EvoRS evolves the whole reward system"
    use_instead: "method:draco"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL"
    use_instead: "method:sao"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Open-ended writing/roleplay (paper) with a GRM. Qwen3-4B/8B policy, Qwen3.5-27B or RewardAnything-8B GRM. Reward-DAG starts from the same single-node continuous scorer as RLAIF and evolves every five RL steps."
  - "No official GitHub as of 2026-09-14. Not AppWorld TGC."
last_reviewed: "2026-09-14"
papers:
  - paper:evors
recipes:
  - recipe:evors
claims:
  - benchmark: "WritingBench + CoSER, three-judge average (GPT-5.6-Terra / DeepSeek-V4-Pro / GLM-5.2)"
    metric: "final policy quality vs static and dynamic rubric RL"
    value: "best among RLAIF / RaR / RLER / OpenRS-style pairwise in the paper"
    baseline: "static rubrics (RLAIF, RaR) and dynamic rubrics (RLER)"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12459"
    notes: "Also lowers reward-hacking (HR) and coverage-failure (CFR) rates. Not a CANOPY/DRACO AppWorld bake-off."
tags:
  - post-training
  - rubrics
  - open-ended
  - evors
  - active
---

# EvoRS (On-Policy Reward-System Self-Evolution)

## Method Overview
Open-ended RL breaks the reward as the policy learns: hacking, holes, and collapsed informativeness. EvoRS stores the reward system as an executable Reward-DAG. A designer reads on-policy traces, proposes bounded DAG edits, and accepts a candidate only if success, anti-hack, health, and informativeness guards pass. The accepted DAG then scores the next policy updates.

## When to Use
- Writing / roleplay / other open-ended RL where a static or one-shot dynamic rubric starts to hack or go silent.

## When NOT to Use
- Checker exists → `method:canopy`. Frozen-judge step credit → `method:draco`. Async tools → `method:sao`. Math Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active note on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace CANOPY or DRACO. Different domain (writing/roleplay Reward-DAG vs AppWorld TGC).

## Gotchas & Failure Modes
- Guards are load-bearing. Skipping self-validation is just another hacking channel.
- No public code as of 2026-09-14.
