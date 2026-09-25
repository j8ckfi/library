---
id: method:rufus-air
type: method
title: "Rufus-Air"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the production RL engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier post-train stack; Rufus-Air is an open 8-stage recipe on slime"
    use_instead: "method:miles"
  - when: "factory process / experiments-as-code / lineage"
    reason: "Poolside remains the factory control plane"
    use_instead: "method:poolside-model-factory"
  - when: "async stragglers / tool-latency replay"
    reason: "SAO remains the async-algorithm default; Rufus-Air documents slime infra, not straggler IS"
    use_instead: "method:sao"
  - when: "dense math/code Pass@1 loss"
    reason: "CISPO remains Pass@1; Rufus-Air hosts GSPO/GRPO inside stages"
    use_instead: "method:cispo"
assumptions:
  - "Start from public GLM-4.5-Air-Base (106B-A12B). Serial eight-stage pipeline on the same parameters."
  - "Infra: Slime + SGLang + Megatron. Paper uses GSPO/GRPO, Rollout Routing Replay, token-in/token-out multi-turn. SFT: 64×8 H200, batch 4096, AdamW peak 5e-5. RL: 8–32 nodes."
  - "No dedicated Rufus-Air GitHub as of 2026-09-25. Reproduce on THUDM/slime. Miles remains the engine."
last_reviewed: "2026-09-25"
papers:
  - paper:rufus-air
recipes:
  - recipe:rufus-air
claims:
  - benchmark: "IFBench / IFEval prompt-strict vs official GLM-4.5-Air"
    metric: "pass@1"
    value: "76.9 / 95.4"
    baseline: "GLM-4.5-Air 33.6 / 83.0"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29421"
    notes: "Table 1. Same-harness eval of the finished serial recipe. Not a Miles retarget."
  - benchmark: "LiveCodeBench v6 / Terminal-Bench 2.1 / SWE-bench Verified vs GLM-4.5-Air"
    metric: "pass@1"
    value: "76.4 / 42.7 / 65.6"
    baseline: "GLM-4.5-Air 59.6 / 24.7 / 50.6"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29421"
    notes: "Table 1. Coding and coding-agent stages. Competitive with Nemotron-3-Super on TB2.1 (tie 42.7)."
  - benchmark: "BrowseComp / HLE-Verified Gold vs GLM-4.5-Air"
    metric: "pass@1"
    value: "37.1 / 51.1"
    baseline: "GLM-4.5-Air 22.7 / 20.2"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29421"
    notes: "Table 1. Search-agent stage. Arena-Hard v2 Creative Writing loses to GLM-4.5-Air (53.0 vs 60.3)."
tags:
  - systems
  - training-systems
  - post-training
  - agentic
  - rufus-air
  - active
---

# Rufus-Air

## Method Overview
Rufus-Air is an **open 8-stage serial post-train playbook**, not a new RL engine. Start from GLM-4.5-Air-Base (106B-A12B) and train SFT → Reasoning RL → Coding RL → IF RL → General Agent → Coding Agent → Search Agent → RLHF, each stage on the previous checkpoint. Stage order tracks reward reliability: hard verifiers first, judge/preference last, so gameable rewards see less optimization time. Difficulty filtering drops already-solved and (in most stages) never-solved prompts. Infra that the paper treats as load-bearing: Slime + SGLang + Megatron, GSPO/GRPO, Rollout Routing Replay, token-in/token-out multi-turn, one chat template from SFT through agent stages.

Miles remains the production engine first hop on this task. Rufus-Air is the documented open recipe / stage-order sibling.

## When to Use
- You want a full open post-train recipe, stage order, and slime/SGLang agentic RL playbook on a public ~100B-A12B base.

## When NOT to Use
- Production RL engine (SGLang / Megatron / LoRA RL / OPD) → `method:miles`. Factory process → `method:poolside-model-factory`. Async stragglers → `method:sao`. Pass@1 kernel → `method:cispo`.

## Relation to Existing SOTA
- Active on `task:frontier-rl-posttrain-stack` beside Miles. Does **not** enter `current_sota`. Does **not** replace `method:miles`, `method:sao`, `method:cispo`, or `method:poolside-model-factory`.

## Gotchas & Failure Modes
- No dedicated Rufus-Air repo as of 2026-09-25. Reproduce on `THUDM/slime` + SGLang; do not invent a Miles replacement.
- Later stages update the same parameters. The order does not freeze earlier gains; measure each stage against the checkpoint it starts from.
- Arena-Hard v2 Creative Writing is worse than the vendor GLM-4.5-Air release. Do not cite Table 1 as a sweep of every bench.
- IF RL uses a rubric judge yet runs early because instruction following is close to what the policy already does. Do not reorder purely by "hard vs soft reward format."
