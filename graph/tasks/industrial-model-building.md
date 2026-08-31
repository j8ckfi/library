---
id: task:industrial-model-building
type: task
title: "Industrial Model Building (Model Factory Process)"
domain: "systems"
summary: "Turn foundation-model development into a repeatable industrial process (versioned data, train, eval, infer) so iteration is a config change rather than a rewrite."
current_sota:
  - method: method:poolside-model-factory
    as_of: "2026-08"
    benchmark: "Laguna XS.2 from-scratch factory cycle (Apache-2.0 release)"
    metric: "wall-clock start-of-training to public release after M.1"
    value: "five weeks"
    notes: "Process SOTA from Laguna M.1/XS.2 (arXiv:2605.27605). Not a loss/optimizer/architecture SOTA. Poolside ran Muon (Moonlight) and CISPO on this stack; those remain the train-kernel defaults."
methods:
  - method:poolside-model-factory
  - method:automixer
  - method:blender-streaming
  - method:hive-synth
tags:
  - systems
  - training-systems
  - model-factory
  - process
  - lineage
  - dagster
---

# Industrial Model Building (Model Factory Process)

## Problem Definition
Foundation-model work is usually artisanal: data shards are pre-materialized, research and production live in different codebases, and a research win is a rewrite rather than a flag. The industrial-model-building problem is to treat data, training, evaluation, and inference as one versioned process so a lab can reproduce any checkpoint, change a mix or synth pipeline as configuration, and promote a win without plumbing.

This is the **process** task. It does **not** replace train-kernel SOTA:

- Dense optimizer: `method:muon2` / `method:soap-muon-scale` on `task:pretrain-dense-7b`
- Open data recipe: `method:olmo-3` on `task:open-data-recipe` (AutoMixer is a factory component, not the new Dolma/OLMo default)
- MoE architecture: `method:deepseek-v4` / `method:kimi-k3` on `task:pretrain-moe-frontier`
- Dense math/code RL: `method:cispo` on `task:math-code-rl-dense`

Poolside's Laguna run used Muon (Moonlight) and CISPO **inside** the factory. That is "they ran the library's existing train defaults on a factory stack," not a reason to retarget those methods.

## Evaluation Protocol & Benchmarks
- **Cycle time**: wall-clock from committed config to a released checkpoint (Laguna XS.2: five weeks from-scratch after M.1).
- **Lineage**: any token, checkpoint, or eval result traces both ways through data + config.
- **Promotion cost**: a research win is a config flag against a shared train+infer codebase, not a fork.
- **Scale-down honesty**: few-GPU / small-lab operators keep the process ideas; they do not copy 10k-H200 machinery.

## SOTA Landscape
As of 2026-08 the date-stamped process default is **Poolside Model Factory** (`method:poolside-model-factory`, Laguna M.1/XS.2 `arXiv:2605.27605` plus the 2025 factory blog series). Named machines (Dagster control plane, Iceberg/Spark assets, Blender, Titan, Atlas, Hive, AutoMixer, code-exec/Saucer, Podium) are closed internals except TorchTitan as Titan's public seed. Mixture-of-Kittens (`task:train-moe-nvl72`) remains the NVL72 megakernel SOTA; it is a different systems problem.
