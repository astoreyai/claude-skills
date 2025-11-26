# Portfolio Report

**Command**: `/portfolio-report`
**Category**: Financial Analysis
**Agent**: portfolio-analysis-agent

## Description

Generate comprehensive portfolio analysis report in PDF or markdown format.

## Usage

```bash
/portfolio-report --format pdf
```

**Options**:
```bash
/portfolio-report --format markdown              # Markdown report
/portfolio-report --format latex                 # LaTeX source
/portfolio-report --format pdf                   # Compile PDF
/portfolio-report --sync-gdrive                  # Upload to Google Drive
```

## Prerequisites

Must have run `/analyze-portfolio` first to generate analysis data.

## What It Does

1. **Load Analysis Results**
   - Read dashboard JSON
   - Load calculated metrics
   - Access projections and risk data

2. **Generate Report Sections**
   - Executive Summary
   - Trading Performance Analysis
   - Edge Identification
   - Forward Projections (3-5 years)
   - Risk Assessment
   - Tax Planning
   - Recommendations

3. **Format Output**
   - **Markdown**: Clean text format
   - **LaTeX**: Professional formatting
   - **PDF**: Compiled report (requires pdflatex)

4. **Optional Google Drive Sync**
   - Upload to configured folder
   - Version tracking
   - Shareable link generation

## Report Structure

### PDF Report (15+ pages)

**Section 1: Executive Summary** (1 page)
- Account overview
- Key performance metrics
- Critical findings
- Immediate actions

**Section 2: Trading Performance** (2-3 pages)
- Trade-by-trade breakdown
- Win rate and profit factor
- Average returns
- Commission analysis
- P&L distribution

**Section 3: Edge Analysis** (2-3 pages)
- Time-of-day performance
- Intraday vs swing comparison
- Symbol-level profitability
- Repeatability assessment
- Best/worst windows

**Section 4: Forward Projections** (3-4 pages)
- 3-year baseline scenario
- Alternative scenarios (conservative/aggressive)
- Monthly and quarterly breakdowns
- Tax-adjusted projections
- Milestone tracking

**Section 5: Risk Assessment** (2-3 pages)
- Drawdown analysis
- Volatility metrics
- Sharpe ratio calculations
- Position sizing audit
- Stop-loss impact simulation

**Section 6: Tax Planning** (2 pages)
- Quarterly obligations
- Federal + state breakdown
- Payment schedule
- Reserve account strategy
- Multi-state comparison

**Section 7: Recommendations** (1-2 pages)
- Immediate actions (critical)
- Risk management improvements
- Tax optimization strategies
- Performance targets
- Next steps

## Output Examples

### Markdown Report
```markdown
# Portfolio Analysis Report

**Generated**: 2025-11-22 10:30:00
**Account**: U21858510
**Period**: Jan 1 - Nov 20, 2025

---

## Executive Summary

### Key Metrics
- Total Trades: 10
- Win Rate: 90%
- Average Return: 3.58% per trade
- Net P&L: $283.94

### Critical Findings
1. **Intraday Edge Confirmed**: 100% win rate on intraday trades
2. **Position Sizing Risk**: 75% average (should be 10%)
3. **Stop-Loss Violation**: GETY trade lost -44% without stop

### Immediate Actions
- [ ] Implement 5% hard stops on all positions
- [ ] Reduce position sizing to 10% max
- [ ] Focus 100% on intraday trading
```

### LaTeX Report Features
- Professional typography
- Mathematical notation for formulas
- High-quality tables (booktabs)
- Charts and visualizations
- Proper citations and references
- Institutional-grade formatting

## PDF Compilation

**Requirements**:
```bash
sudo apt-get install texlive-full  # Linux
brew install texlive               # macOS
```

**Automatic Compilation**:
- LaTeX source generated
- pdflatex run automatically
- Errors logged
- PDF output created

## Google Drive Sync

**Setup**:
1. Configure MCP google-drive server
2. Authenticate with OAuth
3. Set target folder ID

**Sync Process**:
- Upload PDF to Drive
- Create shareable link
- Update metadata (version, date)
- Log sync status

**Output**:
```
✓ Report uploaded to Google Drive
  URL: https://drive.google.com/file/d/...
  Folder: Portfolio Reports/2025/
  Version: v20251122
```

## Usage Examples

### Example 1: Monthly Report
```bash
# After monthly trading review
/analyze-portfolio nov_trades.csv
/portfolio-report --format pdf --sync-gdrive
```

### Example 2: Quarterly Report
```bash
# End of quarter
/analyze-portfolio q4_trades.csv --years 5
/portfolio-report --format pdf
```

### Example 3: Markdown Only
```bash
# Quick text report
/portfolio-report --format markdown
```

## File Locations

**Output Directory**: `~/projects/portfolio/`

**Files**:
- `portfolio_analysis_20251122.md` - Markdown report
- `portfolio_analysis_20251122.tex` - LaTeX source
- `portfolio_analysis_20251122.pdf` - Compiled PDF

## Customization

Edit report templates in:
- `portfolio_analysis_agent.py` (line ~600)
- Modify `_generate_markdown_report()` for markdown
- Modify `_generate_latex_report()` for LaTeX

## Troubleshooting

### Issue: PDF compilation fails
**Solution**: Install texlive-full or check LaTeX syntax errors in .tex file

### Issue: Google Drive sync fails
**Solution**: Verify MCP server config and OAuth authentication

### Issue: Report has missing data
**Solution**: Run `/analyze-portfolio` first to generate analysis data

## See Also

- `/analyze-portfolio` - Run complete analysis first
- `/portfolio-track` - Track performance over time
- `/forecast-5year` - Detailed projections
