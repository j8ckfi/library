---
id: method:self-play-pretraining
type: method
title: "Self-Play Pretraining with Zero Data"
category: "data-curriculum"
status: experimental
sota_for: []
supersedes: []
do_not_use_for:
  - when: "data-free post-train Challenger-Solver-Judge"
    reason: "This paper pretrains from random init with a UTM; J-Zero remains post-train self-evolution"
    use_instead: "method:j-zero"
  - when: "seed-grounded synthetic pretraining from Wikipedia/Wikibooks"
    reason: "SYNTH amplifies encyclopedic seeds; this method uses no natural-language seeds"
    use_instead: "method:synth"
  - when: "choosing the open pretrain mix"
    reason: "Zero natural text by construction; OLMo-3 remains the open mix"
    use_instead: "method:olmo-3"
  - when: "teacher-free on-policy self-adaptation on existing unlabeled prompts"
    reason: "OPSA adapts a pretrained model on a prompt set; this is pretrain-from-scratch"
    use_instead: "method:opsa"
assumptions:
  - "Both generator and learner are randomly initialized transformers. No natural-language corpus. Generator writes Brainfuck-like UTM programs; learner NTP on output bytes. Paper scale <25M, context 4096, max budget 34.36B tokens."
  - "Generator reward is AdamW-preconditioned gradient alignment with the learner's recent parameter movement, plus GRPO-style policy gradient and expert-iteration SFT on high-reward / mutated programs."
  - "Official code nourya-aliz/self_play_pretraining (acowsik/self_play_pretraining redirects there)."
last_reviewed: "2026-10-03"
papers:
  - paper:self-play-pretraining
recipes:
  - recipe:self-play-pretraining
claims:
  - benchmark: "Zero-shot DCLM byte-loss compute-optimal scaling"
    metric: "exponent b"
    value: "0.123"
    baseline: "literature NTP 0.048–0.099 (Henighan et al. 2020; Aghajanyan et al. 2023)"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30063"
    notes: "Clean transfer test: neither model is trained on natural data. Scale <25M."
  - benchmark: "Zero-shot CIFAR-10 image-byte loss scaling"
    metric: "exponent b"
    value: "0.145"
    baseline: "literature 0.065–0.10"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30063"
  - benchmark: "Fibonacci-like sequence discovery vs uniform program sampling"
    metric: "first discovery round"
    value: "round 512 vs E[first]>53,000 under a uniform prior"
    baseline: "1.64e8 uniform samples; no Fibonacci/geometric/quadratic/cubic hits"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30063"
    notes: "Self-play discovery times are upper bounds (programs retained every 256 rounds)."
  - benchmark: "Self-play warm start then natural-data pretrain, 24.4M"
    metric: "tokens to convergence"
    value: "ESC-50 320M vs 496M; CIFAR-10 421M vs 588M"
    baseline: "random-init 24.4M on the same natural corpus"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30063"
    notes: "Self-play compute is not counted in this comparison; it is treated as a one-time amortized pre-pretrain."
tags:
  - pretraining
  - self-play
  - zero-data
  - experimental
  - self-play-pretraining
---

# Self-Play Pretraining with Zero Data

## Method Overview
Start from two randomly initialized transformers and **no natural text**. Each round:

1. Sample programs from the generator over a Brainfuck-like universal Turing machine.
2. Execute each program (plus a random input tape) to a bounded byte string.
3. Train the learner with mean next-token cross-entropy on those bytes.
4. Train the generator with RL. The reward is an AdamW-preconditioned inner product between the learner's gradient on a program's output and the learner's recent parameter movement, so the generator stays on sequences that are learnable but not yet mastered. A GRPO-style policy gradient is combined with expert-iteration SFT on high-reward, mutated, and replayed programs.

This is pretraining, not J-Zero. J-Zero co-evolves Challenger/Solver/Judge from pretrained chat checkpoints.

## When to Use
- You want a tabula-rasa pretrain with an unbounded synthetic search space and will accept a <25M proof of concept.

## When NOT to Use
- Post-train data-free self-evolution → `method:j-zero`. Wikipedia-seeded synthetic pretrain → `method:synth`. Open mix → `method:olmo-3`. Unlabeled-prompt self-adaptation of a pretrained model → `method:opsa`.

## Relation to Existing SOTA
- Experimental first hop on `task:zero-natural-data-self-play-pretrain` only (`sota_for: []`, listed in that task's `current_sota`). Does **not** enter `task:data-free-self-evolution` and does **not** retarget J-Zero.

## Gotchas & Failure Modes
- Paper scale is below 25M parameters at 4K context. Do not treat DCLM exponent 0.123 as a 7B pretrain result.
- Difficulty-only rewards fail: a program can be made arbitrarily hard without useful structure. The gradient-alignment reward is load-bearing.
- Self-play compute is excluded from the 24.4M warm-start token comparison.
