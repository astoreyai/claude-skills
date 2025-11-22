# Kymera Risk Monitor

Real-time risk monitoring and enforcement across portfolio and MR systems. Implements hard stops, position limits, and daily loss limits - critical for GETY-like loss prevention.

## Key Features

**Hard Rules (Non-negotiable)**:
- Hard stop-loss: **-5%** (from GETY lesson)
- Max position size: **10%** per trade
- Daily loss limit: **-15%** (stops trading)
- MR concentration: **30%** max exposure
- Max concurrent positions: **5**

## Capabilities

- **Position Monitoring**: Real-time position tracking
- **Entry Validation**: Pre-trade risk assessment
- **Stop-Loss Enforcement**: Hard -5% stops
- **Daily Limit Tracking**: -15% daily max loss
- **Alert Generation**: Critical alerts for violations
- **GETY Scenario Testing**: Validates loss prevention

## Use Cases

1. **Monitor Open Position**
   ```
   /kymera-risk-monitor watch SYMBOL ENTRY CURRENT
   ```

2. **Validate Entry**
   ```
   /kymera-risk-monitor validate-entry SYMBOL PRICE WR
   ```

3. **Check Daily Limit**
   ```
   /kymera-risk-monitor daily-check
   ```

4. **GETY Scenario Test** ⭐ Critical
   ```
   /kymera-risk-monitor gety-test
   ```

## GETY Lesson Encoded

Original loss: -$699.47 (-56.7% of position, 71% of all profits)
**Damage prevented by risk monitor: 88.7%**

With proper position sizing (10% max) and -5% stop:
- Max loss per trade: ~$95
- Damage to profits: ~11%

## Integration

Works with:
- Risk adjuster module
- Unified dashboard
- Both portfolio and MR systems

## Compliance

Ensures adherence to:
- Hard stop-loss rule (-5%)
- Position sizing limits (10% max)
- Daily loss limits (-15%)
- Concentration limits (30% MR)

## Author

Aaron Storey | Kymera Strategy (Nov 2025) - **CRITICAL FOR SURVIVAL**
