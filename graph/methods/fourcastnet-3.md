---
id: method:fourcastnet-3
type: method
title: FourCastNet 3 (Spherical Weather Neural Operator)
category: neural-operator
status: sota
sota_for:
- task:operator-weather
supersedes:
- method:sfno
papers:
- paper:fourcastnet-3
recipes:
- recipe:fourcastnet-3
claims:
- benchmark: ERA5 0.25° Global 6-Hourly Forecast / WeatherBench 2
  metric: RMSE, ACC & ensemble CRPS up to 10-day lead time
  value: SOTA geometric spherical weather operator with calibrated probabilistic ensembles
  baseline: FourCastNet 1 / Spherical FNO (SFNO) / GraphCast
  date: '2026-08-28'
  verified: true
  notes: 'Spherical convolutional operator for global atmospheric forecasting; note:
    forecast engine, not mesh CAE.'
tags:
- scientific-ml
- neural-operator
- weather-forecasting
- fourcastnet-3
- sota
---

# FourCastNet 3 (Spherical Weather Neural Operator)

## Method Overview
FourCastNet 3 provides high-resolution probabilistic global weather prediction:
1. **Spherical Geometric Convolutions**: Operates on global 0.25° latitude-longitude grids with spherical harmonic and geometric convolutions.
2. **Probabilistic Ensembles**: Generates calibrated ensemble forecasts capturing atmospheric uncertainty across 10-day lead times.

Note: FourCastNet 3 is a planetary weather forecast engine, not a 3D CAD mesh CAE surrogate.

## Supersession
- Supersedes `method:sfno` (2306.03838) as the spherical global weather operator default.
