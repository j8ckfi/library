---
id: paper:draco
type: paper
title: "DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training"
authors:
  - "Shubham Gandhi"
  - "Saurabh Goyal"
  - "Kiran Kate"
  - "Yara Rizk"
year: 2026
month: 9
arxiv_id: "2609.04094"
url: "https://arxiv.org/abs/2609.04094"
methods:
  - method:draco
cites:
  - paper:grpo
  - paper:canopy
  - paper:sao
tags:
  - post-training
  - agentic
  - outcome-blind
  - rubrics
  - draco
---

# DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training

## Abstract Summary
Most long-horizon agent domains have no programmatic checker. DRACO (Distributing Rubric-based Advantage for Credit Optimization) works in that outcome-blind setting: a judge proposes dynamic per-trajectory rubrics, scores them once per completed rollout, and redistributes the trajectory GRPO advantage onto the steps the judge implicated. Redistribution is closed-form (no trained attribution module). On AppWorld, DRACO reports +15.9 TGC over the base and +5.3 over GRPO trained with the sparse ground-truth reward, without using verifiers at train time. Code: `https://github.com/IBM/draco`.

## Key Contributions
1. **Outcome-blind reward** $R_i=(p_i-f_i)/(p_i+f_i)$ from pass/fail/NA rubric verdicts. Discriminative dropout drops criteria no group member failed.
2. **Dynamic rubrics**: propose from the instruction, extend per sampled trajectory, merge/dedup, score once.
3. **Step credit**: quality $Q_j=p_j/(p_j+f_j)$; winner weights $Q_j$, loser weights $1-Q_j$; $a_j=A_i N w_j/(n_j\sum w_k)$ conserves total push and sign.
4. **First AppWorld RL** (authors' claim) that never reads the environment unit tests during training.

## Empirical Highlights
- Qwen3.6-27B AppWorld Test-Normal TGC p^1: DRACO 85.3 vs base 69.4 (+15.9) vs outcome-reward GRPO 80.0 (+5.3). SGC p^1 70.6 vs base 41.1 vs outcome 59.3.
- AppWorld Test-Challenge TGC p^1: 61.5 vs base 49.7 vs outcome 59.9.
- τ-bench Banking SR p^1 (zero-shot transfer): 20.4 vs base 15.8 vs outcome 17.6. Self-judge variant 21.1 on τ-bench, 81.1 on AppWorld TN.
- Qwen2.5-32B-Instruct AppWorld TN TGC p^1: 62.9 vs base 35.7. SALT outcome-aware 66.2 is a different (verifier) setting.
- Ablations: removing dynamic rubrics or step credit each drops TN TGC (82.1 / 81.9 vs 85.3).

## Open Source Repository & Resources
- Code: `https://github.com/IBM/draco`. Paper trains LoRA GRPO on 8x H100, B=16, G=6, GPT-5.4 judge at T=0.1.
