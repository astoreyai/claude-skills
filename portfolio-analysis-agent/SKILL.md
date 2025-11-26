# Portfolio Analysis Agent

**Version**: 1.0.0
**Category**: Financial Analysis / Portfolio Management
**Author**: Claude Code
**Last Updated**: November 22, 2025

## Overview

Comprehensive portfolio analysis system integrating historical trade analysis, forward projections, tax planning, and risk assessment into a unified workflow.

## Features

### 1. **Integrated Analysis**
- Historical trade performance
- Forward projections (3-5 years)
- Tax obligation forecasting
- Risk metric calculation
- Edge identification
- Complete portfolio dashboard

### 2. **Trading Analysis**
- Load Interactive Brokers CSV statements
- Calculate win rate, average returns, profit factor
- Time-of-day edge analysis
- Symbol-level performance
- Position sizing audit

### 3. **Forward Projections**
- Multi-year portfolio growth forecasts
- Scenario analysis (conservative/baseline/aggressive)
- Quarterly tax extraction modeling
- Monthly and quarterly breakdowns

### 4. **Tax Planning**
- Quarterly tax obligation calculations
- Federal + state tax breakdown
- Multi-state comparisons (NY vs FL/TX)
- Payment schedule generation
- Tax reserve tracking

### 5. **Risk Analysis**
- Maximum drawdown calculations
- Sharpe ratio approximations
- Volatility metrics
- Position sizing recommendations
- Stop-loss impact analysis

### 6. **Dashboard & Reporting**
- Comprehensive portfolio dashboard (JSON)
- Markdown and LaTeX reports
- CSV exports of all data
- Google Drive integration
- Performance tracking over time

## Usage

### Complete Portfolio Analysis
```bash
/analyze-portfolio <path-to-csv>
```

**Workflow**:
1. Load IB CSV statement
2. Calculate trading metrics
3. Identify trading edge
4. Run 3-year projections
5. Analyze risk
6. Calculate tax obligations
7. Generate comprehensive report

**Output**:
- `portfolio_analysis_YYYYMMDD.md` - Full report
- `portfolio_dashboard_YYYYMMDD.json` - Dashboard data
- `portfolio_trades.csv` - Trade-by-trade export

### Generate PDF Report
```bash
/portfolio-report --format pdf
```

**Output**:
- Professional LaTeX PDF report (15+ pages)
- Executive summary
- Trade analysis
- Edge identification
- Forward projections
- Tax planning
- Risk assessment
- Recommendations

### Track Performance
```bash
/portfolio-track --month 11
```

**What It Does**:
- Compare actual vs projected performance
- Calculate variance
- Identify deviations
- Update baseline assumptions
- Recalibrate projections

### Edge Analysis Only
```bash
/portfolio-edge-analysis
```

**Output**:
- Time-of-day performance breakdown
- Symbol-level profitability
- Intraday vs swing trade comparison
- Best/worst time windows
- Repeatable pattern identification

## Configuration

Uses `PORTFOLIO_PARAMETERS_COMPLETE.yaml`:

```yaml
trading:
  return_per_trade:
    all_time_avg: 3.58
  win_rate:
    actual: 90.0
  trade_frequency:
    trades_per_month:
      baseline: 18.5

account:
  initial_capital: 2000
  monthly_deposits: 500

tax:
  quarterly_extraction_pct: 37.0
```

## Complete Workflow

### Step 1: Load Trading Data
```python
agent.load_trading_csv('U21858510_20250101_20251120.csv')
```

**Parses**:
- Closed positions
- Entry/exit prices and dates
- Commissions
- Realized P&L

### Step 2: Calculate Metrics
```python
metrics = agent.calculate_metrics()
```

**Calculates**:
- Win rate (90%)
- Average return per trade (3.58%)
- Trades per month (18.5)
- Gross profits/losses
- Profit factor

### Step 3: Identify Edge
```python
edge = agent.identify_edge()
```

**Identifies**:
- Best time windows (04:00-05:00 ET, 11:00-12:00 ET)
- Intraday vs swing performance
- Repeatable patterns
- Symbol-level edges

### Step 4: Run Projections
```python
projections = agent.run_projections(years=3)
```

**Projects**:
- Year 1: $5.2M
- Year 2: $50B
- Year 3: $3.2T

### Step 5: Analyze Risk
```python
risk = agent.analyze_risk()
```

**Calculates**:
- Max drawdown: -8.2%
- Sharpe ratio: ~2.5
- Position sizing risk
- Stop-loss impact

### Step 6: Calculate Taxes
```python
taxes = agent.calculate_taxes(state='NY')
```

**Calculates**:
- Federal: 37%
- NY State: 10.75%
- Total: 47.75%
- Quarterly payments

### Step 7: Generate Dashboard
```python
dashboard = agent.generate_dashboard()
```

**Includes**:
- All metrics
- Edge analysis
- Projections
- Risk metrics
- Tax obligations

### Step 8: Generate Report
```python
report_path = agent.generate_report(format='markdown')
```

**Generates**:
- Executive summary
- Complete analysis
- Recommendations
- Action items

## Dashboard Structure

