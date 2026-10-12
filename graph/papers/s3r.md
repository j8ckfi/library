---
id: paper:s3r
type: paper
title: 'S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding'
authors:
- Yuhang He
- Hongyu Ge
- Zihan Lin
- Siyi Liu
- Yongqi Zhang
year: 2026
month: 10
arxiv_id: '2610.13202'
url: https://arxiv.org/abs/2610.13202
methods:
- method:s3r
cites:
- paper:miles
- paper:online-draft-cotrain
tags:
- systems
- rlvr
- speculative-decoding
- s3r
---

# S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding

## Abstract Summary
Sparse attention changes the response groups used for GRPO-family updates; even exact response-wise reweighting does not recover the dense-policy update because advantages depend on other group members. S3R drafts with sparse attention, verifies with full attention and exact speculative sampling, shares one policy (no separate drafter), and uses a KV-aware scheduler so dense verify does not thrash the historical KV.

## Key Contributions
1. Proof that group-relative sparse sampling is not fixable by response-wise IS.
2. Self-sparse draft + dense verify with a shared policy.
3. 1.35×–1.39× e2e RLVR throughput on Qwen3 long-context math.

## Empirical Highlights
- See `method:s3r` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13202`
- Code: `none found` (`code_status: none`).
