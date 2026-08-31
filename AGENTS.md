# AGENTS.md: Autonomous Agent Operating Guide for `j8ckfi/library`

This document provides exact instructions for autonomous training and research agents interacting with `j8ckfi/library`.

---

## 1. What This Library Is

`j8ckfi/library` is a machine-readable and human-navigable knowledge graph of current (2025–2026) state-of-the-art machine learning training methods, papers, and code recipes.

When you are asked to **"train model X to do Y"**, **do not rely on outdated pre-training knowledge**. Query this library to determine:
1. What the current date-stamped SOTA method is.
2. What empirical claims, benchmarks, and baselines substantiate it.
3. What primary paper authored the technique.
4. What exact runnable PyTorch/JAX recipe and dependencies execute it.

---

## 2. Agent Routing Cheat-Sheet (First-Hop SOTA Index)

Use this quick-routing table as of **2026-08-31**:

```
task: pretrain dense 7B optimizer  -> muon2 (2604.09967) + kl-soap (2607.20548) if memory allows
task: budget ~1.5-2B dense pretrain on consumer GPUs -> puro-2b (2608.27370); NOT olmo-3 7B, NOT muon2+kl-soap
task: open data recipe             -> olmo-3 / dolma-3 (2512.13961)
task: pretrain MoE architecture    -> deepseek-v4 (2606.19348) + kimi-k3 (2607.24653)
task: train MoE on NVL72        -> mixture-of-kittens (MoK megakernel, 1070 tok/s/GPU on GB300 NVL72)
task: instruct SFT                 -> olmo-3 dolci (2512.13961); industrial alt nemotron-cascade-2 (2603.19220)
task: math/code RL, dense          -> cispo (minimax-m1 2506.13585 + scalerl 2510.13786)
task: math/code RL, Pass@K / coverage / no-backward -> es-reasoning (2608.27351); Pass@1 default remains cispo
task: math/code RL, MoE/VL         -> sapo (2511.20347); gspo only if Qwen3.5-Omni Talker
task: agentic async RL             -> sao (2607.07508)
task: all-zero verifier groups     -> verigate (2605.30451)
task: LoRA quality 24GB            -> vanilla LoRA + rsLoRA + LR sweep (2602.04998, 2601.22708) NOT DoRA
task: LoRA must 4-bit              -> aqlora-q (2608.23816) or autoqra (2602.22268)
task: full-param mem pretrain      -> scale (2506.16659) not galore
task: native 1.58-bit pretrain     -> sparse-bitnet (2603.05168); keep 2B4T as dense cite
task: ternary an existing SOTA LLM -> scaleq-1.58 (2608.01078)
task: FP4 hardware train           -> quartet-ii nvfp4 (2601.22813) / mxfp4 (2605.09825) / kimi-k3 QAT
task: distill student              -> opd 2604.13016 (single-teacher) / open-mopd 2608.19098 (multi-teacher)
task: SNN sequence/SSM             -> longspike (2606.12895); train with a2sg (2606.11236); silif stays as speech-neuron cite
task: continuous control           -> efficienttdmpc (2605.16692) family; dream-mpc (2605.04568) gradient planner
task: neural video GPU             -> dcvc-uf (2606.04410)
task: neural video deploy          -> mlvc (2606.28027)
task: distill a reasoner (OPD+RLVR)-> opdvr (2608.24696)
task: token-level advantages (1/p) -> bpco (2608.23566)
task: posttrain diffusion          -> diffusion-opsd (2608.24646); no task-specific teacher (flow) -> self-opd (2608.26872)
task: video MLLM RL                -> orarl (2608.20492)
task: label-free TTT / no-GT test-time reasoner -> ttpo (2608.27448)
task: unlabeled math reasoner posttrain (no GT) -> u-opsd (2608.06296)
task: privileged-teacher OPSD / gold-solution self-distillation -> vista (2608.28306)
task: data-free self-evolution incl. unverifiable -> j-zero (2608.26582)
task: SAE dictionary               -> sasa (2606.06333) KEEP
task: SAE circuits                 -> circuitsteer (2608.05732)
task: SAE effect geometry          -> fega (2607.24645)
task: operator, regular-grid PDE     -> cvit / poseidon-finetune; fno is baseline only
task: operator, industrial CAD mesh  -> transolver-3 (2602.04940); alts ab-upt / geotransolver / domino
task: operator, pretrained foundation-> poseidon (2405.19101) or unisolver (2405.17527); fine-tune when PDE family shifts
task: operator, physics-informed     -> pi-cvit (2606.06164) + SOAP; not a 2021 PINN
task: operator, Fourier LoRA/adapt   -> f-adapter (2509.23173) NOT vanilla LoRA
task: operator, weather/climate      -> fourcastnet-3 (2507.12144) (forecast cousin, not CAE)
task: industrial model-building / factory -> poolside-model-factory (Laguna 2605.27605). Process default, not a train-kernel default. Small lab: configs-as-code + Dagster lineage + streamed mixes; skip custom scheduler. CISPO/Muon stay the train defaults. [2026-08-31]
task: directed SSSP distances, sparse, comparison-addition -> BMSSP; need vertex order or typical n -> Dijkstra
```

