# Validate Trade

Run pre-trade validation checklist for 95% concentrated position.

## Usage
```
/validate-trade <symbol> <direction> [position_pct]
```

## Arguments
- `symbol`: Ticker symbol (e.g., SPY)
- `direction`: LONG or SHORT
- `position_pct`: Position size (default: 0.95)

## Workflow

1. Load concentrated-risk skill
2. Fetch multi-timeframe data (5m, 15m, 1hr)
3. Run validation checklist:
   - Signal quality checks
   - Statistical validity
   - Risk parameters
   - Regime filters
   - Account state
   - Market conditions
4. Calculate position sizing
5. Output approval/rejection with details

## Output Format
```
TRADE VALIDATION
================
Symbol: QQQ
Direction: LONG
Position: 95%

CHECKLIST:
[PASS] Confluence >= 0.70 (0.76)
[PASS] Z-score extreme (-2.34)
[PASS] Half-life < 20 (12 bars)
[PASS] MTF Alignment (2/3)
[PASS] VIX < 25 (18.5)
[PASS] Spread < 0.03% (0.01%)
[PASS] Volume adequate (1.2x avg)
[WARN] RSI not extreme (32)

RESULT: APPROVED (11/12 checks passed)

POSITION DETAILS:
Entry: $388.50
Stop: $386.56 (-0.5%)
Shares: 24
Position Value: $9,324
Account Risk: 0.47%

TARGETS:
1R: $390.44 (exit 50%)
2R: $392.38 (exit 30%)
3R: $394.32 (let 20% run)
```

## Integration
- Uses: concentrated-risk skill
- MCP: quant-trading-mcp (validate_entry, calculate_position)
- Agent: quant-risk-manager
