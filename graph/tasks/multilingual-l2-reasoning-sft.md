---
id: task:multilingual-l2-reasoning-sft
type: task
title: "Multilingual L2 Reasoning SFT"
domain: "post-training"
summary: "Supervised fine-tuning so a model reasons in the language of the user's prompt (L2 reasoning), not only answers multilingual questions in English CoT."
scope: "Data mixing and scheduling for in-language chain-of-thought SFT, including transfer to languages without reasoning supervision."
out_of_scope:
  - "Open pretrain mix / Dolma-3"
  - "General chat / instruct SFT without an in-language CoT requirement"
  - "Single-turn math/code Pass@1 RLVR"
  - "Olympiad NL proof TTC"
redirects:
  - when: "open pretrain mix / Dolma-3 recipe"
    to: "task:open-data-recipe"
  - when: "general chat / instruct SFT without L2 language fidelity"
    to: "task:instruct-sft-alignment"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "olympiad-style natural-language proofs / IMO TTC"
    to: "task:olympiad-math-posttrain"
current_sota:
  - method: method:tiny-aya-l2-thinker
    as_of: "2026-09-14"
    benchmark: "L2 reasoning rate, 60 languages, 6 benchmarks, 3.35B"
    metric: "in-language reasoning rate"
    value: ">93%"
    notes: "Tiny Aya L2-Thinker / Multilingual Bridges (2609.10445). Mix MR+NR+English reasoning backbone. Not a Pass@1 or Dolci replacement."
methods:
  - method:tiny-aya-l2-thinker
  - method:olmo-3
  - method:cispo
last_reviewed: "2026-09-14"
tags:
  - post-training
  - multilingual
  - sft
  - l2-reasoning
  - aya
---

# Multilingual L2 Reasoning SFT

## Problem Definition
English-centric reasoners translate the problem internally and write English CoT even when the user asked in another language. This task is in-language reasoning fidelity: the trace should match the prompt language, including for languages that never saw reasoning supervision.

## Evaluation Protocol
- **Primary Benchmarks**: L2 reasoning rate plus task accuracy on MGSM/GlobalMGSM, PolyMath, Marco-Bench-MIF, GlobalPIQA, MIST-OEG, cultural suites; seen vs held-out languages.
- **Evaluation Pitfalls**: Do not rank L2 models by English olympiad Pass@1. PolyMath accuracy can trail larger English reasoners even when L2 rate is high.

## SOTA Recommendation (as of 2026-09-14)
- **Primary Method (this task only)**: **Tiny Aya L2-Thinker** (`method:tiny-aya-l2-thinker`, `paper:multilingual-bridges` `arXiv:2609.10445`).
- **Not This Task**: `method:olmo-3` remains open instruct / Dolma-3; `method:cispo` remains Pass@1; `method:nemotron-imo-gold` remains olympiad TTC.