---

## 3. SOTA Map (What You Actually Pick Today — 2026-08-31)

1. **Train a ~7B dense LM from scratch**: Use **Muon2** (`method:muon2`, `paper:muon2` `arXiv:2604.09967`) with **KL-SOAP** (`method:soap-muon-scale`, `paper:soap-muon-scale` `arXiv:2607.20548`) if GPU memory allows. Keep embeddings / `lm_head` on AdamW. Data: **OLMo-3 / Dolma-3** open data recipe (`method:olmo-3`, `paper:olmo-3` `arXiv:2512.13961`).
2. **Pretrain an MoE architecture**: Use **DeepSeek-V4** (`method:deepseek-v4`, `paper:deepseek-v4` `arXiv:2606.19348`) with **Kimi-K3** (`method:kimi-k3`, `paper:kimi-k3` `arXiv:2607.24653`) as co-default.
3. **SFT a chat / instruct model**: **OLMo-3 Dolci stack** (`method:olmo-3`, `paper:olmo-3` `arXiv:2512.13961`); industrial alternative **Nemotron-Cascade 2** (`method:nemotron-cascade-2`, `paper:nemotron-cascade-2` `arXiv:2603.19220`).
4. **RL a reasoner (math/code, verifiable)**: For dense models, use **CISPO** (`method:cispo`, MiniMax-M1 `paper:minimax-m1` `arXiv:2506.13585` + ScaleRL `paper:scalerl` `arXiv:2510.13786`). For MoE and Vision-Language models, use **SAPO** (`method:sapo`, `paper:sapo` `arXiv:2511.20347`, ms-swift `loss_type=sapo`); use **GSPO** (`method:gspo`) only for Qwen3.5-Omni Talker (`paper:qwen35-omni` `arXiv:2604.15804`). Gate process supervision with **VeriGate** (`method:verigate`, `paper:verigate` `arXiv:2605.30451`).
5. **Agentic async RL**: Use **SAO** (`method:sao`, `paper:sao` `arXiv:2607.07508`) for asynchronous environment and tool-use reinforcement learning.
6. **LoRA a local model on 24GB**: Quality default is **Vanilla LoRA + rsLoRA + LR sweep** (`method:lr-matters-lora`, `paper:lr-matters-lora` `arXiv:2602.04998`, `paper:lora-unified-study` `arXiv:2601.22708`) — NOT DoRA. If memory must fit on a 4-bit stack, use **AQLoRA-Q** (`method:aqlora-q`, `paper:aqlora` `arXiv:2608.23816`) or **AutoQRA** (`method:autoqra`, `paper:autoqra` `arXiv:2602.22268`). For memory-efficient full-parameter pretraining, use **SCALE** (`method:scale`, `paper:scale` `arXiv:2506.16659`, ICML 2026) — not GaLore.
7. **Extreme compression / on-device**: For native 1.58-bit pretraining from scratch, use **Sparse-BitNet** (`method:sparse-bitnet`, `paper:sparse-bitnet` `arXiv:2603.05168`); keep 2B4T (`paper:bitnet-b158`) as dense citation. For post-training ternarization of existing pre-trained LLMs, use **ScaleQ-1.58** (`method:scaleq-158`, `paper:scaleq-158` `arXiv:2608.01078`). For native FP4 hardware training, use **Quartet-II NVFP4** (`method:quartet-ii`, `paper:quartet-ii` `arXiv:2601.22813`) or **MXFP4** (`method:mxfp4-mi355x`, `paper:mxfp4-mi355x` `arXiv:2605.09825`) / Kimi-K3 QAT.
8. **Distill a student from a teacher**: Use **OPD** (`method:opd`, `paper:opd` `arXiv:2604.13016`) for single-teacher distillation and **Open-MOPD** (`method:open-mopd`, `paper:open-mopd` `arXiv:2608.19098`) for multi-teacher distillation.
9. **Train a spiking neural net (SNN)**: Use **LongSpike** (`method:longspike`, `paper:longspike` `arXiv:2606.12895`) for SSM-SNN sequence modeling; train with **A2SG** (`method:a2sg`, `paper:a2sg` `arXiv:2606.11236`) adaptive surrogate gradients. SiLIF (`method:silif`) stays as speech-neuron citation.
10. **Learned control / world-model RL**: Use **EfficientTDMPC** (`method:efficienttdmpc`, `paper:efficienttdmpc` `arXiv:2605.16692`) family; **Dream-MPC** (`method:dream-mpc`, `paper:dream-mpc` `arXiv:2605.04568`, ICML 2026) gradient planner.
11. **Neural video compression**: For GPU neural video, use **DCVC-UF** (`method:dcvc-uf`, `paper:dcvc-uf` `arXiv:2606.04410`). For deployable edge/mobile neural video, use **MLVC** (`method:mlvc`, `paper:mlvc` `arXiv:2606.28027`). DCVC-RT (`method:dcvcrt`) stays as 2025 realtime reference.
12. **Mechanistic interpretability & SAEs**: Dictionary default is **SASA** (`method:sasa`, `paper:sasa` `arXiv:2606.06333`) KEEP. For SAE circuits and steering, use **CircuitSteer** (`method:circuitsteer`, `paper:circuitsteer` `arXiv:2608.05732`). For SAE effect geometry, use **FEGA** (`method:fega`, `paper:fega` `arXiv:2607.24645`).
13. **Train an MoE on NVL72 / systems megakernel**: Use **Mixture-of-Kittens** (`method:mixture-of-kittens`, `paper:mixture-of-kittens`, `recipe:mixture-of-kittens`) for fused dispatch + SwiGLU + combine on Blackwell GB200/GB300 NVL72 racks.
14. **Distill a reasoner with verifiable reward (OPD + RLVR)**: Use **OPDVR** (`method:opdvr`, `paper:opdvr` `arXiv:2608.24696`) for zero-extra-hyperparameter ReLU correctness gating.
15. **Token-level advantages from 1 sample/prompt**: Use **BPCO** (`method:bpco`, `paper:bpco` `arXiv:2608.23566`) actor-critic optimization with DPPO, bounded value head, MC targets, and length-adaptive GAE.
16. **Diffusion post-training & reward alignment**: Use **DiffusionOPSD** (`method:diffusion-opsd`, `paper:diffusion-opsd` `arXiv:2608.24646`) for on-policy self-distillation with bounded intermediate clean-output targets; use **Self-OPD** (`method:self-opd`, `paper:self-opd` `arXiv:2608.26872`) for teacher-free flow matching multi-objective alignment.
17. **Video MLLM reinforcement learning**: Use **OraRL** (`method:orarl`, `paper:orarl` `arXiv:2608.20492`) for annotation-as-rollout with decoupled baseline and sign-balanced pruning without CoT overhead.
18. **Label-free test-time reasoning (TTT)**: Use **TTPO** (`method:ttpo`, `paper:ttpo` `arXiv:2608.27448`) for asymmetric test-time policy optimization (agreeing rollout OPSD + disagreeing rollout Grouped RL).
19. **Unlabeled math reasoner post-training (no GT)**: Use **u-OPSD** (`method:u-opsd`, `paper:u-opsd` `arXiv:2608.06296`) for unsupervised on-policy self-distillation via rollout consensus pseudo-solutions and disagreement targeting.
20. **Neural operators for regular-grid PDEs**: Use **CViT** (`method:cvit`, `paper:cvit` `arXiv:2405.13998`, ICLR 2025) Continuous Vision Transformer; alternatively **Poseidon** (`method:poseidon`, `paper:poseidon` `arXiv:2405.19101`) fine-tuned for the target PDE family. FNO (`method:fno`) remains a classical baseline.
21. **Neural operators for industrial CAD meshes & 3D CFD**: Use **Transolver-3** (`method:transolver-3`, `paper:transolver-3` `arXiv:2602.04940`, ICML 2026) for >160M cell geometries (DrivAerML / AhmedML / NASA-CRM). Industrial alternatives: **AB-UPT** (`method:ab-upt`, `paper:ab-upt` `arXiv:2502.09692`), **GeoTransolver** (`method:geotransolver`, `paper:geotransolver` `arXiv:2512.20399`), and **DoMINO** (`method:domino`, `paper:domino` `arXiv:2501.13350`). GAOT (`method:gaot`) is active but not industrial default (lost on DrivAerML surface pressure 34.00 vs 3.71). Honest gaps: shocks, long chaotic rollouts, out-of-family geometry, stationary-aero-mostly.
22. **Pretrained foundation neural operators**: Use **Poseidon** (`method:poseidon`, `paper:poseidon` `arXiv:2405.19101`) scOT SwinV2 foundation model or **Unisolver** (`method:unisolver`, `paper:unisolver` `arXiv:2405.17527`, ICML 2025) PDE-conditional transformer. Fine-tune when PDE family shifts.
23. **Physics-informed neural operators (little/no labeled data)**: Use **PI-CViT** (`method:pi-cvit`, `paper:pi-cvit` `arXiv:2606.06164`) with GradNorm balancing, causal temporal weighting, and SOAP second-order optimizer — not a 2021 PINN / PINO.
24. **Parameter-efficient fine-tuning for Fourier operators**: Use **F-Adapter** (`method:f-adapter`, `paper:f-adapter` `arXiv:2509.23173`, NeurIPS 2025) with ~2% trainable parameters. Hard rule: do NOT use vanilla LoRA on Fourier latent operators due to depth-amplified spectral error floors.
25. **Global weather & climate forecasting neural operators**: Use **FourCastNet 3** (`method:fourcastnet-3`, `paper:fourcastnet-3` `arXiv:2507.12144`) spherical convolutional neural operator with calibrated probabilistic ensembles (weather forecasting engine, not CAD mesh CAE).
26. **Industrial model-building / factory process**: Use **Poolside Model Factory** (`method:poolside-model-factory`, `paper:laguna-m1-xs2` `arXiv:2605.27605`). Process default, not a train-kernel default. Small lab: experiments-as-code + Dagster lineage + streamed mixes; skip custom FoundationDB scheduler / NCCL P2P / AutoMixer swarms / Titan megakernel. CISPO and Muon stay the train defaults (Laguna ran those on the factory stack).
27. **Privileged-teacher OPSD / gold-solution self-distillation**: Use **VISTA** (`method:vista`, `paper:vista` `arXiv:2608.28306`) when a same-size teacher is privileged with a gold reference solution and a deterministic outcome verifier. Keeps the OPSD student update and adapts the teacher on verified rollouts at top-k teacher-first KL positions. Does **not** replace `method:opd` (single-teacher student distillation), `method:open-mopd` (multi-teacher), `method:opdvr` (OPD+RLVR), `method:cispo` (dense RLVR), or `method:u-opsd` (unlabeled/no-GT).
28. **Data-free self-evolution (verifiable and unverifiable)**: Use **J-Zero** (`method:j-zero`, `paper:j-zero` `arXiv:2608.26582`) for Challenger-Solver-Judge co-evolution from zero external data. Judge co-adapts from loop-structure preference pairs (role-asymmetry and subtask-amplification), not from its own scores. Does **not** replace `method:u-opsd` (unlabeled existing math problems), `method:ttpo` (test-time), or `method:cispo` / `method:sapo` / `method:sao` (labeled/agentic RL). GRPO here is the inner self-play optimizer, not the library's math/code RLVR default.
29. **Budget ~1.5-2B dense pretrain on consumer GPUs**: Use **Puro-2B** (`method:puro-2b`, `paper:puro-2b` `arXiv:2608.27370`) for Qwen3-1.7B-arch ~2B from scratch on RTX 5090 (blockwise FP8, MuonH, CMA, Kaiyuan-Spark). Does **not** replace `method:muon2` + KL-SOAP as the 7B optimizer default, `method:olmo-3` as the open 7B/instruct data recipe, or `method:quartet-ii` as NVFP4. FP8 here is blockwise E4M3/MXFP8, not NVFP4.
30. **Math/code RLVR for Pass@K / coverage / no-backward**: Use **ES-reasoning** (`method:es-reasoning`, `paper:es-reasoning` `arXiv:2608.27351`) one-point z-scored ES. Default when labels exist and the goal is Pass@1 remains **CISPO**. This is not a GRPO revival.
31. **Directed SSSP distances (sparse, comparison-addition)**: Use **BMSSP** (`method:bmssp`, `paper:sorting-barrier-sssp` `arXiv:2504.17033`) for \(O(m\log^{2/3}n)\) distances, not vertex order. Need the distance order or typical \(n\) → **Dijkstra** (`method:dijkstra`). Not an ML training method; do not use for train-dense, MoE, CISPO, Muon, or OLMo.

