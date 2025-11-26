# Trading Analysis Skill

Professional trading performance analysis and edge identification for Interactive Brokers accounts.

## Quick Start

```bash
# Generate markdown analysis
/analyze-trades ~/path/to/U21858510_YYYYMMDD_YYYYMMDD.csv

# Generate PDF report
/analyze-trades ~/path/to/U21858510_YYYYMMDD_YYYYMMDD.csv --output latex

# Quick stats only
/analyze-trades ~/path/to/U21858510_YYYYMMDD_YYYYMMDD.csv --depth quick
```

## Files

- **SKILL.md** - Complete skill documentation
- **trading_analysis_agent.py** - Python agent implementation
- **commands/analyze-trades.md** - Slash command specification
- **examples/** - Example analyses and outputs

## Features

✅ CSV statement parsing (Interactive Brokers format)
✅ Win rate, profit factor, average return calculations
✅ Edge identification (intraday vs swing, time-of-day, symbol-level)
✅ Risk analysis (position sizing, drawdown, stop-loss impact)
✅ Markdown reports (7,000+ words)
✅ Professional PDF reports (11 pages)
✅ CSV data exports
✅ Growth projections
✅ Scenario analysis

## Integration

### With Claude Code
- Use `/analyze-trades <csv>` command in Claude Code
- Automatically syncs results to Google Drive
- Integrates with portfolio forecasting

### With Portfolio Forecasting Skill
```
Trading Edge (90% win rate) → /analyze-trades command
                           ↓
                 Actual performance metrics
                           ↓
                 Feed to quarterly tax forecast
```

## Example Output

```
# Trading Analysis Report
Account: U21858510 (Kymera Systems LLC)

## Executive Summary
- Total Trades: 10
- Win Rate: 90%
- Net P&L: $283.94
- Profit Factor: 1.41

## Edge Analysis

### Intraday Trading (Best)
- Trades: 6
- Win Rate: 100%
- Total P&L: +$1,020.63
- Avg Return: 7.8%

### Swing Trading (Weak)
- Trades: 4
- Win Rate: 50%
- Total P&L: -$661.16
- Avg Return: -3.2%
```

## Status

**Version**: 1.0.0 (Production Ready)
**Last Updated**: November 22, 2025
**Maintenance**: Active

---

Part of [astoreyai/claude-skills](https://github.com/astoreyai/claude-skills) distribution.
