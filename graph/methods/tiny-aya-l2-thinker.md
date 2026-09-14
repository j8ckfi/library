---
id: method:tiny-aya-l2-thinker
type: method
title: "Tiny Aya L2-Thinker (Multilingual Bridges)"
category: "data-curriculum"
status: sota
sota_for:
  - task:multilingual-l2-reasoning-sft
supersedes: []
do_not_use_for:
  - when: "open pretrain mix / Dolma-3 recipe"
    reason: "This is L2 reasoning SFT mixing, not a 7B pretrain corpus"
    use_instead: "method:olmo-3"
  - when: "general chat / instruct SFT without an in-language CoT requirement"
    reason: "OLMo-3 Dolci / Nemotron-Cascade 2 remain instruct defaults"
    use_instead: "method:olmo-3"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "L2 rate is not Pass@1; CISPO remains Pass@1. PolyMath accuracy here trails Qwen3.5-4B"
    use_instead: "method:cispo"
assumptions:
  - "Start from a massively multilingual base (paper: Tiny Aya 3.35B). Mix multilingual reasoning, multilingual non-reasoning, and an English reasoning backbone. Dual-mode: English thinker vs L2 thinker."
  - "Weights and data on Hugging Face (CohereLabs). No official train GitHub as of 2026-09-14."
last_reviewed: "2026-09-14"
papers:
  - paper:multilingual-bridges
recipes:
  - recipe:tiny-aya-l2-thinker
claims:
  - benchmark: "L2 reasoning rate across 60 languages on 6 benchmarks (math, commonsense, IF, open-ended, cultural)"
    metric: "in-language reasoning rate"
    value: ">93%"
    baseline: "English-centric reasoners near 0% L2; M-Thinker-7B 87.7-96.5% on the same L2 metric"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10445"
    notes: "3.35B Tiny Aya L2-Thinker. Exceeds M-Thinker-7B on five of six L2-rate tasks at half the size. Held-out languages need NR coverage plus an English reasoning backbone."
  - benchmark: "PolyMath accuracy vs Qwen3.5-4B (user-prefix language forcing)"
    metric: "accuracy"
    value: 11.1
    baseline: "Qwen3.5-4B 40.3; Tiny Aya English-thinker 18.6"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10445"
    notes: "Gotcha: L2 fidelity is the task, not olympiad Pass@1. Most of the PolyMath gap is English-reasoning strength."
tags:
  - post-training
  - multilingual
  - sft
  - l2-reasoning
  - aya
  - sota
---

# Tiny Aya L2-Thinker (Multilingual Bridges)

## Method Overview
L2 reasoning means the chain of thought matches the prompt language. The recipe is data mixing and scheduling, not a new optimizer: (1) a strong English reasoning backbone, (2) multilingual reasoning traces in a subset of languages, (3) readily available multilingual non-reasoning data so held-out languages still follow instructions in-language. Tiny Aya L2-Thinker is the 3.35B artifact; an English-thinker sibling isolates the L2 objective.

## When to Use
- You need in-language CoT across many languages, including languages without reasoning traces.
- Small multilingual bases where language-forcing a larger English reasoner is unacceptable.

## When NOT to Use
- Pretrain mix → `method:olmo-3`. General instruct → `method:olmo-3` / `method:nemotron-cascade-2`. Pass@1 math → `method:cispo`.

## Relation to Existing SOTA
- First hop for `task:multilingual-l2-reasoning-sft` only. Does **not** replace OLMo-3, Nemotron-Cascade 2, or CISPO.

## Gotchas & Failure Modes
- Do not rank this model by PolyMath / AIME against Qwen reasoners. The paper's own decomposition shows most of that gap is English-reasoning, not L2 mixing.
- Dual-mode: pick L2-Thinker for in-language traces, EN-Thinker when English CoT is acceptable.
- No public train scripts as of 2026-09-14; reproduce from the paper's mix, not from a GitHub trainer.