---

## 4. Supersedes Edges & Lineage

The knowledge graph encodes the following explicit supersession relationships:
- `muon2` supersedes `muon` and `muon-scalable` (2502.16982) as what to implement.
- `olmo-3` supersedes `olmo-2` (2501.00656) and `tulu3-rlvr` (2411.15124) for open instruct and data recipes.
- `deepseek-v4` supersedes `deepseek-v3` as architecture template; `kimi-k3` remains co-default.
- `cispo` supersedes `dapo` as dense RL default (`dapo` stays as systems paper).
- `sapo` supersedes `gspo` as Qwen MoE/VL algorithm.
- `sao` supersedes `group-GRPO` / `grpo` for agentic async RL.
- `opd` (2604.13016) supersedes `on-policy-distillation` / `gkd` as the distill cite.
- `aqlora-q` supersedes `qlora` as speed/recipe default on 4-bit stack.
- `lr-matters-lora` (2602.04998) supersedes `dora` and `delora` as quality default.
- `scale` (2506.16659) supersedes `galore` for mem-efficient pretrain.
- `sparse-bitnet` (2603.05168) supersedes `bitnet-b158` as the 2026 BitNet line (keep 2B4T as downloadable dense cite).
- `longspike` (2606.12895) supersedes `silif` as SSM-SNN default (`silif` stays speech-neuron).
- `efficienttdmpc` (2605.16692) supersedes `td-mpc2`.
- `dcvc-uf` (2606.04410) supersedes `dcvcrt` as GPU NVC; `mlvc` (2606.28027) supersedes `dcvcrt` as deployable NVC.
- `a2sg` (2606.11236) supersedes static `surrogate-gradient-snn`.
- `sasa` (2606.06333) supersedes `gated-sae` and `standard-sae` vector SAEs.
- `transolver-3` (2602.04940) supersedes `transolver` (2402.02366) and `transolver-pp` (2502.02414) as the industrial mesh default (`transolver` and `transolver-pp` stay active).
- `pi-cvit` (2606.06164) supersedes `pino` (2111.03794) as physics-informed operator default.
- `fourcastnet-3` (2507.12144) supersedes `sfno` (2306.03838) as spherical weather operator default.
- `vista` (2608.28306) improves vanilla OPSD (Zhao et al. 2601.18734) in the privileged-teacher setting (same-size teacher that sees the gold solution). VISTA does not supersede `opd`, `open-mopd`, `opdvr`, `cispo`, or `u-opsd`.
- `j-zero` (2608.26582) is the first-hop for data-free self-evolution covering unverifiable domains. It does not supersede `u-opsd`, `ttpo`, `cispo`, `sapo`, or `sao`. R-Zero / G-Zero are paper baselines, not graph nodes.
- `puro-2b` (2608.27370) is the first-hop for ~1.5-2B consumer-GPU / tight-budget dense pretrain. It does not supersede `muon2`, `olmo-3`, or `quartet-ii`. MuonH is a documented Muon/Muon2-family variant; Muon2's `sota_for` is unchanged.
- `es-reasoning` (2608.27351) is the first-hop for Pass@K / reasoning coverage / no-backward RLVR. It does not supersede `cispo`. GRPO stays retired.
- `bmssp` (2504.17033) supersedes `dijkstra` for directed SSSP *distances* in the comparison-addition model on sparse graphs; Dijkstra remains the practical default and is optimal if the vertex distance *order* is required.

