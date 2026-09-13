---
id: paper:recurrent-looped-transformer
type: paper
title: "Recurrent Looped Transformer"
authors:
  - "Yifan Zhang"
year: 2026
month: 9
arxiv_id: ""
url: "https://github.com/yifanzhang-pro/recurrent-looped-tranformer"
methods:
  - method:recurrent-looped-transformer
cites: []
tags:
  - architecture
  - recurrent
  - encoder-decoder
  - rlt
  - tech-report
---

# Recurrent Looped Transformer

## Abstract Summary
Recurrent Looped Transformer (RLT) pairs a causal encoder with a recurrent decoder that carries its final hidden state and layerwise sliding-window attention (SWA) cache across every prompt and response token. The encoder constructs global key–value memory; the decoder extends a continuous latent computation as the sequence grows. Pretraining, SFT, sampling, and current-policy RL replay share one complete-state transition. "Infinite temporal depth" means the path length grows with the sequence (\(t \times L_D\)), not infinite work inside a token. The report develops mechanisms; it does not report measured efficiency, scaling, or RL results.

## Key Contributions
1. **All-token recurrence**: decoder state \(H_t = (s_t, C_t^D)\) does not reset at the prompt–response boundary.
2. **Causal encoder memory**: prefix-restricted global KV available before decoder replay; extended as new tokens arrive.
3. **Shared transition**: the same update for prefill, generation, pretrain, SFT, and exact current-policy RL replay under current weights.
4. **Reference config**: 48 encoder + 48 decoder layers, optional weight sharing across stages.

## Empirical Highlights
- None. The author states realized reasoning gains, hardware efficiency, and RL scaling remain to be established.
- Priors discussed in prose only (YOCO, Feedback Transformer, Recurrent Transformer); those are not library nodes.

## Open Source Repository & Resources
- GitHub (repo name misspells "transformer"): `https://github.com/yifanzhang-pro/recurrent-looped-tranformer`
- Site: `https://yifanzhang-pro.github.io/recurrent-looped-tranformer/`
- English PDF: `https://github.com/yifanzhang-pro/recurrent-looped-tranformer/blob/master/Recurrent_Looped_Transformer.pdf`
- No training code as of 2026-09-12 (`recipe:recurrent-looped-transformer` `code_status: partial`).
