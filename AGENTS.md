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

Use this quick-routing table as of **2026-09-01**:

<!-- CHEAT-SHEET:START -->
```
task:directed-sssp-nonneg -> method:bmssp (2504.17033, 2026-08)
task:1bit-extreme-quantization -> method:sparse-bitnet (2603.05168, 2026-08-26)
task:fp4-hardware-training -> method:quartet-ii (2601.22813, 2026-08-26) + method:mxfp4-mi355x (2605.09825, 2026-08-26)
task:post-training-ternary-quantization -> method:scaleq-158 (2608.01078, 2026-08-26)
task:continuous-control-world-model -> method:efficienttdmpc (2605.16692, 2026-08-26) + method:dream-mpc (2605.04568, 2026-08-26)
task:visuomotor-servo-control -> method:td-mpc2 (2310.16828, 2026-08-26)
task:posttrain-diffusion -> method:diffusion-opsd (2608.24646, 2026-08-27) + method:self-opd (2608.26872, 2026-08-28)
task:4bit-peft-quantization -> method:aqlora-q (2608.23816, 2026-08-26) + method:autoqra (2602.22268, 2026-08-26)
task:full-lowbit-finetune -> method:gradcodes (2608.30908, 2026-09-01)
  when memory must fit a 4-bit stack but a mixed-precision adapter at inference is acceptable -> task:4bit-peft-quantization
  when native FP4 forward/backward hardware training from scratch -> task:fp4-hardware-training
  when quality LoRA on 24GB without a fully quantized checkpoint constraint -> task:lora-quality-tuning
task:full-param-memory-efficient-pretrain -> method:scale (2506.16659, 2026-08-26)
task:lora-quality-tuning -> method:lr-matters-lora (2602.04998, 2026-08-26)
task:parameter-efficient-fine-tuning -> method:lr-matters-lora (2602.04998, 2026-08-26) + method:aqlora-q (2608.23816, 2026-08-26)
task:mechanistic-interpretability-dictionaries -> method:sasa (2606.06333, 2026-08-26) + method:circuitsteer (2608.05732, 2026-08-26) + method:fega (2607.24645, 2026-08-26)
task:sae-circuits -> method:circuitsteer (2608.05732, 2026-08-26)
task:sae-effect-geometry -> method:fega (2607.24645, 2026-08-26)
task:training-data-attribution -> method:magic (2504.16430, 2026-09-01)
  when mix-ratio search or replacing an open pretrain mix -> task:open-data-recipe
  when SAE dictionaries, circuits, or effect geometry -> task:mechanistic-interpretability-dictionaries
  when factory process / experiments-as-code / lineage -> task:industrial-model-building
task:agentic-async-rl -> method:sao (2607.07508, 2026-08-26)
task:all-zero-verifier-groups -> method:verigate (2605.30451, 2026-08-26)
task:data-free-self-evolution -> method:j-zero (2608.26582, 2026-08-31)
task:direct-preference-alignment -> method:olmo-3 (2512.13961, 2026-08-26)
task:distill-reasoner-verifier -> method:opdvr (2608.24696, 2026-08-27)
task:instruct-sft-alignment -> method:olmo-3 (2512.13961, 2026-08-26) + method:nemotron-cascade-2 (2603.19220, 2026-08-26)
task:label-free-reasoner-posttrain -> method:u-opsd (2608.06296, 2026-08-28)
task:label-free-test-time-reasoner -> method:ttpo (2608.27448, 2026-08-28)
task:math-code-rl-dense -> method:cispo (2506.13585, 2026-08-26)
task:math-code-rl-moe -> method:sapo (2511.20347, 2026-08-26)
task:passk-reasoning-coverage -> method:es-reasoning (2608.27351, 2026-08-31)
task:privileged-teacher-opsd -> method:vista (2608.28306, 2026-08-31)
task:reasoning-rl-alignment -> method:cispo (2506.13585, 2026-08-26) + method:sapo (2511.20347, 2026-08-26)
task:student-distillation -> method:opd (2604.13016, 2026-08-26) + method:open-mopd (2608.19098, 2026-08-28)
task:teacher-free-on-policy-self-adaptation -> method:opsa (2608.31046, 2026-09-01)
  when verifiable labels exist and the goal is Pass@1 RLVR -> task:math-code-rl-dense
  when a strong teacher is available and the goal is intentional distillation -> task:student-distillation
  when unlabeled existing math problems with majority-vote pseudo-solutions -> task:label-free-reasoner-posttrain
  when test-time adaptation on unlabeled queries -> task:label-free-test-time-reasoner
  when zero external problems, including unverifiable domains -> task:data-free-self-evolution
  when flow matching or continuous diffusion post-training -> task:posttrain-diffusion
task:token-level-critic-rl -> method:bpco (2608.23566, 2026-08-27)
task:budget-consumer-pretrain -> method:puro-2b (2608.27370, 2026-08-31)
task:linear-time-sequence-modeling -> method:mamba-2 (2405.21060, 2024-05)
task:llm-pretraining-optimization -> method:muon2 (2604.09967, 2026-08-26)
task:open-data-recipe -> method:olmo-3 (2512.13961, 2026-08-26)
task:pretrain-dense-7b -> method:muon2 (2604.09967, 2026-08-26)
task:pretrain-moe-frontier -> method:deepseek-v4 (2606.19348, 2026-08-26) + method:kimi-k3 (2607.24653, 2026-08-26)
task:operator-foundation -> method:poseidon (2405.19101, 2026-08-28) + method:unisolver (2405.17527, 2026-08-28)
task:operator-fourier-adapt -> method:f-adapter (2509.23173, 2026-08-28)
task:operator-grid-pde -> method:cvit (2405.13998, 2026-08-28) + method:poseidon (2405.19101, 2026-08-28)
task:operator-industrial-mesh -> method:transolver-3 (2602.04940, 2026-08-28)
task:operator-physics-informed -> method:pi-cvit (2606.06164, 2026-08-28)
task:operator-weather -> method:fourcastnet-3 (2507.12144, 2026-08-28)
task:snn-sequence-modeling -> method:longspike (2606.12895, 2026-08-26)
task:spiking-neural-networks-training -> method:longspike (2606.12895, 2026-08-26) + method:a2sg (2606.11236, 2026-08-26)
task:industrial-model-building -> method:poolside-model-factory (2605.27605, 2026-08)
task:train-moe-nvl72 -> method:mixture-of-kittens (2026-08-26)
task:learned-video-compression -> method:dcvc-uf (2606.04410, 2026-08-26) + method:mlvc (2606.28027, 2026-08-26)
task:neural-video-deploy -> method:mlvc (2606.28027, 2026-08-26)
task:neural-video-gpu -> method:dcvc-uf (2606.04410, 2026-08-26)
task:rl-video-mllm -> method:orarl (2608.20492, 2026-08-27)
```
<!-- CHEAT-SHEET:END -->

