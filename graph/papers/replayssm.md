---
id: paper:replayssm
type: paper
title: 'ReplaySSM: Cache SSM Inputs, Not State'
authors:
- Ze-Wei Liou
- Harris Nover
- Amey Naik
- Andrii Skliar
- Igor Shovkun
- Ido Shahaf
- Tri Dao
year: 2026
month: 10
arxiv_id: '2610.13778'
url: https://arxiv.org/abs/2610.13778
methods:
- method:replayssm
cites:
- paper:mamba-2-paper
tags:
- systems
- ssm
- serving
- replayssm
---

# ReplaySSM: Cache SSM Inputs, Not State

## Abstract Summary
ReplaySSM keeps a checkpoint plus a recent-input buffer for hybrid SSM state instead of caching the full recurrent state. On vLLM Mamba-2 / Gated DeltaNet, decode is 1.20–1.47× at batch 256; ~1.8× vs vLLM speculative decoding on 120B-class. Relevant for RL rollout throughput. Plug-in on `task:linear-time-sequence-modeling`; link `task:input-heavy-agentic-moe-serving`.

## Key Contributions
1. Checkpoint + recent-input buffer instead of full SSM state cache.
2. vLLM integration for Mamba-2 and Gated DeltaNet.
3. Decode throughput at large batch; comparison to speculative decoding.

## Empirical Highlights
- vLLM Mamba-2 / Gated DeltaNet batch-256 decode 1.20–1.47×.
- ~1.8× vs vLLM speculative decoding on 120B-class.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13778`
- Code: `https://github.com/Johnny-Liou/ReplaySSM` (`code_status: released`; HTTP 200 as of 2026-10-13).
