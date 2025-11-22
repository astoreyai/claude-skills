# Kymera Tax Optimizer

Manages quarterly tax planning and extraction for the trading strategy. Ensures tax compliance and optimizes extraction timing.

## Capabilities

- **Quarterly Tax Calculation**: Federal + state tax calculation
- **Tax Extraction**: 37% safety margin extraction to reserve
- **Tax-Loss Harvesting**: Identify harvesting opportunities
- **Annual Projections**: Project year-end tax liability
- **Payment Scheduling**: Estimated quarterly payment schedule
- **Compliance Tracking**: Filing requirement tracking

## Use Cases

1. **Process Quarterly P&L**
   ```
   /kymera-tax-optimizer quarter Q1
   ```

2. **Project Annual Tax**
   ```
   /kymera-tax-optimizer project-annual
   ```

3. **Tax-Loss Harvesting**
   ```
   /kymera-tax-optimizer harvest-losses
   ```

4. **Annual Summary**
   ```
   /kymera-tax-optimizer annual-summary
   ```

## Key Parameters

**Extraction Rate**: 37% safety margin
- Covers federal taxes (up to 37%)
- Covers state taxes (e.g., 5% CA)
- Safety buffer for unexpected liability

**Payment Schedule**:
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: January 15 (next year)

## Tax Categories

- **Short-term gains** (<1 year): Ordinary income rates
- **Long-term gains** (≥1 year): Preferential rates (15%)
- **Net Investment Income Tax** (NIIT): 3.8% on excess over $200k
- **State taxes**: Varies by state (5% for CA)

## Integration

Works with:
- Portfolio and MR trading systems
- Risk adjuster
- Unified dashboard
- Annual planning

## Compliance

Generates documents for:
- Form 8949 (Sales of Capital Assets)
- Schedule D (Capital Gains and Losses)
- Form 1040 (Income Tax Return)
- Quarterly estimated payments

## Author

Aaron Storey | Kymera Strategy (Nov 2025)
