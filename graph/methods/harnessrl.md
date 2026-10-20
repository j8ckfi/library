---
id: method:harnessrl
type: method
title: 'HarnessRL'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production harness kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the kernel; HarnessRL is a training-time rubric harness'
  use_instead: method:omp2-harness
- when: 'alternating harness+policy RSI'
  reason: 'Self-HPO is the alternating-RSI plug-in'
  use_instead: method:self-hpo
- when: 'outcome-only coverage with a programmatic checker'
  reason: 'CANOPY remains coverage first hop'
  use_instead: method:canopy
assumptions:
- 'Open-ended rubric RL. Paper: Rubric-Mix-10k, Qwen3.5-4B/9B.'
- 'Code Tongyi-ConvAI/Qwen-Character/HarnessRL as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:harnessrl
recipes:
- recipe:harnessrl
claims:
- benchmark: 'Rubric-Mix-10k in-domain / OOD, Qwen3.5-4B and 9B'
  metric: 'rubric quality vs strongest baseline; steps to best checkpoint'
  value: '4B 64.5 in-domain / 49.8 OOD, +3.0 / +2.8 vs strongest baseline; 2.8-3.1 points at 4B and 9B; nearly halves steps to best ckpt'
  baseline: 'GRPO on static rubrics; strongest paper baselines'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26426'
  notes: 'Non-discriminative and spurious rubric rewards. Does not replace omp2, Self-HPO, or CANOPY.'
tags:
- agent-harness
- rubric-rl
- active
---

# HarnessRL

## Method Overview
HarnessRL co-evolves a just-in-time training harness with the policy through prompt, guidance, and criterion interfaces plus harness memory. Static rubric GRPO fails as scores collapse or become spurious (61.6% of pairs in the measured 4B run).

## When to Use
- Open-ended rubric RL where fixed criteria saturate or get hacked as the policy evolves.

## When NOT to Use
Production kernel → `method:omp2-harness`. Alternating RSI → `method:self-hpo`. Checker coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:agent-harness-runtime` (`sota_for: []`). Does **not** replace omp2, Self-HPO, or CANOPY.

## Gotchas & Failure Modes
- Work-in-progress paper.
- Rubric-Mix-10k is in-house; not HealthBench protocol.
