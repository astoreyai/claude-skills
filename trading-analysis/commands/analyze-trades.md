# /analyze-trades Command

Conducts comprehensive trading performance analysis on Interactive Brokers CSV statement.

## Usage

```
/analyze-trades <path-to-csv> [--output markdown|latex|both|csv] [--depth quick|standard|detailed] [--risk conservative|realistic|aggressive]
```

## Examples

### Basic Analysis (Markdown)
```
/analyze-trades ~/projects/portfolio/U21858510_20250101_20251120.csv
```

### Full PDF Report
```
/analyze-trades ~/projects/portfolio/U21858510_20250101_20251120.csv --output latex
```

### Quick Stats Only
```
/analyze-trades ~/projects/portfolio/U21858510_20250101_20251120.csv --depth quick
```

### Conservative Scenarios
```
/analyze-trades ~/projects/portfolio/U21858510_20250101_20251120.csv --risk conservative
```

## Output Options

- **markdown** (default): Detailed text analysis (7,000+ words)
- **latex**: Professional PDF report (11 pages)
- **both**: Both markdown + PDF
- **csv**: Raw data exports only

## Depth Options

- **quick** (2 min): Summary stats only
- **standard** (5 min): Full analysis with recommendations
- **detailed** (10 min): Full analysis + LaTeX report + CSV exports

## Risk Analysis Options

- **conservative**: Assume proper 5% stops and 10% position sizing
- **realistic**: Current methodology and actual position sizing
- **aggressive**: No changes, current positions

## Output Files

Generated in same directory as input CSV:

```
trading_analysis_2025.md              # Markdown report
trading_analysis_report.pdf           # PDF report (if --output latex/both)
trading_analysis_stats.csv            # Trade-by-trade summary
trading_symbol_analysis.csv           # Symbol performance ranking
trading_time_analysis.csv             # Time-of-day breakdown
```

## Automatic Sync

All output files automatically synced to Google Drive folder: `Portfolio Forecasts/`

---

This command uses the Trading Analysis skill from astoreyai/claude-skills
