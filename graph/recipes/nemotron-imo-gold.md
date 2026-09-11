---
id: recipe:nemotron-imo-gold
type: recipe
title: "Nemotron IMO Gold SFT+RL+TTC"
method: method:nemotron-imo-gold
task: task:olympiad-math-posttrain
target_hardware: "Nemotron 3 Ultra 550B-A55B class (multi-node BF16 SFT at 425,984 ctx; RL on NeMo-RL)"
framework: "NeMo-Skills + NeMo-RL"
repo_url: "https://github.com/NVIDIA-NeMo/Skills"
pip_dependencies:
  - "nemo-skills"
  - "nemo-rl"
tags:
  - recipe
  - nemotron
  - olympiad
  - math
---

# Nemotron IMO Gold SFT+RL+TTC

## Hardware & Environment Setup
- Collection: `https://huggingface.co/collections/nvidia/nemotron-labs-imo-2026`.
- Base: `https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16` (`method:nemotron-3-ultra`).
- Specialists: `https://huggingface.co/nvidia/Nemotron-3-Labs-Ultra-Math-SFT`, `https://huggingface.co/nvidia/Nemotron-3-Labs-Ultra-Math-RL`.
- Data: `https://huggingface.co/datasets/nvidia/Nemotron-Math-Proofs-v3-SFT`, `https://huggingface.co/datasets/nvidia/Nemotron-Math-Proofs-v3-RL`.
- Eval: `https://huggingface.co/datasets/nvidia/Nemotron-IMO-Bench` (200 items).
- TTC / submitted proofs: `https://github.com/NVIDIA-NeMo/Skills/tree/main/recipes/nemotron-imo-tts`.
- RL guide: `https://github.com/NVIDIA-NeMo/RL/blob/imo-26-ultra-v3/docs/guides/nemotron-3-ultra-imo.md`.
- Pass@1 kernel stays CISPO. This recipe is olympiad NL proofs + TTC.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class NemotronImoTtc:
    generate: str = "nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16"
    sft: str = "nvidia/Nemotron-3-Labs-Ultra-Math-SFT"
    rl: str = "nvidia/Nemotron-3-Labs-Ultra-Math-RL"
    max_sft_seq: int = 425984
    prover: bool = False
    tools: bool = False
    internet: bool = False


def ttc_loop(problem: str, cfg: NemotronImoTtc) -> str:
    """Generate–verify–refine over GA + SFT + RL specialists; high-compute select last."""
    if cfg.prover or cfg.tools or cfg.internet:
        raise ValueError("recipe is natural-language only")
    pool: list[tuple[str, float]] = []
    for ckpt in (cfg.generate, cfg.sft, cfg.rl):
        proof, score, feedback = ckpt, 0.0, ""  # host: NeMo-Skills nemotron-imo-tts
        pool.append((proof, score))
        _ = feedback
    return max(pool, key=lambda item: item[1])[0]
```

## Critical Hyperparameters & Tuning Advice
- SFT max length 425,984 is load-bearing. Do not compress proofs into short-CoT CISPO batches.
- Keep a separate high-compute selection stage after iterative refine.
- Nemotron-IMO-Bench (`nvidia/Nemotron-IMO-Bench`, 200) is the released eval; do not mix with AIME Pass@1.
