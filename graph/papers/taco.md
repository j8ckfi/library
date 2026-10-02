---
id: paper:taco
type: paper
title: "TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning"
authors:
  - "Jichao Jiang"
  - "Cristian McGee"
  - "El Houcine Bergou"
  - "Hanqin Cai"
  - "Aritra Dutta"
year: 2026
month: 10
arxiv_id: "2610.02199"
url: "https://arxiv.org/abs/2610.02199"
methods:
  - method:taco
cites:
  - paper:scale
  - paper:muon2
tags:
  - optimizer
  - efficiency
  - memory-efficient
  - taco
  - fine-tuning
---

# TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning

## Abstract Summary
Full-parameter LLM fine-tuning is bottlenecked by optimizer state. Muon cuts dense state versus AdamW but can mismatch AdamW-pretrained checkpoints. TACO takes Muon's operator-norm steepest-descent view to a dimension-normalized \(1\to 1\) geometry: each column of a 2D weight picks the sign of its largest-magnitude gradient entry, so an \(m\times n\) update has at most \(n\) nonzeros. Practical TACO stores a small FP8 heavy-hitter set per column. University of Central Florida / UM6P. Code: `https://github.com/Jichao2357/TACO_optimizer`.

## Key Contributions
1. **Geometry-induced sparsity**: exact steepest descent under a dimension-normalized \(1\to 1\) operator norm is column-wise Top-1 ternary.
2. **Sparse heavy-hitter state**: history-free vanilla TACO is unstable; practical TACO keeps \(\mathcal{O}(n)\) FP8 state.
3. **FT memory Pareto**: 13B SST-2 on one 80 GB H100; 30–32B full-param FT that AdamW cannot fit.

## Empirical Highlights
- OPT-13B SST-2: 94.22% at 27.5 GB peak / 0.16 GB optimizer state vs AdamW8bit 80.6 GB / 27.7 GB (174× state, 2.9× peak).
- OPT-30B and Qwen3-32B full-param FT on one 80 GB H100; optimizer state 0.267 GB on OPT-30B (<0.5% of peak).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02199`
- Code: `https://github.com/Jichao2357/TACO_optimizer` (`code_status: released`).
