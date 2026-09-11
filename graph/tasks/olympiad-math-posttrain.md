---
id: task:olympiad-math-posttrain
type: task
title: "Olympiad Proof Post-Training and Test-Time Compute"
domain: "post-training"
summary: "Post-train specialist checkpoints and a natural-language generate–verify–refine loop for olympiad-style proofs, not single-turn Pass@1 RLVR."
scope: "Hard olympiad / IMO-style natural-language proof post-train plus TTC (SFT+RL specialists, NL verify/refine, no formal prover required)."
out_of_scope:
  - "Single-turn dense math/code Pass@1 RLVR (CISPO)"
  - "General chat / instruct SFT (OLMo-3 / Nemotron-Cascade 2)"
  - "Nemotron 3 Ultra pretrain architecture choice"
  - "Formal Lean / prover-in-the-loop systems"
redirects:
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "general chat / instruct SFT"
    to: "task:instruct-sft-alignment"
  - when: "choosing the Nemotron 3 Ultra / frontier MoE architecture"
    to: "task:pretrain-moe-frontier"
current_sota:
  - method: method:nemotron-imo-gold
    as_of: "2026-09-11"
    benchmark: "IMO 2026 official contest"
    metric: "points / 42"
    value: "30 (gold threshold)"
    notes: "Nemotron IMO Gold (2609.10712). NL TTC, no prover. Does not replace CISPO as Pass@1."
methods:
  - method:nemotron-imo-gold
  - method:nemotron-3-ultra
  - method:cispo
  - method:olmo-3
last_reviewed: "2026-09-11"
tags:
  - post-training
  - math
  - olympiad
  - nemotron
  - test-time-compute
---

# Olympiad Proof Post-Training and Test-Time Compute

## Problem Definition
Train and serve natural-language olympiad proofs: specialist SFT/RL checkpoints plus a generate–verify–refine test-time loop. Pass@1 AIME/MATH RLVR is a different task (`task:math-code-rl-dense` / CISPO).

## Evaluation Protocol
- **Primary Benchmarks**: IMO contest scores; Nemotron-IMO-Bench (200 novel items).
- **Evaluation Pitfalls**: Do not mix 30/42 TTC with CISPO Pass@1. Do not treat Ultra architecture papers as this recipe.

## SOTA Recommendation (as of 2026-09-11)
- **Primary Method (this task only)**: **Nemotron IMO Gold** (`method:nemotron-imo-gold`, `paper:nemotron-imo-gold` `arXiv:2609.10712`). Status on the method node is `active` (recipe/specialist, not a Pass@1 kernel).
- **Not This Task**: `method:cispo` remains Pass@1; `method:olmo-3` remains instruct SFT; `method:nemotron-3-ultra` remains the base architecture.
