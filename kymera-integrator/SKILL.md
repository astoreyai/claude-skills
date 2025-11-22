# Kymera Strategy Integrator

Manages bidirectional integration between portfolio and mean-reversion systems. Orchestrates data flow, monitors system health, and enables unified operation.

## Capabilities

- **Bidirectional Data Flow**: Portfolio metrics → MR parameters, MR trades → portfolio projections
- **System Correlation**: Detect divergence between systems
- **Health Monitoring**: Real-time monitoring of both systems
- **Capital Allocation**: Dynamic rebalancing recommendations
- **Integration Issues**: Detect and report integration problems

## Use Cases

1. **Run Integration Cycle**
   ```
   /kymera-integrator sync
   ```

2. **Check System Alignment**
   ```
   /kymera-integrator check-alignment
   ```

3. **Generate Integration Report**
   ```
   /kymera-integrator report
   ```

## Integration Points

- Portfolio → Strategy: Metrics extraction, parameter configuration
- Strategy → Portfolio: Trade results, correlation analysis
- Risk Management: Enforcement across both systems
- Monitoring: Unified dashboard

## Health Checks

- Win rate correlation (target: <10% divergence)
- Profit factor alignment
- System-specific alerts
- Rebalancing triggers

## Author

Aaron Storey | Kymera Strategy (Nov 2025)
