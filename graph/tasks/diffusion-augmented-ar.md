---
id: task:diffusion-augmented-ar
type: task
title: "Diffusion-Augmented Autoregressive LLMs"
domain: "efficiency"
summary: "Keep an AR/NTP model distribution and add lightweight diffusion weights plus a lossless parallel multi-token sampler, without a separate draft model and without switching to a quality-sacrificing d-LLM."
scope: "Train-addon Diffusion Distillation and lossless Ψ-Spec / speculative-style decode for AR LLMs (serving throughput and rollout speedups)."
out_of_scope:
  - "Text-to-image / flow reward alignment (DiffusionOPSD / Self-OPD)"
  - "~7B dense pretrain optimizer (Muon2)"
  - "Pass@1 labeled math/code RLVR algorithm (CISPO)"
  - "Standalone discrete diffusion LMs that replace the AR distribution"
redirects:
  - when: "aligning text-to-image diffusion or flow models with rewards"
    to: "task:posttrain-diffusion"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
current_sota:
  - method: method:uno
    as_of: "2026-09-08"
    benchmark: "8B Uno vs DiffusionGemma-26B-A4B / Mercury 2 / EAGLE-3 / DFlash (1K/8K H200)"
    metric: "quality + system throughput"
    value: "SWE-Verified 68.4 vs DiffusionGemma 18.7; system 5255 tok/s vs 1136 / 1197; Uno Qwen 1.6× vs base AR at max batch"
    notes: "Uno (2609.04010). Does not replace DiffusionOPSD/Self-OPD, Muon2, or CISPO."
methods:
  - method:uno
last_reviewed: "2026-09-08"
tags:
  - efficiency
  - inference
  - diffusion
  - speculative-decoding
  - uno
---

# Diffusion-Augmented Autoregressive LLMs

## Problem Definition
AR next-token prediction is sequential. Speculative decoding needs a separate draft model. Discrete diffusion LMs (d-LLMs) draft in parallel but typically give up AR quality and large-batch throughput. This task is the hybrid: keep the AR distribution, add cheap diffusion weights, verify drafts with the AR pathway so decode is lossless.

## Evaluation Protocol
- **Primary Benchmarks**: 1K-input / 8K-output throughput vs batch (H200), tokens-per-forward, plus agentic/coding/long-context quality (SWE-bench Verified, Terminal-Bench, $\tau$-bench, AA-LCR).
- **Evaluation Pitfalls**: Do not mix batch-1 per-request tok/s with system throughput. Do not treat d-LLM quality as interchangeable with lossless AR. Do not mix this shelf with image-policy post-train.

## SOTA Recommendation (as of 2026-09-08)
- **Primary Method**: **Uno** (`method:uno`, `paper:uno` `arXiv:2609.04010`) Diffusion Distillation + $\Psi$-Spec. Code: ifm-ai/uno.
- **Not This Task**: `method:diffusion-opsd` / `method:self-opd` remain image/flow post-train; `method:muon2` remains the 7B optimizer; `method:cispo` remains Pass@1 RLVR.
