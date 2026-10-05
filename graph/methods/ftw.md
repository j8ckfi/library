---
id: method:ftw
type: method
title: "Follow the Winners (FTW)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "variable environment latency / async stragglers"
    reason: "SAO remains the async algorithm default; FTW is critic-free RFT from a replay ordinal filter when group rollouts are impractical"
    use_instead: "method:sao"
  - when: "single-turn dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; FTW is stateful-agent RFT"
    use_instead: "method:cispo"
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains coverage / anti-drift; FTW does not scale same-task groups"
    use_instead: "method:canopy"
assumptions:
  - "Stateful environment where repeating a prompt from an identical initial state is impractical. Replay buffer of past trajectories. NeurIPS 2026."
  - "Paper: Search-R1 Qwen2.5-3B-Instruct; Sokoban curves (no single Sokoban headline)."
  - "No dedicated public repo as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:ftw
recipes:
  - recipe:ftw
claims:
  - benchmark: "Search-R1, Qwen2.5-3B-Instruct Avg. Test Acc. %"
    metric: "average test accuracy"
    value: "35.46 ± 0.15"
    baseline: "Search-R1 GRPO 33.6 / PPO 32.5"
    date: "2026-10-05"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.03361"
    notes: "NeurIPS 2026. FTW-K1-C4. Not a SAO async-straggler retarget."
tags:
  - post-training
  - rl-alignment
  - agentic
  - ftw
  - active
---

# Follow the Winners (FTW)

## Method Overview
GRPO estimates a baseline from several rollouts of the same prompt in the same initial state. FTW instead keeps a replay buffer and applies a CEM-style ordinal filter: keep the top quantile of returns in the minibatch and project the policy onto those winners. Selection pressure controls a bounded risk-seeking offset that FTW shares with DPO; GRPO is risk-neutral under the same control-as-inference view.

## When to Use
- Stateful agent RFT (live services, security sandboxes) where you cannot reconstruct initial states for GRPO groups and you do not want a second-model critic.

## When NOT to Use
- Async tool stragglers → `method:sao`. Dense math Pass@1 → `method:cispo`. AppWorld coverage with a checker → `method:canopy`.

## Relation to Existing SOTA
- Active plug-in on `task:agentic-async-rl` beside SAO (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace SAO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05. Do not treat verl-agent as an FTW release.
- Sokoban is curves, not a single number — do not invent one.
- GRPO stays retired as a library math/code default; citing FTW vs GRPO on Search-R1 does not revive GRPO on `task:math-code-rl-dense`.
