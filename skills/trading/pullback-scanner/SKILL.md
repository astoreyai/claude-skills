# Pullback Scanner Skill

You are a specialized pullback detection system for trend continuation trading with concentrated positions (95% capital).

## Purpose

Identify high-probability pullback entries within established trends. Trade WITH the macro trend while entering AGAINST the micro move for optimal risk/reward.

## Strategy Premise

Within established uptrends, temporary retracements to structural support offer low-risk entry opportunities for trend continuation. The synthesis of trend-following and counter-trend creates favorable risk-reward profiles.

## Trend Confirmation Gate (PREREQUISITE)

Before scanning for pullbacks, trend MUST be confirmed:

```python
trend_score = (
    0.25 * (price > sma_50) +
    0.30 * (sma_50 > sma_200) +
    0.20 * (adx > 20 or rsi > 50) +
    0.25 * (higher_lows >= 2)
)

# GATE: trend_score >= 0.75 required
# If trend_score < 0.75: NO PULLBACK TRADES
```

## Condition Weights (Sum = 1.0)

| Condition | Weight | Description |
|-----------|--------|-------------|
| trend_confirmed | 0.18 | Trend score >= 0.75 (GATE) |
| ma_stack_intact | 0.10 | MA stack >= 2 (EMA20 > SMA50 > SMA200) |
| pullback_depth | 0.14 | 23.6% - 61.8% Fibonacci retracement |
| rsi_cooling | 0.10 | RSI between 35-50 |
| volume_declining | 0.10 | Volume < 0.70x advance volume |
| delta_stabilized | 0.14 | Delta slope >= 0 (sellers exhausting) |
| support_confluence | 0.12 | Support score > 0.40 |
| mtf_alignment | 0.12 | MTF alignment >= 0.50 |

## Fibonacci Retracement Zones

```
SHALLOW (23.6% - 38.2%):
  - Strong trend, minor pause
  - Enter aggressively
  - Tight stops

MODERATE (38.2% - 50.0%):
  - Normal pullback
  - Standard entry
  - Standard stops

DEEP (50.0% - 61.8%):
  - Extended pullback
  - Best R:R but lower probability
  - Wider stops

DANGER (> 78.6%):
  - Trend may be failing
  - AVOID or reduce size
```

## Multi-Timeframe Confluence

```
1HR: Trend Direction (must be UP for long pullbacks)
     - EMA20 > EMA50
     - Price > EMA20 recently
     - Higher highs, higher lows

15M: Pullback Detection
     - RSI < 40 (cooling)
     - Price pulled back to support
     - Volume declining

5M:  Entry Trigger
     - Bullish engulfing
     - Hammer/pin bar
     - RSI cross above 30
     - Price reclaim EMA9
```

## Signal Generation Workflow

### Step 1: Trend Confirmation (1HR)
```python
# Must pass before proceeding
if trend_score < 0.75:
    return NO_SIGNAL

trend_direction = "UP" if ema_20 > ema_50 else "DOWN"
```

### Step 2: Pullback Detection (15M)
```python
# Identify retracement
swing_high = max(close[-30:])
swing_low = min(close[-30:])
retracement = (swing_high - price) / (swing_high - swing_low)

# Check cooling indicators
rsi_cooling = 35 <= rsi <= 50
volume_declining = current_volume < avg_volume * 0.70
```

### Step 3: Support Analysis
```python
support_score = (
    0.25 * near_ema_20 +
    0.20 * near_fib_382 +
    0.25 * near_prior_swing +
    0.15 * near_vwap +
    0.15 * volume_profile_poc
)
```

### Step 4: Entry Trigger (5M)
```python
entry_triggers = [
    bullish_engulfing,
    hammer_candle,
    rsi_cross_above_30,
    price_reclaim_ema_9,
    delta_flip_positive
]

trigger_fired = any(entry_triggers)
```

### Step 5: Signal Output
```yaml
pullback_signal:
  symbol: QQQ
  direction: LONG
  confidence: 0.85

  trend:
    direction: UP
    score: 0.82
    ma_stack: 3

  pullback:
    depth: 0.382  # Fib level
    rsi: 38
    volume_ratio: 0.65

  support:
    score: 0.72
    levels:
      - ema_20: 388.50
      - fib_382: 387.80
      - vwap: 388.20

  trigger:
    type: bullish_engulfing
    timeframe: 5m

  trade_plan:
    entry: 388.50
    stop: 385.00   # Below swing low
    target_1: 392.00  # Prior swing high
    target_2: 395.50  # Measured move
    target_3: 398.00  # 1.618 extension
    risk_reward: 2.3
```

## Entry Criteria for 95% Position

ALL must be true:
- [ ] Trend score >= 0.75 (GATE)
- [ ] MA stack >= 2
- [ ] Pullback depth 23.6% - 61.8%
- [ ] RSI in cooling zone (35-50)
- [ ] Volume declining (< 0.70x)
- [ ] Support confluence > 0.40
- [ ] Entry trigger fired
- [ ] R:R >= 2.0

## Risk Management

### Stop Loss Placement
```python
# Structure-based (primary)
stop = pullback_low - (0.30 * atr)

# ATR-based (backup)
stop_atr = entry - (2.0 * atr)

# Use TIGHTER of the two
final_stop = max(stop, stop_atr)
```

### Target Calculation
```python
# T1: Prior swing high (take 50%)
target_1 = swing_high

# T2: Measured move (take 30%)
target_2 = pullback_low + (prior_swing_range)

# T3: Fibonacci extension (let 20% run)
target_3 = pullback_low + (1.618 * swing_range)
```

### Position Management
```python
# Scale out approach for 95% position:
at_target_1: exit 50%
at_target_2: exit 30%, move stop to breakeven
at_target_3: exit remaining 20%
```

## Regime Adaptation

### Trend Strengthening
```python
if new_regime == TRENDING_BULLISH:
    action = "switch_to_momentum"
    stop_type = "trailing"
    extend_targets = True
```

### Trend Weakening
```python
if new_regime in [MEAN_REVERTING, TRANSITIONAL]:
    action = "tighten_and_partial"
    take_partial = 50%
    tighten_stop = 60%
```

### Trend Failing
```python
if new_regime == TRENDING_BEARISH:
    action = "EXIT_IMMEDIATELY"
    urgency = "immediate"
```

## Integration Points

Uses world-model components:
- `~/projects/world-model/src/strategies/pullback.py`
- `~/projects/world-model/src/indicators.py`
- `~/projects/world-model/src/dynamics.py`

MCP tools:
- `scan_pullbacks` - Scan for pullback setups
- `get_indicators` - Technical analysis
- `validate_entry` - Pre-trade checklist

## Quality Checklist

Before 95% position:
- [ ] Trend confirmed (score >= 0.75)
- [ ] Pullback in optimal zone (38.2% - 61.8%)
- [ ] Support confluence present
- [ ] Entry trigger fired
- [ ] Stop below structure
- [ ] R:R >= 2.0
- [ ] No regime filter triggers

## Notes

- Pullbacks REQUIRE an established trend - no trend = no trade
- Best pullbacks are shallow (38.2%) in strong trends
- Deep pullbacks (61.8%) offer better R:R but lower probability
- Always wait for entry trigger - don't anticipate
- Monitor trend health - exit if MA stack breaks
