---
id: paper:sparse-opd-supervision
type: paper
title: "Extremely Sparse Supervision Incentivizes Reasoning Ability"
authors:
  - "Zhishuai Liu"
  - "Xingzi Xu"
  - "Mehmet Saygin Seyfioglu"
  - "Pan Xu"
  - "Karim Bouyarmane"
year: 2026
month: 9
arxiv_id: "2609.04565"
url: "https://arxiv.org/abs/2609.04565"
methods:
  - method:sparse-opd-supervision
cites:
  - paper:opd
  - paper:dapo
  - paper:grpo
tags:
  - post-training
  - distillation
  - on-policy
  - sparse-supervision
  - opd
---

# Extremely Sparse Supervision Incentivizes Reasoning Ability

## Abstract Summary
On-policy distillation admits a teacher advantage on every generated token. This paper sparsifies that mask. On Qwen3 math OPD, supervising one or two tokens per trajectory (keep-frac ~0.02%–0.05% of response tokens; abstract: ~0.05%) matches or beats full-token OPD on most of nine teacher–student families, and is checked on coding, Llama, and sparse PPO. Variants: `rand1tok` (one uniform token), `mintok` / `maxtok` (highest / lowest OPD-reward token; Table 2), `minmaxtok` (both extremes), `randmask 0.1%`, `pctltail 0.05%` (top and bottom 0.05% by reward). Best sparse students often raise reverse KL relative to plain OPD, so the gain is not "imitate the teacher more closely." No official code as of 2026-09-08.

## Key Contributions
1. **Token mask on sampled-token OPD**: keep 1–2 tokens (or 0.05%–0.1% tails) per trajectory; same reverse-KL token loss on the kept positions.
2. **Nine Qwen3 families** covering large-teacher/small-student, same-scale, and small-teacher/large-student.
3. **Non-monotonic sparsity**: random 1-token still beats the base student; extreme-reward 1–2 tokens usually match/beat dense OPD.
4. **Cross-checks**: coding (LiveCodeBench v6), Llama, and PPO with the same sparse masks.

## Empirical Highlights
- Family 8 (Qwen3-1.7B ← 30B-A3B-Instruct), Table 3 avg@8 mean AIME24/25/HMMT-Feb: student 8.7, plain OPD 27.5, `pctltail 0.05%` 30.1 (keep 0.138%), `maxtok` 29.0, `minmaxtok` 28.9, `rand1tok` 15.6.
- Family 9 (Qwen3-8B ← 4B-Instruct-2507), Table 5: teacher 46.8, student 19.3, plain OPD 47.5, `minmaxtok` 49.3, `maxtok` 48.1 (revKL 1.116 vs plain 0.184).
- Family 4 (4B-Base ← 4B-GRPO-5ep), Table 4: teacher 15.8, student 6.1, plain OPD 16.1, `maxtok` 16.4.
- Across nine families the paper reports at least one sparse variant at 0.01%–0.1% keep matching or beating plain OPD.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-08. Host loop is sampled-token OPD (`method:opd`) with a keep-mask.
