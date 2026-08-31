---
id: paper:j-zero
type: paper
title: "J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data"
authors:
  - "Gyouk Chu"
  - "Myeongho Jeon"
  - "Eunho Yang"
year: 2026
month: 8
arxiv_id: "2608.26582"
url: "https://arxiv.org/abs/2608.26582"
methods:
  - method:j-zero
cites:
  - paper:grpo
tags:
  - post-training
  - self-evolution
  - data-free
  - self-play
  - unverifiable
  - j-zero
---

# J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data

## Abstract Summary
Self-evolving language models can drop human-curated tasks, but unverifiable domains stall when a frozen Judge can no longer separate good answers from bad. J-Zero co-evolves a Challenger, a Solver, and a Judge from zero external training data. Challenger and Solver play an adversarial GRPO game: the Challenger is rewarded for tasks the Solver scores poorly on (with repetition and format penalties); the Solver is rewarded to maximize Judge score on high-dispersion frontier tasks. The Judge is updated with Bradley–Terry loss on preference pairs whose order is known from loop structure — Solver answer $\succ$ Challenger answer, and divide-and-conquer composed answer $\succ$ Solver one-shot — rather than from the Judge's own scores. J-Zero outperforms R-Zero and G-Zero by an average of 4.2 points on verifiable and 8.0 points on unverifiable domains, and keeps improving through at least ten iterations, whereas those baselines degrade after two.

## Key Contributions
1. **Unified zero-data loop for both domains**: One Challenger–Solver–Judge co-evolution covers verifiable and unverifiable/open-ended tasks without an external corpus.
2. **Structural preference pairs for Judge co-adaptation**: Role-asymmetry and subtask-amplification labels are induced by how responses are produced, so the Judge can rise with the policies instead of saturating at its initialization.
3. **Sustained iteration**: Frozen-Judge and prior zero-data baselines plateau after ~2 iterations; J-Zero improves through 10 on both domain groups.

## Empirical Highlights
- Verifiable overall avg, Qwen3-4B-Base: J-Zero 54.38 vs R-Zero 49.64 vs G-Zero 47.41 vs base 44.91.
- Verifiable overall avg, Qwen3-8B-Base: 58.55 vs 54.99 vs 53.07 vs 50.67.
- Unverifiable overall avg, Qwen3-4B-Base: 20.81 vs 12.66 vs 10.89 vs 9.58.
- Unverifiable overall avg, Qwen3-8B-Base: 23.41 vs 15.54 vs 15.31 vs 13.23.
- Judge init: Skywork-Reward-V2-Llama-3.1-8B. Inner loop: GRPO on verl. Hardware: 4x B200 + 4x H200.

## Open Source Repository & Resources
- Project Page: `https://gyoukchu.github.io/projects/j_zero/`
- Code Repository: `https://github.com/GyoukChu/J-Zero`
