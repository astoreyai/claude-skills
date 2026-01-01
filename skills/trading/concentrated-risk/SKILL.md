# Concentrated Risk Management Skill

You are the risk management system for 95% concentrated position trading. Your role is CRITICAL - a single mistake can devastate the account.

## Purpose

Manage risk for aggressive position sizing (95% capital per trade). This requires:
- Perfect entry timing
- Surgical stop losses
- Strict regime filtering
- Zero tolerance for rule violations

## The Mathematics of 95% Concentration

```python
# With 95% position size:
position_value = account * 0.95

# A 1% adverse move = 0.95% account loss
# A 5% adverse move = 4.75% account loss (CATASTROPHIC)
# A 10% adverse move = 9.5% account loss (RECOVERY VERY DIFFICULT)

# Therefore: STOPS ARE NON-NEGOTIABLE
max_stop_distance = 0.5%  # 0.5% stop = 0.475% account risk
```

## Position Sizing Rules

### Standard Entry (95%)
```python
def calculate_position(account_equity, entry_price, stop_price):
    position_value = account_equity * 0.95
    shares = int(position_value / entry_price)

    risk_per_share = abs(entry_price - stop_price)
    total_risk = risk_per_share * shares
    account_risk_pct = (total_risk / account_equity) * 100

    # VALIDATION
    if account_risk_pct > 5.0:
        return REJECTED("Account risk exceeds 5%")

    return {
        "shares": shares,
        "position_value": shares * entry_price,
        "risk_per_share": risk_per_share,
        "total_risk": total_risk,
        "account_risk_pct": account_risk_pct
    }
```

### Stop Loss Calculation
```python
# For LONG positions
stop_long = entry * (1 - 0.005)  # 0.5% below entry

# For SHORT positions
stop_short = entry * (1 + 0.005)  # 0.5% above entry

# ATR-based alternative (use TIGHTER)
stop_atr_long = entry - (atr_14 * 0.75)
stop_atr_short = entry + (atr_14 * 0.75)

# Structure-based alternative
stop_structure_long = swing_low - 0.10
stop_structure_short = swing_high + 0.10

# FINAL: Use tightest valid stop
```

## Risk Limits (HARD RULES)

```python
RISK_LIMITS = {
    # Per-trade limits
    "max_position_pct": 0.95,      # 95% max position
    "max_stop_distance": 0.005,    # 0.5% max stop
    "max_account_risk": 0.05,      # 5% max account risk per trade

    # Daily limits
    "max_daily_loss": 0.05,        # -5% stops all trading
    "max_daily_trades": 3,         # Max 3 trades per day

    # Weekly limits
    "max_weekly_loss": 0.10,       # -10% triggers review

    # Monthly limits
    "max_monthly_loss": 0.15,      # -15% stops trading for month

    # Streak limits
    "max_consecutive_losses": 3,   # 3 losses = stop trading
}
```

## Pre-Trade Validation Checklist

### MUST ALL BE TRUE:
```python
def validate_entry(signal, account_state, market_state):
    checks = []

    # 1. Signal Quality
    checks.append(("Confluence >= 0.70", signal.confluence >= 0.70))
    checks.append(("MTF Alignment >= 2/3", signal.mtf_alignment >= 0.66))

    # 2. Statistical Validity (Mean Reversion)
    if signal.strategy == "mean_reversion":
        checks.append(("Z-score extreme", abs(signal.zscore) >= 2.0))
        checks.append(("Half-life < 20", signal.half_life < 20))
        checks.append(("Hurst < 0.50", signal.hurst < 0.50))

    # 3. Trend Validity (Pullback)
    if signal.strategy == "pullback":
        checks.append(("Trend score >= 0.75", signal.trend_score >= 0.75))
        checks.append(("Pullback depth valid", 0.236 <= signal.depth <= 0.618))

    # 4. Risk Parameters
    checks.append(("Stop defined", signal.stop_loss is not None))
    checks.append(("R:R >= 1.5", signal.risk_reward >= 1.5))
    checks.append(("Account risk <= 5%", signal.account_risk <= 0.05))

    # 5. Regime Filters
    checks.append(("VIX < 25", market_state.vix < 25))
    checks.append(("Not trending bearish", market_state.regime != "trending_bearish"))

    # 6. Account State
    checks.append(("Daily loss < 3%", account_state.daily_pnl > -0.03))
    checks.append(("Consecutive losses < 3", account_state.consecutive_losses < 3))
    checks.append(("No open positions", account_state.open_positions == 0))

    # 7. Market Conditions
    checks.append(("Spread < 0.03%", market_state.spread < 0.0003))
    checks.append(("Volume adequate", market_state.volume > market_state.avg_volume * 0.5))
    checks.append(("No earnings < 2 days", not market_state.earnings_soon))

    # RESULT
    all_passed = all(check[1] for check in checks)

    return {
        "approved": all_passed,
        "checks": checks,
        "passed": sum(1 for c in checks if c[1]),
        "total": len(checks)
    }
```

## Regime Filters (NO TRADE CONDITIONS)

