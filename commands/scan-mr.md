# Scan Mean Reversion

Scan watchlist for mean reversion setups using the mean-reversion-detector skill.

## Usage
```
/scan-mr [symbols] [timeframe]
```

## Arguments
- `symbols`: Comma-separated list or "default" for SPY,QQQ,IWM,DIA
- `timeframe`: 5m, 15m (default), 1hr

## Workflow

1. Load mean-reversion-detector skill
2. For each symbol:
   - Fetch bars via quant-trading-mcp
   - Calculate z-score, RSI, stochastic, Hurst
   - Evaluate all 9 MR conditions
   - Calculate confluence score
3. Rank signals by confluence
4. Output actionable setups

## Output Format
```
MEAN REVERSION SCAN - 15m
========================

SIGNALS FOUND: 2

1. QQQ - LONG (Score: 0.82)
   Z-score: -2.34 | RSI: 28 | Stoch: 15/18
   Entry: $388.50 | Stop: $386.56 | Target: $392.00
   R:R: 1.8:1

2. SPY - LONG (Score: 0.71)
   Z-score: -2.05 | RSI: 32 | Stoch: 22/25
   Entry: $445.50 | Stop: $443.25 | Target: $448.00
   R:R: 1.5:1

NO SIGNAL: IWM (z=-1.2), DIA (z=-0.8)
```

## Integration
- Uses: mean-reversion-detector skill
- MCP: quant-trading-mcp (get_indicators, scan_mean_reversion)
- Agent: quant-signal-generator
