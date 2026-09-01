---
id: paper:ek-fac
type: paper
title: "Studying Large Language Model Generalization with Influence Functions"
authors:
  - "Roger Grosse"
  - "Juhan Bae"
  - "Cem Anil"
  - "Nelson Elhage"
  - "Alex Tamkin"
  - "Amirhossein Tajdini"
  - "Benoit Steiner"
  - "Dustin Li"
  - "Esin Durmus"
  - "Ethan Perez"
  - "Evan Hubinger"
  - "Kamilė Lukošiūtė"
  - "Karina Nguyen"
  - "Nicholas Joseph"
  - "Sam McCandlish"
  - "Jared Kaplan"
  - "Samuel R. Bowman"
year: 2023
month: 8
arxiv_id: "2308.03296"
url: "https://arxiv.org/abs/2308.03296"
methods:
  - method:ek-fac
cites: []
tags:
  - interpretability
  - data-attribution
  - ek-fac
  - influence
---

# Studying Large Language Model Generalization with Influence Functions

## Abstract Summary
EK-FAC (Eigenvalue-corrected Kronecker-Factored Approximate Curvature) approximates the Hessian so influence functions can run on LLMs. The paper studies generalization with influences up to 52B parameters: sparsity, abstraction with scale, math and programming, cross-lingual transfer, and role-play. Bergson reimplements EK-FAC as an influence baseline; Kronfluence remains the larger verified EK-FAC-model library on the Bergson Appendix C protocol (14B vs Bergson 7B on one 8×A100 node).

## Key Contributions
1. **EK-FAC IHVP**: Kronecker-factored curvature with eigenvalue correction, orders of magnitude faster than iterative IHVP solvers.
2. **Query batching and TF-IDF filtering** to share training-gradient cost across influence queries.
3. **Generalization case studies** at LLM scale, including influence decay when key-phrase order is flipped.

## Empirical Highlights
- Bergson GPT-2 WikiText FT LDS (Table 1, Adam): Spearman 0.257 ± 0.015 / Pearson 0.295 ± 0.016.
- README Muon-trained: EK-FAC 0.474 ± 0.036 (Shampoo 0.522 ± 0.037).
- Sorted-subset / filtering-shaped LDS (appendix): EK-FAC 0.865.
- Verified Bergson single-node EK-FAC: 7B on 8×A100. Kronfluence EK-FAC: 14B on the same protocol.