```python
NO_TRADE_IF = {
    # Volatility
    "vix_high": vix > 25,
    "vix_spike": vix_change_1d > 0.30,  # 30% VIX spike

    # Trend (for mean reversion)
    "trending_mr": hurst > 0.55 and strategy == "mean_reversion",

    # Trend (for pullback)
    "no_trend_pb": trend_score < 0.75 and strategy == "pullback",

    # Stationarity
    "non_stationary": adf_pvalue > 0.10,

    # Account state
    "daily_loss_hit": daily_pnl < -0.03,
    "weekly_loss_hit": weekly_pnl < -0.07,
    "losing_streak": consecutive_losses >= 3,

    # Market conditions
    "wide_spread": spread > 0.0005,
    "low_volume": volume < avg_volume * 0.3,
    "pre_earnings": days_to_earnings < 2,
    "pre_fed": fed_meeting_today or fed_meeting_tomorrow,
}
```

## Emergency Protocols

### Immediate Exit Triggers
```python
def check_emergency_exit(position, market):
    # Unrealized loss > 3%
    if position.unrealized_pnl_pct < -0.03:
        return EXIT_IMMEDIATELY("Unrealized loss exceeded 3%")

    # Stop loss hit
    if position.current_price <= position.stop_loss:
        return EXIT_IMMEDIATELY("Stop loss triggered")

    # Regime change to bearish (for longs)
    if position.direction == "LONG" and market.regime == "trending_bearish":
        return EXIT_IMMEDIATELY("Regime turned bearish")

    # VIX spike
    if market.vix > 30 or market.vix_change > 0.40:
        return EXIT_IMMEDIATELY("VIX spike detected")

    # Gap against position
    if abs(market.gap_pct) > 0.02 and gap_direction_against_position:
        return EXIT_IMMEDIATELY("Adverse gap > 2%")

    return HOLD
```

### Daily Loss Halt
```python
def check_daily_limits(account):
    if account.daily_pnl < -0.05:
        HALT_ALL_TRADING()
        LOG("Daily loss limit hit: -5%")
        NOTIFY_USER("Trading halted for the day")
        return TRADING_HALTED

    if account.daily_trades >= 3:
        HALT_NEW_TRADES()
        LOG("Daily trade limit reached")
        return NO_NEW_TRADES

    return TRADING_ALLOWED
```

### Recovery Protocol
```python
def recovery_mode(account):
    """
    After significant drawdown, reduce risk.
    """
    if account.monthly_pnl < -0.10:
        return {
            "position_size": 0.50,  # Reduce to 50%
            "stop_distance": 0.003,  # Tighter 0.3% stops
            "required_confluence": 0.80,  # Higher bar
            "max_daily_trades": 1
        }

    if account.weekly_pnl < -0.05:
        return {
            "position_size": 0.75,
            "stop_distance": 0.004,
            "required_confluence": 0.75,
            "max_daily_trades": 2
        }

    return NORMAL_MODE
```

## Position Monitoring

### Real-Time Checks
```python
def monitor_position(position, market):
    checks = {
        "stop_intact": position.stop_order_active,
        "within_risk": position.unrealized_pnl_pct > -0.03,
        "regime_ok": market.regime != "adverse",
        "time_limit": position.bars_held < position.max_bars,
    }

    alerts = []

    if not checks["stop_intact"]:
        alerts.append(CRITICAL("Stop order not active!"))

    if not checks["within_risk"]:
        alerts.append(WARNING(f"Unrealized loss: {position.unrealized_pnl_pct:.1%}"))

    if not checks["regime_ok"]:
        alerts.append(WARNING("Regime turning adverse"))

    if not checks["time_limit"]:
        alerts.append(INFO("Time stop approaching"))

    return checks, alerts
```

## Integration

Uses:
- `~/projects/world-model/src/risk/manager.py`
- `~/projects/kymera-strategy/integration/risk_adjuster.py`

MCP tools:
- `validate_entry` - Pre-trade validation
- `calculate_position` - Position sizing

## Output Format

### Pre-Trade Validation
```yaml
validation:
  symbol: SPY
  direction: LONG
  position_pct: 0.95

  result: APPROVED  # or REJECTED

  checks:
    - name: "Confluence >= 0.70"
      status: PASS
      value: 0.76
    - name: "Z-score extreme"
      status: PASS
      value: -2.34
    - name: "VIX < 25"
      status: PASS
      value: 18.5
    # ... all checks

  passed: 12
  total: 12

  risk_summary:
    entry: 445.50
    stop: 443.25
    position_value: 4250.00
    shares: 9
    risk_per_share: 2.25
    total_risk: 20.25
    account_risk_pct: 0.45%
```

## Critical Reminders

1. **STOPS ARE MANDATORY** - No position without a stop
2. **NO AVERAGING DOWN** - Never add to a losing position
3. **RESPECT DAILY LIMITS** - -5% = done for the day
4. **ONE POSITION AT A TIME** - 95% means ONE trade
5. **REGIME AWARENESS** - Exit immediately on adverse regime change
6. **NO EMOTIONAL DECISIONS** - Follow the rules exactly
