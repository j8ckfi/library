---
id: paper:exppo
type: paper
title: "Exploration-Preserving Policy Optimization"
authors:
  - Hangzhan jin
  - Mohammad Hamdaqa
  - Doina Precup
year: 2026
month: 10
arxiv_id: "2610.04011"
url: "https://arxiv.org/abs/2610.04011"
methods:
  - method:exppo
cites:
  - paper:minimax-m1
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - exppo
---

# Exploration-Preserving Policy Optimization

## Abstract Summary
Group-relative objectives give equal advantages to equally rewarded responses, so credit tracks sampled mode frequency. ExPPO reshapes advantages with prompt-relative length-normalized surprisal and prompt pass rate, bounded so verifier polarity and group absolute-advantage mass stay approximately intact. Improved in-domain and OOD reasoning coverage, higher aggregate accuracy, strong coverage at large sampling budgets, and more diverse verified-correct modes. Code: https://github.com/jinhangzhan/ExPPO. Beside CISPO.

## Key Contributions
1. **Surprisal × pass-rate advantage shaping** on a GRPO-family host.
2. **Bounded / shared-normalized** so verifier polarity and group |A| mass stay intact.
3. **Coverage**: in-domain and OOD, plus diversity among verified-correct responses.

## Empirical Highlights
- Abstract: improved in-domain and OOD coverage, higher aggregate accuracy, strong coverage at large sampling budgets.
- Controlled multi-answer eval: more correct-mode yield and diversity among verified-correct responses.
- No numeric table in the abstract; do not invent one.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04011`
- Code: `https://github.com/jinhangzhan/ExPPO` (`code_status: released`; HTTP 200 as of 2026-10-06).
