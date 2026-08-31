---
id: task:directed-sssp-nonneg
type: task
title: "Directed Single-Source Shortest Paths (Non-Negative Real Weights)"
domain: "algorithms"
summary: "Compute distances from a source to all vertices on a directed graph with real non-negative edge weights in the comparison-addition model. The output is the distance vector, not a total order of vertices by distance."
current_sota:
  - method: method:bmssp
    as_of: "2026-08"
    benchmark: "Directed SSSP, real non-negative weights, comparison-addition model"
    metric: "worst-case time"
    value: "O(m log^{2/3} n)"
    notes: "First break of Dijkstra's O(m + n log n) on sparse directed graphs. Distances only; Dijkstra remains optimal if the vertex order is required, and remains the practical default for typical n."
methods:
  - method:bmssp
  - method:dijkstra
tags:
  - algorithms
  - graph-algorithms
  - sssp
  - directed-graphs
  - comparison-addition
  - bmssp
---

# Directed Single-Source Shortest Paths (Non-Negative Real Weights)

## Problem Definition
Given a directed graph \(G=(V,E)\) with \(n=|V|\) vertices, \(m=|E|\) edges, a source \(s\in V\), and a non-negative weight function \(w:E\to\mathbb{R}_{\geq 0}\), compute \(d(v)\) (the shortest-path distance from \(s\) to \(v\)) for every \(v\in V\). The computational model is comparison-addition: only comparisons and additions on edge weights are allowed, each in unit time. The task is the distance vector, not a sort of vertices by \(d(v)\).

This is a classical graph-algorithm problem. It is not an ML training, routing-policy, or geo-location task.

## Evaluation Protocol & Benchmarks
- **Primary metric**: worst-case running time in the comparison-addition model on sparse directed graphs (\(m=\Theta(n)\)).
- **Baseline**: Dijkstra with Fibonacci / relaxed heaps, \(O(m+n\log n)\).
- **Evaluation hazards**: requiring the vertex order by distance re-imposes a sorting lower bound; Haeupler–Hladík–Rozhoň–Tarjan–Tětek (FOCS 2024) show Dijkstra is then optimal. Practical wall-clock on typical \(n\) is a different question from the asymptotic bound.

## SOTA Landscape
- **Theoretical SOTA (as of 2026-08)**: **BMSSP** (`method:bmssp`, Duan–Mao–Mao–Shu–Yin, `arXiv:2504.17033`) deterministic \(O(m\log^{2/3}n)\). First to break Dijkstra on sparse directed graphs; also the first *deterministic* break of \(O(m+n\log n)\) even on undirected graphs (DMSY23 was randomized undirected).
- **Practical default**: **Dijkstra** (`method:dijkstra`). Use Dijkstra when you need the distance order, when \(n\) is typical, or when you want a production shortest-path implementation.
