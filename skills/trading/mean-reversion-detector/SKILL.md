# Mean Reversion Detector Skill

You are a specialized mean reversion signal detection system for concentrated position trading (95% capital deployment).

## Purpose

Identify high-probability mean reversion setups where price has deviated significantly from its statistical mean and is likely to revert. This skill is optimized for aggressive position sizing requiring exceptional signal quality.

## Core Statistical Framework

### Z-Score Calculation
```python
z_score = (price - sma_period) / std_period

# Thresholds:
# STRONG LONG:  z < -2.5
# LONG:         z < -2.0
# NEUTRAL:      -1.5 < z < 1.5
# SHORT:        z > 2.0
# STRONG SHORT: z > 2.5
```

### Half-Life Estimation
```python
# OLS regression: price_t = alpha + beta * price_{t-1} + epsilon
half_life = -log(2) / log(beta)

# Valid mean reversion: half_life < 20 bars
# Optimal: half_life between 5-15 bars
# Reject if: half_life > 30 bars (too slow)
```

### Hurst Exponent
```python
# R/S analysis or DFA method
H < 0.40  -> Strong mean reversion (HIGH CONFIDENCE)
H < 0.50  -> Mean reverting (tradeable)
H = 0.50  -> Random walk (AVOID)
H > 0.50  -> Trending (use pullback strategy instead)
```

### ADF Stationarity Test
```python
# Augmented Dickey-Fuller
p-value < 0.01  -> Strongly stationary (HIGH CONFIDENCE)
p-value < 0.05  -> Stationary (tradeable)
p-value >= 0.05 -> Non-stationary (REJECT)
```

## Condition Weights (Sum = 1.0)

| Condition | Weight | Description |
|-----------|--------|-------------|
| zscore_extreme | 0.16 | Z-score < -2.0 (long) or > +2.0 (short) |
| rsi_percentile | 0.11 | RSI in bottom/top 5th percentile |
| bullish_divergence | 0.14 | Price lower low, RSI higher low |
| exhaustion_signal | 0.09 | Falling but decelerating |
| stoch_crossover | 0.07 | K > D while both < 20 |
| absorption_signal | 0.09 | Price falling, delta rising |
| vwap_deviation | 0.06 | Price below VWAP -2 sigma |
| mtf_alignment | 0.18 | Multi-timeframe alignment |
| prev_day_support | 0.10 | Near/below previous day low |

## Signal Generation Workflow

### Step 1: Universe Screening
Filter for mean-reverting candidates:
- Hurst exponent < 0.50
- ADF p-value < 0.05
- Average volume > 1M shares
- Spread < 0.05%

### Step 2: Z-Score Analysis (Per Timeframe)
Calculate for 5m, 15m, 1hr:
```
For each symbol:
  z_5m  = z-score on 5-minute bars
  z_15m = z-score on 15-minute bars
  z_1hr = z-score on 1-hour bars
```

### Step 3: Half-Life Validation
```
Reject if half_life > 20 bars
Optimal zone: 5-15 bars
Calculate expected reversion time
```

### Step 4: Multi-Timeframe Confluence
Require 2/3 timeframes aligned:
```
alignment_score = sum([
  1 if z_5m < -2.0 else 0,
  1 if z_15m < -2.0 else 0,
  1 if z_1hr < -1.5 else 0
]) / 3

PASS if alignment_score >= 0.66
```

### Step 5: Final Signal Output
```yaml
signal:
  symbol: SPY
  direction: LONG
  confidence: 0.87

  statistics:
    z_score: -2.34
    half_life: 12.5
    hurst: 0.38
    adf_pvalue: 0.02

  conditions_met:
    zscore_extreme: true
    rsi_percentile: true
    bullish_divergence: false
    exhaustion_signal: true
    stoch_crossover: true
    absorption_signal: false
    vwap_deviation: true
    mtf_alignment: true
    prev_day_support: true

  confluence_score: 0.76

  timeframes:
    5m: LONG
    15m: LONG
    1hr: NEUTRAL

  trade_plan:
    entry_price: 445.50
    stop_loss: 443.25    # 0.5% - CRITICAL for 95% position
    target_1: 447.75     # VWAP (mean)
    target_2: 448.50     # BB mid
    target_3: 450.00     # 1R profit
    risk_reward: 2.0
```

## Entry Criteria for 95% Position

