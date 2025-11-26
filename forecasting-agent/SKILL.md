# Portfolio Forecasting Agent

**Version**: 1.0.0
**Category**: Financial Analysis / Portfolio Management
**Author**: Claude Code
**Last Updated**: November 22, 2025

## Overview

Advanced portfolio forecasting system with multi-year projections, Monte Carlo simulations, tax planning, and comprehensive risk analysis. Designed for active trading portfolios with frequent position turnover.

## Features

### 1. **Multi-Year Projections**
- 3-year and 5-year forward projections
- Three scenarios: Conservative, Baseline, Aggressive
- Monthly and quarterly breakdowns
- Compound growth modeling
- Tax-adjusted projections

### 2. **Monte Carlo Simulations**
- 1,000+ path simulations
- Probabilistic outcome distributions
- Milestone probability calculations
- Risk of ruin analysis
- Confidence intervals (50%, 95%, 99%)

### 3. **Tax Forecasting**
- Quarterly tax reserve calculations
- Federal + state tax obligations
- Multi-state comparison (NY vs FL/TX)
- Estimated payment schedules
- Tax-optimized withdrawal strategies

### 4. **Risk Analysis**
- Maximum drawdown calculations
- Monthly volatility metrics
- Sharpe ratio approximations
- Sensitivity analysis
- Scenario stress testing

### 5. **Report Generation**
- Professional PDF reports (LaTeX)
- Markdown analysis documents
- CSV data exports
- Interactive dashboards
- Google Drive integration

## Usage

### Quick 3-Year Projection
```bash
/forecast-portfolio
```

**Output**:
- 3-year baseline projection
- Monthly and quarterly breakdowns
- Tax reserve schedules
- Markdown summary report

### Full 5-Year Analysis
```bash
/forecast-5year
```

**Output**:
- 5-year projection (all scenarios)
- Monte Carlo simulation (1,000 paths)
- Risk analysis
- Tax planning
- LaTeX PDF report

### Monte Carlo Only
```bash
/forecast-monte-carlo --paths 1000 --months 60
```

**Output**:
- 1,000 simulation paths
- Percentile distributions
- Milestone probabilities
- Risk metrics

### Sensitivity Analysis
```bash
/forecast-sensitivity --win-rate 80-95 --return 2-5
```

**Output**:
- Win rate impact table
- Return variance analysis
- Parameter sensitivity charts
- Optimal parameter identification

### Tax Forecasting
```bash
/forecast-tax --years 5 --state NY
```

**Output**:
- Quarterly tax obligations
- Federal + state breakdown
- Payment schedule
- Multi-state comparisons

## Configuration

### Parameter File
Location: `~/projects/portfolio/PORTFOLIO_PARAMETERS_COMPLETE.yaml`

**Key Parameters**:
```yaml
trading:
  return_per_trade:
    all_time_avg: 3.58      # % per trade
  win_rate:
    actual: 90.0            # %
  trade_frequency:
    trades_per_month:
      conservative: 17
      baseline: 18.5
      aggressive: 20

account:
  initial_capital: 2000     # $
  monthly_deposits: 500     # $

tax:
  quarterly_extraction_pct: 37.0  # %
```

### Scenarios

#### Conservative (17 trades/month)
- Lower trade frequency
- More defensive posture
- Realistic for part-time trading
- Final balance: $10.8M (5 years)

#### Baseline (18.5 trades/month)
- Historical average
- Sustainable frequency
- Default scenario
- Final balance: $8.98B (5 years)

#### Aggressive (20 trades/month)
- Maximum trade frequency
- Requires full-time focus
- Optimistic projections
- Final balance: $647B (5 years)

## Key Calculations

### Monthly Compounding
```
Monthly Return = (1 + Return_Per_Trade)^Trades_Per_Month - 1

Example (Baseline):
  = (1 + 0.0358)^18.5 - 1
  = 1.9096 - 1
  = 90.96% per month
```

### Tax Reserve Extraction
```
Quarterly Gains = Ending_Balance - Starting_Balance - Deposits
Tax Reserve = Quarterly_Gains × 0.37
Portfolio Retained = Quarterly_Gains × 0.63
```

### Monte Carlo Simulation
```python
for each path:
    for each month:
        for each trade:
            if random() < win_rate:
                balance *= (1 + avg_winner%)
            else:
                balance *= (1 + avg_loser%)
        balance += monthly_deposit
```

## Output Formats

### 1. Monthly Projection CSV
**Columns**:
- Month, Year, Quarter
- Starting Balance, Ending Balance
- Gains This Month
- Tax Extracted (37%)
- Deposit
- Cumulative Gains/Taxes
- Tax Reserve Account

### 2. Quarterly Summary CSV
**Columns**:
- Quarter (Y1Q1, Y1Q2, etc.)
- Starting Balance
- Deposits (3 months)
- Gains, Tax Reserved, Net Gains
- Ending Balance
- Tax Reserve Account

### 3. Monte Carlo Results JSON
**Fields**:
- `final_balance`: {mean, median, std, percentiles}
- `milestones`: {1M, 10M, 100M, 500M, 1B} probabilities
- `risk_metrics`: {risk_of_ruin, prob_profit}
- `all_paths`: Array of all simulation paths

