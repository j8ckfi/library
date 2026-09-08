---
id: method:uno
type: method
title: "Uno (Diffusion-Augmented AR LLM)"
category: "architecture"
status: sota
sota_for:
  - task:diffusion-augmented-ar
supersedes: []
do_not_use_for:
  - when: "aligning text-to-image diffusion / flow models with rewards"
    reason: "Uno is AR+diffusion serving/train, not image-policy post-train"
    use_instead: "method:diffusion-opsd"
  - when: "teacher-free flow-matching visual alignment"
    reason: "Self-OPD is the flow post-train default"
    use_instead: "method:self-opd"
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Diffusion Distillation is an add-on phase; Muon2 remains the 7B optimizer"
    use_instead: "method:muon2"
  - when: "Pass@1 labeled math/code RLVR"
    reason: "CISPO remains the dense RLVR default; frozen Uno adapters can speed rollouts but do not change the algorithm"
    use_instead: "method:cispo"
assumptions:
  - "AR backbone exists (train from scratch or attach LoRA diffusion weights to an open-weight AR LLM). Paper 8B from-scratch + Qwen3-8B adapters."
  - "Lossless decode needs AR verification of diffusion drafts (Ψ-Spec). Linear B=4 for system throughput; tree (B,K,V)=(16,32,32) for batch-1. Tree verification wants FlashAttention-3."
  - "Diffusion Distillation on Qwen3-8B: OpenThoughts3-1.2M, LoRA rank 128 / α 2048, global batch 128, LR 1e-5, tv-gamma 1."
last_reviewed: "2026-09-08"
papers:
  - paper:uno
recipes:
  - recipe:uno
claims:
  - benchmark: "8B Uno SWE-bench Verified / Terminal-Bench v2.1 / AA-LCR"
    metric: "accuracy"
    value: "68.4 / 39.6 / 68.0"
    baseline: "DiffusionGemma-26B-A4B 18.7 / 14.7 / 19.7; Mercury 2 — / 27 / 36"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04010"
    notes: "Table 1. τ2 Telecom 90.1 vs Mercury 71 vs DiffusionGemma 68.1. GPQA-Diamond 77.1 vs Mercury 77 vs DiffusionGemma 70.7. Mercury 2 from Artificial Analysis 2026-08-30."
  - benchmark: "8B Uno 1K/8K H200 system / per-request throughput"
    metric: "tokens/s"
    value: "5255 / 405"
    baseline: "DiffusionGemma 1136 / 836; Mercury 2 1197 / 769; Nemotron-Labs-Diffusion 2794 / 290"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04010"
    notes: "Table 1. Linear B=4 for system TPF 1.9; tree (16,32,32) for per-request TPF 2.7. Mercury system throughput is AA's 1K-in batch-10 on faster Blackwell; Uno is still ~4.6× higher on H200."
  - benchmark: "Uno Qwen3-8B vs base AR at max H200 batch (1K/8K)"
    metric: "system throughput speedup"
    value: "1.6× over base AR, >5700 tok/s (Linear B=4)"
    baseline: "Qwen3-8B AR; EAGLE-3 and DFlash at their best system-throughput configs"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04010"
    notes: "§5.2 / Figure 2. Pareto-dominates speculative decoding at every batch; figure caption up to 2.5× over base AR. Abstract: up to 3× including at largest device batch. DFlash thinking-off accuracy 76.36→55.40."
tags:
  - inference
  - diffusion
  - speculative-decoding
  - architecture
  - uno
  - sota
---

# Uno (Diffusion-Augmented AR LLM)

## Method Overview
Uno keeps an AR/NTP distribution and adds lightweight diffusion weights that draft a block of tokens in parallel from that distribution. AR weights are trained (or frozen from an open checkpoint) with next-token prediction. Diffusion weights are trained in a **Diffusion Distillation** phase: conditional LoRA on the AR backbone, TV objective (`tv-gamma=1` in the public Qwen recipe), small extra compute. At decode, $\Psi$-Spec proposes a block and the AR pathway verifies prefixes (rejection sampling), so the output law matches the AR model. Linear sampler ($B=4$) maximizes system throughput; tree sampler $(B,K,V)=(16,32,32)$ maximizes batch-1. No separate draft model.

This is a serving + train-addon shelf. It does not replace CISPO, Muon2, DiffusionOPSD, or Self-OPD.

## When to Use
- Need lossless multi-token decode on an AR LLM without training a draft model, including at large serving batch.
- Adding a Diffusion Distillation phase so RL/SFT rollouts can use frozen diffusion adapters (paper: up to ~40% e2e on math/code experts).

## When NOT to Use
- Image/flow reward alignment → `method:diffusion-opsd` / `method:self-opd`.
- 7B pretrain optimizer → `method:muon2`. Labeled Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- `status: sota` only for `task:diffusion-augmented-ar`. Does **not** supersede `method:diffusion-opsd`, `method:self-opd`, `method:muon2`, or `method:cispo`.
- Distinct from d-LLMs (they change the model distribution and typically lose AR quality / large-batch throughput) and from EAGLE-3 / DFlash (separate drafters).

## Gotchas & Failure Modes
- Per-request tok/s can lose to DiffusionGemma at batch 1 (405 vs 836) while system throughput and quality go the other way. Pick the metric that matches serving.
- Tree sampler wants FlashAttention-3; linear decode is FA2.
- Qwen3-8B trained on OpenThoughts for adapters can degrade AR quality (paper Table 9); the adapters still give lossless speedups on that checkpoint.
- Concurrent Orthrus (2605.12825) is a related frozen-backbone + diffusion pathway; Uno's claim is unchanged architecture + causal diffusion path + public 8B bake-off. Not a library supersession either way.
- RL speedup numbers are promised "in the next revision"; treat 40% as the paper's qualitative claim, not a table.
