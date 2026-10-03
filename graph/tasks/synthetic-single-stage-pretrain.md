---
id: task:synthetic-single-stage-pretrain
type: task
title: "Fully Synthetic Single-Stage LLM Pretraining"
domain: "pretraining"
summary: "Pretrain a generalist LM on a fully synthetic corpus amplified from curated encyclopedic seeds, with reasoning traces in the mix and no separate SFT/RL stage."
scope: "Seed-grounded synthetic pretraining that collapses pre-/mid-/post-training into one NTP stage (Wikipedia/Wikibooks seeds amplified by auxiliary models). First hop is SYNTH as trained into Baguettotron-600M. Not the open web mix and not zero-natural-data self-play."
out_of_scope:
  - "Open multi-trillion-token web/Dolma mix (OLMo-3 / Dolma-3)"
  - "~7B dense NTP optimizer choice (Muon2)"
  - "Consumer-GPU ~1.5-2B open-mix pretrain (Puro-2B)"
  - "Zero-natural-data self-play pretraining (programs on a UTM, no Wikipedia seeds)"
  - "Data-free post-train Challenger-Solver-Judge (J-Zero)"
redirects:
  - when: "open pretrain mix / Dolma-3 recipe rather than seed-grounded synthetic pretrain"
    to: "task:open-data-recipe"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "standard dense ~7B NTP from scratch on web/open data"
    to: "task:pretrain-dense-7b"
  - when: "zero-natural-data self-play pretraining (generator proposes programs, no Wikipedia seeds)"
    to: "task:zero-natural-data-self-play-pretrain"
  - when: "data-free post-train self-evolution (Challenger-Solver-Judge)"
    to: "task:data-free-self-evolution"
current_sota:
  - method: method:synth
    as_of: "2026-10-03"
    benchmark: "FActScore-style Wikipedia seed entities n=500, Baguettotron-600M chat 158B"
    metric: "S/(S+C) precision and macro S/(S+C+I)"
    value: "79.3%±2.1 precision / 41.7%±2.2 macro vs Qwen3-0.6B 65.7%/31.6% (~36T) and Phi-4-mini 77.4%/29.5% (~5T)"
    notes: "SYNTH (2609.37891). 594M params, 48 layers, d=1024, ~158B tokens. No separate SFT/RL. Knowledge is capped by ~58k Wikipedia seeds."
methods:
  - method:synth
  - method:olmo-3
  - method:muon2
  - method:puro-2b
  - method:self-play-pretraining
  - method:j-zero
last_reviewed: "2026-10-03"
tags:
  - pretraining
  - synthetic-data
  - data-curriculum
  - single-stage
  - synth
  - baguettotron
---

# Fully Synthetic Single-Stage LLM Pretraining

## Problem Definition
Train a generalist language model from scratch on a **fully synthetic** corpus that is amplified from a fixed set of curated encyclopedic seeds (Wikipedia / Wikibooks), with instruction and reasoning traces already in the pretrain mix. The point of this task is a **single NTP stage** — no separate SFT or RL. This is seed-grounded synthetic pretraining, not web-crawl mixing and not self-play over a universal Turing machine.

## Evaluation Protocol
- **Primary Benchmarks**: FActScore-style atomic-fact precision on in-seed Wikipedia entities (paper Table 1); iso-compute downstream vs FineWiki / FinePDFs-Edu at matched 600M; optional domain-adaptation (TeleQnA / 3GPP).
- **Evaluation Pitfalls**: Do not treat Baguettotron as a Dolma-3 or Muon2 replacement. Held-out entities outside the ~58k seeds are a coverage ceiling, not an optimizer bake-off. Hugging Face `PleIAs/Baguettotron` is the 321M / ~200B card, not the 594M FActScore run.

## SOTA Recommendation (as of 2026-10-03)
- **Primary Method (this task only)**: **SYNTH / Baguettotron** (`method:synth`, `paper:synth` `arXiv:2609.37891`). First hop is the SYNTH recipe as trained into Baguettotron-600M (594M, ~158B tokens in Table 1).
- **Not This Task**: `method:olmo-3` remains the open mix; `method:muon2` remains the ~7B optimizer; `method:puro-2b` remains consumer-GPU open-mix ~2B; `method:self-play-pretraining` remains zero-natural-data UTM self-play; `method:j-zero` remains post-train Challenger–Solver–Judge.
