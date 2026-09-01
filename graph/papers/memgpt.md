---
id: paper:memgpt
type: paper
title: "MemGPT: Towards LLMs as Operating Systems"
authors:
  - "Charles Packer"
  - "Sarah Wooders"
  - "Kevin Lin"
  - "Vivian Fang"
  - "Shishir G. Patil"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
year: 2023
month: 10
arxiv_id: "2310.08560"
url: "https://arxiv.org/abs/2310.08560"
methods:
  - method:memgpt
cites: []
tags:
  - agents
  - agent-memory
  - memgpt
---

# MemGPT: Towards LLMs as Operating Systems

## Abstract Summary
MemGPT pages context in and out of a hierarchical memory, like an OS. Nested conversational DMR: GPT-4 **32.1% → 92.5%**. Sleep-time compute (Lin et al. 2504.13171) later showed ~5× less test-time by precomputing memory offline. Use for long-lived persona agents, not SWE patch loops.

## Key Contributions
1. OS-style main / archival memory with explicit paging.
2. DMR GPT-4 32.1% → 92.5%.
3. Complementary sleep-time compute (2504.13171): ~5× less test-time.

## Empirical Highlights
- Document-QA DMR, GPT-4: 32.1% → **92.5%**.
- Sleep-time compute (2504.13171): ~5× less test-time. Source: https://arxiv.org/abs/2504.13171
