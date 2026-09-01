---
id: paper:coding-agents-long-context
type: paper
title: "Coding Agents are Effective Long-Context Processors"
authors:
  - "Weili Cao"
  - "Xunjian Yin"
  - "Bhuwan Dhingra"
  - "Shuyan Zhou"
year: 2026
month: 3
arxiv_id: "2603.20432"
url: "https://arxiv.org/abs/2603.20432"
methods:
  - method:coding-agent-file-offload
cites:
  - paper:rlm
tags:
  - agents
  - long-context
  - file-offload
---

# Coding Agents are Effective Long-Context Processors

## Abstract Summary
Give the agent a filesystem and grep instead of a 10M-token prompt. Complementary to RLM: if the corpus can live on disk, use file offload; if it is a dumped string that must be sliced in a REPL, use RLM. RAH (2606.13643) cites GPT-5 Codex no-retriever Oolong-Synthetic **71.75%** vs RLM **64.38%**. RAH has no public code; evidence_level preprint; not a new SOTA method.

This does **not** replace mini-SWE-agent as the SWE harness.

## Key Contributions
1. Filesystem+grep as long-context offload for coding agents.
2. Complementary, not competing, with RLM dumped-prompt REPL.

## Empirical Highlights
- RAH citation (2606.13643): GPT-5 Codex no-retriever Oolong-Synthetic **71.75%** vs RLM **64.38%**.
