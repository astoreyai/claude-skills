# Portfolio Forecasting Agent

Multi-year portfolio projections with Monte Carlo simulations and tax planning.

## Quick Start

```bash
# 3-year baseline projection
/forecast-portfolio

# Full 5-year analysis with Monte Carlo
/forecast-5year

# Monte Carlo only
python forecasting_agent.py --monte-carlo --years 5

# Tax forecasting
/forecast-tax --years 5 --state NY
```

## Features

- **3/5-Year Projections**: Conservative, Baseline, Aggressive scenarios
- **Monte Carlo**: 1,000 path simulations with probabilistic outcomes
- **Tax Planning**: Quarterly tax reserves (federal + state)
- **Risk Analysis**: Drawdown, volatility, Sharpe ratio
- **Report Generation**: Markdown, LaTeX, PDF, CSV exports

## Requirements

```bash
pip install numpy pandas pyyaml
```

## Configuration

Edit `~/projects/portfolio/PORTFOLIO_PARAMETERS_COMPLETE.yaml`:

```yaml
trading:
  return_per_trade:
    all_time_avg: 3.58      # % per trade
  win_rate:
    actual: 90.0            # %
  trade_frequency:
    trades_per_month:
      baseline: 18.5
```

## Outputs

- `forecast_baseline_3y_monthly.csv` - Monthly projections
- `forecast_baseline_3y_quarterly.csv` - Quarterly summaries
- `portfolio_forecast_20251122.md` - Markdown report
- `portfolio_forecast_20251122.pdf` - PDF report (LaTeX)

## Documentation

See [SKILL.md](./SKILL.md) for complete documentation.

---

**Version**: 1.0.0 | **License**: MIT
