---
id: paper:lesser
type: paper
title: "LESSER: Post-Training Data Selection with Output-Layer Gradients"
authors:
  - "Lyuxin David Zhang"
  - "Eric Wong"
  - "Surbhi Goel"
  - "Anton Xue"
year: 2026
month: 10
arxiv_id: "2610.03702"
url: "https://arxiv.org/abs/2610.03702"
methods:
  - method:lesser
cites:
  - paper:magic
  - paper:circuitlens
tags:
  - post-training
  - data-attribution
  - data-selection
  - lesser
---

# LESSER: Post-Training Data Selection with Output-Layer Gradients

## Abstract Summary
Gradient-based data selection (LESS, GIST, GradAlign, GRACE) scores each candidate with a full-parameter gradient. LESSER keeps only the output-layer (LM-head) gradient as the feature. That is 9.7× cheaper for SFT and 3.0× cheaper for RL feature extraction vs a 4-checkpoint LESS baseline on Llama-2-7B, while tracking full-gradient downstream accuracy (same final RL accuracy as GradAlign in the paper). Active plug-in on `task:training-data-attribution` beside MAGIC. No public code as of 2026-10-05.

## Key Contributions
1. **Output-layer gradient features** instead of full-parameter influence embeddings.
2. **9.7× SFT / 3.0× RL** cheaper features vs 4-checkpoint LESS on Llama-2-7B.
3. **Jaccard 0.53** vs random 0.075 against full-gradient selection.

## Empirical Highlights
- Downstream RL accuracy matches GradAlign in the paper. Do not invent a 1.3-point lift.
- MAGIC remains the LDS first hop when you control the trainer. LESSER is a cheaper feature for selection wrappers.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03702`
- Code: none found as of 2026-10-05 (`code_status: none`).
