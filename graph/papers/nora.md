---
id: paper:nora
type: paper
title: "Normalized Low-Rank Adaptation"
authors:
  - "Jiale Kang"
  - "Ziyin Yue"
  - "Zheng Zhan"
  - "Yangyi Huang"
  - "Weiyang Liu"
year: 2026
month: 8
arxiv_id: "2608.31036"
url: "https://arxiv.org/abs/2608.31036"
methods:
  - method:nora
cites:
  - paper:lora-paper
  - paper:lr-matters-lora
tags:
  - peft
  - lora
  - nora
  - rlvr
---

# Normalized Low-Rank Adaptation

## Abstract Summary
LoRA initializes the up-projection $B$ to zero, so early optimization is governed by the down-projection $A$. NoRA normalizes each column of $A$ along the rank dimension, yielding $\Delta y=\alpha B\,\mathrm{Norm}(A)x$. The update stays linear in $x$ and mergeable. NoRA-init applies the same normalization once at initialization. Across pretraining, SFT, and RLVR, both variants accelerate convergence, improve stability, and reduce forgetting, with no extra parameters or inference cost. Spectral inits (PiSSA, MiLoRA) are fragile under RLVR; NoRA stays stable.

## Key Contributions
1. **Rank-dimension column normalization** of LoRA $A$, transferring MLA-style latent scale control without breaking mergeability.
2. **NoRA-init and BIMI**: initialization-only normalization, plus block-identity matrix initialization whose columns are already unit-norm.
3. **Cross-regime evidence**: SFT average 43.37 vs LoRA 37.93 vs RSLoRA 41.28 on Llama-3.2-3B; RLVR average 44.4 vs LoRA 42.8 vs base 41.0, while PiSSA/MiLoRA collapse.

## Empirical Highlights
- Llama-3.2-3B SFT (GSM8K / Math / HumanEval / MBPP avg): NoRA 43.37, NoRA-init 42.38, LoRA 37.93, DoRA 38.30, RSLoRA 41.28. Forgetting Avg $\Delta$: NoRA +0.02 vs LoRA $-0.56$.
- DeepSeek-R1-Distill-Qwen-1.5B RLVR overall avg: NoRA 44.4 vs LoRA 42.8 vs PiSSA 0.2 vs MiLoRA 18.0.
- Recommend $\alpha=r$ (unit scaling) because column norms are 1.

## Open Source Repository & Resources
- Code: `https://github.com/Joluck/NoRA` (PEFT fork with `use_nora`)
