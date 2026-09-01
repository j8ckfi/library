---
id: paper:bergson
type: paper
title: "Bergson: An Open Source Library for Data Attribution"
authors:
  - "Lucia Quirke"
  - "Louis Jaburi"
  - "David Johnston"
  - "William Z. Li"
  - "Gonçalo Paulo"
  - "Guillaume Martres"
  - "Girish Gupta"
  - "Stella Biderman"
  - "Nora Belrose"
year: 2026
month: 6
arxiv_id: "2606.11660"
url: "https://arxiv.org/abs/2606.11660"
methods:
  - method:bergson
  - method:magic
  - method:trackstar
  - method:ek-fac
  - method:source-unrolling
cites:
  - paper:magic
  - paper:trackstar
  - paper:source-tda
  - paper:ek-fac
tags:
  - interpretability
  - data-attribution
  - influence
  - bergson
  - eleutherai
---

# Bergson: An Open Source Library for Data Attribution

## Abstract Summary
Bergson is an EleutherAI MIT-licensed library for training-data attribution on language models: on-disk gradient stores, YAML pipelines, CLI and programmatic APIs, and multi-node FSDP. It ships the first public implementations of MAGIC (unrolled differentiation), SOURCE (approximate unrolling), and TrackStar (compressed influence / fact tracing), plus EK-FAC influence functions. Attribution scores estimate the leave-one-out / leave-k-out effect of training tokens or sequences on a query behavior. The library is `pip install bergson` (v0.26.2); code at https://github.com/EleutherAI/bergson; docs at https://bergson.readthedocs.io.

## Key Contributions
1. **First OSS MAGIC / SOURCE / TrackStar**: public implementations of three leading TDA methods that previously lacked open tooling, plus EK-FAC and grad-dot baselines.
2. **Composable pipeline**: Hessian options (identity, K-FAC/EK-FAC, Shampoo/TK-FAC, autocorrelation), optimizer normalization (Adam/Adafactor), TRAK-style projection, per-token or per-sequence scores, FAISS ANN, HF Trainer callback.
3. **Measured LDS on GPT-2 WikiText FT** (Table 1; 50 queries, N=400 retrains, 95% CI, Adam): MAGIC Spearman 0.983 ± 0.005 / Pearson 0.979 ± 0.006; SOURCE 0.387 ± 0.039 / 0.431 ± 0.048; EK-FAC 0.257 ± 0.015 / 0.295 ± 0.016; TrackStar (proj 1024/module) 0.184 ± 0.015 / 0.206 ± 0.015.
4. **Verified single-node scale** (Appendix C, one 8×A100): grad-dot 72B, EK-FAC 7B. Kronfluence EK-FAC reaches 14B on the same protocol. Intro "on the order of 405B" is a multi-node design claim, not a completed off-the-shelf run.

## Empirical Highlights
- README Muon-trained influence: Shampoo 0.522 ± 0.037, EK-FAC 0.474 ± 0.036.
- Sorted-subset / filtering-shaped LDS (appendix): MAGIC 1.000, EK-FAC 0.865, TrackStar 0.803. Do not describe TrackStar 0.18 random-subset LDS as too noisy to filter with.
- WMDP bio (§6.1): Deep Ignorance 7B LoRA r=32, 130M tokens, MAGIC per-token. Reweight top 10% tokens ×5 → +4.61 pp vs unweighted FT +3.11 pp (+1.5 pp extra). Sequence-level: +3.81 pp overall (+0.7 pp extra).
- MAGIC ~3–5 train-run compute; EK-FAC / TrackStar ~1–2. HF Trainer callback ~17% overhead.

## Open Source Repository & Resources
- Code: `https://github.com/EleutherAI/bergson`
- Docs: `https://bergson.readthedocs.io`
- Install: `pip install bergson` (v0.26.2)
