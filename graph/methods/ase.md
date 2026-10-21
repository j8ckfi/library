---
id: method:ase
type: method
title: 'ASE'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-turn dense math/code Pass@1 with CISPO as the loss'
  reason: 'CISPO remains Pass@1; ASE diversifies GRPO rollouts via activation steering'
  use_instead: method:cispo
- when: 'embedding-space directional exploration / anchored noise (EDEN)'
  reason: 'EDEN perturbs embeddings; ASE steers activation-difference clusters'
  use_instead: method:eden
assumptions:
- 'GRPO-family math RLVR. Paper: Qwen3-1.7B-Base / 8B-Base on DAPO-Math-17k.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:ase
recipes:
- recipe:ase
claims:
- benchmark: 'Qwen3-1.7B-Base / 8B-Base DAPO-Math-17k; six math benches Mean@8'
  metric: 'Mean@8 vs GRPO under the same rollout budget'
  value: '+4.87pp (1.7B) / +1.87pp (8B) vs GRPO'
  baseline: 'GRPO'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27012'
  notes: 'Clusters correct-vs-incorrect activation differences into a steering bank. Does not retarget CISPO.'
tags:
- rlvr
- exploration
- activation-steering
- active
---

# ASE

## Method Overview
ASE (Activation-Space Exploration) clusters activation differences between correct and incorrect responses, then applies those latent vectors to later rollouts so a fixed budget covers more reasoning paths.

## When to Use
- GRPO-family RLVR where rollouts collapse onto similar traces under a fixed sample budget.

## When NOT to Use
Pass@1 default → `method:cispo`. Embedding noise → `method:eden`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- Steering bank is built from the policy's own correct/incorrect pairs; empty banks give no exploration.
- Not a Pass@1 loss.