---

## 5. Fast Navigation Paths (Hops)

The graph connects concepts across 4 node types:
- **`task:<slug>`** (Problem / Benchmark)
- **`method:<slug>`** (Algorithm / Architecture / Optimizer)
- **`paper:<slug>`** (Literature / arXiv reference)
- **`recipe:<slug>`** (Executable PyTorch/JAX implementation)

Canonical query paths:
```
[User Request] "Train an LLM with RL reasoning"
   │
   ▼
1. Query Task: task:math-code-rl-dense
   │
   ▼
2. Resolve SOTA Method: method:cispo (Clipped IS-weight Policy Optimization)
   │
   ├──► 3. Inspect Literature: paper:minimax-m1 / paper:scalerl
   │
   └──► 4. Load Runnable Code: recipe:cispo
```

---

## 6. Querying the Library via CLI

The library provides a zero-dependency CLI (`python -m library`):

### 6.1 Resolving SOTA for a Task or Domain
```bash
# Look up canonical SOTA method, claims, paper, and recipe for pretraining
python -m library sota "pretrain dense 7B"

# Direct task ID lookup
python -m library sota "task:math-code-rl-dense"

# Structured JSON output for agent tools
python -m library sota "task:parameter-efficient-fine-tuning" --json
```

### 6.2 Searching the Graph
```bash
# Keyword query across all nodes
python -m library query "muon2"

# Filter by node type or domain
python -m library query "quantization" --type method
python -m library query "longspike" --domain snn

# Filter only active SOTA nodes
python -m library query "distillation" --sota-only --json
```

