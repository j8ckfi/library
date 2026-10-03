---
id: paper:synth
type: paper
title: "It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs"
authors:
  - "Pierre-Carl Langlais"
  - "Pieter Delobelle"
  - "Yannick Detrois"
  - "Pavel Chizhov"
  - "Carlos Rosas-Hinostroza"
  - "Neil Si Smail"
  - "Benjamin Burtin"
  - "Hanna Shcharbakova"
  - "Ivan Yamshchikov"
  - "Anastasia Stasenko"
year: 2026
month: 9
arxiv_id: "2609.37891"
url: "https://arxiv.org/abs/2609.37891"
methods:
  - method:synth
cites:
  - paper:olmo-3
tags:
  - pretraining
  - synthetic-data
  - data-curriculum
  - synth
  - baguettotron
---

# It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs

## Abstract Summary
Web-crawl pretrain mixes were not designed for mid- and post-training (little explicit reasoning). SYNTH is an open synthetic corpus derived from 58,698 Wikipedia articles, collapsing pre-, mid-, and post-training into one NTP stage via structured amplification of encyclopedic seeds. Models: Monad 56M, Baguettotron 0.3B–0.6B dense, and a 13B-total / 1B-active MoE. At iso-compute SYNTH outperforms filtered web data. Because traces are back-translated from grounded passages, factual precision stays high despite 10–140× fewer tokens, with memorization targeted at the seed set. No separate SFT or RL. PleIAs.

## Key Contributions
1. **Seed-grounded synthetic corpus**: ~80B tokens in 8 languages from 50k vital + 8,698 specialized Wikipedia articles, 3,727 Wikibooks pages, and 130 extra documents, amplified by auxiliary query/reasoning models under a constraint grammar (including a 20% refusal/hedge axis).
2. **Single-stage generalist**: instruction and stenographic reasoning traces live in the pretrain mix; reported models are not SFT'd or RL'd after NTP.
3. **Factual-precision bake-off**: FActScore-style labeling on n=500 in-seed entities; held-out Good Articles show a seed-coverage ceiling.

## Empirical Highlights
- Baguettotron-600M (594M, 48 layers, d=1024, 158B tokens) Table 1 chat: Sup% 42.1, Con% 11.0, Inc% 47.0, S/(S+C) 79.3%±2.1, macro 41.7%±2.2 vs Qwen3-0.6B 65.7%/31.6% (~36T) and Phi-4-mini-instruct 77.4%/29.5% (~5T).
- Iso-compute 600M: SYNTH leads post-trained FineWiki / FinePDFs-Edu by 16–17 MC / 11–14 open-ended.
- Telecom slice: TeleQnA 41.6%→56.7%, 3GPP FactScore 21.5%→38.8%.
- Held-out: Baguettotron-MoE abstains 67% vs 20% in-seed; precision 82%→62%. OLMoE abstains 7% and keeps ~81%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.37891`
- Dataset: `https://huggingface.co/datasets/PleIAs/SYNTH` and `https://huggingface.co/datasets/SYNTH-Initiative/SYNTH`
- Weights: `https://huggingface.co/PleIAs/Baguettotron` (321M / ~200B card; not the 594M FActScore run)
- Training and data-generation code are not released (`recipe:synth` `code_status: partial`).
