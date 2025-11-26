# Trading Analysis Skill

**Version**: 1.0.0
**Category**: Financial Analysis / Trading
**Author**: Claude Code
**Last Updated**: November 22, 2025

## Overview

Comprehensive trading performance analysis and edge identification system for Interactive Brokers accounts. Analyzes CSV statements to identify trading patterns, position sizing issues, time-of-day edges, and risk management problems.

## Features

### 1. **CSV Statement Parsing**
- Parse Interactive Brokers activity statements (CSV format)
- Extract closed positions with entry/exit prices
- Calculate returns, commissions, and net P&L
- Identify open positions and unrealized gains

### 2. **Trading Pattern Analysis**
- Holding period distribution (intraday vs swing)
- Time-of-day entry analysis
- Position sizing audit
- Trade duration statistics

### 3. **Performance Metrics**
- Win rate and profit factor calculation
- Per-trade return analysis
- Return by symbol/sector
- Drawdown and recovery analysis
- Risk-adjusted metrics (Sharpe ratio approximation)

### 4. **Edge Identification**
- Intraday vs swing trading performance
- Time window performance (04:00-05:00 ET, etc.)
- Symbol-level profitability
- Strategy efficiency (wins/losses by category)
- Repeatability analysis (which trades work consistently)

### 5. **Risk Analysis**
- Position sizing as % of capital
- Over-leverage detection
- Stop-loss impact simulation
- Single trade impact on portfolio
- Sequence of returns risk

### 6. **LaTeX Report Generation**
- Professional PDF reports
- Visual performance tables
- Recommendations with actionable steps
- Growth projections
- Scenario analysis

## Usage

### Basic Analysis (Markdown Report)
```bash
/analyze-trades <path-to-csv>
```

**Output**: Detailed markdown analysis with:
- Executive summary
- Trading patterns
- Edge identification
- Risk analysis
- Actionable recommendations

### Full Analysis (LaTeX + PDF)
```bash
/analyze-trades-pdf <path-to-csv>
```

**Output**:
- Professional PDF report (11 pages)
- High-quality charts and tables
- Institutional-grade formatting
- Synced to Google Drive

### Quick Stats Only
```bash
/trading-stats <path-to-csv>
```

**Output**: Summary table with:
- Win rate, profit factor, average return
- Best/worst trades
- Position sizing metrics

## Data Requirements

### Input Format
Interactive Brokers Activity Statement (CSV) containing:
- Statement header information
- Account summary (capital, dates)
- Trade list with:
  - Symbol, entry date, entry price
  - Exit date, exit price
  - Quantity, commission
  - Realized P&L
- Deposit/withdrawal history

### Example CSV Structure
```
Statement,Header,Field Name,Field Value
Statement,Data,BrokerName,Interactive Brokers LLC
Account Information,Data,Account,U21858510
Trades,Data,Order,Stocks,USD,SYMBOL,2025-10-24,...
```

## Output Formats

### 1. Markdown Analysis
- **File**: `trading_analysis_2025.md`
- **Size**: 7,500+ words
- **Sections**:
  - Executive summary with key metrics
  - Detailed trade-by-trade breakdown
  - Edge identification with statistics
  - Risk analysis with scenarios
  - Actionable recommendations

### 2. LaTeX Report (PDF)
- **File**: `trading_analysis_report.pdf`
- **Pages**: 10-15
- **Includes**:
  - Professional formatting
  - Mathematical notation for risk analysis
  - Scenario tables
  - Growth projections
  - Decision framework

### 3. CSV Exports
- Trade-by-trade summary
- Symbol performance ranking
- Time-of-day analysis
- Position sizing audit

## Key Metrics Calculated

| Metric | Calculation | Interpretation |
|--------|-----------|-----------------|
| **Win Rate** | Wins / Total Trades | % of profitable trades |
| **Profit Factor** | Gross Wins / Gross Losses | >2.0 is professional |
| **Avg Winner** | Total Wins / # Wins | Average profitable trade |
| **Avg Loser** | Total Losses / # Losses | Average losing trade |
| **Payoff Ratio** | Avg Winner / Abs(Avg Loser) | Risk-reward balance |
| **Position Size %** | Position Cost / Capital | Leverage check |
| **Return/Day** | Total P&L / Trading Days | Daily compounding equivalent |
| **Stop Loss Impact** | Loss without vs with stop | Protection value |

