---
id: paper:prep-opd
type: paper
title: "How Should Teachers Be Prepared? RL on Student-Induced States for On-Policy Distillation"
authors:
  - Xiaoyu Ma
  - Haoyue Liu
  - Zhichao Wang
  - Jionghao Zhu
  - Xiaoying Tang
year: 2026
month: 10
arxiv_id: "2610.04950"
url: "https://arxiv.org/abs/2610.04950"
methods:
  - method:prep-opd
cites:
  - paper:opd
  - paper:scout
tags:
  - post-training
  - distillation
  - opd
  - prep-opd
---

# How Should Teachers Be Prepared? RL on Student-Induced States for On-Policy Distillation

## Abstract Summary
Teachers that solve problems independently can fail to continue student prefixes. Prep-OPD RL-trains the teacher on fixed student prefixes with final-answer correctness, then freezes that teacher for OPD. Qwen3-4B-Instruct-2507 teacher, Qwen3-0.6B/1.7B students, eight math benchmarks. 4B→1.7B: +8.28 vs OPD and +2.30 vs Relay-OPD. Student-prefix teacher RL beats problem-start teacher RL with and without handoff on 1.7B. Same prepared teacher also helps 0.6B. Separate method beside SCOUT (prepare-then-freeze vs interleaved teacher RL). No public code as of 2026-10-06.

## Key Contributions
1. **Prepare-then-freeze**: teacher RL on fixed student prefixes, then ordinary OPD.
2. **Prefix conditioning is load-bearing** vs problem-start teacher RL ± handoff.
3. **Reusable teacher**: one prepared 4B teacher helps both 1.7B and 0.6B students.

## Empirical Highlights
- 4B teacher → 1.7B student, eight math benches: +8.28 vs OPD, +2.30 vs Relay-OPD.
- Student-prefix teacher RL beats problem-start teacher RL with and without handoff on 1.7B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04950`
- Code: none found as of 2026-10-06 (`code_status: none`). Relay-OPD is a paper baseline, not a library method.
