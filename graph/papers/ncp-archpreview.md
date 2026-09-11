---
id: paper:ncp-archpreview
type: paper
title: "NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction"
authors:
  - "The Intern-NCP Team"
year: 2026
month: 9
arxiv_id: "2609.10715"
url: "https://arxiv.org/abs/2609.10715"
methods:
  - method:ncp-archpreview
cites:
  - paper:olmo-3
tags:
  - pretraining
  - architecture
  - latent-lm
  - ncp
  - dolma-3
---

# NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction

## Abstract Summary
NCP-ArchPreview jointly trains next-token prediction and Next Concept Prediction. A product-quantized concept vocabulary is built from hidden states; a Concept Module predicts future multi-token concepts and feeds them back into token generation. The architecture is scaled to 8.9B parameters on 5.73T Dolma-3 tokens — claimed as the largest latent-space LM demonstration. At 51.3% of the token budget it matches OLMo-3-7B's final pretraining loss; after full pretrain it is +2.45 macro and +5.99 GSM8K vs OLMo-3-7B. At 85% compute it approaches a parameter-matched 8.9B NTP baseline. Post-pretrain, a 17M VQ module is a lightweight domain-adaptation interface; injecting concepts into a DFlash2 drafter raises mean accepted length by 4.17%.

## Key Contributions
1. **Joint NTP + NCP** over a product-quantized concept vocab from hidden states.
2. **Scale**: 8.9B / 5.73T Dolma-3.
3. **Post-pretrain uses**: 17M VQ domain adaptation; DFlash2 concept injection.

## Empirical Highlights
- 51.3% of tokens to match OLMo-3-7B Stage-1 final loss; +2.45 downstream macro; +5.99 GSM8K.
- 85% compute vs a strictly parameter-aligned 8.9B NTP baseline.
- DFlash2 mean accepted length +4.17%.

## Open Source Repository & Resources
- Weights: `https://huggingface.co/collections/ArchSpace-Collection/ncp-archpreview` (`ArchSpace-Collection/NCP_ArchPreview_*`)
- Eval: `https://github.com/LUMIA-Group/ncp_olmo_eval`
- Serving: `https://github.com/LuckySJTU/vllm_ncp_archpreview` (obsolete fork; use LuckySJTU/vllm `dev/ncp-archpreview` / `dev/ncp-archpreview-dflash`); InternLM/lmdeploy
- No official from-scratch train GitHub as of 2026-09-11 (`recipe:ncp-archpreview` `code_status: partial`).
