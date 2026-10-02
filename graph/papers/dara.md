---
id: paper:dara
type: paper
title: "Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL"
authors:
  - "Tong Zheng"
  - "Skylar Zhai"
  - "Zhan Cheng"
  - "TianMing Sha"
  - "Youling Huang"
  - "Shuo Zhou"
  - "Shaotong Qi"
  - "Jingcheng Liang"
  - "Xuwei Ding"
  - "Pengcheng Xu"
year: 2026
month: 10
arxiv_id: "2610.00574"
url: "https://arxiv.org/abs/2610.00574"
methods:
  - method:dara
cites:
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - multi-reward
  - dara
  - density
---

# Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL

## Abstract Summary
Reward-wise GDPO normalization equalizes each active group, but batch advantage energy \(E_k=\sum_{i,j}(A_k^{(i,j)})^2\) still scales with active-group density \(\pi_k\). Sparse or saturating rewards (format, length) starve. DARA applies an inverse-sqrt density weight so low-density rewards match the densest reward's energy. Default DARA-Asym amplifies only positive advantages. GDPO is prior art in the paper, not a library method. Code: `https://github.com/zhaihaotian/DARA`.

## Key Contributions
1. **Advantage energy**: under idealized GDPO, batch energy is proportional to active-group density.
2. **Inverse-sqrt calibration**: \(w_k=\min(w_{\max},\sqrt{\pi_{\mathrm{ref}}/\pi_k})\) computed per rollout batch.
3. **Asym vs Sym**: Asym (default) does not amplify conflicting negatives.

## Empirical Highlights
- Tool calling (ToolRL, Qwen2.5-1.5B/3B): up to 26% fewer steps to high format compliance vs GDPO; competitive final BFCL-v4 score.
- Math length+correctness: up to 65% fewer steps to near-saturated length compliance vs GDPO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.00574`
- Code: `https://github.com/zhaihaotian/DARA` (`code_status: released`).
