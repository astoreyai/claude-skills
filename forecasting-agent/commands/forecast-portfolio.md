# Forecast Portfolio

**Command**: `/forecast-portfolio`
**Category**: Financial Analysis
**Agent**: forecasting-agent

## Description

Run 3-year baseline portfolio projection with quarterly tax extraction.

## Usage

```bash
/forecast-portfolio
```

**Optional flags**:
```bash
/forecast-portfolio --years 5                    # 5-year projection
/forecast-portfolio --scenario aggressive        # Aggressive scenario
/forecast-portfolio --no-tax                     # No tax extraction
```

## What It Does

1. Load configuration from `PORTFOLIO_PARAMETERS_COMPLETE.yaml`
2. Run 3-year projection with baseline parameters (18.5 trades/month)
3. Calculate monthly compounding with 3.58% per trade
4. Extract 37% quarterly tax reserves
5. Generate monthly and quarterly summaries
6. Export CSV files
7. Generate markdown report

## Output

**Files Created**:
- `forecast_baseline_3y_monthly.csv`
- `forecast_baseline_3y_quarterly.csv`
- `portfolio_forecast_YYYYMMDD.md`

**Summary Displayed**:
```
✓ 3-Year Baseline Projection Complete

Final Balance: $3,200,000,000,000 ($3.2T)
Tax Reserves: $800,000,000,000 ($800B)
Liquid Net Worth: $4,000,000,000,000 ($4.0T)

Total Gains: $3,199,992,000,000
Total Deposits: $18,000
ROI: 159,999,500%
```

## Scenarios

- `conservative`: 17 trades/month → $666.8B (3 years)
- `baseline`: 18.5 trades/month → $3.2T (3 years)
- `aggressive`: 20 trades/month → $21T (3 years)

## Notes

- Projections assume perfect execution (no slippage)
- Win rate maintained at 90%
- 5% stop-loss enforced on all positions
- Monthly deposits of $500 continue
- Tax reserves extracted quarterly

## See Also

- `/forecast-5year` - Extended 5-year analysis
- `/forecast-monte-carlo` - Probabilistic simulation
- `/forecast-sensitivity` - Parameter sensitivity analysis
