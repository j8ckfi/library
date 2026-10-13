---
id: method:latentgrm
type: method
title: LatentGRM
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; LatentGRM is a faster generative judge, not the RLVR
    loss
  use_instead: method:cispo
- when: MoE/VL RLVR loss
  reason: SAPO remains MoE/VL RLVR; LatentGRM is latent reward modeling
  use_instead: method:sapo
assumptions:
- 'Generative RM / rubric judge. Paper: Qwen3-4B/8B vs matched Rubric-RM SFT on OpenRubrics.'
- 'Code: EADMO/LatentGRM (code_status: released).'
last_reviewed: '2026-10-13'
papers:
- paper:latentgrm
recipes:
- recipe:latentgrm
claims:
- benchmark: LatentGRM-4B/8B vote@5 Avg-8 preference vs matched Rubric-RM; vLLM vote@5
    cost
  metric: Avg-8 accuracy; trajectory/time compression
  value: 67.8 / 69.0 vs 67.0 / 68.1; 8.87–9.23× shorter steps; 6.11–6.95× vLLM speedup
  baseline: matched explicit Rubric-RM SFT judges
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.09788
  notes: Does not retarget CISPO or SAPO. RewardBench Chat still favors explicit Rubric-RM.
tags:
- post-training
- reward-model
- latentgrm
- active
---

# LatentGRM

## Method Overview
Chunk a rubric-guided evaluation into semantic units, compress them into a short latent trajectory, and emit a pairwise preference without generating the critique online. An offline interpreter reconstructs the text.

## When to Use
- Generative / rubric RM inference is the bottleneck (vote@k, repeated judging) and a matched explicit SFT judge is the alternative.

## When NOT to Use
Dense Pass@1 RLVR loss → `method:cispo`. MoE/VL RLVR → `method:sapo`.

## Relation to Existing SOTA
Active plug-in on `task:reasoning-rl-alignment` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO or SAPO.

## Gotchas & Failure Modes
- **code: released** EADMO/LatentGRM as of 2026-10-13.
- RewardBench Chat still favors explicit Rubric-RM; the gain concentrates on Focus / Chat Hard.
- Interpreter is offline; do not treat reconstructed text as the online judge.
