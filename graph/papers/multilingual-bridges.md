---
id: paper:multilingual-bridges
type: paper
title: "Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning"
authors:
  - "Mehrnaz Mofakhami"
  - "Ananya Sahu"
  - "Alejandro R. Salamanca"
  - "Daniel D'souza"
  - "Alexandre Berard"
  - "Thomas Euyang"
  - "Marzieh Fadaee"
  - "Julia Kreutzer"
year: 2026
month: 9
arxiv_id: "2609.10445"
url: "https://arxiv.org/abs/2609.10445"
methods:
  - method:tiny-aya-l2-thinker
cites: []
tags:
  - post-training
  - multilingual
  - sft
  - l2-reasoning
  - aya
---

# Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning

## Abstract Summary
Reasoning LMs remain English-centric: they reason in English even when prompted in another language. L2 reasoning is the ability to reason in the language of the user's prompt. The paper treats this as a data-composition and scheduling problem for reasoning SFT. Tiny Aya L2-Thinker (3.35B) reaches an L2 reasoning rate above 93% across 60 languages on six benchmarks (math, commonsense, instruction following, open-ended generation, cultural reasoning) while keeping task performance strong. Generalizing to held-out languages needs broader language coverage, multilingual non-reasoning data, and a sufficient English reasoning backbone. Reasoning supervision is not required in every target language.

## Key Contributions
1. **L2 reasoning as the metric**: in-language CoT, not just multilingual answers.
2. **Mix and schedule**: multilingual reasoning (MR) + multilingual non-reasoning (NR) + English reasoning backbone.
3. **Released 3.35B dual-mode model** and multilingual reasoning data.

## Empirical Highlights
- L2 rate >93% on every reported benchmark across seen and unseen languages; exceeds M-Thinker-7B (87.7-96.5%) on five of six tasks at half the size.
- PolyMath accuracy is not the win: Qwen3.5-4B 40.3 vs Tiny Aya L2-Thinker 11.1; most of that gap is English-reasoning strength, not L2 transfer (English-reasoning Tiny Aya 18.6).
- Dual-mode: English thinker and L2 thinker siblings released.

## Open Source Repository & Resources
- Project: `https://cohere.com/research/papers/building-multilingual-bridges-2026-09-10`
- Weights: `https://huggingface.co/CohereLabs/tiny-aya-l2-thinker` (also `tiny-aya-en-thinker`, `tiny-aya-base-32K`)
- Data: `https://huggingface.co/datasets/CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning`
- No official train GitHub as of 2026-09-14.
