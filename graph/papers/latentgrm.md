---
id: paper:latentgrm
type: paper
title: 'Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving
  Compression'
authors:
- Mingqing Yuan
- Xiaobo Liang
- Junwei Yang
- Ziwei Chen
- Zeren Zhang
- Hejin Wang
- Yubin Wang
- Juntao Li
year: 2026
month: 10
arxiv_id: '2610.09788'
url: https://arxiv.org/abs/2610.09788
methods:
- method:latentgrm
cites:
- paper:minimax-m1
tags:
- post-training
- reward-model
- latentgrm
---

# Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression

## Abstract Summary
LatentGRM is a generative reward model that judges in latent space via rubric-guided semantic chunking and compression. Competitive preference accuracy vs matched explicit Rubric-RM at 4B/8B. ~8.9–9.2× shorter eval trajectories and 6.1–7.0× faster at vote@5. Plug-in on `task:reasoning-rl-alignment`.

## Key Contributions
1. Rubric-guided semantic chunking into a compact latent judge trajectory.
2. Autonomous pairwise preference without generating textual assessments online.
3. Offline Latent Trace Interpreter for reconstruction.

## Empirical Highlights
- LatentGRM-4B/8B vote@5 Avg-8 67.8 / 69.0 vs Rubric-RM 67.0 / 68.1.
- LatentGRM-8B vote@5: 8.87–9.23× shorter generated steps; 6.11–6.95× vLLM speedup.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.09788`
- Code: `https://github.com/EADMO/LatentGRM` (`code_status: released`; HTTP 200 as of 2026-10-13).
