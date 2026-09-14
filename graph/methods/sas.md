---
id: method:sas
type: method
title: "SAS (Simple Attention Sparsification)"
category: "architecture"
status: sota
sota_for:
  - task:posttrain-attention-sparsification
supersedes: []
do_not_use_for:
  - when: "dumped corpus much larger than the window"
    reason: "SAS sparsifies attention inside the transformer; RLM offloads the prompt"
    use_instead: "method:rlm"
  - when: "linear-time architecture from scratch (SSM / Mamba)"
    reason: "SAS is a post-train gated sparse attention on a dense pretrained Transformer"
    use_instead: "method:mamba-2"
  - when: "lossless multi-token AR serving / diffusion-augmented decode"
    reason: "Uno keeps dense AR attention and adds diffusion adapters"
    use_instead: "method:uno"
  - when: "GitHub issue to patch / SWE harness"
    reason: "Sparse attention is not a harness"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Dense pretrained Transformer. Train only AttnGates; freeze the backbone. Paper: Qwen3-4B/8B/14B, OpenR1-Math-220k, block size 64, 8x H20."
  - "Host selector is the SeerAttention-R AttnGate; SAS changes the training signal from dense-attention distillation to LM-loss gates."
last_reviewed: "2026-09-14"
papers:
  - paper:sas
recipes:
  - recipe:sas
claims:
  - benchmark: "MATH500 / GPQA-Diamond at 1024-token attention budget, Qwen3-4B/8B/14B"
    metric: "accuracy lift vs SeerAttention-R"
    value: "+6.0 to +7.7 MATH500; +10.6 to +15.5 GPQA-Diamond"
    baseline: "SeerAttention-R (dense-attention distillation + Top-K)"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13141"
    notes: "Largest gains at tight budgets. Backbone frozen. Not a pretrain-architecture SOTA."
  - benchmark: "LongBench 8K+ bucket, Qwen3-4B, budget 2048"
    metric: "LongBench score"
    value: "+3.2 vs SeerAttention-R"
    baseline: "SeerAttention-R"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13141"
    notes: "SAS leads SeerAttention-R at every reported LongBench budget."
tags:
  - efficiency
  - sparse-attention
  - post-training
  - sas
  - sota
---

# SAS (Simple Attention Sparsification)

## Method Overview
Hard Top-K blocks LM-loss gradients into the selector, so prior trainable sparse attention distills dense attention. SAS keeps Top-K for compute but multiplies selected blocks by continuous log-space gates added to attention logits. The language-modeling loss then ranks context under the actual budget. Current block is always retained; historical blocks get a normalized softmax gate.

## When to Use
- Post-train a dense LLM to spend a fixed attention budget on the blocks that actually move the next-token loss.
- Tight decode budgets where SeerAttention-R / Top-K distillation wastes the budget.

## When NOT to Use
- 10M-token dumped prompt → `method:rlm`. SSM from scratch → `method:mamba-2`. AR multi-token serving → `method:uno`. SWE loop → `method:mini-swe-agent`.

## Relation to Existing SOTA
- First hop for `task:posttrain-attention-sparsification` only. Does **not** replace RLM, Mamba-2, Uno, or mini-SWE-agent.

## Gotchas & Failure Modes
- Train gates only; do not unfreeze the backbone in the paper recipe.
- Eval uses a SGLang block-sparse fork (`rayleizhu/sglang`), not stock SGLang.
- Full attention remains the quality ceiling; SAS is budgeted recovery.
