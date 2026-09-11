---
id: method:t1-terminal-rl
type: method
title: "T1 Terminal Agent RL"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "AppWorld outcome-only coverage / anti-drift"
    reason: "T1 is a 122B terminal-MoE recipe on slime; CANOPY remains AppWorld coverage"
    use_instead: "method:canopy"
  - when: "async stragglers / tool-latency replay algorithm"
    reason: "SAO remains the async-algorithm default"
    use_instead: "method:sao"
  - when: "production post-train engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier stack; T1 runs on slime v0.3.0, Miles' ancestor"
    use_instead: "method:miles"
  - when: "SWE issue-to-patch harness"
    reason: "mini-SWE-agent remains the harness"
    use_instead: "method:mini-swe-agent"
  - when: "single-turn math/code Pass@1"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "122B-total MoE, real shell in a cloud sandbox, ≤300+ tool turns, per-task verifier reward. Host: slime v0.3.0 (commit bf14dc21), Megatron-Core, SGLang 0.5.12.post1."
  - "Project page + HF collection; no dedicated T1 trainer repo as of 2026-09-11."
last_reviewed: "2026-09-11"
papers:
  - paper:t1-terminal-rl
recipes:
  - recipe:t1-terminal-rl
claims:
  - benchmark: "Terminal-Bench 2.1 resolved rate"
    metric: "resolved %"
    value: 64.0
    baseline: "same-size base 43.8%"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11042"
    notes: "OOD train corpus vs the bench. TITO + R3: train–inference logp gap 0.021→0.013."
  - benchmark: "Long-Horizon Terminal Bench"
    metric: "resolved %"
    value: 27.9
    baseline: "paper: surpasses GPT-5.4 and GLM-5.1 under the same harness"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11042"
    notes: "300+ tool-call turns. Not an AppWorld TGC number; do not retarget CANOPY."
tags:
  - post-training
  - agentic
  - terminal
  - moe
  - slime
  - active
---

# T1 Terminal Agent RL

## Method Overview
122B MoE trained with RL on a live terminal. Aggressive critic warm-start with a dense process reward (count of passing verifiers). **TITO**: token-in preserves prefixes; token-out stitches streams under loss masks; drift repair at turn boundaries. **R3**: record sampler expert IDs at every MoE layer during rollout and replay them at train time. Data disjoint from Terminal-Bench 2.1.

Active long-horizon **terminal** recipe on slime. Miles is the production stack (slime-descended). SAO is async stragglers. CANOPY is AppWorld coverage. None of those first hops move.

## When to Use
- Training or reproducing a large MoE terminal agent with verifier-per-task rewards and you need train–serve routing identity (R3) plus token identity (TITO).

## When NOT to Use
- AppWorld coverage → `method:canopy`. Async algorithm → `method:sao`. Stack → `method:miles`. Harness → `method:mini-swe-agent`. Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active mention on `task:outcome-only-long-horizon-agent-rl`, `task:frontier-rl-posttrain-stack`, and `task:agentic-async-rl`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- No standalone T1 GitHub trainer; attach to slime. Miles v0.1 is the library's production engine if you need the stack, not this 122B checkpoint recipe.
- 64% Terminal-Bench 2.1 is not AppWorld TGC and not a reason to drop CANOPY.