---

## 3. SOTA Map (What You Actually Pick Today — 2026-09-01)

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
32. **Teacher-free / label-free on-policy self-adaptation**: Use **OPSA** (`method:opsa`, `paper:opsa` `arXiv:2608.31046`) for entropy-adaptive negative advantages on the lowest-logp tokens with no teacher, reward, or hint. Does **not** replace `method:cispo` when labels exist, `method:opd` when a strong teacher is available and intentional distillation is the goal, `method:u-opsd` (consensus pseudo-solutions), `method:ttpo` (test-time), `method:self-opd` (flow matching), `method:vista`, or `method:j-zero`.
33. **RLVR-stable LoRA upgrade candidate**: Use **NoRA** (`method:nora`, `paper:nora` `arXiv:2608.31036`) to rank-normalize LoRA $A$ (or NoRA-init). Status `active`. The 24GB quality default remains **Vanilla LoRA + rsLoRA + LR sweep** (`method:lr-matters-lora`). Do not treat this as a completed supersession.
34. **RLVR token-filter plug-in**: Use **GMTS** (`method:gmts`, `paper:gmts` `arXiv:2608.30632`) to keep top-20% tokens by $|E\cdot\omega|$ on GRPO/DAPO/CISPO-family trainers. Does **not** replace CISPO.
35. **Teacher OPD trajectory filter**: Use **RA-OPD** (`method:ra-opd`, `paper:ra-opd` `arXiv:2608.27960`) to keep trajectories with $(2R-1)G\geq 0$. Modular filter on teacher OPD. Does **not** replace OPD or OPSA. Tension with OPSA's teacher-noise finding is documented, not a supersession.
36. **Hybrid residual / Qwen-style next architecture**: Use **Qwen3.8-Next** (`method:qwen38-next`, `paper:qwen38-next` `arXiv:2608.30320`) as the GDN↔attention + Gated Residual + QSA + Muon/AdamW-split production recipe. Does **not** replace Muon2 as the ~7B optimizer default or DeepSeek-V4 / Kimi-K3 as MoE architecture defaults. FlashQLA is the public kernel.
37. **Communication-efficient MoE layout**: Use **CE-MoE** (`method:ce-moe`, `paper:ce-moe` `arXiv:2608.28511`) to concentrate experts in fewer routed layers (~33% fewer GPU-h at 31.5B in the paper). Layout niche. Does **not** replace DeepSeek-V4 / Kimi-K3.
38. **Fully low-bit fine-tune in code space**: Use **GradCodeS** (`method:gradcodes`, `paper:gradcodes` `arXiv:2608.30908`) when the deployed checkpoint must stay NF4/INT4/MXFP4 with no high-precision adapter. Does **not** replace AQLoRA-Q as 4-bit PEFT default or Quartet-II as NVFP4 hardware training.
39. **Training data attribution (LOO / LDS / query-conditioned scoring)**: Use **MAGIC** (`method:magic`, `paper:magic` `arXiv:2504.16430`) when you control the trainer and need peak LDS. Library: **Bergson** (`method:bergson`, `paper:bergson` `arXiv:2606.11660`, `pip install bergson`) — status `active`, `sota_for: []`, optional factory component like AutoMixer, never mix/kernel/factory SOTA. Small-lab filtering default: **TrackStar** (`method:trackstar`). Does **not** replace CISPO, Muon2, OPD, OLMo-3, Poolside factory, BMSSP, OPSA, or SAE dictionaries.

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
- `opsa` (2608.31046) is the first-hop for teacher-free / label-free on-policy self-adaptation. It does not supersede `cispo`, `opd`, `u-opsd`, `ttpo`, `self-opd`, `vista`, or `j-zero`.
- `nora` (2608.31036) is an active RLVR-stable LoRA upgrade candidate. It does not supersede `lr-matters-lora` as the 24GB quality default.
- `gmts` (2608.30632) is an optional RLVR token-filter plug-in. It does not supersede `cispo`.
- `ra-opd` (2608.27960) is a modular teacher-OPD trajectory filter. It does not supersede `opd` or `opsa`.
- `qwen38-next` (2608.30320) is an adjacent hybrid residual / Qwen-style production architecture recipe. It does not supersede `muon2` or `deepseek-v4` / `kimi-k3`.
- `ce-moe` (2608.28511) is an optional MoE layer-layout niche. It does not supersede `deepseek-v4` / `kimi-k3`.
- `gradcodes` (2608.30908) is the first-hop for fully low-bit code-space fine-tuning. It does not supersede `aqlora-q` or `quartet-ii`.
- `magic` (2504.16430) is the first-hop for `task:training-data-attribution` only (narrow LDS). `bergson` (2606.11660) is the library umbrella and does not supersede MAGIC. Neither retargets CISPO, Muon2, OPD, OLMo-3, factory process, BMSSP, OPSA, or SAE SOTA.

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