### 6.3 Reading Node Content & Walking Neighbors
```bash
# Display node markdown body and metadata
python -m library show "method:cispo"

# Inspect connected edges (papers, tasks, recipes, supersedes)
python -m library walk "method:muon2"

# Find path between any two graph nodes
python -m library path --from "task:pretrain-dense-7b" --to "recipe:muon2-pretraining"
```

---

## 7. What "SOTA" Means in This Library

In this library, **SOTA is not a vibe or marketing label**. A method is labeled `status: sota` only when:
1. **Date-stamped**: An explicit `as_of: "YYYY-MM-DD"` or claim date exists.
2. **Benchmark-grounded**: Measured against specific competitive baselines on established benchmarks.
3. **Verifiable**: Contains link to verified literature and reproducible recipes.

---

## 8. Ingesting a Paper (5-Minute Recipe)

1. **Scaffold the templates**:
   ```bash
   python -m library new paper <paper-slug> --title "Paper Title"
   python -m library new method <method-slug> --title "Method Name"
   python -m library new recipe <recipe-slug> --title "Recipe Title"
   ```

2. **Populate metadata**:
   - `paper:<paper-slug>`: arXiv ID, authors, publication date, abstract summary, contributions.
   - `method:<method-slug>`: status, sota_for, supersedes, claims with metric & date, mathematical overview, gotchas.
   - `recipe:<recipe-slug>`: hardware, framework, pip dependencies, runnable code snippet.

3. **Handle Supersession**:
   - If the new method supersedes an older method `method:old-method`, edit `graph/methods/old-method.md`:
     - Change `status: superseded` (or `active`)
     - Add `superseded_by: method:<new-slug>`
   - Update the parent task in `graph/tasks/<task-slug>.md`: update `current_sota`.

4. **Validate**:
   ```bash
   python -m library validate
   ```
   Every PR must pass validation with 0 errors.
