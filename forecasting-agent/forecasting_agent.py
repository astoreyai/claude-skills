#!/usr/bin/env python3
"""
Portfolio Forecasting Agent
Multi-year portfolio projections with Monte Carlo simulations, tax planning, and risk analysis

Part of astoreyai/claude-skills
Version: 1.0.0
Author: Claude Code
Date: 2025-11-22

Day Check Integration:
- Automatically injects current date/day into all analysis
- Session timestamp tracked in logs and reports
- Date context available to all agents/skills
"""

import csv
import json
import logging
import numpy as np
import pandas as pd
import yaml
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

# Day check integration
try:
    day_check_path = Path.home() / ".local" / "lib"
    sys.path.insert(0, str(day_check_path))
    from day_check import inject_day_context, DayCheck
    DAY_CHECK_AVAILABLE = True
except ImportError:
    DAY_CHECK_AVAILABLE = False


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('forecasting_agent')

# Log session start with day context
if DAY_CHECK_AVAILABLE:
    day_context = inject_day_context()
    logger.info(f"Forecasting Agent started on {day_context['day_name']}, {day_context['current_day']}")
else:
    logger.warning("Day check not available - using system datetime")


@dataclass
class ForecastParams:
    """Portfolio forecasting parameters"""
    initial_capital: float
    monthly_deposits: float
    trades_per_month: float
    win_rate: float
    avg_winner_pct: float
    avg_loser_pct: float
    tax_rate: float
    forecast_years: int
    scenario_name: str


@dataclass
class MonteCarloParams:
    """Monte Carlo simulation parameters"""
    paths: int
    months: int
    trades_per_month: float
    win_probability: float
    avg_winner_pct: float
    avg_loser_pct: float
    monthly_deposits: float
    initial_capital: float