## Analysis Examples

### Example 1: Intraday Scalping Edge
**Input**: 10 trades over 28 days
- 9 wins (4 intraday <3hr, 5 swing >1 day)
- 1 loss (swing trade, no stop)

**Output**:
- Intraday: 100% win rate, +$1,020 P&L
- Swing: 50% win rate, -$661 P&L
- **Edge**: Scalping 04:00-05:00 ET and 11:00-12:00 ET
- **Recommendation**: 100% intraday trading, abandon swings

### Example 2: Position Sizing Audit
**Input**: 10 trades with varying position sizes
- Average: 75% of capital
- Max: 105% (overleveraged)
- Min: 49.7%

**Output**:
- Risk score: 9/10 (dangerous)
- One bad trade can eliminate 100% of capital
- Recommended max: 10% per position
- Projected impact if stops added: prevent catastrophic loss

## Skill Parameters

### Analysis Depth
- **Quick**: Basic stats (2 min)
- **Standard**: Full analysis (5 min)
- **Detailed**: LaTeX report generation (10 min)

### Output Preferences
- **markdown**: Plain text analysis
- **latex**: Professional PDF report
- **both**: Both markdown + PDF
- **csv**: Data exports only

### Risk Analysis
- **conservative**: Assume 5% stops, 10% position sizing
- **realistic**: Current methodology
- **aggressive**: Current positions, no changes

## Integration Points

### With Portfolio Forecasting
```
CSV Analysis → Performance Metrics → Baseline Return Rate
                                  ↓
                    (Feed to quarterly tax forecast)
                    - Use actual win rate (90%)
                    - Use actual position sizing (75%)
                    - Account for drawdown risk
```

### With Tax Planning
```
Trading Edge (90% win rate) → Projected Annual Gains
                           ↓
                 (Feed to quarterly tax reserves)
                 - 37% quarterly reserves
                 - Federal/state tax estimates
                 - Growth projections
```

## Known Limitations

1. **Historical Data Only**: Analyzes past performance; future not guaranteed
2. **No Live Trading Integration**: CSV-based, not real-time
3. **Simplified Risk Metrics**: Uses basic calculations (not full Monte Carlo)
4. **Single Account**: One account per analysis (can be extended)
5. **Assumptions**: Assumes fills at entry/exit prices (no slippage modeling)

## Future Enhancements

- [ ] Multi-account aggregation
- [ ] Real-time streaming integration
- [ ] Monte Carlo simulations (1,000+ paths)
- [ ] Machine learning pattern recognition
- [ ] Options strategy analysis
- [ ] Tax lot tracking and loss harvesting
- [ ] Correlation analysis across symbols
- [ ] Machine learning trade classification

## Troubleshooting

### Issue: CSV parsing fails
**Solution**: Verify format matches Interactive Brokers statement. Check for:
- Correct column headers
- Date format (YYYY-MM-DD)
- Proper quote escaping

### Issue: No trades detected
**Solution**: Check that "Trades" section exists in CSV with:
- "Order" or "SubTotal" indicators
- Non-zero quantities
- Realized P&L values

### Issue: Positions sizing calculated wrong
**Solution**: Verify capital amount in statement. Check:
- Starting cash balance
- Deposits/withdrawals recorded
- Cost basis calculations

## References

### Theory
- Kelly Criterion for position sizing
- Expectancy and payoff ratio theory
- Risk-adjusted return metrics (Sharpe, Sortino)
- Money management best practices

### IB Statement Format
- [IB Activity Statement Guide](https://www.interactivebrokers.com)
- CSV export format: `U[AccountNumber]_[DateRange].csv`

## Support

For issues or feature requests:
1. Check CSV format (most common issue)
2. Review example reports in `/examples/`
3. Verify calculations manually
4. Run quick stats first (easier to debug than full analysis)

---

**License**: MIT (Part of astoreyai/claude-skills distribution)
**Repository**: https://github.com/astoreyai/claude-skills/