The library provides a zero-dependency CLI (`python -m library`). Prefer `sota` / `decide` over `query`. JSON is first-class (`--json`); `--brief` is the ~10-line tier. `graph/INDEX.md` and the §2 cheat-sheet are L3 derived views — regenerate with `index`, never hand-edit them.

### 6.1 Resolving SOTA for a Task or Domain
```bash
# Look up canonical SOTA method, claims, paper, and recipe for pretraining
python -m library sota "pretrain dense 7B"

# Direct task ID lookup (decision-shaped default)
python -m library sota "task:math-code-rl-dense"

# Brief (~10 lines) and structured JSON
python -m library sota "task:math-code-rl-dense" --brief
python -m library sota "task:parameter-efficient-fine-tuning" --json

# Six-question decision: use / instead / do-not-use / gotchas / code / trust
python -m library decide "task:math-code-rl-dense"
python -m library decide "task:math-code-rl-dense" --json
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

### 6.4 Routing, freshness, index, and supersession
```bash
# Rank candidate tasks (scope / out_of_scope / redirects). Never empty without near-misses.
python -m library route "pretrain dense 7B"
python -m library route "pretrain dense 7B" --json

# Freshness queue. Default budget 120 days. Exit 1 if any task current_sota is over budget.
python -m library stale
python -m library stale --max-age-days 120 --json

