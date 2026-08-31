---
id: task:data-free-self-evolution
type: task
title: "Data-Free Self-Evolution across Verifiable and Unverifiable Domains"
domain: "post-training"
summary: "Closed-loop self-evolution with no external training data, covering both verifiable tasks and unverifiable/open-ended domains via co-evolving Challenger, Solver, and Judge."
current_sota:
  - method: method:j-zero
    as_of: "2026-08-31"
    benchmark: "Verifiable overall avg and unverifiable overall avg (Qwen3-4B-Base / Qwen3-8B-Base)"
    metric: "domain-average score"
    value: "Verifiable 54.38 / 58.55; unverifiable 20.81 / 23.41"
    notes: "J-Zero (2608.26582) vs R-Zero 49.64/54.99 and 12.66/15.54, G-Zero 47.41/53.07 and 10.89/15.31, base 44.91/50.67 and 9.58/13.23. Stated average gains +4.2 verifiable and +8.0 unverifiable."
methods:
  - method:j-zero
  - method:u-opsd
  - method:ttpo
  - method:cispo
tags:
  - post-training
  - self-evolution
  - data-free
  - self-play
  - unverifiable
  - j-zero
---

# Data-Free Self-Evolution across Verifiable and Unverifiable Domains

## Problem Definition
Improve a language model with zero external training tasks or labels. A Challenger writes tasks, a Solver answers them, and a Judge scores the answers. Verifiable domains have checkable answers; unverifiable/open-ended domains do not, so a frozen Judge becomes a ceiling after a few iterations.

## Evaluation Protocol
- **Primary Benchmarks**: Verifiable overall average (math, general reasoning, IFEval) and unverifiable overall average (AlpacaEval 2.0, Arena-Hard-v2.0, EQ-Bench Creative Writing v3) on Qwen3-4B-Base and Qwen3-8B-Base.
- **Evaluation Pitfalls**: Do not confuse with unlabeled post-training on an existing problem corpus (`task:label-free-reasoner-posttrain` / `method:u-opsd`) or test-time adaptation (`task:label-free-test-time-reasoner` / `method:ttpo`). Those start from given prompts; this task generates the curriculum from scratch.

## SOTA Recommendation (as of 2026-08-31)
- **Primary Method**: **J-Zero** (`method:j-zero`, `paper:j-zero` `arXiv:2608.26582`) for Challenger–Solver–Judge co-evolution from zero data.
- **Not This Task**: `method:u-opsd` remains the unlabeled existing-math-problems default; `method:ttpo` remains test-time; `method:cispo` / `method:sapo` / `method:sao` remain labeled and agentic RL defaults.
