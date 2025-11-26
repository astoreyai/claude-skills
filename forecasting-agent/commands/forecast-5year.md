# Forecast 5-Year

**Command**: `/forecast-5year`
**Category**: Financial Analysis
**Agent**: forecasting-agent

## Description

Comprehensive 5-year portfolio analysis with all scenarios, Monte Carlo simulation, and full PDF report generation.

## Usage

```bash
/forecast-5year
```

**Optional flags**:
```bash
/forecast-5year --monte-carlo-paths 5000      # More simulation paths
/forecast-5year --format latex                # LaTeX PDF output
/forecast-5year --no-monte-carlo              # Skip Monte Carlo
```

## What It Does

1. Run 5-year projections for all three scenarios:
   - Conservative (17 trades/month)
   - Baseline (18.5 trades/month)
   - Aggressive (20 trades/month)

2. Execute Monte Carlo simulation:
   - 1,000 paths × 60 months
   - Probabilistic outcome distribution
   - Milestone probability calculations
   - Risk metrics (drawdown, volatility)

3. Comprehensive risk analysis:
   - Maximum drawdown scenarios
   - Monthly volatility
   - Sharpe ratio approximation
   - Sensitivity to parameters

4. Tax forecasting:
   - Quarterly obligations
   - Federal + state breakdown
   - Payment schedules
   - Multi-state comparison

5. Generate professional report:
   - LaTeX PDF (15+ pages)
   - Executive summary
   - Scenario tables
   - Monte Carlo charts
   - Tax planning section
   - Recommendations

## Output

**Files Created**:
- `forecast_conservative_5y_monthly.csv`
- `forecast_conservative_5y_quarterly.csv`
- `forecast_baseline_5y_monthly.csv`
- `forecast_baseline_5y_quarterly.csv`
- `forecast_aggressive_5y_monthly.csv`
- `forecast_aggressive_5y_quarterly.csv`
- `monte_carlo_results.json`
- `portfolio_forecast_5year_YYYYMMDD.pdf`

**Report Sections**:
1. Executive Summary
2. Methodology
3. Scenario Projections
4. Monte Carlo Analysis
5. Risk Analysis
6. Tax Planning
7. Recommendations

## Scenario Results (5-Year)

### Conservative
- Final Balance: $10.8M
- ROI: 33,699%
- Annual Growth: ~5.2x

### Baseline
- Final Balance: $8.98B
- ROI: 447,010,700%
- Annual Growth: ~21.6x

### Aggressive
- Final Balance: $647B
- ROI: 32,289,802,686%
- Annual Growth: ~46.4x

## Monte Carlo Results

**Expected Outcomes** (Baseline, 60 months):
```
Median: $1.01B
95% CI: $36.6M - $11.5B

Milestones:
- $1M: 99.9% probability
- $100M: 96.2% probability
- $1B: 52.3% probability

Risk of Ruin: 0.0%
Avg Max Drawdown: -8.2%
```

## Processing Time

- Projection calculations: ~2 seconds
- Monte Carlo (1,000 paths): ~10 seconds
- LaTeX PDF generation: ~5 seconds
- **Total**: ~15-20 seconds

## Notes

- **Theoretical Upper Bounds**: These projections assume perfect execution
- **Use Monte Carlo**: For realistic probability distributions
- **Tax Reserves Critical**: 37% quarterly extraction required
- **Position Sizing**: Must enforce 10% max (current 75% is unsustainable)

## See Also

- `/forecast-portfolio` - Quick 3-year projection
- `/forecast-monte-carlo` - Monte Carlo only
- `/forecast-tax` - Tax planning focus
