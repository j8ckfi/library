---
id: task:recurrent-encoder-decoder-lm
type: task
title: "Recurrent Encoder-Decoder Language Models"
domain: "pretraining"
summary: "Causal-encoder plus recurrent-decoder LMs with unbounded temporal depth, all-token recurrence across the prompt–response boundary, and exact current-policy RL replay under one state transition."
scope: "Recurrent CED-style LM architecture: causal encoder KV memory plus a recurrent decoder that carries hidden state and layerwise SWA cache across every prompt and response token. Experimental first hop is Recurrent Looped Transformer."
out_of_scope:
  - "Standard dense ~7B NTP from scratch (Muon2 / OLMo-3)"
  - "Frontier MoE pretrain template (DeepSeek-V4 / Kimi-K3)"
  - "Latent-space / next-concept LM (NCP-ArchPreview)"
  - "Input-heavy agentic MoE serving / KV-compressed CED (DeepSeek-V4.1-Flash)"
  - "SWE issue-to-patch harness (mini-SWE-agent)"
  - "Production harness kernel (omp2)"
  - "Compute-matched MoE looping of middle layers (SMELT)"
redirects:
  - when: "standard dense ~7B NTP from scratch"
    to: "task:pretrain-dense-7b"
  - when: "frontier MoE architecture / DeepSeek-V4 template"
    to: "task:pretrain-moe-frontier"
  - when: "latent-space / next-concept LM architecture"
    to: "task:latent-space-lm-pretrain"
  - when: "input-heavy agentic / KV-compressed CED serving rather than recurrent LM pretrain"
    to: "task:input-heavy-agentic-moe-serving"
  - when: "GitHub issue to patch / SWE harness"
    to: "task:software-engineering-agent-harness"
  - when: "building a production engine (rewind, sandbox, remote, TUI)"
    to: "task:agent-harness-runtime"
  - when: "compute-matched looped MoE pretrain (middle layers twice)"
    to: "task:compute-matched-moe-looped-pretrain"
current_sota:
  - method: method:recurrent-looped-transformer
    as_of: "2026-09-12"
    benchmark: "Technical report (mechanisms only)"
    metric: "measured efficiency or scaling"
    value: "none reported"
    notes: "RLT (2026-09-12). Experimental. Report develops encoder memory + all-token recurrence; does not report measured results. Conceptual sibling of DeepSeek-V4.1-Flash CED, not a replacement."
methods:
  - method:recurrent-looped-transformer
  - method:deepseek-v41-flash
  - method:ncp-archpreview
  - method:deepseek-v4
last_reviewed: "2026-09-12"
tags:
  - pretraining
  - architecture
  - recurrent
  - encoder-decoder
  - rlt
---

# Recurrent Encoder-Decoder Language Models

## Problem Definition
Train or specify a language model whose decoder carries complete state across every token, including the prompt–response boundary. The encoder builds prefix-restricted global KV; the decoder is recurrent (final hidden state plus layerwise sliding-window cache). This is not dense NTP 7B, not the V4 MoE pretrain template, and not a SWE harness.

## Evaluation Protocol
- **Primary Benchmarks**: none in the RLT report. Future work would need efficiency, scaling, and RL replay measurements.
- **Evaluation Pitfalls**: Do not treat "infinite temporal depth" as infinite work per token. Do not cite V4.1-Flash serving numbers as RLT results. Do not retarget Muon2, DeepSeek-V4 / Kimi-K3, NCP, mini-SWE-agent, or V4.1-Flash serving SOTA.

## SOTA Recommendation (as of 2026-09-12)
- **Experimental first hop (this task only)**: **Recurrent Looped Transformer** (`method:recurrent-looped-transformer`, `paper:recurrent-looped-transformer`). Status `experimental`. No measured efficiency or scaling.
- **Production CED serving (different task)**: `method:deepseek-v41-flash` on `task:input-heavy-agentic-moe-serving`.
- **Not This Task**: `method:muon2` remains the ~7B optimizer; `method:deepseek-v4` / `method:kimi-k3` remain frontier MoE pretrain; `method:ncp-archpreview` remains latent-space LM; `method:mini-swe-agent` remains the SWE harness.
