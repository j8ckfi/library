---
id: method:forkgrpo
type: method
title: ForkGRPO
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: recycle an AR post-training weight delta onto a converted dLLM
  reason: A2D recycles a weight delta; ForkGRPO is dLLM RL from high-entropy forks
  use_instead: method:a2d
- when: AR→discrete-dLLM on-policy distillation
  reason: JustOPD distills AR logits; ForkGRPO is GRPO-family RL on the dLLM
  use_instead: method:justopd
- when: curriculum RL for a discrete diffusion LM (canvas anneal)
  reason: CanvasAnneal is canvas curriculum; ForkGRPO forks rollouts
  use_instead: method:canvasanneal
- when: single-turn dense AR math/code Pass@1 RLVR
  reason: CISPO remains AR Pass@1
  use_instead: method:cispo
assumptions:
- Discrete diffusion LM RL. Fork continuations from high-entropy intermediate states; reuse prefixes; mix within-state group advantages with MC state-value differences.
- No dedicated repo as of 2026-10-15 (JustGRPO host exists separately).
last_reviewed: '2026-10-15'
papers:
- paper:forkgrpo
recipes:
- recipe:forkgrpo
claims:
- benchmark: dLLM RL GSM8K / MATH-500 / HumanEval / MBPP vs JustGRPO
  metric: accuracy; generated tokens; ForkGRPO-fast wall-clock
  value: 90.4/46.6/51.8/49.0 vs JustGRPO +0.8/+0.6/+1.2/+0.4; 18.75-27.83% fewer tokens; ForkGRPO-fast 2.49x, 90.3 GSM8K
  baseline: JustGRPO left-to-right GRPO (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19408
  notes: Does not retarget A2D, JustOPD, or CanvasAnneal.
tags:
- diffusion
- dllm
- rlvr
- active
---

# ForkGRPO

## Method Overview
Independent left-to-right dLLM rollouts miss alternative continuations from intermediate states and smear trajectory-level advantage across tokens. ForkGRPO samples multiple continuations from high-entropy states on a reference trajectory, prefers textual boundaries, and reuses shared prefixes. Within-state group-relative advantages pick continuations; Monte Carlo state-value differences credit the segments that changed expected outcome.

## When to Use
- Discrete dLLM RL where entropy collapse and uniform trajectory credit waste tokens.

## When NOT to Use
AR-delta recycle → `method:a2d`. AR→dLLM distill → `method:justopd`. Canvas curriculum → `method:canvasanneal`. AR Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:diffusion-lm-ar-delta-recycle` (`sota_for: []`) with a mention on `task:posttrain-diffusion`. Does **not** replace A2D.

## Gotchas & Failure Modes
- **code: none** dedicated as of 2026-10-15.
- Best on three of four benches among architecture-preserving RL methods in the paper.
