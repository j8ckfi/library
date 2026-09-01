---
id: recipe:foldgrpo
type: recipe
title: "FoldAgent / FoldGRPO"
method: method:foldgrpo
task: task:long-horizon-tool-agent
target_hardware: "multi-GPU train (paper Seed-OSS-36B); search server on a separate machine for BrowseComp-Plus"
framework: "PyTorch / verl (sunnweiwei/FoldAgent reimplementation)"
repo_url: "https://github.com/sunnweiwei/FoldAgent"
pip_dependencies:
  - "torch"
  - "verl"
tags:
  - recipe
  - agents
  - foldgrpo
---

# FoldAgent / FoldGRPO

Open reimplementation on verl; may differ from the paper train code. This is trajectory folding, not RLM and not mini-SWE-agent.

## Hardware & Environment Setup
Search server (BrowseComp-Plus) on a separate machine, then train:

```bash
cd envs && python search_server.py \
  --model Qwen/Qwen3-Embedding-8B \
  --corpus Tevatron/browsecomp-plus-corpus \
  --corpus-embedding-dataset miaolu3/browsecomp-plus \
  --host 0.0.0.0 --port 8000
export LOCAL_SEARCH_URL="http://<search-server>:8000"
bash scripts/train_bc_qwen3_8b.sh
```

## Quickstart Implementation

```python
def fold_active_context(completed_subtrees, live_window_tokens):
    """Keep a small live window; completed sub-trajectories are folded summaries."""
    if not live_window_tokens:
        raise ValueError("live window must stay non-empty")
    return {"folded": list(completed_subtrees), "active": list(live_window_tokens)}
```

## Critical Hyperparameters & Tuning Advice
- **Active context**: 32K×10 in the Seed-OSS-36B paper setting.
- **Not GPT-5 SOTA**: GPT-5 ReAct 0.793 / 0.718 still ahead.
- **Not RLM**: do not point this at a 10M dumped prompt.
