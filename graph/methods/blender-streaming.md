---
id: method:blender-streaming
type: method
title: "Blender Streaming Mix (BlendConfig)"
category: "training-systems"
status: active
sota_for: []
supersedes: []
papers:
  - paper:laguna-m1-xs2
claims:
  - benchmark: "Laguna pretrain data plane (Blender)"
    metric: "mix mutability without rematerializing shards"
    value: "gRPC BlendConfig over weighted Iceberg sources, including live tables; mix changeable mid-run"
    baseline: "pre-materialized packed shard tied to a fixed blend and cluster size"
    date: "2026-08"
    verified: true
    notes: "Laguna M.1/XS.2 §3.1.2 Data Loading; 2025 factory blogs. Worth copying at small scale even if the transport is a simpler dataloader."
tags:
  - systems
  - training-systems
  - data-streaming
  - blender
  - factory-component
---

# Blender Streaming Mix (BlendConfig)

## Method Overview
Blender is Poolside's streaming data service for the Model Factory. Training does not read a giant pre-materialized shard from local disk. A `BlendConfig` names weighted Iceberg sources (including live tables still being written), mixture weights, and curriculum. Blender exposes a gRPC API that serves batches with consistent global composition across workers. A sidecar prefetches into shared memory; the trainer copies to GPU via pinned memory. Mix weights can change mid-run without redistributing a packed corpus.

This is the factory idea most worth copying at few-GPU scale: **stream a weighted mix, do not freeze a shard**.

## When to Use
- Any lab that currently dumps a full packed dataset before training.
- Mid-run mix or curriculum changes, or branching an experiment off an existing Iceberg (or local equivalent) table.

## Scale-down (few-GPU / small lab)
**Keep** the idea. A simple weighted iterable over tokenized sources is enough; gRPC and Iceberg are optional. Commit the mix as config with a unique run ID so lineage still works.

**Skip** Poolside's gRPC service, sidecar shared-memory path, and cluster-wide Iceberg lake until the DAG already tracks assets.

## Gotchas & Failure Modes
- Pre-materializing "for simplicity" reintroduces the cost the method exists to remove (fixed cluster size, delayed start, rematerialize on every mix change).
- Global composition across workers still needs an explicit sampler; naively concatenating files is not a BlendConfig.

## Supersession
Active component of `method:poolside-model-factory`. Does not supersede `method:olmo-3`.
