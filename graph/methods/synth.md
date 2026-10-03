---
id: method:synth
type: method
title: "SYNTH / Baguettotron"
category: "data-curriculum"
status: sota
sota_for:
  - task:synthetic-single-stage-pretrain
supersedes: []
do_not_use_for:
  - when: "choosing the open pretrain mix / Dolma-3 recipe"
    reason: "SYNTH is a seed-grounded synthetic corpus, not a replacement for Dolma-3"
    use_instead: "method:olmo-3"
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "SYNTH is a data recipe plus small-model runs; Muon2 remains the 7B optimizer"
    use_instead: "method:muon2"
  - when: "zero-natural-data self-play pretraining (no Wikipedia seeds)"
    reason: "SYNTH amplifies ~58k Wikipedia/Wikibooks seeds; it is not UTM self-play"
    use_instead: "method:self-play-pretraining"
  - when: "data-free post-train Challenger-Solver-Judge"
    reason: "J-Zero is post-train self-evolution, not synthetic pretraining"
    use_instead: "method:j-zero"
assumptions:
  - "Fully synthetic NTP from Wikipedia/Wikibooks seeds amplified by auxiliary query/reasoning models. No separate SFT/RL. Paper: Monad 56M/180B; Baguettotron-350M 321M/200B; Baguettotron-600M 594M/158B; Baguettotron-MoE 13.2B total / 1.05B active, 50B tokens."
  - "AdamW, sequence 2048, 16×H100 (torchtitan/FSDP); early Nanotron. Dataset: PleIAs/SYNTH and SYNTH-Initiative/SYNTH. HF PleIAs/Baguettotron is the 321M/200B card, not the 594M FActScore run."
  - "Knowledge is capped by ~58k Wikipedia seeds; the model abstains heavily outside that set."
last_reviewed: "2026-10-03"
papers:
  - paper:synth
recipes:
  - recipe:synth
claims:
  - benchmark: "FActScore-style Wikipedia seed entities n=500, Baguettotron-600M chat"
    metric: "S/(S+C) precision / macro S/(S+C+I)"
    value: "79.3%±2.1 / 41.7%±2.2"
    baseline: "Qwen3-0.6B 65.7%/31.6% (~36T); Phi-4-mini-instruct 77.4%/29.5% (~5T)"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37891"
    notes: "Table 1. 594M, 48 layers, d=1024, 158B tokens. Sup% 42.1, Con% 11.0, Inc% 47.0. No SFT/RL."
  - benchmark: "Iso-compute 600M vs FineWiki / FinePDFs-Edu (post-trained web)"
    metric: "multiple-choice / open-ended lead"
    value: "16–17 MC / 11–14 open-ended"
    baseline: "matched 600M FineWiki and FinePDFs-Edu"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37891"
    notes: "Both web models stay at chance on MMLU (24.0% and 25.6%)."
  - benchmark: "Telecom domain adaptation of Baguettotron-600M"
    metric: "TeleQnA accuracy / 3GPP FactScore"
    value: "41.6%→56.7% / 21.5%→38.8%"
    baseline: "600M SYNTH base before telecom fine-tune"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37891"
    notes: "~460M synthetic telecom tokens from Wikipedia telecom slice + 3GPP seeds."
  - benchmark: "Held-out Wikipedia Good Articles, Baguettotron-MoE"
    metric: "abstain rate / attempted-answer precision"
    value: "abstains 67% (vs 20% in-seed); precision 82%→62%"
    baseline: "OLMoE-1B-7B-Instruct abstains 7% and keeps ~81% precision"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37891"
    notes: "Coverage ceiling of the seed set, not a web-mix replacement."
tags:
  - pretraining
  - synthetic-data
  - data-curriculum
  - synth
  - baguettotron
  - sota
---

# SYNTH / Baguettotron

## Method Overview
SYNTH back-translates instruction, RAG, and stenographic reasoning traces from a fixed encyclopedic seed set, then trains with ordinary next-token prediction. There is no separate SFT or RL stage.

Seeds: 50k Wikipedia vital articles plus 8,698 specialized articles (58,698 Wikipedia total), 3,727 Wikibooks pages, and 130 extra documents. Stage 1 fine-tunes query and reasoning auxiliaries; Stage 2 amplifies each seed (~100× on memorization) under a constraint grammar (query type, complexity, user profile, language, style, including a 20% refusal/hedge axis). Frozen bge-m3 retrieval pairs each query with its seed paragraph and a near-neighbor.

Corpus: ~80B tokens in 8 languages. Models in the paper: Monad 56M / 180B tokens; Baguettotron-350M 321M parameters, 80 layers, d=576, 200B tokens; Baguettotron-600M 594M, 48 layers, d=1024, 158B tokens (main Table 1 reference); Baguettotron-MoE 13.2B total / 1.05B active, 50B tokens. Optimizer is AdamW on 16×H100 (torchtitan/FSDP).

## When to Use
- Fully synthetic single-stage pretrain from curated Wikipedia/Wikibooks seeds, including domain slices where no instruction data exists.

## When NOT to Use
- Open web/Dolma mix → `method:olmo-3`. ~7B optimizer → `method:muon2`. Zero-natural-data UTM self-play → `method:self-play-pretraining`. Post-train Challenger–Solver–Judge → `method:j-zero`.

## Relation to Existing SOTA
- First hop on `task:synthetic-single-stage-pretrain` only. Does **not** retarget `task:open-data-recipe`, `task:llm-pretraining-optimization`, or `task:pretrain-dense-7b`. Distinct from `method:hive-synth` (Poolside factory synth pipelines). Distinct from `method:self-play-pretraining` and `method:j-zero`.

## Gotchas & Failure Modes
- Knowledge is capped by ~58k Wikipedia seeds. Baguettotron-MoE abstains on 67% of held-out Good Article entities (20% in-seed); attempted precision drops 82%→62%. OLMoE on the same protocol abstains 7% and keeps ~81%.
- Hugging Face `PleIAs/Baguettotron` is the 321M / ~200B card. Do not cite it as the 594M / 158B FActScore checkpoint.
- Training and data-generation code are not released; dataset construction and training configs are in the paper. Dataset: `PleIAs/SYNTH` and `SYNTH-Initiative/SYNTH`.
- Distinct from `method:hive-synth`.
