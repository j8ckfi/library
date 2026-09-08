---
id: paper:uno
type: paper
title: "Unlocking Lossless Speedups in LLMs via Discrete Diffusion"
authors:
  - "Subham Sekhar Sahoo"
  - "Lingjie Chen"
  - "Khiem Pham"
  - "Jonathan Geuter"
  - "Chaitanya Dwivedi"
  - "Varad Pimpalkhute"
  - "Yash Akhauri"
  - "Alexander Moreno"
  - "Mikhail Yurochkin"
  - "Zhenting Wang"
  - "Mostafa Elhoushi"
  - "Nolan Dey"
  - "Shane Bergsma"
  - "Joel Hestness"
  - "John Thickstun"
  - "Eric Xing"
  - "Zhengzhong Liu"
year: 2026
month: 9
arxiv_id: "2609.04010"
url: "https://arxiv.org/abs/2609.04010"
methods:
  - method:uno
cites: []
tags:
  - inference
  - diffusion
  - speculative-decoding
  - uno
---

# Unlocking Lossless Speedups in LLMs via Discrete Diffusion

## Abstract Summary
Autoregressive NTP is sequential. Uno is a diffusion-augmented AR LLM: AR weights trained with standard NTP keep the AR distribution; lightweight diffusion weights are trained with a Diffusion Distillation phase (small overhead) to draft multiple tokens in parallel from that same distribution. $\Psi$-Spec samplers (linear for system throughput, tree for per-request) verify drafts with the AR pathway so generation is lossless relative to the AR model, without a separate draft model. Unlike d-LLMs, quality of the AR backbone is not sacrificed for parallel decode. Models can be trained from scratch or by attaching diffusion adapters to an open-weight AR LLM. 8B Uno beats 26B-A4B DiffusionGemma and proprietary Mercury 2 on agentic tool use, coding, and long-context reasoning, and reports higher system throughput than EAGLE-3 / DFlash at every evaluated batch size. Code: `https://github.com/ifm-ai/uno`. Project: `https://s-sahoo.com/uno/`.

## Key Contributions
1. **Decoupled weights**: AR/NTP for quality; lightweight diffusion adapters for parallel draft. Diffusion Distillation is a drop-in phase on an existing LLM pipeline.
2. **$\Psi$-Spec**: lossless multi-token decode via AR verification (linear $B=4$ for system throughput; tree $(B,K,V)=(16,32,32)$ for batch-1).
3. **No separate draft model**, unlike EAGLE-3 (0.40B AR drafter) or DFlash (1.05B diffusion drafter; train context $B\cdot L$ vs Uno's $2\cdot L$).
4. **Train from scratch or augment** open-weight AR (Qwen3-8B adapters on OpenThoughts). Frozen diffusion adapters can speed RL rollouts (~40% e2e on math/code experts; TPF −6% after RL).

## Empirical Highlights
- Table 1 (8B Uno vs DiffusionGemma 26B-A4B vs Mercury 2): SWE-bench Verified 68.4 vs 18.7; $\tau$2 Telecom 90.1 vs 68.1 vs 71; Terminal-Bench v2.1 39.6 vs 14.7 vs 27; AA-LCR 68.0 vs 19.7 vs 36; system throughput 5255 vs 1136 vs 1197 tok/s; per-request 405 vs 836 vs 769 tok/s (H200, 1K/8K test).
- Uno Qwen vs base AR: up to $2.5\times$ in Figure 2; $1.6\times$ and $>5700$ tok/s at the largest batch (Linear $B=4$). Abstract: up to $3\times$ including at max device batch.
- Avg TPF 1.9 / 2.7 (system / per-request sampler). DFlash thinking-off drops accuracy 76.36% → 55.40% — Uno keeps AR quality.

## Open Source Repository & Resources
- Code: `https://github.com/ifm-ai/uno` (Nano-vLLM inference, conditional-LoRA training).
- Project: `https://s-sahoo.com/uno/`.
- Checkpoints: `IFM/K2-Horizon-7B-Uno`, `IFM/K2-Horizon-0.9B-Uno`, `s-sahoo/uno-qwen3-8B`.
