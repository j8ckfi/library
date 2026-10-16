---
id: method:scope-t2i
type: method
title: 'SCOPE (T2I semantic-span GRPO)'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'privileged-OPSD Fisher subspace (SCOPE-OPSD)'
  reason: 'scope-opsd is hidden-state OPSD; this SCOPE is T2I span credit'
  use_instead: method:scope-opsd
- when: 'aggregation-first reward tilting for diffusion RL'
  reason: 'DiffusionART is reward tilting, not prompt-span GRPO'
  use_instead: method:diffusionart
- when: 'flow-model RL via proximal velocity matching'
  reason: 'MEND is velocity matching; SCOPE rewrites prompts'
  use_instead: method:mend
- when: 'on-policy self-distillation of a diffusion generator'
  reason: 'DiffusionOPSD remains generator OPSD'
  use_instead: method:diffusion-opsd
assumptions:
- 'Frozen image generator plus a prompt rewriter that emits a semantic partition. Paper: Qwen-Image / SD3 / FLUX.1-dev.'
- 'Code: MAC-AutoML/SCOPE (code_status: released). Distinct from method:scope-opsd.'
last_reviewed: '2026-10-16'
papers:
- paper:scope-t2i
recipes:
- recipe:scope-t2i
claims:
- benchmark: 'GeneVal / T2I-CompBench, Qwen-Image / SD3 / FLUX.1-dev vs vanilla GRPO'
  metric: 'average relative gain over GRPO'
  value: '+9.48% GeneVal; +7.62% T2I-CompBench'
  baseline: 'vanilla GRPO prompt rewriting (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22264'
  notes: 'Slug is scope-t2i. Distinct from method:scope-opsd. Does not retarget DiffusionOPSD / Self-OPD.'
tags:
- diffusion
- t2i
- grpo
- active
---

# SCOPE (T2I semantic-span GRPO)

## Method Overview
The rewriter emits an enhanced prompt and a semantic partition. SCOPE pools within-span log-probability shifts into one shared coefficient for those token losses, keeping a single completion advantage. No extra renders.

## When to Use
- GRPO prompt rewriting for a frozen T2I generator where credit should follow objects / counts / relations.

## When NOT to Use
Privileged OPSD subspace → `method:scope-opsd`. Diffusion generator OPSD → `method:diffusion-opsd`. Reward tilting → `method:diffusionart`. Velocity matching → `method:mend`.

## Relation to Existing SOTA
Active plug-in on `task:posttrain-diffusion` (`sota_for: []`). Does **not** replace DiffusionOPSD / Self-OPD.

## Gotchas & Failure Modes
- Name collision with `method:scope-opsd` (Fisher-subspace OPSD). Use `method:scope-t2i`.
- Relies on the rewriter's own span partition being meaningful.

