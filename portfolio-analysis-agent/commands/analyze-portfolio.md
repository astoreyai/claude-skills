# Analyze Portfolio

**Command**: `/analyze-portfolio`
**Category**: Financial Analysis
**Agent**: portfolio-analysis-agent

## Description

Run complete portfolio analysis integrating historical trades, forward projections, tax planning, and risk assessment.

## Usage

```bash
/analyze-portfolio <path-to-csv>
```

**Optional flags**:
```bash
/analyze-portfolio trades.csv --years 5           # 5-year projections
/analyze-portfolio trades.csv --state NY          # NY tax calculations
/analyze-portfolio trades.csv --format latex      # LaTeX report
```

## What It Does

**Complete 8-Step Workflow**:

1. **Load Trading CSV**
   - Parse Interactive Brokers statement
   - Extract closed positions
   - Calculate P&L per trade

2. **Calculate Metrics**
   - Win rate (90%)
   - Average return per trade (3.58%)
   - Trades per month (18.5)
   - Profit factor

3. **Identify Edge**
   - Time-of-day analysis
   - Intraday vs swing performance
   - Symbol-level profitability
   - Repeatable patterns

4. **Run Projections**
   - 3-year baseline forecast
   - Monthly compounding
   - Quarterly tax extraction
   - Year-by-year breakdown

5. **Analyze Risk**
   - Maximum drawdown
   - Monthly volatility
   - Sharpe ratio
   - Position sizing audit

6. **Calculate Taxes**
   - Quarterly obligations
   - Federal + state breakdown
   - Payment schedule
   - Reserve requirements

7. **Generate Dashboard**
   - JSON with all metrics
   - Edge analysis results
   - Projection summaries
   - Risk metrics

8. **Generate Report**
   - Markdown or LaTeX
   - Executive summary
   - Detailed analysis
   - Recommendations

## Output

**Files Created**:
- `portfolio_analysis_YYYYMMDD.md` - Full report
- `portfolio_dashboard_YYYYMMDD.json` - Dashboard data
- `portfolio_trades.csv` - Trade-by-trade export

**Report Sections**:
1. Executive Summary
2. Trading Metrics
3. Edge Identification
4. Forward Projections
5. Risk Assessment
6. Tax Planning
7. Recommendations

## Example Output

```markdown
# Portfolio Analysis Report

**Generated**: 2025-11-22 10:30:00

## Trading Metrics

- Total Trades: 10
- Win Rate: 90.0%
- Average Return: 3.58%
- Total P&L: $283.94

## Edge Analysis

- Edge Identified: Yes
- Best Time Window: premarket_0400_0500
  - Trades: 2
  - Win Rate: 100%
  - Avg P&L: $79.49

## Forward Projections (3 Years)

- Year 1: $5,200,000
- Year 2: $50,000,000,000
- Year 3: $3,200,000,000,000

## Risk Metrics

- Max Drawdown: -44.13% (without stops)
- With 5% Stops: -8.2%
- Position Sizing: 75% avg (should be 10%)

## Tax Analysis (FL)

- Total Tax (3 years): $1,184,000,000,000
- Federal Rate: 37%
- State Rate: 0%

## Recommendations

1. **CRITICAL**: Implement 5% hard stops on all positions
2. **CRITICAL**: Reduce position sizing to 10% max
3. **HIGH**: Focus 100% on intraday trading (abandon swings)
4. **HIGH**: Set up tax reserve account (37% quarterly)
```

## Dashboard JSON

```json
{
  "generated_at": "2025-11-22T10:30:00",
  "metrics": {
    "total_trades": 10,
    "win_rate": 0.90,
    "avg_return_pct": 0.0358
  },
  "edge_analysis": {
    "edge_identified": true,
    "best_window": "premarket_0400_0500"
  },
  "projections": {
    "final_balance": 3200000000000
  },
  "risk_metrics": {
    "max_drawdown_pct": -8.2
  },
  "tax_analysis": {
    "total_tax": 1184000000000
  }
}
```

## Processing Time

- CSV parsing: ~1 second
- Metric calculation: ~1 second
- Edge analysis: ~2 seconds
- Projections: ~2 seconds
- Report generation: ~3 seconds
- **Total**: ~10 seconds

## Use Cases

### Use Case 1: Monthly Review
Run at end of each month to:
- Track actual vs projected performance
- Identify deviations from edge
- Recalibrate assumptions
- Update tax reserves

### Use Case 2: Quarterly Planning
Run quarterly for:
- Tax payment preparation
- Risk assessment review
- Strategy adjustment
- Performance reporting

### Use Case 3: Onboarding New Strategy
Run when testing new approach:
- Establish baseline metrics
- Identify edge characteristics
- Set projection targets
- Define risk parameters

## Notes

- **Historical Data**: Analysis is retrospective; use for baseline only
- **Projections**: Theoretical upper bounds; use Monte Carlo for realism
- **Tax**: Estimates only; consult CPA for exact calculations
- **Edge**: Requires 10+ trades for statistical significance

## See Also

- `/portfolio-report` - Generate PDF report
- `/portfolio-track` - Track performance over time
- `/portfolio-edge-analysis` - Edge analysis only
- `/forecast-portfolio` - Projections only