```json
{
  "generated_at": "2025-11-22T10:30:00",
  "account_info": {
    "account": "U21858510",
    "entity": "Kymera Systems LLC"
  },
  "metrics": {
    "total_trades": 10,
    "win_rate": 0.90,
    "avg_return_pct": 0.0358,
    "total_pnl": 283.94
  },
  "edge_analysis": {
    "edge_identified": true,
    "best_window": "premarket_0400_0500",
    "best_window_stats": {
      "trades": 2,
      "win_rate": 100.0,
      "avg_pnl": 79.49
    }
  },
  "projections": {
    "years": 3,
    "final_balance": 3200000000000
  },
  "risk_metrics": {
    "max_drawdown_pct": -8.2,
    "sharpe_ratio": 2.5
  },
  "tax_analysis": {
    "state": "FL",
    "total_tax": 1184000000000
  }
}
```

## Report Sections

### 1. Executive Summary
- Account overview
- Performance highlights
- Key findings
- Critical actions

### 2. Trading Analysis
- Win rate and profit factor
- Average returns
- Trade frequency
- Commission analysis

### 3. Edge Identification
- Time-of-day performance
- Symbol-level analysis
- Intraday vs swing comparison
- Repeatability assessment

### 4. Forward Projections
- 3-year baseline scenario
- Alternative scenarios
- Sensitivity analysis
- Milestone tracking

### 5. Risk Assessment
- Drawdown analysis
- Volatility metrics
- Position sizing review
- Stop-loss recommendations

### 6. Tax Planning
- Quarterly obligations
- Federal + state breakdown
- Payment schedule
- Reserve account strategy

### 7. Recommendations
- Immediate actions
- Risk management improvements
- Tax optimization strategies
- Performance targets

## Integration Points

### With Trading Analysis Agent
```
Trading CSV → Portfolio Analysis → Metrics + Edge
                                 ↓
                      (Feeds to projections)
```

### With Forecasting Agent
```
Metrics → Portfolio Analysis → Projections
                            ↓
                 (Monte Carlo simulations)
```

### With Tax Planning
```
Projections → Portfolio Analysis → Tax Obligations
                                ↓
                    (Quarterly payment schedule)
```

## Example Analysis

### Input
- IB CSV: 10 trades over 28 days
- Initial capital: $2,000
- Current balance: $2,283.94

### Output

**Metrics**:
- Win rate: 90% (9 wins, 1 loss)
- Average return: 3.58% per trade
- Trades/month: 18.5 (baseline)
- Total P&L: $283.94

**Edge Identified**:
- Intraday: 100% win rate, $1,020 profit
- Premarket (04:00-05:00): Best time window
- Recommendation: 100% intraday trading

**Projections (3 years)**:
- Year 1: $5.2M
- Year 2: $50B
- Year 3: $3.2T

**Risk**:
- Max drawdown: -44% (GETY trade without stop)
- With 5% stops: -8.2% max
- Position sizing: 75% avg (should be 10%)

**Tax (FL resident)**:
- Federal only: 37%
- Year 3 tax: $1.184T
- Quarterly reserves required

**Recommendations**:
1. Implement 5% hard stops (critical)
2. Reduce position sizing to 10% max
3. 100% intraday trading (abandon swings)
4. Set up tax reserve account (37% quarterly)

## Performance Tracking

Track actual vs projected monthly:

| Month | Projected | Actual | Variance | Status |
|-------|-----------|--------|----------|--------|
| Jan | $2,500 | $2,284 | -8.6% | On track |
| Feb | $5,000 | — | — | Pending |
| Mar | $10,000 | — | — | Pending |

## Known Limitations

1. **Simplified Projections**: Uses compound factor without full Monte Carlo
2. **CSV Parsing**: May need adjustment for different IB statement formats
3. **Edge Detection**: Requires sufficient historical trades (10+ recommended)
4. **Tax Calculations**: Simplified federal + state (consult CPA for exact)
5. **No Live Integration**: CSV-based, not real-time

## Future Enhancements

- [ ] Real-time performance dashboard
- [ ] Automatic CSV import (scheduled)
- [ ] Interactive charts and visualizations
- [ ] Multi-account aggregation
- [ ] Machine learning edge detection
- [ ] Automated tax form generation (1040-ES)
- [ ] Slack/email alerts for milestones
- [ ] Integration with brokerage APIs

## Troubleshooting

### Issue: CSV parsing fails
**Solution**: Verify IB statement format. Check for "Trades" section with proper columns.

### Issue: No edge identified
**Solution**: Ensure sufficient trade history (10+ trades). Check time format in CSV.

### Issue: Projections seem unrealistic
**Solution**: These are theoretical maximums. Use Monte Carlo for realistic ranges.

### Issue: Tax calculations don't match
**Solution**: Consult CPA for exact calculations. This tool provides estimates only.

## Support

For issues:
1. Check CSV format (most common issue)
2. Verify config YAML structure
3. Review log output for errors
4. Test with smaller datasets first

---

**License**: MIT (Part of astoreyai/claude-skills)
**Repository**: https://github.com/astoreyai/claude-skills/
