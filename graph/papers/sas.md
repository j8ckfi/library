---
id: paper:sas
type: paper
title: "SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking"
authors:
  - "Zhiwei Li"
  - "Lei Zhu"
  - "Hao Gu"
  - "Xiang Hu"
  - "Yan Wang"
  - "Haitao Mi"
  - "Sirui Han"
  - "Leo Liang"
  - "Zhijiang Guo"
year: 2026
month: 9
arxiv_id: "2609.13141"
url: "https://arxiv.org/abs/2609.13141"
methods:
  - method:sas
cites: []
tags:
  - efficiency
  - sparse-attention
  - post-training
  - sas
  - long-context
---

# SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking

## Abstract Summary
Post-training attention sparsification selects a small set of context units (tokens or blocks) per query under a fixed attention budget. Trainable selectors usually score units then apply hard Top-K, which blocks gradients from the language-modeling loss, so prior work distills dense attention. That ranking is not aligned with prediction impact under the budget. SAS injects the selector's continuous scores into attention logits as log-space softmax gates so LM loss updates the selector by standard backprop. Practical details: gate inside softmax in log form, normalized softmax gates that calibrate historical context against the always-retained current block, and continuous scores rather than only hard selections. A Triton kernel folds SAS into FlashAttention-style compute.

## Key Contributions
1. **End-to-end context ranking** under a frozen backbone: train only AttnGates.
2. **Log-space gates inside softmax** instead of dense-attention distillation (vs SeerAttention-R).
3. **Public training and SGLang eval**: Qwen3-4B/8B/14B recipes; Hugging Face gates.

## Empirical Highlights
- At 1024-token budget, SAS beats SeerAttention-R by 6.0-7.7 MATH500 and 10.6-15.5 GPQA-Diamond on Qwen3-4B/8B/14B.
- LongBench: leads SeerAttention-R at every budget; +3.2 on the 8K+ bucket of Qwen3-4B at budget 2048.
- Agentic: BFCL up to +3.5; VitaBench nearly recovers full attention at budget 4096.
- Train: 8x H20, OpenR1-Math-220k, block size 64, backbone frozen, AdamW 1e-3.

## Open Source Repository & Resources
- Code: `https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification` (default branch `release`).
- Weights: `https://huggingface.co/tencent/Simple-Attention-Sparsification`.
- Eval backend: `rayleizhu/sglang` (sglang-blocksparse submodule).
