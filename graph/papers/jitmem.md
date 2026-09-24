---
id: paper:jitmem
type: paper
title: "Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents"
authors:
  - "Yefan Zhou"
  - "Yang Li"
  - "Zeyu Leo Liu"
  - "Semih Yavuz"
  - "Shafiq Joty"
year: 2026
month: 9
arxiv_id: "2609.27334"
url: "https://arxiv.org/abs/2609.27334"
methods:
  - method:jitmem
cites:
  - paper:ace
  - paper:code2skill
  - paper:jev-mem
  - paper:memgpt
  - paper:grpo
tags:
  - agents
  - agent-memory
  - jitmem
---

# Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents

## Abstract Summary
Most agentic memory systems curate at write time: a finished trajectory is distilled into a fixed reflection, skill, or strategy and later retrieved by similarity. That decision is irreversible and query-independent, and learning the writer is a long-horizon credit problem. JitMem keeps raw trajectories and defers curation to read time. A curator sees the current task plus retrieved traces and synthesizes a compact task-adaptive payload. Because that payload is consumed on the same task, the curator trains from immediate success (GRPO over candidate payloads, frozen executor). Even an untrained read-time curator is competitive with write-time baselines; training compounds.

## Key Contributions
1. **Read-time curation**: same stored trajectory yields different payloads for different downstream tasks.
2. **Immediate curator reward**: no task-grouping scaffold required by learned write-time curators (SkillOS).
3. **JitMem**: lossless episodic bank + BM25 retrieve + GRPO curator + frozen executor.

## Empirical Highlights
- ALFWorld / WebShop / \(\tau^2\)-bench: +16.2 / +16.3 / +3.9 absolute success vs strongest write-time baseline.
- Qwen3-8B executor: ALFWorld 77.4 vs SkillOS 61.2 (+16.2); WebShop SR 32.8 vs SkillOS 16.5 (+16.3).
- Compact payload cuts input tokens 50.3%–56.3% and executor steps 28.4%–31.4% vs write-time methods.
- Untrained JitMem-gemini already competitive (WebShop 61.0 vs SkillOS 41.0 with Gemini-2.5-Pro curator/executor).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.27334`
- No public GitHub found as of 2026-09-24 (`recipe:jitmem` `code_status: none`).
