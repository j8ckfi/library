---
id: recipe:ddo
type: recipe
title: "DDO Divergence-Tree Preference Train"
method: method:ddo
task: task:direct-preference-alignment
target_hardware: "LoRA + vLLM eval (BabyAI / BabaIsAI / WebShop)"
framework: "PyTorch 3.10 env / PEFT LoRA / managed vLLM"
repo_url: "https://github.com/koguma00/direct_diverse_optimization"
pip_dependencies: []
tags:
  - recipe
  - ddo
  - preference-alignment
---

# DDO Divergence-Tree Preference Train

## Hardware & Environment Setup
- Official: `https://github.com/koguma00/direct_diverse_optimization`
- `conda env create -f environment.yml && conda activate ddo && python -m pip install -e .`
- Extract released trajectory and checkpoint ZIPs in-repo. Clone pinned BALROG and WebShop under `benchmarks/`.
- Chat default stays OLMo-3. Checker agents stay CANOPY.

## Quickstart Implementation

```bash
python train.py --config configs/training.yaml --dry-run
python train.py --config configs/training.yaml
python eval.py --config configs/eval.yaml
```

Set `method: ddo` in `configs/training.yaml`. `start_from` is `scratch`, `dtc`, or `dataset`. Paper defaults: reference SFT 10 epochs; preference 5 epochs (BabyAI/BabaIsAI) or 15 (WebShop); DTC `divergence_count: 5`, `alt_budget: 3`.

## Critical Hyperparameters & Tuning Advice
- Successful-only imitation and decoding-time diversification are controls, not DDO.
- If eval hits `max_tokens` before an action, raise both train and eval token caps together and report them.
