---
id: method:spectral-moe
type: method
title: Spectral-MoE
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: dense-to-MoE via learned binary-mask experts over a frozen FFN
  reason: MASKerade remains the upcycling first hop; Spectral-MoE allocates per-layer utilization
  use_instead: method:maskerade
- when: choosing the frontier MoE architecture template
  reason: DeepSeek-V4 / Kimi-K3 remain sparse-from-scratch
  use_instead: method:deepseek-v4
- when: static sparse upcycling via token-indexed embedding residuals
  reason: STAPLE is embedding residuals, not routed experts
  use_instead: method:staple
assumptions:
- Converted dense FFN experts with a utilization budget. Static per-layer scalar or dynamic per-token schedule.
- GitHub ZacharyBroveak/Spectral-MoE README-only as of 2026-10-15 (`code_status: announced`).
last_reviewed: '2026-10-15'
papers:
- paper:spectral-moe
recipes:
- recipe:spectral-moe
claims:
- benchmark: Llama-2-7B / Llama-3-8B / Qwen2.5-7B dense-to-MoE at 25% FFN utilization
  metric: WikiText-2 PPL drop vs uniform; six-task mean accuracy
  value: dynamic learned -1.04/-2.96/-2.71 PPL; analytic -2.45/-6.26/-2.17; six-task +1.5/+4.2/+3.6 at 12.5/25/50%
  baseline: uniform per-layer expert count on analytic and learned converters (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19232
  notes: Does not retarget MASKerade.
tags:
- architecture
- moe
- upcycling
- active
---

# Spectral-MoE

## Method Overview
Dense-to-MoE converters usually activate the same expert count in every layer. Spectral-MoE spends a utilization budget heterogeneously: a static per-layer scalar shared across tokens, or a dynamic per-token schedule. Both wrap analytic and learned conversion bases.

## When to Use
- You already convert a dense FFN to experts and the remaining gain is where to spend the active-expert budget.

## When NOT to Use
Mask-expert upcycling default → `method:maskerade`. From-scratch MoE → `method:deepseek-v4`. Embedding-residual upcycle → `method:staple`.

## Relation to Existing SOTA
Active plug-in on `task:dense-to-moe-upcycling` (`sota_for: []`). Does **not** replace MASKerade.

## Gotchas & Failure Modes
- **code: announced** (README-only) as of 2026-10-15.
