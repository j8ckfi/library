---
id: task:input-heavy-agentic-moe-serving
type: task
title: "Input-Heavy Agentic MoE Serving"
domain: "systems"
summary: "Serve a large multimodal MoE under long, input-heavy agentic workloads by compressing global KV and activating fewer parameters on prefill than on decode (causal encoder-decoder)."
scope: "KV-footprint / CED serving for input-heavy agentic MoE (encoder memory, decoder global KV from final encoder states, CSA2, SWA bounded replay). First hop is DeepSeek-V4.1-Flash."
out_of_scope:
  - "Frontier MoE pretrain architecture template (DeepSeek-V4 / Kimi-K3)"
  - "SWE issue-to-patch harness (mini-SWE-agent)"
  - "Frontier RL post-train engine (Miles)"
  - "Diffusion-augmented AR serving / lossless multi-token decode (Uno)"
  - "Recurrent all-token CED LM pretrain (RLT; experimental)"
  - "Compute-matched looped MoE pretrain (SMELT)"
redirects:
  - when: "choosing the frontier MoE pretrain architecture template"
    to: "task:pretrain-moe-frontier"
  - when: "GitHub issue to patch / SWE harness rather than serving architecture"
    to: "task:software-engineering-agent-harness"
  - when: "production post-train stack rather than KV-compressed serving"
    to: "task:frontier-rl-posttrain-stack"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    to: "task:diffusion-augmented-ar"
  - when: "recurrent CED-style LM architecture (all-token recurrence), not Flash serving"
    to: "task:recurrent-encoder-decoder-lm"
  - when: "compute-matched looped MoE pretrain"
    to: "task:compute-matched-moe-looped-pretrain"
current_sota:
  - method: method:deepseek-v41-flash
    as_of: "2026-09-10"
    benchmark: "DeepSeek-V4.1-Flash instruct, max reasoning effort; Terminal-Bench 2.1 / DeepSWE v1.1 / global KV bytes"
    metric: "agentic Pass@1 + KV bytes/token"
    value: "TB2.1 90.6; DeepSWE 74.2; global KV 890 B/token (~1/4 of V4-Flash); persistent KV ~1/8 of V4-Flash"
    notes: "DeepSeek-V4.1-Flash CED (HF tech report, 2026-09-10). Vendor-reported. Does not replace DeepSeek-V4 / Kimi-K3 as the MoE pretrain co-default."
methods:
  - method:deepseek-v41-flash
  - method:deepseek-v4
  - method:kimi-k3
  - method:recurrent-looped-transformer
  - method:mhc
  - method:mini-swe-agent
last_reviewed: "2026-09-12"
tags:
  - systems
  - serving
  - kv-cache
  - moe
  - ced
  - deepseek-v41-flash
---

# Input-Heavy Agentic MoE Serving

## Problem Definition
Serve a frontier multimodal MoE when prompts are long and agentic (tools, images, 1M context) and KV cache plus prefill FLOPs dominate cost. Causal encoder-decoder (CED) builds encoder memory once and projects decoder global KV from final encoder states, so prefill activates fewer parameters than decode.

## Evaluation Protocol
- **Primary Benchmarks**: agentic boards (Terminal-Bench, DeepSWE, AutomationBench) plus KV bytes/token and persistent KV vs V4-Flash.
- **Evaluation Pitfalls**: Do not replace DeepSeek-V4 / Kimi-K3 as the *pretrain* architecture default. Do not treat Flash serving numbers as RLT measurements. Do not retarget mini-SWE-agent, Miles, or Uno.

## SOTA Recommendation (as of 2026-09-12)
- **Primary Method (this task only)**: **DeepSeek-V4.1-Flash** (`method:deepseek-v41-flash`, `paper:deepseek-v41-flash`). CED 20+20, CSA2, SWA Bounded Replay, Single-Pass mHC, Engram, DSpark. Weights: `deepseek-ai/DeepSeek-V4.1-Flash`.
- **Not This Task**: `method:deepseek-v4` / `method:kimi-k3` remain MoE pretrain co-defaults; `method:mini-swe-agent` remains the SWE harness; `method:miles` remains the post-train engine; `method:uno` remains diffusion-augmented AR serving; `method:recurrent-looped-transformer` is the experimental all-token-recurrence sibling.
