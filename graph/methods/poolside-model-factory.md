---
id: method:poolside-model-factory
type: method
title: "Poolside Model Factory"
category: "training-systems"
status: sota
sota_for:
  - task:industrial-model-building
supersedes: []
papers:
  - paper:laguna-m1-xs2
recipes:
  - recipe:small-lab-model-factory
claims:
  - benchmark: "Laguna XS.2 from-scratch factory cycle"
    metric: "wall-clock start-of-training to Apache-2.0 release after M.1"
    value: "five weeks"
    baseline: "artisanal per-model pipelines (week-scale scheduling for steps the factory later automated)"
    date: "2026-08"
    verified: true
    notes: "Laguna M.1/XS.2 technical report (arXiv:2605.27605). Process claim, not a loss/optimizer claim."
  - benchmark: "Poolside Spark/Dagster data plane"
    metric: "steady-state ingest"
    value: "~20T tokens/day (2e13)"
    baseline: "per-job ad-hoc Spark without asset lineage"
    date: "2026-08"
    verified: true
    notes: "Report §3.2.1; cluster-scale number. Small labs keep Iceberg-style versioned assets, not this throughput."
  - benchmark: "Titan distributed Muon on Laguna M.1"
    metric: "optimizer share of step time"
    value: "<1%"
    baseline: "naive per-rank full-parameter Newton–Schulz Muon"
    date: "2026-08"
    verified: true
    notes: "Report §3.1.2. Laguna used Moonlight Muon; library dense default remains Muon2 + KL-SOAP."
tags:
  - systems
  - training-systems
  - model-factory
  - process
  - lineage
  - dagster
  - sota
---

# Poolside Model Factory

## Method Overview
Poolside Model Factory is an industrial **process** for building foundation models: versioned data, train, eval, and infer under one control plane so iteration is a configuration change. Primary source: Laguna M.1/XS.2 (`paper:laguna-m1-xs2`, arXiv:2605.27605, May 2026) plus the 2025 factory blog series. It is orthogonal to train-kernel SOTA. Laguna used Muon (Moonlight) and CISPO on this stack; CISPO, Muon2 / SOAP-Muon, OLMo-3, OPD, DeepSeek-V4, and the rest of the library's train defaults stay.

Laguna §2 principles:
1. **Experiments as code + Dagster control plane + full lineage.** Every data, ablation, and train job is a committed config with a unique run ID. Assets live in an Iceberg-style lake; Spark jobs register Dagster assets. A token in a packed shard traces back through dedup/filter/synth; every checkpoint and eval traces back to the run.
2. **Composable decoupled components, one research+prod codebase.** Titan (train) and Atlas (infer) share model definitions so a research win is a config flag. Hive synth, Blender mixes, and evals are the same job types with different configs.
3. **Reserve human attention for novel decisions.** Custom batch scheduler, auto-recovery, and cross-replica hash checks absorb mechanical work. On-call pages only when automatic recovery fails.

Named machines (closed internals; do not invent public Titan/Atlas/Hive repos — TorchTitan is Titan's public seed):
- **Dagster**: DAG control plane; jobs launched by registering a config asset (CLI or UI).
- **Iceberg / Spark**: versioned assets; ~20T tok/day ingest at Poolside.
- **Blender**: gRPC `BlendConfig` of weighted Iceberg sources including live tables; sidecar prefetch; mix changeable mid-run (`method:blender-streaming`).
- **Titan**: PyTorch trainer seeded from TorchTitan, 2200+ patches; DDP/FSDP/TP/EP/PP; distributed Muon <1% of step.
- **Atlas**: vLLM-based infer consuming Titan defs; NVIDIA / AMD / Trainium.
- **Hive**: declarative synth pipelines as config (`method:hive-synth`).
- **AutoMixer**: proxy-swarm mix search (`method:automixer`); component, not the Dolma/OLMo default.
- **Code-exec / Saucer**: ~1M-repo OCI farm for RL rewards, synth, and evals.
- **Podium**: dataset/model viewer; company-wide vibe check on produced models.
- **GPU↔GPU weight transfer**: NCCL P2P / GPUDirect RDMA trainer→infer for online RL.

Cluster (Poolside scale): ~10k H200, Helm/Terraform. Scheduler evolved from Volcano to in-house: per-job eviction, topology in FoundationDB, sticky pod respawn, sub-minute placement. M.1 trained on 6144 H200s; XS.2 on 2048. Laguna is a coding MoE (M.1 225.8B/23.4B active, XS.2 33.4B/3B, >30T pretrain tokens); DeepSeek-V4 / Kimi-K3 remain the MoE architecture defaults.

Blogs: https://poolside.ai/blog/introducing-the-model-factory (2025-07-17) and the rest of the 2025 series listed on `paper:laguna-m1-xs2`. Hub: https://poolside.ai/research.

## When to Use
- Default **process** SOTA when the job is "make model building repeatable" (Abiome, future SLp-X, any small lab), not "pick a loss/optimizer/architecture."
- When a research win must promote by config flag against a shared train+infer codebase.
- When every checkpoint must answer "which data + config produced this?"

## Scale-down (few-GPU / small lab)
The factory **ideas** scale down; the 10k-GPU machinery does not.

**Keep:** experiments-as-code (every run is a committed config with a unique ID); a DAG control plane (Dagster is the published choice) with Iceberg-style versioned assets and two-way lineage; one trainer+infer codebase so a research win is a config flag; streamed data mixes (do not pre-materialize a giant shard); synthetic pipelines as config; evals hooked to checkpoints automatically; lab-wide vibe check on produced models.

**Skip until cluster-scale / split trainer-infer RL:** custom FoundationDB batch scheduler (Volcano, vanilla Kubernetes, or even local Dagster is enough); GPU↔GPU NCCL P2P weight sync; 1M-repo OCI code-exec farm; AutoMixer swarms of 60×0.5B proxies; Titan's fused MoE dispatch megakernel.

Concrete SOP: `recipe:small-lab-model-factory`.

## Gotchas & Failure Modes
- Copying Poolside's cluster (FoundationDB scheduler, NCCL P2P, 1M-repo farm) before trainer and infer actually live on separate GPU pools wastes the whole effort.
- Treating this method as a replacement for CISPO, Muon2, OLMo-3, or DeepSeek-V4. Laguna **used** those families; it did not supersede them.
- Inventing open Poolside Titan/Atlas/Hive packages. They are closed. Train with TorchTitan or the lab's existing trainer.
- Attaching the factory to `task:pretrain-dense-7b`, `task:pretrain-moe-frontier`, or `task:math-code-rl-dense` as a kernel default.

## Supersession
Does **not** supersede CISPO, Muon2 / SOAP-Muon, OLMo-3 / Dolma-3, OPD / Open-MOPD / u-OPSD / TTPO, DeepSeek-V4, Quartet II, Transolver-3, BMSSP, or Mixture-of-Kittens. Process shelf only.