# Regenerate graph/INDEX.md and this file's §2 cheat-sheet from graph state
python -m library index
python -m library index --json

# Validate: exit 1 only for schema/integrity errors. INDEX.md / cheat-sheet drift is a WARNING (exit 0).
python -m library validate

# Transactional supersession (refuses unless post-conditions hold). --dry-run writes nothing.
python -m library supersede method:new method:old --task task:example --dry-run
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

5. **Write the receipt**: append a one-paragraph audit entry to `graph/CHANGELOG.md` (format in
   [docs/ingestion-guide.md](docs/ingestion-guide.md) §5). A supersession that updates the new method but
   not the old method and its parent task is an **incomplete write** — do not commit it.

---

## 9. Agent Decision Protocol

This section is the operating protocol for any agent driving this library. The full system design — the
abstraction tower, the contracts behind these rules, and the CLI ergonomics roadmap — is in
[docs/system-design.md](docs/system-design.md). Schema extensions (routing guards, evidence levels,
staleness) are in [docs/ontology.md](docs/ontology.md) §4.1.1.

### 9.1 Decision loop

```
1. ROUTE    user request -> task:<slug>. Try the cheat-sheet (§2) first; if no hit or the request
            plausibly sits near a task boundary, check that task's `scope`, `out_of_scope`, and
            `redirects` before resolving. Follow `redirects` mechanically — they encode hard-won
            negative knowledge ("not this scale", "NOT DoRA").
2. RESOLVE  `python -m library sota <task>` or `python -m library decide <task>` -> method + claims + papers + recipes.
3. VERIFY   weight each claim by evidence (verified + evidence_level) and freshness
            (as_of / last_reviewed). If a task's current_sota is older than 4 months, say so in your
            answer and re-check literature before committing an expensive plan.
4. EXECUTE  `python -m library show recipe:<slug>`; check `target_hardware` and `pip_dependencies`
            against the user's actual budget before promising anything.
5. WRITE    if you discovered something the graph lacks: ingest per §8, appending a receipt to
            `graph/CHANGELOG.md`. Ingestion includes the supersession check (§8 step 3).
```

### 9.2 Token discipline

- **Remote first**: if you are working against the GitHub remote (no local clone), fetch the compiled
  graph in one call — `gh api repos/j8ckfi/library/contents/dist/graph.json` (CI keeps it fresh) — and
  fall back to per-node `contents/` fetches only for files you will act on.
- Prefer `sota` / `decide` over `query` (one call returns the whole resolution path); prefer `query --json` for
  scripted filtering; use `show` only on the specific nodes you will act on; use `walk`/`path` only when
  `sota`/`query` leave a genuine traversal question open.
- Never re-derive what a single `validate` can tell you; run it after every write and before reporting
  graph changes.

### 9.3 Trust calibration

- `verified: true` + comparator baseline is the only basis for a default recommendation.
- `evidence_level` ranks claims: `peer-reviewed` > `preprint` > `unofficial-repro` > `self-reported`.
- A `current_sota[].as_of` older than ~4 months means **stale**: the routing may still be right, but the
  rank order deserves a literature re-check before you stake a training run on it.
