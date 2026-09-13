---
id: task:pretrain-moe-frontier
type: task
title: "Pretrain Mixture-of-Experts (MoE) Architecture at Scale"
domain: "pretraining"
summary: "Frontier pretraining of sparse Mixture-of-Experts (MoE) architectures with multi-head latent attention and multi-token prediction."
scope: "Frontier MoE pretrain architecture template. Co-default is DeepSeek-V4 + Kimi-K3."
out_of_scope:
  - "Input-heavy agentic / KV-compressed CED serving (DeepSeek-V4.1-Flash)"
  - "Compute-matched looped MoE (SMELT)"
  - "Recurrent CED all-token recurrence (RLT)"
  - "Communication-efficient expert layout as the architecture default (CE-MoE stays niche)"
  - "NVL72 fused dispatch megakernel (Mixture-of-Kittens)"
  - "Olympiad specialist post-train (Nemotron IMO Gold)"
redirects:
  - when: "input-heavy agentic / KV-footprint / CED serving, not general MoE pretrain template"
    to: "task:input-heavy-agentic-moe-serving"
  - when: "compute-matched looped MoE (middle layers twice), not V4/K3 architecture"
    to: "task:compute-matched-moe-looped-pretrain"
  - when: "recurrent CED-style architecture (all-token recurrence / encoder memory / SWA decoder), not NTP MoE V4"
    to: "task:recurrent-encoder-decoder-lm"
  - when: "NVL72 fused dispatch+SwiGLU+combine megakernel"
    to: "task:train-moe-nvl72"
  - when: "olympiad-style natural-language proofs / IMO TTC rather than architecture"
    to: "task:olympiad-math-posttrain"
current_sota:
  - method: method:deepseek-v4
    as_of: "2026-08-26"
    benchmark: "Frontier MoE Benchmarks & Throughput"
    metric: "compute-optimal loss"
    value: "Frontier Pareto SOTA"
    notes: "DeepSeek-V4 (2606.19348) + Kimi-K3 (2607.24653)."
  - method: method:kimi-k3
    as_of: "2026-08-26"
    benchmark: "Frontier MoE Benchmarks & Long-Context Throughput"
    metric: "Pareto FLOP-to-accuracy efficiency"
    value: "Frontier Co-Default SOTA"
    notes: "Kimi-K3 (2607.24653) architecture co-default with DeepSeek-V4."
methods:
  - method:deepseek-v4
  - method:kimi-k3
  - method:deepseek-v3
  - method:nemotron-3-ultra
  - method:nemotron-3-super-latentmoe
  - method:mixture-of-kittens
  - method:apertus
  - method:glm-5
  - method:muonclip-kimi-k2
  - method:qwen38-next
  - method:ce-moe
  - method:moe-sparsity-hp-scaling
  - method:moe-data-repetition
  - method:nemotron-imo-gold
  - method:smelt
  - method:deepseek-v41-flash
  - method:recurrent-looped-transformer
last_reviewed: "2026-09-12"
tags:
  - pretraining
  - moe
  - frontier
---

# Pretrain Mixture-of-Experts (MoE) Architecture at Scale

## Problem Definition
Training sparse Mixture-of-Experts models enables scaling parameter capacity into hundreds of billions of parameters while keeping active FLOPs per token bounded.

## SOTA Recommendation (as of 2026-09-01)
- **Architecture**: **DeepSeek-V4** (`method:deepseek-v4`, 2606.19348) + **Kimi-K3** (`method:kimi-k3`, 2607.24653). Unchanged.
- **Optimizer**: **MuonClip** (`paper:muonclip-kimi-k2`) / **Muon2** (`method:muon2`).
- **NVL72 Systems Megakernel**: **Mixture-of-Kittens** (`method:mixture-of-kittens`, `task:train-moe-nvl72`).
- **Adjacent Qwen-style hybrid residual recipe**: `method:qwen38-next` (`arXiv:2608.30320`). Does not replace DeepSeek-V4 / Kimi-K3 or Muon2.
- **Optional communication-efficient layout**: `method:ce-moe` (`arXiv:2608.28511`) when expert-parallel all-to-all dominates. Layout niche only.
- **Optional compute-matched looped MoE**: `method:smelt` (`arXiv:2609.01343`) on `task:compute-matched-moe-looped-pretrain`. Sibling of CE-MoE. Does not replace DeepSeek-V4 / Kimi-K3 / CE-MoE.
- **Input-heavy agentic / KV-compressed CED serving (not this template)**: `method:deepseek-v41-flash` on `task:input-heavy-agentic-moe-serving`. Different family from the V4 MoE pretrain template.
- **Experimental recurrent CED LM (not this template)**: `method:recurrent-looped-transformer` on `task:recurrent-encoder-decoder-lm`.
- **Optional LR/batch vs activation-ratio transfer**: `method:moe-sparsity-hp-scaling` (`arXiv:2609.08690`). Pretrain HP guidance. Does not replace DeepSeek-V4 / Kimi-K3.
- **Gotcha (repetition × sparsity)**: `method:moe-data-repetition` (`arXiv:2609.11917`). MoEs degrade from ~4× repeats; dense 80M tolerated 8×. Does not replace DeepSeek-V4 / Kimi-K3.
- **Olympiad specialist post-train on Ultra (not this architecture task)**: `method:nemotron-imo-gold` on `task:olympiad-math-posttrain`.
