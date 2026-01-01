# Scan Pullbacks

Scan watchlist for pullback entries in uptrends using the pullback-scanner skill.

## Usage
```
/scan-pb [symbols] [timeframe]
```

## Arguments
- `symbols`: Comma-separated list or "default" for SPY,QQQ,IWM,DIA
- `timeframe`: 5m, 15m (default), 1hr

## Workflow

1. Load pullback-scanner skill
2. For each symbol:
   - Check trend confirmation (GATE)
   - If trend confirmed:
     - Calculate pullback depth (Fibonacci)
     - Check RSI cooling zone
     - Evaluate support confluence
     - Check for entry triggers
   - Calculate confluence score
3. Rank signals by confluence
4. Output actionable setups

## Output Format
```
PULLBACK SCAN - 15m
===================

SIGNALS FOUND: 1

1. QQQ - LONG (Score: 0.78)
   Trend: UP (0.85) | Depth: 38.2%
   RSI: 42 | Support: EMA20, Fib382
   Trigger: bullish_engulfing (5m)
   Entry: $388.50 | Stop: $385.00 | Target: $395.50
   R:R: 2.3:1

NO TREND: SPY (score: 0.62), IWM (score: 0.58)
DEEP PULLBACK: DIA (depth: 72% - caution)
```

## Integration
- Uses: pullback-scanner skill
- MCP: quant-trading-mcp (get_indicators, scan_pullbacks)
- Agent: quant-signal-generator