class PortfolioForecastingAgent:
    """Main forecasting agent for portfolio projections"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize forecasting agent

        Args:
            config_path: Path to PORTFOLIO_PARAMETERS_COMPLETE.yaml
        """
        self.config_path = config_path or "/home/aaron/projects/portfolio/PORTFOLIO_PARAMETERS_COMPLETE.yaml"
        self.config = self._load_config()
        self.results = {}

        logger.info(f"Initialized PortfolioForecastingAgent with config: {self.config_path}")

    def _load_config(self) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info("Configuration loaded successfully")
            return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            raise

    def load_trading_data(self, csv_path: str) -> pd.DataFrame:
        """
        Load trading metrics from IB CSV

        Args:
            csv_path: Path to Interactive Brokers CSV statement

        Returns:
            DataFrame with trading metrics
        """
        logger.info(f"Loading trading data from: {csv_path}")

        try:
            # Parse IB CSV
            trades = []
            with open(csv_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 3:
                        continue
                    if row[0] == 'Trades' and row[1] == 'Data' and row[2] == 'Order':
                        # Extract trade data
                        # This is simplified - extend based on actual CSV format
                        trades.append({
                            'symbol': row[5] if len(row) > 5 else '',
                            'date': row[6] if len(row) > 6 else '',
                            'quantity': float(row[7]) if len(row) > 7 else 0,
                            'price': float(row[8]) if len(row) > 8 else 0,
                        })

            df = pd.DataFrame(trades)
            logger.info(f"Loaded {len(df)} trades from CSV")
            return df

        except Exception as e:
            logger.error(f"Failed to load trading data: {e}")
            raise

    def calculate_metrics(self, trades_df: Optional[pd.DataFrame] = None) -> Dict:
        """
        Calculate trading metrics from CSV or use config defaults

        Args:
            trades_df: Optional DataFrame with trades

        Returns:
            Dict with calculated metrics
        """
        if trades_df is not None and len(trades_df) > 0:
            # Calculate from actual trades
            logger.info("Calculating metrics from actual trades")
            # Implementation would go here
            metrics = {}
        else:
            # Use config defaults
            logger.info("Using config defaults for metrics")
            metrics = {
                'win_rate': self.config['trading']['win_rate']['actual'] / 100,
                'avg_winner_pct': self.config['trading']['return_per_trade']['all_time_avg'] / 100,
                'avg_loser_pct': self.config['trading']['loss_parameters']['avg_loser_pct'] / 100,
                'trades_per_month': self.config['trading']['trade_frequency']['trades_per_month']['baseline'],
                'initial_capital': self.config['account']['initial_capital'],
                'monthly_deposits': self.config['account']['monthly_deposits'],
            }

        return metrics

    def run_projection(self,
                      years: int = 3,
                      scenario: str = 'baseline',
                      extract_tax: bool = True) -> Tuple[pd.DataFrame, pd.DataFrame, Dict]:
        """
        Run multi-year portfolio projection

        Args:
            years: Number of years to project (3 or 5)
            scenario: 'conservative', 'baseline', or 'aggressive'
            extract_tax: Whether to extract quarterly tax reserves

        Returns:
            (monthly_df, quarterly_df, summary_dict)
        """
        logger.info(f"Running {years}-year {scenario} projection")

        # Get scenario parameters
        if scenario == 'conservative':
            trades_per_month = self.config['trading']['trade_frequency']['trades_per_month']['conservative']
        elif scenario == 'aggressive':
            trades_per_month = self.config['trading']['trade_frequency']['trades_per_month']['aggressive']
        else:
            trades_per_month = self.config['trading']['trade_frequency']['trades_per_month']['baseline']

        # Build params
        params = ForecastParams(
            initial_capital=self.config['account']['initial_capital'],
            monthly_deposits=self.config['account']['monthly_deposits'],
            trades_per_month=trades_per_month,
            win_rate=self.config['trading']['win_rate']['actual'] / 100,
            avg_winner_pct=self.config['trading']['return_per_trade']['all_time_avg'] / 100,
            avg_loser_pct=self.config['trading']['loss_parameters']['avg_loser_pct'] / 100,
            tax_rate=self.config['tax']['quarterly_extraction_pct'] / 100 if extract_tax else 0,
            forecast_years=years,
            scenario_name=scenario
        )

        # Run projection
        monthly_df, quarterly_df, summary = self._forecast_with_params(params)

        # Store results
        self.results[f'{scenario}_{years}y'] = {
            'monthly': monthly_df,
            'quarterly': quarterly_df,
            'summary': summary,
            'params': asdict(params)
        }

        logger.info(f"Projection complete. Final balance: ${summary['final_balance']:,.2f}")

        return monthly_df, quarterly_df, summary

    def _forecast_with_params(self, params: ForecastParams) -> Tuple[pd.DataFrame, pd.DataFrame, Dict]:
        """
        Internal forecast calculation

        Args:
            params: ForecastParams object

        Returns:
            (monthly_df, quarterly_df, summary)
        """
        # Calculate monthly compounding factor
        # Formula: (1 + avg_winner_pct)^trades_per_month * win_rate +
        #          (1 + avg_loser_pct)^trades_per_month * (1 - win_rate)
        # Simplified to: (1 + return_per_trade)^trades_per_month
        return_per_trade = params.avg_winner_pct
        monthly_factor = (1 + return_per_trade) ** params.trades_per_month

        total_months = params.forecast_years * 12
        periods_data = []

        balance = params.initial_capital
        tax_reserve = 0.0
        cumulative_gains = 0.0
        cumulative_taxes = 0.0

        for month in range(1, total_months + 1):
            # Calculate gains this month
            pre_growth = balance
            balance_after_growth = balance * monthly_factor
            gains_this_month = balance_after_growth - balance

            # Extract tax if enabled
            if params.tax_rate > 0:
                tax_this_month = gains_this_month * params.tax_rate
                cumulative_taxes += tax_this_month
                tax_reserve += tax_this_month
                balance = balance_after_growth - tax_this_month
            else:
                tax_this_month = 0
                balance = balance_after_growth

            # Add monthly deposit
            balance += params.monthly_deposits

            # Track cumulative
            cumulative_gains += gains_this_month

            periods_data.append({
                'Month': month,
                'Year': (month - 1) // 12 + 1,
                'Quarter': f"Y{(month - 1) // 12 + 1}Q{((month - 1) % 12) // 3 + 1}",
                'Starting_Balance': pre_growth,
                'Monthly_Factor': monthly_factor,
                'Balance_After_Growth': balance_after_growth,
                'Gains_This_Month': gains_this_month,
                'Tax_Extracted': tax_this_month,
                'Deposit': params.monthly_deposits,
                'Ending_Balance': balance,
                'Cumulative_Gains': cumulative_gains,
                'Cumulative_Taxes': cumulative_taxes,
                'Tax_Reserve': tax_reserve,
            })

        # Create DataFrames
        monthly_df = pd.DataFrame(periods_data)

        # Quarterly summary
        quarterly_data = []
        for year in range(1, params.forecast_years + 1):
            for quarter in range(1, 5):
                month_end = year * 12 if quarter == 4 else (year - 1) * 12 + quarter * 3
                if month_end > total_months:
                    continue

                row = periods_data[month_end - 1]
                month_start = (year - 1) * 12 + (quarter - 1) * 3 + 1

                if month_start > 1:
                    start_row = periods_data[month_start - 2]
                    q_gains = row['Cumulative_Gains'] - start_row['Cumulative_Gains']
                    q_taxes = row['Cumulative_Taxes'] - start_row['Cumulative_Taxes']
                    start_balance = start_row['Ending_Balance']
                else:
                    q_gains = row['Cumulative_Gains']
                    q_taxes = row['Cumulative_Taxes']
                    start_balance = params.initial_capital

                quarterly_data.append({
                    'Quarter': f'Y{year}Q{quarter}',
                    'Starting_Balance': start_balance,
                    'Deposits': params.monthly_deposits * 3,
                    'Gains': q_gains,
                    'Tax_Reserved': q_taxes,
                    'Net_Gains': q_gains - q_taxes,
                    'Ending_Balance': row['Ending_Balance'],
                    'Tax_Reserve_Account': row['Tax_Reserve'],
                })

        quarterly_df = pd.DataFrame(quarterly_data)

        # Summary
        final_row = periods_data[-1]
        summary = {
            'scenario': params.scenario_name,
            'years': params.forecast_years,
            'final_balance': final_row['Ending_Balance'],
            'total_gains': final_row['Cumulative_Gains'],
            'total_taxes_reserved': final_row['Cumulative_Taxes'],
            'tax_reserve_account': final_row['Tax_Reserve'],
            'liquid_net_worth': final_row['Ending_Balance'] + final_row['Tax_Reserve'],
            'total_deposits': params.monthly_deposits * total_months,
            'capital_invested': params.initial_capital + (params.monthly_deposits * total_months),
            'roi_pct': ((final_row['Ending_Balance'] - params.initial_capital) / params.initial_capital) * 100,
        }

        return monthly_df, quarterly_df, summary

    def run_monte_carlo(self,
                       months: int = 60,
                       paths: int = 1000,
                       scenario: str = 'baseline') -> Dict:
        """
        Run Monte Carlo simulation

        Args:
            months: Simulation duration in months
            paths: Number of simulation paths
            scenario: Scenario name for params

        Returns:
            Dict with simulation results
        """
        logger.info(f"Running Monte Carlo: {paths} paths × {months} months")

        # Get parameters
        params = MonteCarloParams(
            paths=paths,
            months=months,
            trades_per_month=self.config['trading']['trade_frequency']['trades_per_month']['baseline'],
            win_probability=self.config['trading']['win_rate']['actual'] / 100,
            avg_winner_pct=self.config['trading']['return_per_trade']['all_time_avg'] / 100,
            avg_loser_pct=self.config['trading']['loss_parameters']['avg_loser_pct'] / 100,
            monthly_deposits=self.config['account']['monthly_deposits'],
            initial_capital=self.config['account']['initial_capital'],
        )

        # Run simulation
        final_balances = []
        all_paths = np.zeros((paths, months))

        for path_idx in range(paths):
            balance = params.initial_capital
            path_balances = []

            for month in range(months):
                # Simulate trades for this month
                for _ in range(int(params.trades_per_month)):
                    if np.random.random() < params.win_probability:
                        # Win
                        balance *= (1 + params.avg_winner_pct)
                    else:
                        # Loss
                        balance *= (1 + params.avg_loser_pct)

                # Add deposit
                balance += params.monthly_deposits
                path_balances.append(balance)

            all_paths[path_idx] = path_balances
            final_balances.append(balance)

        # Calculate statistics
        final_balances = np.array(final_balances)

        results = {
            'paths': paths,
            'months': months,
            'final_balance': {
                'mean': float(np.mean(final_balances)),
                'median': float(np.median(final_balances)),
                'std': float(np.std(final_balances)),
                'min': float(np.min(final_balances)),
                'max': float(np.max(final_balances)),
                'percentile_5': float(np.percentile(final_balances, 5)),
                'percentile_25': float(np.percentile(final_balances, 25)),
                'percentile_75': float(np.percentile(final_balances, 75)),
                'percentile_95': float(np.percentile(final_balances, 95)),
            },
            'milestones': {
                '1M': float(np.sum(final_balances >= 1_000_000) / paths * 100),
                '10M': float(np.sum(final_balances >= 10_000_000) / paths * 100),
                '100M': float(np.sum(final_balances >= 100_000_000) / paths * 100),
                '500M': float(np.sum(final_balances >= 500_000_000) / paths * 100),
                '1B': float(np.sum(final_balances >= 1_000_000_000) / paths * 100),
            },
            'risk_metrics': {
                'risk_of_ruin': float(np.sum(final_balances < params.initial_capital) / paths * 100),
                'prob_profit': float(np.sum(final_balances > params.initial_capital) / paths * 100),
            },
            'all_paths': all_paths.tolist(),
        }

        logger.info(f"Monte Carlo complete. Median final balance: ${results['final_balance']['median']:,.2f}")

        return results

    def analyze_risk(self, projection_results: Dict) -> Dict:
        """
        Analyze risk metrics from projection

        Args:
            projection_results: Results from run_projection()

        Returns:
            Dict with risk metrics
        """
        logger.info("Analyzing risk metrics")

        monthly_df = projection_results['monthly']

        # Calculate month-over-month changes
        monthly_df['Monthly_Return_Pct'] = (
            (monthly_df['Ending_Balance'] / monthly_df['Starting_Balance']) - 1
        ) * 100

        # Drawdown analysis
        monthly_df['Peak'] = monthly_df['Ending_Balance'].cummax()
        monthly_df['Drawdown_Pct'] = (
            (monthly_df['Ending_Balance'] - monthly_df['Peak']) / monthly_df['Peak']
        ) * 100

        risk_metrics = {
            'max_drawdown_pct': float(monthly_df['Drawdown_Pct'].min()),
            'avg_monthly_return_pct': float(monthly_df['Monthly_Return_Pct'].mean()),
            'monthly_volatility_pct': float(monthly_df['Monthly_Return_Pct'].std()),
            'sharpe_ratio_approx': float(
                monthly_df['Monthly_Return_Pct'].mean() /
                monthly_df['Monthly_Return_Pct'].std()
                if monthly_df['Monthly_Return_Pct'].std() > 0 else 0
            ),
            'best_month_pct': float(monthly_df['Monthly_Return_Pct'].max()),
            'worst_month_pct': float(monthly_df['Monthly_Return_Pct'].min()),
        }

        logger.info(f"Risk analysis complete. Max drawdown: {risk_metrics['max_drawdown_pct']:.2f}%")

        return risk_metrics

    def forecast_taxes(self, projection_results: Dict, state: str = 'FL') -> Dict:
        """
        Forecast tax obligations

        Args:
            projection_results: Results from run_projection()
            state: State code ('NY', 'FL', 'TX')

        Returns:
            Dict with tax forecasts
        """
        logger.info(f"Forecasting taxes for state: {state}")

        quarterly_df = projection_results['quarterly']

        # Federal tax
        federal_rate = 0.37  # Top bracket

        # State tax
        if state == 'NY':
            state_rate = self.config['tax']['state_ny']['combined_rate'] / 100
        else:
            state_rate = 0.0  # FL/TX

        combined_rate = federal_rate + state_rate

        # Calculate quarterly payments
        quarterly_df['Federal_Tax'] = quarterly_df['Gains'] * federal_rate
        quarterly_df['State_Tax'] = quarterly_df['Gains'] * state_rate
        quarterly_df['Total_Tax_Due'] = quarterly_df['Gains'] * combined_rate

        tax_forecast = {
            'state': state,
            'federal_rate': federal_rate,
            'state_rate': state_rate,
            'combined_rate': combined_rate,
            'quarterly_payments': quarterly_df[['Quarter', 'Total_Tax_Due']].to_dict('records'),
            'total_tax_liability': float(quarterly_df['Total_Tax_Due'].sum()),
            'total_gains': float(quarterly_df['Gains'].sum()),
            'effective_rate': float(quarterly_df['Total_Tax_Due'].sum() / quarterly_df['Gains'].sum())
            if quarterly_df['Gains'].sum() > 0 else 0,
        }

        logger.info(f"Tax forecast complete. Total liability: ${tax_forecast['total_tax_liability']:,.2f}")

        return tax_forecast

    def generate_report(self,
                       output_format: str = 'markdown',
                       output_dir: Optional[str] = None) -> str:
        """
        Generate comprehensive forecast report

        Args:
            output_format: 'markdown' or 'latex'
            output_dir: Output directory (default: portfolio project dir)

        Returns:
            Path to generated report
        """
        logger.info(f"Generating {output_format} report")

        output_dir = Path(output_dir or "/home/aaron/projects/portfolio")
        output_dir.mkdir(parents=True, exist_ok=True)

        if output_format == 'markdown':
            report_path = output_dir / f"portfolio_forecast_{datetime.now().strftime('%Y%m%d')}.md"
            content = self._generate_markdown_report()
        else:
            report_path = output_dir / f"portfolio_forecast_{datetime.now().strftime('%Y%m%d')}.tex"
            content = self._generate_latex_report()

        with open(report_path, 'w') as f:
            f.write(content)

        logger.info(f"Report generated: {report_path}")

        return str(report_path)

    def _generate_markdown_report(self) -> str:
        """Generate markdown report content"""
        lines = [
            "# Portfolio Forecast Report",
            f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n---\n",
            "\n## Summary\n",
        ]

        for key, result in self.results.items():
            lines.append(f"\n### {key}\n")
            lines.append(f"- Final Balance: ${result['summary']['final_balance']:,.2f}")
            lines.append(f"- Total Gains: ${result['summary']['total_gains']:,.2f}")
            lines.append(f"- ROI: {result['summary']['roi_pct']:.2f}%")

        return '\n'.join(lines)

    def _generate_latex_report(self) -> str:
        """Generate LaTeX report content"""
        # Simplified LaTeX template
        return r"""\documentclass{article}
\begin{document}
\title{Portfolio Forecast Report}
\maketitle
% Content here
\end{document}
"""

    def export_results(self, output_dir: Optional[str] = None) -> List[str]:
        """
        Export all results to CSV files

        Args:
            output_dir: Output directory

        Returns:
            List of exported file paths
        """
        logger.info("Exporting results to CSV")

        output_dir = Path(output_dir or "/home/aaron/projects/portfolio")
        output_dir.mkdir(parents=True, exist_ok=True)

        exported_files = []

        for key, result in self.results.items():
            # Export monthly data
            monthly_path = output_dir / f"forecast_{key}_monthly.csv"
            result['monthly'].to_csv(monthly_path, index=False)
            exported_files.append(str(monthly_path))

            # Export quarterly data
            quarterly_path = output_dir / f"forecast_{key}_quarterly.csv"
            result['quarterly'].to_csv(quarterly_path, index=False)
            exported_files.append(str(quarterly_path))

        logger.info(f"Exported {len(exported_files)} files")

        return exported_files

    def sync_to_gdrive(self, files: List[str]) -> bool:
        """
        Sync results to Google Drive (placeholder)

        Args:
            files: List of file paths to sync

        Returns:
            True if successful
        """
        logger.info("Syncing to Google Drive")
        # Implementation would use google-drive MCP server
        # For now, just log
        logger.warning("Google Drive sync not yet implemented")
        return False


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Portfolio Forecasting Agent')
    parser.add_argument('--config', help='Path to config YAML')
    parser.add_argument('--years', type=int, default=3, help='Forecast years')
    parser.add_argument('--scenario', default='baseline', choices=['conservative', 'baseline', 'aggressive'])
    parser.add_argument('--monte-carlo', action='store_true', help='Run Monte Carlo simulation')
    parser.add_argument('--output', default='markdown', choices=['markdown', 'latex'])

    args = parser.parse_args()

    # Initialize agent
    agent = PortfolioForecastingAgent(config_path=args.config)

    # Run projection
    monthly_df, quarterly_df, summary = agent.run_projection(
        years=args.years,
        scenario=args.scenario
    )

    # Run Monte Carlo if requested
    if args.monte_carlo:
        mc_results = agent.run_monte_carlo(months=args.years * 12)
        print(f"\nMonte Carlo Results:")
        print(f"  Median final balance: ${mc_results['final_balance']['median']:,.2f}")
        print(f"  95th percentile: ${mc_results['final_balance']['percentile_95']:,.2f}")

    # Generate report
    report_path = agent.generate_report(output_format=args.output)

    print(f"\n✓ Forecast complete")
    print(f"  Final balance: ${summary['final_balance']:,.2f}")
    print(f"  Report: {report_path}")


if __name__ == '__main__':
    main()
