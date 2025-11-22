# Kymera Mean-Reversion Optimizer

Continuously optimizes mean-reversion strategy parameters based on real performance data. Identifies winning patterns and recommends parameter adjustments.

## Capabilities

- **Performance Analysis**: Analyze MR trade results and identify patterns
- **Win Rate Optimization**: Detect entry quality degradation
- **Parameter Tuning**: Recommend VWAP thresholds, stop-loss levels, profit targets
- **Symbol Selection**: Identify best-performing symbols
- **Portfolio Alignment**: Validate correlation with portfolio system

## Use Cases

1. **Analyze MR Performance**
   ```
   /kymera-mr-optimizer analyze
   ```

2. **Generate Optimization Report**
   ```
   /kymera-mr-optimizer report
   ```

3. **Validate System Alignment**
   ```
   /kymera-mr-optimizer check-alignment
   ```

## Key Parameters

- Win rate (target: ≥50%)
- Profit factor (target: ≥1.2)
- VWAP band threshold (1.5σ - 2.5σ)
- Stop-loss level (-2% to -4%)
- Profit targets (0.5% - 2%)
- Position sizing (Kelly-based)

## Integration

Works with:
- Strategy-to-portfolio integrator
- Portfolio-to-strategy converter
- Unified dashboard
- Risk adjuster

## Author

Aaron Storey | Kymera Strategy (Nov 2025)
