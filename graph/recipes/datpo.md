---
id: recipe:datpo
type: recipe
title: "DATPO Tree-Structured Coverage RLVR"
method: method:datpo
task: task:passk-reasoning-coverage
target_hardware: "1x NVIDIA A100 80GB per run (paper); 8x A100 cluster used for the study"
framework: "PyTorch / GRPO-Zero"
repo_url: "https://github.com/policy-gradient/GRPO-Zero"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - datpo
  - rlvr
  - passk
---

# DATPO Tree-Structured Coverage RLVR

## Hardware & Environment Setup
- Paper codebase is GRPO-Zero (`https://github.com/policy-gradient/GRPO-Zero`). No DATPO-named repo as of 2026-09-09.
- Tree expansion default (N, Kmax, Bmax)=(4,3,4). Clip-higher (0.28, 0.2). 16 prompts/step, mini-batch 64, micro-batch 2. Embeddings: gte-large-en-v1.5 (smaller GTE/mpnet also work).
- Host Pass@1 algorithm stays CISPO. Pass@K no-backward default stays ES-reasoning.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def sentence_entropy(token_entropy: torch.Tensor, sentence_ids: torch.Tensor) -> torch.Tensor:
    """Mean token entropy per sentence. token_entropy/sentence_ids: [T]."""
    n = int(sentence_ids.max().item()) + 1 if sentence_ids.numel() else 0
    out = token_entropy.new_zeros(n)
    counts = token_entropy.new_zeros(n)
    out.scatter_add_(0, sentence_ids, token_entropy)
    counts.scatter_add_(0, sentence_ids, torch.ones_like(token_entropy))
    return out / counts.clamp(min=1.0)


def sibling_diversity(block_emb: torch.Tensor) -> torch.Tensor:
    """1 − mean pairwise cosine among sibling block embeddings [B, D], B>=2."""
    if block_emb.shape[0] < 2:
        return block_emb.new_tensor(0.0)
    normed = F.normalize(block_emb, dim=-1)
    sim = normed @ normed.T
    b = sim.shape[0]
    off = sim.sum() - sim.diag().sum()
    n_pairs = b * (b - 1)
    return 1.0 - off / n_pairs


def annealed_alpha(step: int, total: int, start: float = 0.2) -> float:
    """Linear α: start → 0 over training."""
    if total <= 0:
        return 0.0
    t = min(max(step, 0), total) / float(total)
    return float(start) * (1.0 - t)


def datpo_advantage(outcome: torch.Tensor, sibdiv: torch.Tensor, alpha: float) -> torch.Tensor:
    """Block advantage = outcome + α * sibling diversity (detached)."""
    return outcome + float(alpha) * sibdiv.detach()
```

## Critical Hyperparameters & Tuning Advice
- Anneal α. Fixed α=0 loses late pass@k.
- Match generated tokens to GRPO/AttnRL; do not match wall-clock.
- Difficulty-adaptive expansion is load-bearing for pass@k (Table 12: 54.9 vs 49.8 without it).
