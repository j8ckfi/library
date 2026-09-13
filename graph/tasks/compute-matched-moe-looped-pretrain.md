---
id: task:compute-matched-moe-looped-pretrain
type: task
title: "Compute-Matched MoE Looped Pretraining"
domain: "pretraining"
summary: "Loop a contiguous span of MoE Transformer layers while matching an unlooped baseline on per-token FLOPs, non-embedding parameters, and KV cache, then measure scaling-law compute savings."
scope: "Compute-matched looped MoE pretrain recipes (which layers to loop, how many visits, width/expert/KV matching). First hop is SMELT. Does not choose the frontier MoE architecture template."
out_of_scope:
  - "Frontier MoE architecture template (DeepSeek-V4 / Kimi-K3)"
  - "Communication-efficient expert-layer layout (CE-MoE)"
  - "NVL72 fused dispatch megakernel (Mixture-of-Kittens)"
  - "Recurrent CED all-token recurrence (RLT)"
  - "Input-heavy agentic CED serving (DeepSeek-V4.1-Flash)"
  - "~7B dense NTP optimizer (Muon2)"
redirects:
  - when: "choosing the frontier MoE architecture template"
    to: "task:pretrain-moe-frontier"
  - when: "expert-parallel all-to-all layout rather than looping"
    to: "task:pretrain-moe-frontier"
  - when: "NVL72 fused dispatch+SwiGLU+combine megakernel"
    to: "task:train-moe-nvl72"
  - when: "recurrent CED-style architecture / all-token recurrence"
    to: "task:recurrent-encoder-decoder-lm"
  - when: "input-heavy agentic / KV-compressed CED serving"
    to: "task:input-heavy-agentic-moe-serving"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
current_sota:
  - method: method:smelt
    as_of: "2026-09-01"
    benchmark: "Chinchilla-style MoE scaling ladder, compute-optimal CE Gain vs unlooped Baseline"
    metric: "training FLOPs saved at matched loss"
    value: "6.8–18.0% on the fitted sparse-grid frontier (10^20–10^21 FLOPs)"
    notes: "SMELT (2609.01343). Active looped-MoE recipe. Does not replace DeepSeek-V4 / Kimi-K3 / CE-MoE."
methods:
  - method:smelt
  - method:ce-moe
  - method:deepseek-v4
  - method:kimi-k3
last_reviewed: "2026-09-12"
tags:
  - pretraining
  - moe
  - looped-transformer
  - smelt
  - scaling-laws
---

# Compute-Matched MoE Looped Pretraining

## Problem Definition
Decide whether looping MoE layers helps when you cannot spend extra FLOPs, extra stored parameters, or extra KV. Match all three budgets against an unlooped MoE baseline, then compare loss and downstream. This is not the V4 / K3 architecture default and not CE-MoE's communication layout.

## Evaluation Protocol
- **Primary Benchmarks**: compute-optimal validation-loss frontier (CE Gain); DCLM Core / Completion; MMLU; domain splits (Code largest in SMELT).
- **Evaluation Pitfalls**: Iso-parameter looping that grows FLOPs and KV is a different comparison. Do not treat SMELT as a replacement of DeepSeek-V4 / Kimi-K3.

## SOTA Recommendation (as of 2026-09-12)
- **Primary Method (this task only)**: **SMELT** (`method:smelt`, `paper:smelt` `arXiv:2609.01343`). Status `active`. Loop the middle 50% of MoE layers twice; narrow width; raise experts; scale looped residuals by \(1/2\); match FLOPs / non-embedding params / KV.
- **Not This Task**: `method:deepseek-v4` / `method:kimi-k3` remain frontier MoE co-defaults; `method:ce-moe` remains the communication-layout niche.
