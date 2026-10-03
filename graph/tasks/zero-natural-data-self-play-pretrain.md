---
id: task:zero-natural-data-self-play-pretrain
type: task
title: "Zero-Natural-Data Self-Play Pretraining"
domain: "pretraining"
summary: "Pretrain from random initialization with zero natural text: a generator proposes programs for a universal Turing machine and a learner predicts the output bytes under an RL curriculum."
scope: "Tabula-rasa pretraining with no natural-language corpus. Generator proposes Brainfuck-like UTM programs; learner NTP on output bytes; generator RL on a learning-progress reward. First hop is Self-Play Pretraining with Zero Data. Not J-Zero post-train and not SYNTH Wikipedia amplification."
out_of_scope:
  - "Data-free post-train Challenger-Solver-Judge (J-Zero)"
  - "Seed-grounded synthetic pretraining from Wikipedia/Wikibooks (SYNTH)"
  - "Open web/Dolma mix (OLMo-3)"
  - "~7B dense NTP optimizer (Muon2)"
  - "Teacher-free on-policy self-adaptation on existing unlabeled prompts (OPSA)"
redirects:
  - when: "data-free post-train self-evolution (Challenger-Solver-Judge, not pretrain-from-scratch)"
    to: "task:data-free-self-evolution"
  - when: "seed-grounded synthetic pretraining from Wikipedia/Wikibooks seeds"
    to: "task:synthetic-single-stage-pretrain"
  - when: "open pretrain mix / Dolma-3 recipe"
    to: "task:open-data-recipe"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "teacher-free on-policy self-adaptation on an existing unlabeled prompt set"
    to: "task:teacher-free-on-policy-self-adaptation"
current_sota:
  - method: method:self-play-pretraining
    as_of: "2026-10-03"
    benchmark: "Zero-shot DCLM byte-loss scaling exponent vs literature NTP"
    metric: "compute-optimal scaling exponent b"
    value: "0.123 vs literature 0.048–0.099"
    notes: "Self-Play Pretraining with Zero Data (2609.30063). Experimental first hop: models <25M, context 4096, max budget 34.36B tokens. Not J-Zero. Method status experimental."
methods:
  - method:self-play-pretraining
  - method:j-zero
  - method:synth
  - method:olmo-3
  - method:opsa
last_reviewed: "2026-10-03"
tags:
  - pretraining
  - self-play
  - zero-data
  - synthetic-data
  - self-play-pretraining
---

# Zero-Natural-Data Self-Play Pretraining

## Problem Definition
Pretrain from **random initialization with zero natural text**. A generator proposes programs for a minimal universal Turing machine; execution yields byte sequences; a learner is trained by next-token prediction on those bytes. The generator is reinforced to stay at the learner's capability frontier. This is a pretraining algorithm, not post-train self-evolution.

## Evaluation Protocol
- **Primary Benchmarks**: zero-shot loss scaling on held-out natural byte streams (DCLM, CIFAR-10 image bytes, ESC-50, and the paper's other modalities); in-context learning on held-out tasks; discovery of recognizable mathematical sequences vs a uniform-program baseline.
- **Evaluation Pitfalls**: Do not file this under J-Zero (`task:data-free-self-evolution`). J-Zero starts from pretrained 4B/8B chat policies. Do not file it under SYNTH: SYNTH starts from Wikipedia seeds. Scale in the paper is below 25M parameters.

## SOTA Recommendation (as of 2026-10-03)
- **Experimental first hop (this task only)**: **Self-Play Pretraining with Zero Data** (`method:self-play-pretraining`, `paper:self-play-pretraining` `arXiv:2609.30063`).
- **Not This Task**: `method:j-zero` remains post-train Challenger–Solver–Judge; `method:synth` remains seed-grounded synthetic pretrain; `method:olmo-3` remains the open mix; `method:opsa` remains teacher-free adaptation on existing unlabeled prompts.
