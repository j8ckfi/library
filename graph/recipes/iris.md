---
id: recipe:iris
type: recipe
title: "Iris Search-Agent Recipe"
method: method:iris
task: task:web-search-agent-rl
target_hardware: "MoE search-agent cluster (paper: Qwen3.6-35B-A3B / Qwen3.5-397B-A17B, 256K; in-cluster 397B-A17B FP8 judge)"
framework: "PyTorch / Relax + Iris-Harness"
repo_url: "https://github.com/AllSpark-Research/Iris"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - iris
  - web-search
  - sft-rl-climbing
---

# Iris Search-Agent Recipe

## Hardware & Environment Setup
- Official repo: `https://github.com/AllSpark-Research/Iris`. Harness lives in `Iris-Harness`. Weights: `AllSpark-Research/Iris-mini`, `AllSpark-Research/Iris-pro`.
- Paper RL engine: Relax (`https://github.com/redai-infra/Relax`). SFT: 2 epochs, global batch 64, max sequence 262144. Tools: SEARCH, SCRAPE. Block huggingface.co/datasets and huggingface.co/spaces at search, scrape, and the tool manager.
- AppWorld coverage stays CANOPY. Async stragglers stay SAO. SWE harness stays mini-SWE-agent. Dense Pass@1 stays CISPO.

## Quickstart Implementation

```python
from typing import Sequence


def climb_keep(pass_rate: float, n_tool: int, k_rft: int) -> bool:
    """Keep a query for the next SFT if it is solvable but not yet reliable, and deep enough."""
    return 0.0 < float(pass_rate) <= 0.5 and int(n_tool) >= int(k_rft)


def shortest_success(successes: Sequence[int]) -> int:
    """Among successful rollouts, take the one with fewest tool-call turns (index into successes)."""
    if not successes:
        raise ValueError("no successful rollouts")
    return min(range(len(successes)), key=lambda i: successes[i])


def dual_admit(closed_book_wrong: bool, open_book_correct: bool) -> bool:
    """Keep only questions the reference model fails closed-book and solves with evidence."""
    return bool(closed_book_wrong) and bool(open_book_correct)
```

## Critical Hyperparameters & Tuning Advice
- Climbing band is $0 < \bar{R}(q) \le 1/2$. Depth $K_{\mathrm{rft}}$ drops lucky shallow solves. At most 10% of assistant turns MASK.
- Default report is discard-all CM, not discard-all+retry. Always log the no-CM number.
- Does not replace CANOPY, SAO, mini-SWE-agent, FoldGRPO, or CISPO.
