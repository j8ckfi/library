---
id: paper:self-play-pretraining
type: paper
title: "Self-Play Pretraining with Zero Data"
authors:
  - "Aditya Cowsik"
  - "Kfir Dolev"
  - "Michael Y. Li"
  - "G. Bruno De Luca"
  - "Nourya Cohen"
  - "Noah D. Goodman"
  - "Yoav Levine"
year: 2026
month: 9
arxiv_id: "2609.30063"
url: "https://arxiv.org/abs/2609.30063"
methods:
  - method:self-play-pretraining
cites:
  - paper:j-zero
tags:
  - pretraining
  - self-play
  - zero-data
  - self-play-pretraining
---

# Self-Play Pretraining with Zero Data

## Abstract Summary
Internet pretraining still has the data mix curated on the model's behalf. This paper pretrains from random initialization with **zero natural text**. A generator proposes programs for a minimal universal Turing machine; execution produces byte sequences; a learner is trained by next-token prediction. The generator is trained with RL so that proposed programs sit at the frontier of the learner's capabilities. Zero-shot loss on held-out natural datasets (language, images, speech, DNA, math sequences) follows a compute-optimal power law. The learner also shows in-context learning, and the generator discovers recognizable mathematical sequences. Distinct from SYNTH (Wikipedia-seeded synthetic pretrain) and from J-Zero (post-train Challenger–Solver–Judge). Cowsik, Dolev, and Li are equal contribution.

## Key Contributions
1. **UTM self-play pretrain**: Brainfuck-like programs → byte tapes → learner NTP, with no natural-language corpus.
2. **Learning-progress generator reward**: AdamW-preconditioned gradient alignment with the learner's recent parameter movement, plus GRPO-style PG and expert-iteration SFT.
3. **Transfer scaling**: zero-shot natural-data loss scales with self-play compute at exponents comparable to literature NTP, at model scale <25M.

## Empirical Highlights
- DCLM exponent b=0.123 vs literature 0.048–0.099. CIFAR-10 image bytes b=0.145 vs 0.065–0.10.
- Fibonacci-like (and quadratic/cubic/geometric) programs appear by round 512 vs E[first]>53,000 under uniform sampling.
- 24.4M warm start then natural-data pretrain: ESC-50 320M vs 496M tokens; CIFAR-10 421M vs 588M. Self-play compute is not counted in that comparison.
- Context 4096; max budget 34.36B tokens.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.30063`
- Code: `https://github.com/nourya-aliz/self_play_pretraining` (`https://github.com/acowsik/self_play_pretraining` redirects there; `code_status: released`).
