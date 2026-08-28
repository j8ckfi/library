---
id: task:operator-weather
type: task
title: Global Weather & Climate Forecasting Neural Operators
domain: scientific-ml
summary: Global data-driven atmospheric and weather forecasting using spherical and
  geometric neural operators.
current_sota:
- method: method:fourcastnet-3
  as_of: '2026-08-28'
  benchmark: ERA5 0.25° Global 6-Hourly Forecast (10-day lead)
  metric: RMSE, ACC & ensemble CRPS vs IFS
  value: Default SOTA Spherical Weather Operator
  notes: FourCastNet 3 (2507.12144); spherical convolutional operator with geometric
    probabilistic ensemble modeling.
methods:
- method:fourcastnet-3
- method:sfno
tags:
- scientific-ml
- neural-operator
- weather-forecasting
- climate
- fourcastnet-3
---

# Global Weather & Climate Forecasting Neural Operators

## Problem Definition
Data-driven global weather prediction and atmospheric dynamics modeling on spherical domains (ERA5 at 0.25° resolution) across medium-range (10-day) forecast horizons.

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **FourCastNet 3** (`method:fourcastnet-3`, 2507.12144), spherical convolutional neural operator with calibrated probabilistic ensembles (weather forecasting engine, not CAD mesh CAE).
- **Lineage**: **Spherical FNO (SFNO)** (`method:sfno`, 2306.03838).