ALL of these must be true:
- [ ] Z-score < -2.0 (long) or > +2.0 (short)
- [ ] Half-life < 20 bars
- [ ] Hurst < 0.50
- [ ] 2+ timeframes aligned
- [ ] VIX < 25 (no regime filter trigger)
- [ ] Confluence score >= 0.70
- [ ] Spread < 0.03%
- [ ] Volume > average

## Risk Management Rules

### Stop Loss (MANDATORY)
```python
# For 95% position, max 0.5% stop
stop_long = entry - (entry * 0.005)
stop_short = entry + (entry * 0.005)

# Or ATR-based (tighter of the two)
stop_atr = entry - (atr_14 * 0.75)
```

### Position Sizing
```python
position_size = account_equity * 0.95
max_loss = position_size * 0.005  # 0.5% stop
account_risk = max_loss / account_equity  # ~0.475% account risk
```

### Exit Rules
1. **Target hit**: Exit 100% at mean (VWAP or BB mid)
2. **Stop hit**: Exit immediately, no adjustment
3. **Time stop**: Exit if no reversion in 2x half_life bars
4. **Regime change**: Exit if Hurst crosses above 0.55

## Regime Filters (NO TRADE IF)

```python
no_trade_conditions = [
    vix > 25,                    # High volatility
    hurst > 0.55,                # Trending market
    adf_pvalue > 0.10,           # Non-stationary
    daily_loss > 3%,             # Daily loss limit
    consecutive_losses >= 3,     # Losing streak
]
```

## Integration with World-Model

This skill wraps the existing implementation at:
- `~/projects/world-model/src/strategies/mean_reversion.py`
- `~/projects/world-model/src/indicators.py`
- `~/projects/world-model/src/dynamics.py`

### Tracking Infrastructure (v0.5.0+)
All signals MUST be tracked for accuracy measurement:
- `~/projects/world-model/src/tracking/` - Outcome tracking module
- `~/projects/world-model/src/confidence/` - Confidence grading (A/B/C/D)
- `~/projects/world-model/src/monitoring/` - Drift detection

### Recording Signals
```python
from tracking import record_signal

signal = record_signal(
    symbol="AAPL",
    strategy="mean_reversion",
    timeframe="15m",
    direction="LONG",
    confluence_score=0.76,
    conditions_met=["zscore_extreme", "rsi_percentile", ...],
    entry_price=175.50,
    stop_price=174.63,
    target_1=178.50,
)
```

### Confidence Grades
Before trading, check historical win rate for similar signals:
- **Grade A (70%+)**: FULL position (95%)
- **Grade B (62-70%)**: Standard position (75%)
- **Grade C (55-62%)**: Half position or skip
- **Grade D (<55%)**: DO NOT TRADE

Use MCP tools:
- `get_indicators` - Fetch technical indicators
- `scan_mean_reversion` - Scan for MR setups
- `validate_entry` - Pre-trade validation

## Quality Checklist

Before taking a 95% position:
- [ ] Statistical criteria met (z-score, half-life, Hurst)
- [ ] Multi-timeframe confluence >= 2/3
- [ ] Regime favorable (not trending bearish)
- [ ] Stop loss calculated and set
- [ ] Position size calculated correctly
- [ ] Risk/reward >= 1.5:1
- [ ] No conflicting signals

## Examples

### Example 1: Strong Mean Reversion Long
```
Symbol: QQQ
Z-score (15m): -2.67
Half-life: 8 bars
Hurst: 0.35
RSI: 22
Stochastic: K=15, D=18 (crossed up)

Confluence: 0.82
Recommendation: STRONG BUY

Entry: $388.50
Stop: $386.56 (-0.5%)
Target: $392.00 (VWAP)
R:R = 1.8:1
```

### Example 2: Rejected Setup
```
Symbol: TSLA
Z-score (15m): -1.85  # Not extreme enough
Half-life: 35 bars    # Too slow
Hurst: 0.52           # Trending, not reverting

Confluence: 0.45
Recommendation: NO TRADE

Reason: Half-life too long, Hurst indicates trending behavior
```

## Notes

- Mean reversion works best in ranging, low-volatility markets
- NEVER fight a strong trend - use pullback strategy instead
- The 95% position requires PERFECT setups only
- Always have stop loss in place BEFORE entry
- Monitor half-life during trade - exit if it increases significantly
