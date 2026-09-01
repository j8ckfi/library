---
id: paper:osworld-2
type: paper
title: "OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks"
authors:
  - "Mengqi Yuan"
  - "Zilong Zhou"
  - "Xinzhuang Xiong"
  - "Weiming Wu"
  - "Jiayang Sun"
  - "Jiamin Song"
  - "Kaiqian Cui"
  - "Bowen Wang"
year: 2026
month: 6
arxiv_id: "2606.29537"
url: "https://arxiv.org/abs/2606.29537"
methods:
  - method:claude-computer-use
cites: []
tags:
  - agents
  - computer-use
  - osworld
---

# OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks

## Abstract Summary
OSWorld 2.0 is a long-horizon computer-use protocol. On this paper protocol, Claude Opus 4.8 (max think, batched tools) is **20.6% binary / 54.8% partial**; GPT-5.5 is ~13% binary. Humans take ~1.6h. Failures are lost constraints and skipped verification, not GUI grounding. OSWorld-Verified is near-saturated and is not the ranking bench.

Do **not** promote aggregator Opus 5 **70.6%** or Steel GPT-5.6 Sol 62.6% partial as method SOTA. Those are different snapshots/protocols.

## Key Contributions
1. Harder long-horizon OSWorld 2.0 protocol versus saturated OSWorld-Verified.
2. Frontier GUI agents still far below humans on binary success.
3. Error analysis: constraint tracking and verification, not click-grounding, dominate failures.

## Empirical Highlights
- Opus 4.8 max think + batched tools: **20.6% binary / 54.8% partial**.
- GPT-5.5: ~13% binary.
- Humans: ~1.6 hours per task.
