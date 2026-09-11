---
id: paper:nemotron-imo-gold
type: paper
title: "An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics"
authors:
  - "Ivan Moshkov"
  - "Stephen Ge"
  - "George Armstrong"
  - "Wei Du"
  - "Sadegh Mahdavi"
  - "Igor Gitman"
year: 2026
month: 9
arxiv_id: "2609.10712"
url: "https://arxiv.org/abs/2609.10712"
methods:
  - method:nemotron-imo-gold
cites:
  - paper:nemotron-3-ultra
  - paper:minimax-m1
tags:
  - post-training
  - math
  - olympiad
  - nemotron
  - test-time-compute
---

# An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics

## Abstract Summary
Starting from Nemotron 3 Ultra, the authors train two specialist checkpoints (SFT then RL) and pair them with a natural-language generate–verify–refine test-time pipeline. No formal prover, tools, or internet. Three Ultra checkpoints (general-availability plus the two specialists) search, verify, and refine proofs; a separate high-compute stage selects the submission. The system scored 30/42 at IMO 2026 (gold threshold). Released: both specialists, SFT/RL data, training and inference code, submitted solutions, and Nemotron-IMO-Bench (200 novel olympiad problems).

## Key Contributions
1. **Open olympiad recipe**: SFT + RL specialists on Nemotron 3 Ultra plus NL verify/refine TTC.
2. **IMO 2026 gold-threshold score** without a formal prover.
3. **Released artifacts**: checkpoints, data, NeMo-Skills TTC recipe, NeMo-RL training guide, Nemotron-IMO-Bench.

## Empirical Highlights
- IMO 2026: 30/42, gold-medal threshold.
- SFT max sequence length 425,984 tokens from `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`.

## Open Source Repository & Resources
- TTC / proofs: `https://github.com/NVIDIA-NeMo/Skills/tree/main/recipes/nemotron-imo-tts`
- RL guide: `https://github.com/NVIDIA-NeMo/RL/blob/imo-26-ultra-v3/docs/guides/nemotron-3-ultra-imo.md`
- Checkpoints: `nvidia/Nemotron-3-Labs-Ultra-Math-SFT`, `nvidia/Nemotron-3-Labs-Ultra-Math-RL`
- Data: `nvidia/Nemotron-Math-Proofs-v3-SFT`, `nvidia/Nemotron-Math-Proofs-v3-RL`
