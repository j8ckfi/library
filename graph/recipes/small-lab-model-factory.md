---
id: recipe:small-lab-model-factory
type: recipe
title: "Small-Lab Model Factory SOP"
method: method:poolside-model-factory
task: task:industrial-model-building
target_hardware: "few-GPU / small lab (1–8x consumer or datacenter GPUs; not 10k H200)"
framework: "Python + Dagster + Apache Iceberg (or a local equivalent) + a single training library (TorchTitan or the lab's existing trainer) sharing model defs with the infer stack"
repo_url: "https://github.com/pytorch/torchtitan"
pip_dependencies:
  - "dagster"
  - "torch>=2.5.0"
tags:
  - recipe
  - systems
  - training-systems
  - model-factory
  - small-lab
  - dagster
---

# Small-Lab Model Factory SOP

Target is a few-GPU lab (including Abiome / future SLp-X), not Poolside's ~10k H200 cluster. Titan/Atlas/Hive are closed; TorchTitan is the public trainer seed. pip is `dagster` plus whatever the lab already trains with.

## Hardware & Environment Setup
- **Keep:** committed configs with unique run IDs; Dagster (or local equivalent) DAG so any checkpoint traces to data+config; streamed weighted mixes; eval on every N steps from the same infer codepath; promote a win by config flag.
- **Skip until cluster-scale / split trainer-infer RL:** FoundationDB/Volcano custom scheduler, GPU↔GPU NCCL P2P, 1M-repo OCI farm, AutoMixer 60×0.5B swarms, Titan fused MoE megakernel. Vanilla Kubernetes or local Dagster is enough.

## Quickstart Implementation

```python
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Iterator, Mapping

try:
    from dagster import asset
except ImportError:
    def asset(*args, **kwargs):
        if args and callable(args[0]):
            return args[0]

        def wrap(fn):
            return fn

        return wrap


@dataclass(frozen=True)
class RunConfig:
    mix: Mapping[str, float]
    eval_every: int
    use_research_flag: bool
    trainer: str = "torchtitan"


def run_id_for(config: RunConfig) -> str:
    payload = json.dumps(asdict(config), sort_keys=True)
    return hashlib.sha1(payload.encode()).hexdigest()[:12]


def stream_mix(sources: Mapping[str, Iterator[list[int]]], mix: Mapping[str, float]) -> Iterator[list[int]]:
    """Blender idea at small scale: weighted iterable, no pre-materialized shard."""
    import random

    names = list(mix)
    weights = [float(mix[n]) for n in names]
    total = sum(weights)
    if total <= 0:
        raise ValueError("mix weights must sum to a positive value")
    probs = [w / total for w in weights]
    iters = {n: iter(sources[n]) for n in names}
    while True:
        name = random.choices(names, weights=probs, k=1)[0]
        try:
            yield next(iters[name])
        except StopIteration:
            return


@asset
def packed_sources():
    return {
        "code": iter([[1, 2, 3], [4, 5, 6]]),
        "web": iter([[7, 8, 9]]),
        "math": iter([[10, 11, 12]]),
    }


@asset(deps=[packed_sources])
def train_and_eval(packed_sources):
    config = RunConfig(
        mix={"code": 0.40, "web": 0.35, "math": 0.25},
        eval_every=100,
        use_research_flag=True,
    )
    run_id = run_id_for(config)
    checkpoint = None
    for step, batch in enumerate(stream_mix(packed_sources, config.mix)):
        checkpoint = {"run_id": run_id, "step": step, "batch_len": len(batch)}
        if config.use_research_flag and step > 0 and step % config.eval_every == 0:
            checkpoint["eval"] = {"step": step, "codepath": "shared_infer"}
        if step >= 3:
            break
    return checkpoint
```

## Critical Hyperparameters & Tuning Advice
- **Run ID**: hash of the committed config; never a handwritten nickname that can collide.
- **Mix**: BlendConfig-style weights over live sources; change mid-run by editing config, not rematerializing.
- **Eval every N**: default 100–1000 steps as in Poolside's published practice; same infer codepath as serving.
- **Promote**: `use_research_flag` (or equivalent) is how a win ships. Do not fork the trainer.
- **Scheduler**: do not stand up FoundationDB/Volcano/NCCL P2P until trainer and infer are actually on separate GPU pools for online RL.
- **Query-conditioned item scoring (optional)**: Bergson (`method:bergson`) / TrackStar (`method:trackstar`) can rank training sequences or tokens against a query eval (`bergson score`, LESS-style). Complementary to AutoMixer mix-weight search: AutoMixer searches source ratios; Bergson scores items for one query. Not a mix-recipe SOTA and not a factory-process SOTA. Skip until you have a query behavior to attribute.
