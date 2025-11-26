# Portfolio Analysis Agent

Comprehensive portfolio analysis integrating trades, projections, and tax planning.

## Quick Start

```bash
# Complete analysis
/analyze-portfolio path/to/trades.csv

# Generate PDF report
/portfolio-report --format pdf

# Track performance
/portfolio-track --month 11

# Edge analysis only
/portfolio-edge-analysis
```

## Features

- **Integrated Analysis**: Trades + Projections + Taxes in one workflow
- **Edge Identification**: Find your trading edge from historical data
- **Multi-Year Projections**: 3-5 year forward forecasts
- **Tax Planning**: Quarterly obligations with payment schedules
- **Risk Assessment**: Drawdown, volatility, Sharpe ratio
- **Dashboard**: Comprehensive JSON dashboard with all metrics

## Workflow

1. **Load** → Parse IB CSV statement
2. **Analyze** → Calculate metrics and identify edge
3. **Project** → Run forward projections
4. **Assess** → Calculate risk and tax obligations
5. **Report** → Generate comprehensive report

## Requirements

```bash
pip install numpy pandas pyyaml
```

## Configuration

Edit `~/projects/portfolio/PORTFOLIO_PARAMETERS_COMPLETE.yaml`

## Outputs

- `portfolio_analysis_YYYYMMDD.md` - Full report
- `portfolio_dashboard_YYYYMMDD.json` - Dashboard data
- `portfolio_trades.csv` - Trade export
- `portfolio_analysis_YYYYMMDD.pdf` - Professional PDF

## Documentation

See [SKILL.md](./SKILL.md) for complete documentation.

---

**Version**: 1.0.0 | **License**: MIT
