---
id: method:thundersyncrl
type: method
title: "ThunderSyncRL"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "async straggler algorithm / importance-corrected replay"
    reason: "SAO remains the async-algorithm default; ThunderSyncRL is lossless gradient streaming"
    use_instead: "method:sao"
  - when: "production post-train engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier stack; ThunderSyncRL is a GRPO/OPD overlap recipe"
    use_instead: "method:miles"
assumptions:
  - "Agentic GRPO or OPD with long heterogeneous trajectories. Paper: SWE-bench Verified and Terminal Bench 4.0."
  - "No public repo URL as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:thundersyncrl
recipes:
  - recipe:thundersyncrl
claims:
  - benchmark: "SWE-bench Verified / Terminal Bench 4.0 vs synchronous GRPO/OPD"
    metric: "wall-clock to same performance"
    value: "up to 1.9× faster than synchronous"
    baseline: "batch-synchronous GRPO/OPD"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05935"
    notes: "Vs async at fixed budget up to +2.47pp. Does not retarget SAO or Miles."
tags:
  - post-training
  - training-systems
  - thundersyncrl
  - active
---

# ThunderSyncRL

## Method Overview
ThunderSyncRL overlaps learner compute with rollout without changing GRPO or OPD: stream a trajectory's score gradient when its reward arrives, and stream OPD turn gradients while tools run. The paper proves the streamed update equals the batch-sync update.

## When to Use
- Agentic GRPO/OPD where sync bubbles dominate and you refuse stale-policy async.

## When NOT to Use
- Async straggler algorithm → `method:sao`. Production stack → `method:miles`.

## Relation to Existing SOTA
- Active plug-in on `task:agentic-async-rl` beside `method:miles` / `method:sao` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace SAO or Miles.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06 (no URL in the abstract).
- Do not treat this as a SAO staleness-correction; the point is zero staleness.
