---
id: paper:diem
type: paper
title: "Dynamic Important Example Mining for Reinforcement Finetuning"
authors:
  - "Haoru Tan"
  - "Sitong Wu"
  - "Yanfeng Chen"
  - "Shizhen Zhao"
  - "Yang-Tian Sun"
  - "Tianjia Liu"
  - "Chirui Chang"
  - "Shaofeng Zhang"
  - "Samm Sun"
  - "Xiuzhe Wu"
  - "Ruobing Xie"
  - "Xiaojuan Qi"
year: 2026
month: 8
arxiv_id: "2608.29252"
url: "https://arxiv.org/abs/2608.29252"
methods:
  - method:diem
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - data-selection
  - diem
---

# Dynamic Important Example Mining for Reinforcement Finetuning

## Abstract Summary
Most data-centric RFT methods treat a sample's value as fixed. DIEM reweights each minibatch inside the RL step: a gradient-alignment score approximates the sample's marginal contribution to the batch update, then a constrained reweighting maximizes aggregate utility while preserving the unweighted gradient's L2 magnitude. Compatible with GRPO/PPO-family trainers. Reported +1 to +6 points over static/dynamic selection baselines at about 1.2% extra training time. Code: `https://github.com/hrtan/DIEM`.

## Key Contributions
1. **Gradient-alignment importance** $\hat{\mathcal{I}}_t(z)=\eta_t\langle\mathcal{G}_z^{(t)},\mathcal{G}_{\mathcal{B}_t}^{(t)}\rangle$ as a first-order proxy for leave-one-out batch-reward change.
2. **Constrained reweight** $\max_W I^\top W$ s.t. $\|W^\top G\|^2=\|\mathbf{1}^\top G\|^2$, closed form $W^*=P^{-1}I\sqrt{I^\top P^{-1}I}/\sqrt{C}$ with $P=GG^\top$, then clip negative weights to 0.
3. **Self-organizing curriculum** from the reweight, without an external difficulty model.

## Empirical Highlights
- Qwen3-1.7B five-bench math avg: DIEM 33.10 vs GRPO 31.36 vs LIMR 32.20 vs HVS 31.72.
- Qwen3-4B avg: DIEM 40.66 vs GRPO 37.30 vs LIMR 39.42 (AIME24 16.2 vs 13.8).
- Qwen2.5-7B avg: DIEM 35.68 vs GRPO 34.00; AIME25 10.8 vs 5.5.
- Qwen2.5-VL-7B six-bench avg: DIEM 61.8 vs vanilla RFT 59.1 vs SPEED-RL 60.0.
- Qwen2.5-VL-32B avg: DIEM 67.3 vs vanilla RFT 64.9 vs SPEED-RL 65.6.
- Overhead stated as 1.2% extra training time (Gram invert is N×N on the minibatch).

## Open Source Repository & Resources
- Code: `https://github.com/hrtan/DIEM` (veRL / Qwen; CVPR-2026 banner on the repo).
