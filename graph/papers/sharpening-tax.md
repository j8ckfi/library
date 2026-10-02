---
id: paper:sharpening-tax
type: paper
title: "Sharpening Tax in Post-Training"
authors:
  - "Changdae Oh"
  - "Qi Zeng"
  - "Qi Qi"
  - "Andrey Zhmoginov"
  - "Deren Lei"
  - "Yun He"
  - "Hoang Phan"
  - "Hangoo Kang"
  - "Azalia Mirhoseini"
  - "Sharon Li"
year: 2026
month: 10
arxiv_id: "2610.01509"
url: "https://arxiv.org/abs/2610.01509"
methods:
  - method:es-reasoning
  - method:cispo
cites:
  - paper:es-reasoning
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - passk
  - sharpening
  - gotcha
---

# Sharpening Tax in Post-Training

## Abstract Summary
RL post-training often raises Pass@1 by sharpening existing behaviors and collapsing Pass@K coverage. The paper shows the same trade-off on agentic tasks: harness-equipped base models can beat their post-trained counterparts at large \(K\). Sharpening Tax is a diagnostic of lost test-time scalability. Posterior-tempered group sampling (PTGS) is documented in the paper as a sampler plug-in; it is **not** ingested as a library method. Claim note on `task:passk-reasoning-coverage` / `method:es-reasoning`. Does not retarget CISPO or ES-reasoning.

## Key Contributions
1. **Agentic sharpening**: 14 base/post-trained pairs × three agentic benches (42 cases); tax is prevalent.
2. **Bimodal success**: post-training pushes tasks toward always-solved or never-solved.
3. **PTGS** (documented, not a graph method): per-prompt temperature from estimated difficulty. Do not promote it over ES-reasoning or CISPO.

## Empirical Highlights
- Pre-trained LLMs with a light harness often trail Pass@1 but lead Pass@K given enough samples.
- Tax can be estimated from a few rollouts and correlates with other coverage metrics. Code exists (`changdaeoh/sharpening-tax`) but this is a finding, not a trainer.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.01509`
- Project: `https://changdaeoh.github.io/sharpening-tax/`
- Code: `https://github.com/changdaeoh/sharpening-tax` (diagnostic / PTGS sampler; no new library method).
