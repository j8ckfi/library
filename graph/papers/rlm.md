---
id: paper:rlm
type: paper
title: "Recursive Language Models"
authors:
  - "Alex L. Zhang"
  - "Tim Kraska"
  - "Omar Khattab"
year: 2025
month: 12
arxiv_id: "2512.24601"
url: "https://arxiv.org/abs/2512.24601"
methods:
  - method:rlm
  - method:lambda-rlm
cites:
  - paper:codeact
tags:
  - agents
  - agent-recursion
  - long-context
  - rlm
---

# Recursive Language Models

## Abstract Summary
Recursive Language Models (RLMs) treat a dumped prompt as a REPL variable. The model slices the prompt in code and makes recursive sub-LM calls. This is inference-time prompt offload for inputs much larger than the window, not a software-engineering agent harness and not trajectory folding.

Depth 1 is the working setting. Do not cite unofficial notes that list BrowseComp+ 47.3; Table 1 of this paper is **91.3** for BrowseComp+ 1K at depth 1. No 405B-style claims are recorded here.

## Key Contributions
1. Prompt-as-REPL-variable harness: `rlm.completion` instead of stuffing the full corpus into the transformer window.
2. Depth-1 recursive subcalls beat compaction, Claude Code offload, and CodeAct+subcalls on long dumped inputs.
3. Optional SFT of RLM-Qwen3-8B (+28.3% median on 1k trajectories, 48 H100-h) is a sub-claim on this method, not a new SOTA method.

## Empirical Highlights (GPT-5, Table 1)
- OOLONG-Pairs: RLM d=1 **58.0** vs compaction **0.1** vs Claude Code offload **6.5**.
- BrowseComp+ 1K: RLM d=1 **91.3** vs compaction 70.5 vs base 0.0 (OOM).
- Median: +26% vs compaction, +130% vs CodeAct+subcalls, +13% vs Claude Code.
- Depth 2 overthinks (Wang 2603.02615: 3.6s → 344.5s). Not default.

## Open Source
- `https://github.com/alexzhang13/rlm` (`pip install rlms`)
