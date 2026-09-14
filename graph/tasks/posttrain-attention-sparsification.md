---
id: task:posttrain-attention-sparsification
type: task
title: "Post-Training Attention Sparsification"
domain: "efficiency"
summary: "Train a selector so a dense pretrained Transformer spends a fixed per-query attention budget on context units that actually affect the language-modeling loss."
scope: "Post-train (or mid-train) gated / Top-K sparse attention on a frozen or lightly updated dense LM under a fixed attention budget. Context ranking aligned to LM loss."
out_of_scope:
  - "Dumped corpus much larger than the window (RLM prompt offload)"
  - "Linear-time SSM / Mamba architecture from scratch"
  - "Lossless multi-token AR serving with diffusion adapters (Uno)"
  - "SWE issue-to-patch harness"
  - "KV-compressed CED MoE serving (DeepSeek-V4.1-Flash)"
redirects:
  - when: "dumped corpus ≫ window"
    to: "task:long-context-prompt-offload"
  - when: "linear-time architecture from scratch (SSM / Mamba)"
    to: "task:linear-time-sequence-modeling"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    to: "task:diffusion-augmented-ar"
  - when: "GitHub issue to patch / SWE harness"
    to: "task:software-engineering-agent-harness"
  - when: "input-heavy agentic / KV-compressed CED MoE serving"
    to: "task:input-heavy-agentic-moe-serving"
current_sota:
  - method: method:sas
    as_of: "2026-09-14"
    benchmark: "MATH500 / GPQA-Diamond at 1024-token budget, Qwen3-4B/8B/14B"
    metric: "accuracy vs SeerAttention-R"
    value: "+6.0 to +7.7 MATH500; +10.6 to +15.5 GPQA-Diamond"
    notes: "SAS (2609.13141). End-to-end LM-loss gates vs Top-K + dense-attention distillation. Narrow task only."
methods:
  - method:sas
last_reviewed: "2026-09-14"
tags:
  - efficiency
  - sparse-attention
  - post-training
  - sas
  - long-context
---

# Post-Training Attention Sparsification

## Problem Definition
A dense pretrained Transformer must decode under a cap on attended context units per query. Train the selector so the budget is spent on units that change the next-token loss, not on units that merely match the original dense attention.

## Evaluation Protocol
- **Primary Benchmarks**: MATH500, GPQA-Diamond, AIME24/25 at fixed token budgets; LongBench length buckets; BFCL / VitaBench for agentic transfer.
- **Evaluation Pitfalls**: Do not mix this with RLM dumped-prompt offload or with Mamba-style pretrain architecture.

## SOTA Recommendation (as of 2026-09-14)
- **Primary Method (this task only)**: **SAS** (`method:sas`, `paper:sas` `arXiv:2609.13141`).
- **Not This Task**: `method:rlm` remains dumped-prompt offload; `method:mamba-2` remains linear-time pretrain; `method:uno` remains diffusion-augmented AR serving; `method:mini-swe-agent` remains the SWE harness; `method:deepseek-v41-flash` remains CED serving.
