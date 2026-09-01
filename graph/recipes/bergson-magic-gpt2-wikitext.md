---
id: recipe:bergson-magic-gpt2-wikitext
type: recipe
title: "Bergson MAGIC GPT-2 WikiText Tiny"
method: method:magic
task: task:training-data-attribution
target_hardware: "1x NVIDIA GPU (tiny YAML: nproc_per_node=1, batch 64); paper Table 1 LDS used larger retrain compute"
framework: "PyTorch / HuggingFace Transformers + Bergson 0.26.2"
repo_url: "https://github.com/EleutherAI/bergson"
pip_dependencies:
  - "bergson==0.26.2"
tags:
  - recipe
  - data-attribution
  - magic
  - bergson
  - gpt2
---

# Bergson MAGIC GPT-2 WikiText Tiny

Shipped YAML: `examples/magic/gpt2_wikitext_tiny.yaml`. Model `gpt2`, data `EleutherAI/bergson-wikitext-512-chunks`, batch 64. MAGIC unrolls this training run; it is not an influence pass over a downloaded final checkpoint.

## Hardware & Environment Setup

```bash
pip install bergson==0.26.2
```

Docs: https://bergson.readthedocs.io. Always `bergson metasmoothness` before trusting MAGIC LDS.

## Quickstart Implementation

```bash
bergson examples/magic/gpt2_wikitext_tiny.yaml
bergson metasmoothness
```

YAML (batch 64, gpt2, EleutherAI/bergson-wikitext-512-chunks):

```yaml
steps:
  - magic:
      run_path: runs/gpt2_wikitext
      model: gpt2
      overwrite: true
      data:
        dataset: EleutherAI/bergson-wikitext-512-chunks
        split: "train"
        chunk_length: 0
      query:
        dataset: EleutherAI/bergson-wikitext-512-chunks
        split: "test[0:1]"
        chunk_length: 0
      distributed:
        nproc_per_node: 1
      batch_size: 64
      grad_accum_steps: 4
      double_backward_batch_size: 4
      num_epochs: 1
      lr_schedule:
        lr_scheduler_type: polynomial
        lr: 0.0008
        lr_start: 1e-6
        lr_end: 0.00008
        warmup_steps: 0.25
      wandb_project: magic
```

## Critical Hyperparameters & Tuning Advice
- Untuned runs can yield LDS ~0. Check metasmoothness; fix trainer hyperparameters before interpreting scores.
- MAGIC is ~3–5 train-run compute. For a final ckpt or a 7B without that budget, use `recipe:bergson-trackstar`.
- Fused MoE experts unsupported.
