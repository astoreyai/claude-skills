# Kymera Portfolio Reality Checker

Validates the portfolio trading edge claim using real data. Analyzes actual portfolio trades against entry criteria and risk management rules.

## Overview

This agent verifies the core claim that the portfolio system has a 90% win rate and confirmed edge for intraday scalping. It identifies risk management violations early before they compound into catastrophic losses like the GETY trade.

## Capabilities

- **Edge Validation**: Verify 90% win rate claim based on real portfolio data
- **Risk Analysis**: Identify position sizing violations and largest loss issues
- **Quarterly Reports**: Generate periodic validation reports
- **Trend Analysis**: Track edge degradation over time
- **Recommendations**: Generate actionable recommendations for edge preservation

## Use Cases

1. **Validate Portfolio Edge**
   ```
   /kymera-portfolio-checker validate-edge
   ```
   Checks current portfolio performance against entry criteria

2. **Generate Quarterly Report**
   ```
   /kymera-portfolio-checker quarterly-report
   ```
   Creates comprehensive quarterly validation report

3. **Check for Risk Violations**
   ```
   /kymera-portfolio-checker check-violations
   ```
   Identifies position sizing and stop-loss violations

## Key Metrics

- Win rate (target: ≥80%)
- Profit factor (target: ≥1.20)
- Max position size (target: ≤10%)
- Payoff ratio (target: ≥1.0)
- Intraday edge confirmation

## Integration

Works with:
- Portfolio analysis framework
- Portfolio-to-strategy converter
- Unified dashboard

## Configuration

```yaml
edge_targets:
  win_rate: 0.80
  profit_factor: 1.20
  payoff_ratio: 1.0
  max_position: 0.10
  max_drawdown: 0.25
```

## Output

Generates detailed reports with:
- Edge validation status
- Risk violation list
- Confidence assessment
- Actionable recommendations
- Historical trend analysis

## Author

Aaron Storey | Kymera Strategy (Nov 2025)
