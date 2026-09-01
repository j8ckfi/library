---
id: task:training-data-attribution
type: task
title: "Training Data Attribution (LOO / LDS / Query-Conditioned Scoring)"
domain: "interpretability"
summary: "Estimate the leave-one-out or leave-k-out effect of training tokens or sequences on a query behavior, and score examples for fact tracing or LESS-style filtering."
scope: "Leave-one-out / linear datamodeling score (LDS), fact tracing, and LESS-style example or token scoring of a training corpus for a specified query eval."
out_of_scope:
  - "Mix-ratio search over data sources (Dolma / OLMo-3 / AutoMixer)"
  - "SAE dictionaries, circuits, and steering (SASA / CircuitSteer / FEGA)"
  - "Train kernels: optimizer, architecture, RLVR loss (Muon2, CISPO, OPD)"
  - "Unlearning trainers and forget-set optimization"
  - "Fused MoE expert attribution (gpt-oss, Mixtral, Qwen-MoE, OLMoE)"
redirects:
  - when: "mix-ratio search or replacing an open pretrain mix"
    to: "task:open-data-recipe"
  - when: "SAE dictionaries, circuits, or effect geometry"
    to: "task:mechanistic-interpretability-dictionaries"
  - when: "factory process / experiments-as-code / lineage"
    to: "task:industrial-model-building"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:magic
    as_of: "2026-09-01"
    benchmark: "GPT-2 WikiText FT LDS (50 queries, N=400 retrains, 95% CI, Adam)"
    metric: "Spearman rho (LDS)"
    value: "0.983 ± 0.005"
    notes: "MAGIC (2504.16430) via Bergson Table 1. Narrow LDS claim only. Bergson is the library, not the SOTA algorithm. Does not retarget mix, train-kernel, factory, or SAE SOTA."
methods:
  - method:magic
  - method:bergson
  - method:trackstar
  - method:ek-fac
  - method:source-unrolling
tags:
  - interpretability
  - data-attribution
  - influence
  - lds
  - magic
  - bergson
---

# Training Data Attribution (LOO / LDS / Query-Conditioned Scoring)

## Problem Definition
Estimate how a query behavior (eval loss, a fact, a capability probe) would change if particular training tokens or sequences were up-weighted, down-weighted, or removed. Typical outputs are per-token or per-sequence influence scores, Linear Datamodeling Score (LDS) against retrains, and ranked subsets for LESS-style filtering.

This is a **diagnostic / tooling** task, not a training kernel. It does **not** replace:

- Open data mix: `method:olmo-3` on `task:open-data-recipe` (AutoMixer remains a factory mix-search component)
- Dense optimizer: `method:muon2` on `task:pretrain-dense-7b`
- Dense math/code RL: `method:cispo` on `task:math-code-rl-dense`
- Distillation: `method:opd` on `task:student-distillation`
- Factory process: `method:poolside-model-factory` on `task:industrial-model-building`
- SAE dictionaries: `method:sasa` / `method:circuitsteer` / `method:fega`

## Evaluation Protocol & Benchmarks
- **Primary Benchmark**: GPT-2 WikiText fine-tune LDS — Spearman (and Pearson) vs leave-k-out retrains, 50 queries, N=400, 95% CI (Bergson Table 1).
- **Filtering-shaped LDS**: sorted-subset / filtering protocol in the MAGIC/Bergson appendix (MAGIC 1.000, EK-FAC 0.865, TrackStar 0.803). Cite this for filtering; do not treat TrackStar random-subset 0.18 as too noisy to filter with.
- **Applied check**: WMDP bio reweight of MAGIC-scored tokens on Deep Ignorance 7B LoRA (Bergson §6.1).
- **Evaluation Pitfalls**: Untuned Hessian damping or low metasmoothness can drive LDS to ~0. Random-subset LDS and sorted-subset LDS answer different questions. Intro-scale "on the order of 405B" is a multi-node design claim, not a completed off-the-shelf run.

## SOTA Recommendation (as of 2026-09-01)
- **Primary Method**: **MAGIC** (`method:magic`, `paper:magic` `arXiv:2504.16430`) for unrolled differentiation when you control the trainer. Implemented in **Bergson** (`method:bergson`, `paper:bergson` `arXiv:2606.11660`).
- **Small-lab filtering default**: **TrackStar** (`method:trackstar`) compressed influence / fact-tracing path.
- **Influence baseline**: **EK-FAC** (`method:ek-fac`). **SOURCE** (`method:source-unrolling`) is a few-checkpoint unroll, status `niche`.
- **Not This Task**: mix search, SAE circuits, train kernels, unlearning trainers, fused MoE expert attribution.
