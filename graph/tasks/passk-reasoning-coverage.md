---
id: task:passk-reasoning-coverage
type: task
title: "Math/Code RLVR for Pass@K Coverage without Backward Pass"
domain: "post-training"
summary: "Verifiable math/code post-training when the objective is Pass@K / reasoning-path coverage or a no-backward memory budget, rather than Pass@1 alone."
current_sota:
  - method: method:es-reasoning
    as_of: "2026-08-31"
    benchmark: "GSM8K Easy Setting averages and DeepScaleR Hard Setting math average (AIME24/AIME25/AMC23/MATH500)"
    metric: "Pass@1 / Pass@16 / Pass@32"
    value: "ES beats GRPO on Pass@16/@32 while still lifting Pass@1 over base; ES then GRPO keeps most of GRPO Pass@1 and the best Hard Pass@32"
    notes: "ES-reasoning (2608.27351). CISPO remains the Pass@1 dense RLVR default on task:math-code-rl-dense. GRPO stays retired."
methods:
  - method:es-reasoning
  - method:cispo
  - method:grpo
  - method:dapo
tags:
  - post-training
  - rl-alignment
  - passk
  - evolution-strategies
  - es-reasoning
---

# Math/Code RLVR for Pass@K Coverage without Backward Pass

## Problem Definition
Post-train a dense reasoner on verifiable math/code rewards when repeated-sampling coverage (Pass@K) matters, or when backward-pass memory is unavailable. GRPO-style policy gradients often raise Pass@1 while collapsing entropy and dropping large-K versus the base model. This is not the default labeled Pass@1 RLVR task.

## Evaluation Protocol
- **Primary Benchmarks**: Easy setting — GSM8K post-train, Pass@K on GSM8K/CSQA/HotpotQA/Countdown/GPQA/MBPP. Hard setting — DeepScaleR on DeepSeek-R1-Distill-Qwen-1.5B, math average over AIME24/AIME25/AMC23/MATH-500.
- **Evaluation Pitfalls**: FLOP-match uses N=32 ES directions versus GRPO G=8. Do not revive GRPO as the library default. Pass@1-first labeled RLVR stays `method:cispo`.

## SOTA Recommendation (as of 2026-08-31)
- **Primary Method (Pass@K / coverage / no-backward)**: **ES-reasoning** (`method:es-reasoning`, `paper:es-reasoning` `arXiv:2608.27351`).
- **Pass@1 default when labels exist**: **CISPO** (`method:cispo`) on `task:math-code-rl-dense`. Sequential ES then GRPO is a Pareto composition in the ES paper, not a GRPO revival.
