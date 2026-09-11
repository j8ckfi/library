---
id: method:ncp-archpreview
type: method
title: "NCP-ArchPreview (Next Concept Prediction)"
category: "architecture"
status: experimental
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "NCP is a latent architecture + joint NTP/NCP objective; Muon2 remains the optimizer"
    use_instead: "method:muon2"
  - when: "choosing the open pretrain data mix"
    reason: "NCP trained on Dolma-3; OLMo-3 remains the data-recipe default"
    use_instead: "method:olmo-3"
  - when: "standard dense ~7B NTP pretrain without a concept module"
    reason: "That remains task:pretrain-dense-7b / Muon2 + OLMo-3"
    use_instead: "task:pretrain-dense-7b"
assumptions:
  - "Joint NTP + Next Concept Prediction. Product-quantized concept vocab from hidden states. Paper: 8.9B on 5.73T Dolma-3 tokens."
  - "Weights ArchSpace-Collection/NCP_ArchPreview_*; eval LUMIA-Group/ncp_olmo_eval. No official train GitHub (recipe code_status=partial). Serving: LuckySJTU/vllm_ncp_archpreview (obsolete; successor LuckySJTU/vllm dev/ncp-archpreview) and InternLM/lmdeploy."
last_reviewed: "2026-09-11"
papers:
  - paper:ncp-archpreview
recipes:
  - recipe:ncp-archpreview
claims:
  - benchmark: "NCP-ArchPreview 8.9B vs OLMo-3-7B Stage-1 on Dolma-3"
    metric: "tokens to match OLMo-3-7B final pretrain loss"
    value: "51.3% of the 5.73T budget"
    baseline: "OLMo-3-7B Stage-1 full token budget"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10715"
    notes: "Largest claimed latent-space LM demo. Not an optimizer bake-off."
  - benchmark: "Downstream macro-average vs OLMo-3-7B after full pretrain"
    metric: "macro-average lift"
    value: "+2.45"
    baseline: "OLMo-3-7B; GSM8K +5.99"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10715"
    notes: "Controlled ablations attribute gains to latent architecture and the NCP objective."
  - benchmark: "Compute vs parameter-aligned 8.9B NTP baseline"
    metric: "compute to approach baseline train loss"
    value: "85%"
    baseline: "strictly parameter-aligned 8.9B NTP"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10715"
  - benchmark: "DFlash2 drafter with concept injection"
    metric: "mean accepted length lift"
    value: "+4.17%"
    baseline: "DFlash2 without concept injection"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10715"
    notes: "17M VQ module also used as a domain-adaptation interface."
tags:
  - pretraining
  - architecture
  - latent-lm
  - ncp
  - experimental
---

# NCP-ArchPreview (Next Concept Prediction)

## Method Overview
Keep autoregressive token generation. Add a product-quantized concept vocabulary from hidden states and a Concept Module that predicts future multi-token concepts and feeds them back. NTP and NCP train jointly.

Experimental latent-space LM architecture. Optimizer default stays Muon2. Data recipe stays OLMo-3 / Dolma-3 (this run used Dolma-3; it does not replace that node).

## When to Use
- You want to pretrain or evaluate a latent-space LM with an explicit next-concept objective, or to consume the released 8.9B checkpoints / VQ adapter / DFlash2 drafter.

## When NOT to Use
- 7B optimizer → `method:muon2`. Open mix → `method:olmo-3`. Ordinary dense NTP 7B → `task:pretrain-dense-7b`.

## Relation to Existing SOTA
- Experimental first hop on `task:latent-space-lm-pretrain` only. Does **not** retarget Muon2, OLMo-3, or DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- No official from-scratch trainer; recipe is `code_status: partial`. Eval kit is LUMIA-Group/ncp_olmo_eval. Serving is LuckySJTU/vllm_ncp_archpreview (obsolete fork; use LuckySJTU/vllm `dev/ncp-archpreview`) plus InternLM/lmdeploy.
- 8.9B vs OLMo-3-**7B** is not a matched-parameter bake-off; the paper also reports an 8.9B NTP compute comparison (85%).
- Do not cite this as a Muon2 replacement.