### 4. LaTeX Report (PDF)
**Sections**:
- Executive Summary
- Methodology
- Scenario Projections (tables)
- Monte Carlo Analysis (charts)
- Risk Analysis
- Tax Planning
- Recommendations

## Integration Points

### With Trading Analysis
```
Trading CSV → Edge Analysis → Win Rate / Avg Return
                           ↓
                    (Feed to forecasting)
                    - Use actual metrics
                    - Historical validation
                    - Baseline calibration
```

### With Tax Planning
```
Forecast Results → Quarterly Gains → Tax Obligations
                                  ↓
                        (Generate payment schedule)
                        - 1040-ES forms
                        - Quarterly deadlines
                        - Reserve account
```

### With Portfolio Analysis
```
Forecasts + Actuals → Track Performance → Identify Deviations
                                       ↓
                            (Adjust parameters monthly)
                            - Recalibrate projections
                            - Update assumptions
                            - Revise targets
```

## Assumptions

### Trading Assumptions
- Consistent daily returns at expected average
- Win rate maintained over time (90%)
- No catastrophic losses (5% stops enforced)
- Position sizing controlled (10% max)
- Deposits on schedule ($500/month)

### Market Assumptions
- 20 trading days per month
- No extended market closures
- Liquidity sufficient for all positions
- No systematic regime changes

### Tax Assumptions
- 37% federal reserve adequate
- Quarterly extraction on schedule
- No wash sale violations
- Short-term capital gains treatment

## Limitations

1. **Historical Performance**: Past results don't guarantee future performance
2. **Perfect Execution**: Assumes no slippage or missed trades
3. **No Black Swans**: Doesn't model extreme market events
4. **Linear Scaling**: Assumes edge persists at all capital levels
5. **No Capacity Constraints**: Ignores liquidity limits

## Risk Warnings

### Exponential Growth Projections
- Year 3-5 projections are theoretical upper bounds
- Compounding assumptions may not hold indefinitely
- Market capacity constraints will limit growth
- Regulatory/tax changes not modeled

### Position Sizing Critical
- Current 75% position sizing is unsustainable
- Must reduce to 10% max (per recommendations)
- Single bad trade can wipe out gains
- Risk management discipline essential

### Tax Compliance Required
- Quarterly extraction must be disciplined
- Missing payments incurs penalties
- State tax varies significantly (NY vs FL)
- Professional CPA engagement recommended

## Examples

### Example 1: 3-Year Baseline Projection
**Input**: 18.5 trades/month at 3.58% average return

**Output**:
```
Year 1: $5.2M (from $2K + $6K deposits)
Year 2: $50B
Year 3: $3.2T

Tax Reserves: $800B (extracted quarterly)
Liquid Net Worth: $4.0T (portfolio + reserves)
```

### Example 2: Monte Carlo (1,000 paths, 5 years)
**Input**: Same parameters, 1,000 simulations

**Output**:
```
Median Final Balance: $1.01B
95% Confidence Interval: $36.6M - $11.5B

Milestone Probabilities:
- $1M: 99.9%
- $100M: 96.2%
- $1B: 52.3%

Risk of Ruin: 0.0%
Max Drawdown: -8.2% (average)
```

### Example 3: Tax Comparison (NY vs FL)
**Input**: $5M gains in Year 1

**Output**:
```
Federal Tax: $1.85M (37%)
NY State Tax: $537K (10.75%)
Total (NY): $2.39M (47.75%)

FL/TX Tax: $1.85M (37% federal only)
Tax Savings: $537K by relocating
```

## Troubleshooting

### Issue: Projections seem too high
**Solution**: These are theoretical upper bounds assuming perfect execution. Use Monte Carlo for realistic ranges.

### Issue: Tax reserves insufficient
**Solution**: NY residents should use 45% reserve (not 37%). Adjust `tax.quarterly_extraction_pct` in config.

### Issue: Monte Carlo paths diverge wildly
**Solution**: This is expected with exponential compounding. Focus on median/percentiles, not mean.

### Issue: CSV export fails
**Solution**: Check write permissions to output directory. Default: `~/projects/portfolio/`

## Future Enhancements

- [ ] Drawdown recovery simulations
- [ ] Multi-strategy portfolio allocation
- [ ] Real-time parameter updates from live trading
- [ ] Options strategy forecasting
- [ ] Mean reversion edge modeling
- [ ] Correlation analysis (multi-symbol portfolios)
- [ ] Tax loss harvesting optimization
- [ ] Leverage/margin constraint modeling

## References

### Theory
- Kelly Criterion for position sizing
- Geometric mean vs arithmetic mean in compounding
- Log-normal return distributions
- Tax-adjusted performance metrics

### Tools
- NumPy for Monte Carlo simulations
- Pandas for time series analysis
- PyYAML for configuration
- LaTeX for professional reports

## Support

For issues:
1. Verify YAML config format
2. Check parameter ranges (win rate 0-100%, etc.)
3. Review log output for errors
4. Test with smaller scenarios first

---

**License**: MIT (Part of astoreyai/claude-skills)
**Repository**: https://github.com/astoreyai/claude-skills/
