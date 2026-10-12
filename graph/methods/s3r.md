---
id: method:s3r
type: method
title: S3R
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: production post-train engine (SGLang / Megatron / LoRA RL / OPD)
  reason: S3R is sparse-draft / dense-verify rollouts; Miles remains the engine
  use_instead: method:miles
- when: single-turn dense math/code Pass@1 RLVR algorithm
  reason: CISPO remains Pass@1; S3R does not change the loss
  use_instead: method:cispo
- when: speculative draft co-train inside long-context RL (separate draft)
  reason: Online Draft Co-Training trains a separate draft; S3R shares one policy
  use_instead: method:online-draft-cotrain
assumptions:
- 'Long-context RLVR where attention is 72-76% of decode kernel time. Paper: Qwen3, long-context math.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:s3r
recipes:
- recipe:s3r
claims:
- benchmark: Long-context mathematical reasoning RLVR on Qwen3
  metric: end-to-end training throughput vs dense autoregressive rollouts
  value: 1.39×–1.35× with comparable task performance; direct sparse sampling with training-side correction
    is unstable
  baseline: dense autoregressive rollouts; sparse sampling + IS/reweight correction
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13202
  notes: Does not retarget Miles or CISPO. Group-relative advantages are not recovered by response-wise
    reweighting of a sparse policy.
tags:
- systems
- rlvr
- speculative-decoding
- s3r
- active
---

# S3R

## Method Overview
Propose tokens with the same policy under sparse attention. Accept/reject with full-attention speculative sampling so the kept group is exactly the dense policy. Schedule KV so verify does not reload the full history every draft.

## When to Use
- Long-context RLVR rollouts where attention dominates decode and you must keep dense-policy groups for GRPO/CISPO-family advantages.

## When NOT to Use
Production engine choice → `method:miles`. Pass@1 loss → `method:cispo`. Separate learned draft → `method:online-draft-cotrain`.

## Relation to Existing SOTA
Active plug-in on `task:frontier-rl-posttrain-stack` with a mention on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace Miles or CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Do not train on sparse-policy samples even with IS.
- Dense verify still needs the full historical KV; the scheduler is load-bearing.
