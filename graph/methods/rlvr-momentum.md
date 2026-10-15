---
id: method:rlvr-momentum
type: method
title: When Does Momentum Help in RLVR
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the dense math/code Pass@1 RLVR default
  reason: This is a momentum-coefficient rule on GRPO/AdamW; CISPO remains Pass@1
  use_instead: method:cispo
- when: pilot-run cubic rule for Adam's shared beta in pretrain
  reason: Adam shared-beta cubic is NTP pretrain; this paper is RLVR EMA
  use_instead: method:adam-beta-cubic
assumptions:
- Bias-corrected EMA on policy gradients. Paper: Qwen3-4B-Base GRPO; Qwen2.5-32B AdamW.
- Scale beta with eta so eta/(1-beta) stays in the safe regime.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:rlvr-momentum
recipes:
- recipe:rlvr-momentum
claims:
- benchmark: Qwen2.5-32B AdamW RLVR; Qwen3-4B-Base GRPO with SGD-EMA and AdamW
  metric: mean validation accuracy vs conventional beta1
  value: Qwen2.5-32B +~2pp by increasing AdamW beta1; 4B larger coefficients improve and stabilize when paired with smaller LR
  baseline: conventional AdamW first-moment (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.20413
  notes: Does not retarget CISPO. Cousin of adam-beta-cubic, different task.
tags:
- optimizer
- rlvr
- momentum
- active
---

# When Does Momentum Help in RLVR

## Method Overview
Keep EMA momentum in RLVR, but scale beta with the learning rate so eta/(1-beta) stays in a no-overshoot regime. With exact gradients, larger beta accelerates. With sampled responses, a fixed beta's expected gain vanishes faster than sampling noise as eta shrinks; scaling beta preserves a nonvanishing gain.

## When to Use
- GRPO/AdamW RLVR where conventional beta1 looks useless and you can lower eta.

## When NOT to Use
Pass@1 algorithm → `method:cispo`. Pretrain shared-beta cubic → `method:adam-beta-cubic`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- A conventional beta with a small LR can hide the gain under sampling noise.
