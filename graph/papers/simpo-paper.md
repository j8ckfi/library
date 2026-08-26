---
id: paper:simpo-paper
type: paper
title: "SimPO: Simple Preference Optimization with a Reference-Free Objective"
authors:
  - "Yu Meng"
  - "Mengzhou Xia"
  - "Danqi Chen"
year: 2024
month: 5
arxiv_id: "2405.14734"
url: "https://arxiv.org/abs/2405.14734"
methods:
  - method:simpo
cites:
  - paper:dpo-paper
tags:
  - post-training
  - preference-alignment
---

# SimPO: Simple Preference Optimization with a Reference-Free Objective

## Abstract Summary
SimPO proposes an offline preference optimization algorithm that eliminates the reference model entirely and incorporates a sequence-length-normalized margin into the objective. Across AlpacaEval 2 and Arena-Hard benchmarks, SimPO consistently outperforms DPO, KTO, and existing reference-based algorithms while saving substantial GPU memory.

## Key Contributions
1. **Reference-Free Formulation**: Replaced implicit log-ratio reward with length-normalized sequence log-likelihood.
2. **Explicit Target Margin (\(\gamma\))**: Added target margin separation between chosen and rejected generations.
3. **Empirical Superiority**: Demonstrated state-of-the-art win rates without suffering from verbosity bias.
