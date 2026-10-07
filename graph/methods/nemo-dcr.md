---
id: method:nemo-dcr
type: method
title: "NeMo-DCR"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the production frontier RL post-train engine"
    reason: "NeMo-DCR is a weight-sync plug-in; Miles remains the engine"
    use_instead: "method:miles"
  - when: "open 8-stage serial post-train recipe / stage order on slime"
    reason: "Rufus-Air is the stage-order playbook; DCR is delta refit"
    use_instead: "method:rufus-air"
  - when: "lossless gradient/rollout overlap rather than weight sync"
    reason: "ThunderSyncRL overlaps compute; DCR compresses the weight ship"
    use_instead: "method:thundersyncrl"
assumptions:
  - "Disaggregated agentic RL where trainer and rollout do not share memory. Paper: ~1% of BF16 weights change per step at 1T."
  - "Code: NVIDIA-NeMo/RL PR #2444 (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:nemo-dcr
recipes:
  - recipe:nemo-dcr
claims:
  - benchmark: "1T disaggregated agentic RL weight sync"
    metric: "relay-tree sync time vs full BF16 ship"
    value: "150s vs 87.5 min"
    baseline: "full BF16 weight ship"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08430"
    notes: "~1% of BF16 weights change per step. 12–40× faster at 3–5% change. Does not replace Miles."
tags:
  - systems
  - training-systems
  - weight-sync
  - nemo-dcr
  - active
---

# NeMo-DCR

## Method Overview
Bit-exact delta-compressed refit for disaggregated agentic RL. Ship only the coordinates that changed (~1% of BF16 weights per step) over a relay tree.

## When to Use
- Trillion-scale disaggregated RL where weight sync dominates the step.

## When NOT to Use
- Production engine choice → `method:miles`. Stage-order recipe → `method:rufus-air`.

## Relation to Existing SOTA
- Active infra plug-in on `task:frontier-rl-posttrain-stack` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Miles.

## Gotchas & Failure Modes
- **code: released** NVIDIA-NeMo/RL PR #2444 as of 2026-10-07.
- Bit-exact is the contract; do not mix with lossy quantization of the delta.
