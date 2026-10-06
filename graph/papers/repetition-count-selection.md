---
id: paper:repetition-count-selection
type: paper
title: "Selecting Repetition Counts Across Model Scales in Data-Constrained Pretraining"
authors:
  - Ziyue WANG
  - T. Kanamori
year: 2026
month: 10
arxiv_id: "2610.05126"
url: "https://arxiv.org/abs/2610.05126"
methods:
  - method:repetition-count-selection
cites:
  - paper:olmo-3
tags:
  - pretraining
  - data-curriculum
  - data-repetition
  - repetition-count-selection
---

# Selecting Repetition Counts Across Model Scales in Data-Constrained Pretraining

## Abstract Summary
The best repetition count at a small scale may not stay best at a larger scale. Finite target corpus mixed with generic data at a fixed target fraction: Wikipedia-derived and Proof-Pile-2 rankings reverse with model size. A 520M Proof-Pile-2 run: r=8 beats r=16 with fewer tokens. Loss curves from smaller models retain a shortlist of promising r for the larger scale; on PubMed and Caselaw that shortlist keeps the lowest-loss measured count at 200M and 520M. Dual-active first hop on task:data-constrained-pretrain. No public code as of 2026-10-06.

## Key Contributions
1. **Ranking reversal with scale** on Wikipedia-derived data and Proof-Pile-2.
2. **520M Proof-Pile-2**: r=8 beats r=16 with fewer training tokens.
3. **Candidate retention**: small-model loss curves keep a shortlist that still contains the larger-scale winner on PubMed / Caselaw at 200M and 520M.

## Empirical Highlights
- 520M Proof-Pile-2: reducing repetition from 16 to 8 improves loss while using fewer tokens.
- PubMed / Caselaw: candidate sets fixed before target-model training retain the lowest-loss measured count at 200M and 520M.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05126`
- Code: none found as of 2026-10-06 (`code_status: none`).
