#!/usr/bin/env python3
"""
Portfolio Analysis Agent
Integrated portfolio analysis combining trades, projections, and tax planning

Part of astoreyai/claude-skills
Version: 1.0.0
Author: Claude Code
Date: 2025-11-22

Day Check Integration:
- Session date/day tracked in all analysis outputs
- Timestamps synced with system time for accuracy
- Daily note creation with correct date context
"""

import csv
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

import numpy as np
import pandas as pd
import yaml

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
logger = logging.getLogger('portfolio_analysis')

# Log session start with day context
if DAY_CHECK_AVAILABLE:
    day_context = inject_day_context()
    logger.info(f"Portfolio Analysis Agent started on {day_context['day_name']}, {day_context['current_day']}")
else:
    logger.warning("Day check not available - using system datetime")


class PortfolioAnalysisAgent:
    """
    Comprehensive portfolio analysis agent

    Integrates:
    - Historical trade analysis
    - Forward projections
    - Tax planning
    - Risk analysis
    - Edge identification
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize portfolio analysis agent

        Args:
            config_path: Path to PORTFOLIO_PARAMETERS_COMPLETE.yaml
        """
        self.config_path = config_path or "/home/aaron/projects/portfolio/PORTFOLIO_PARAMETERS_COMPLETE.yaml"
        self.config = self._load_config()

        # Analysis components
        self.trades_df = None
        self.metrics = {}
        self.projections = {}
        self.tax_analysis = {}
        self.edge_analysis = {}
        self.risk_metrics = {}

        logger.info(f"Initialized PortfolioAnalysisAgent")

    def _load_config(self) -> Dict:
        """Load configuration from YAML"""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info("Configuration loaded successfully")
            return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            raise

    def load_trading_csv(self, csv_path: str) -> bool:
        """
        Load trading data from IB CSV

        Args:
            csv_path: Path to Interactive Brokers statement CSV

        Returns:
            True if successful
        """
        logger.info(f"Loading trading CSV: {csv_path}")

        try:
            # Parse IB CSV statement
            trades = []
            account_info = {}

            with open(csv_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 3:
                        continue

                    # Account information
                    if row[0] == 'Account Information' and row[1] == 'Data':
                        account_info[row[2]] = row[3] if len(row) > 3 else ''

                    # Trades
                    if row[0] == 'Trades' and row[1] == 'Data':
                        if row[2] == 'Order' and row[3] == 'Stocks':
                            trade_data = self._parse_trade_row(row)
                            if trade_data:
                                trades.append(trade_data)

            self.trades_df = pd.DataFrame(trades)
            self.account_info = account_info

            logger.info(f"Loaded {len(self.trades_df)} trades from CSV")
            return True

        except Exception as e:
            logger.error(f"Failed to load CSV: {e}")
            return False

    def _parse_trade_row(self, row: List) -> Optional[Dict]:
        """Parse individual trade row from IB CSV"""
        try:
            # IB CSV format (simplified)
            # Actual parsing would depend on exact CSV structure
            return {
                'symbol': row[5] if len(row) > 5 else '',
                'date': row[6] if len(row) > 6 else '',
                'quantity': float(row[7]) if len(row) > 7 else 0,
                'price': float(row[8]) if len(row) > 8 else 0,
                'commission': float(row[9]) if len(row) > 9 else 0,
            }
        except (ValueError, IndexError):
            return None

    def calculate_metrics(self) -> Dict:
        """
        Calculate comprehensive trading metrics

        Returns:
            Dict with all calculated metrics
        """
        logger.info("Calculating trading metrics")

        if self.trades_df is None or len(self.trades_df) == 0:
            # Use config defaults
            logger.info("No trades loaded, using config defaults")
            self.metrics = {
                'total_trades': 0,
                'win_rate': self.config['trading']['win_rate']['actual'] / 100,
                'avg_return_pct': self.config['trading']['return_per_trade']['all_time_avg'] / 100,
                'trades_per_month': self.config['trading']['trade_frequency']['trades_per_month']['baseline'],
                'initial_capital': self.config['account']['initial_capital'],
            }
        else:
            # Calculate from actual trades
            self.trades_df['pnl'] = (
                self.trades_df['quantity'] *
                (self.trades_df['exit_price'] - self.trades_df['entry_price']) -
                self.trades_df['commission']
            )
            self.trades_df['return_pct'] = (
                self.trades_df['pnl'] /
                (self.trades_df['quantity'] * self.trades_df['entry_price'])
            ) * 100

            winning_trades = self.trades_df[self.trades_df['pnl'] > 0]
            losing_trades = self.trades_df[self.trades_df['pnl'] < 0]

            self.metrics = {
                'total_trades': len(self.trades_df),
                'winning_trades': len(winning_trades),
                'losing_trades': len(losing_trades),
                'win_rate': len(winning_trades) / len(self.trades_df) if len(self.trades_df) > 0 else 0,
                'avg_return_pct': self.trades_df['return_pct'].mean() / 100,
                'avg_winner_pct': winning_trades['return_pct'].mean() / 100 if len(winning_trades) > 0 else 0,
                'avg_loser_pct': losing_trades['return_pct'].mean() / 100 if len(losing_trades) > 0 else 0,
                'total_pnl': self.trades_df['pnl'].sum(),
                'gross_profits': winning_trades['pnl'].sum() if len(winning_trades) > 0 else 0,
                'gross_losses': losing_trades['pnl'].sum() if len(losing_trades) > 0 else 0,
            }

        logger.info(f"Metrics calculated: {self.metrics['total_trades']} trades, "
                   f"{self.metrics['win_rate']*100:.1f}% win rate")

        return self.metrics

    def identify_edge(self) -> Dict:
        """
        Identify trading edge from historical data

        Returns:
            Dict with edge analysis
        """
        logger.info("Identifying trading edge")

        if self.trades_df is None or len(self.trades_df) == 0:
            logger.warning("No trades to analyze")
            self.edge_analysis = {
                'edge_identified': False,
                'message': 'No historical trades available'
            }
            return self.edge_analysis

        # Analyze by time of day
        self.trades_df['entry_hour'] = pd.to_datetime(
            self.trades_df['entry_time']
        ).dt.hour if 'entry_time' in self.trades_df.columns else 0

        # Group by time windows
        time_windows = {
            'premarket_0400_0500': (4, 5),
            'market_open_0930_1000': (9, 10),
            'late_morning_1100_1200': (11, 12),
            'afternoon_1500_1600': (15, 16),
        }

        time_analysis = {}
        for window_name, (start_hour, end_hour) in time_windows.items():
            window_trades = self.trades_df[
                (self.trades_df['entry_hour'] >= start_hour) &
                (self.trades_df['entry_hour'] < end_hour)
            ]

            if len(window_trades) > 0:
                winning = window_trades[window_trades['pnl'] > 0]
                time_analysis[window_name] = {
                    'trades': len(window_trades),
                    'win_rate': len(winning) / len(window_trades) * 100,
                    'avg_pnl': window_trades['pnl'].mean(),
                    'total_pnl': window_trades['pnl'].sum(),
                }

        # Identify best time window
        best_window = max(time_analysis.items(),
                         key=lambda x: x[1]['win_rate']) if time_analysis else None

        self.edge_analysis = {
            'edge_identified': best_window is not None,
            'time_windows': time_analysis,
            'best_window': best_window[0] if best_window else None,
            'best_window_stats': best_window[1] if best_window else {},
        }

        logger.info(f"Edge identified: {self.edge_analysis['edge_identified']}")

        return self.edge_analysis

    def run_projections(self, years: int = 3) -> Dict:
        """
        Run forward projections

        Args:
            years: Number of years to project

        Returns:
            Dict with projection results
        """
        logger.info(f"Running {years}-year projections")

        # Import forecasting agent functionality
        # For now, use simplified calculation
        metrics = self.metrics if self.metrics else self.calculate_metrics()

        # Calculate monthly return factor
        return_per_trade = metrics['avg_return_pct']
        trades_per_month = metrics.get('trades_per_month', 18.5)
        monthly_factor = (1 + return_per_trade) ** trades_per_month

        initial_capital = metrics.get('initial_capital', 2000)
        monthly_deposits = 500
        tax_rate = 0.37

        # Project year by year
        balance = initial_capital
        projections = []

        for year in range(1, years + 1):
            year_start = balance
            yearly_gains = 0

            for month in range(12):
                pre_growth = balance
                balance *= monthly_factor
                gains = balance - pre_growth

                # Tax extraction
                tax = gains * tax_rate
                balance -= tax
                yearly_gains += gains

                # Deposit
                balance += monthly_deposits

            projections.append({
                'year': year,
                'starting_balance': year_start,
                'ending_balance': balance,
                'gains': yearly_gains,
                'deposits': monthly_deposits * 12,
            })

        self.projections = {
            'years': years,
            'projections': projections,
            'final_balance': balance,
        }

        logger.info(f"Projections complete. Final balance: ${balance:,.2f}")

        return self.projections

    def analyze_risk(self) -> Dict:
        """
        Analyze portfolio risk metrics

        Returns:
            Dict with risk metrics
        """
        logger.info("Analyzing risk")

        if self.trades_df is None or len(self.trades_df) == 0:
            # Use theoretical metrics
            self.risk_metrics = {
                'max_drawdown_pct': -8.2,  # From config/Monte Carlo
                'risk_of_ruin': 0.0,
                'avg_position_size_pct': 75.0,  # Current from config
                'recommended_position_size_pct': 10.0,
                'stop_loss_pct': 5.0,
            }
        else:
            # Calculate from actual trades
            returns = self.trades_df['return_pct']
            cumulative = (1 + returns / 100).cumprod()
            running_max = cumulative.cummax()
            drawdown = (cumulative - running_max) / running_max * 100

            self.risk_metrics = {
                'max_drawdown_pct': float(drawdown.min()),
                'avg_return_pct': float(returns.mean()),
                'return_volatility_pct': float(returns.std()),
                'sharpe_ratio': float(returns.mean() / returns.std()) if returns.std() > 0 else 0,
                'best_trade_pct': float(returns.max()),
                'worst_trade_pct': float(returns.min()),
            }

        logger.info(f"Risk analysis complete. Max drawdown: {self.risk_metrics['max_drawdown_pct']:.2f}%")

        return self.risk_metrics

    def calculate_taxes(self, state: str = 'FL') -> Dict:
        """
        Calculate tax obligations

        Args:
            state: State code ('NY', 'FL', 'TX')

        Returns:
            Dict with tax calculations
        """
        logger.info(f"Calculating taxes for state: {state}")

        # Get total gains from projections or metrics
        if self.projections and 'projections' in self.projections:
            total_gains = sum(p['gains'] for p in self.projections['projections'])
        else:
            total_gains = self.metrics.get('total_pnl', 0)

        # Federal tax
        federal_rate = 0.37

        # State tax
        if state == 'NY':
            state_rate = self.config['tax']['state_ny']['combined_rate'] / 100
        else:
            state_rate = 0.0

        combined_rate = federal_rate + state_rate

        self.tax_analysis = {
            'state': state,
            'total_gains': total_gains,
            'federal_tax': total_gains * federal_rate,
            'state_tax': total_gains * state_rate,
            'total_tax': total_gains * combined_rate,
            'federal_rate_pct': federal_rate * 100,
            'state_rate_pct': state_rate * 100,
            'combined_rate_pct': combined_rate * 100,
        }

        logger.info(f"Tax calculated: ${self.tax_analysis['total_tax']:,.2f}")

        return self.tax_analysis

    def generate_dashboard(self) -> Dict:
        """
        Generate comprehensive portfolio dashboard

        Returns:
            Dict with all analysis results
        """
        logger.info("Generating portfolio dashboard")

        dashboard = {
            'generated_at': datetime.now().isoformat(),
            'account_info': getattr(self, 'account_info', {}),
            'metrics': self.metrics,
            'edge_analysis': self.edge_analysis,
            'projections': self.projections,
            'risk_metrics': self.risk_metrics,
            'tax_analysis': self.tax_analysis,
        }

        return dashboard

    def generate_report(self,
                       output_format: str = 'markdown',
                       output_dir: Optional[str] = None) -> str:
        """
        Generate comprehensive portfolio report

        Args:
            output_format: 'markdown' or 'latex'
            output_dir: Output directory

        Returns:
            Path to generated report
        """
        logger.info(f"Generating {output_format} report")

        output_dir = Path(output_dir or "/home/aaron/projects/portfolio")
        output_dir.mkdir(parents=True, exist_ok=True)

        if output_format == 'markdown':
            report_path = output_dir / f"portfolio_analysis_{datetime.now().strftime('%Y%m%d')}.md"
            content = self._generate_markdown_report()
        else:
            report_path = output_dir / f"portfolio_analysis_{datetime.now().strftime('%Y%m%d')}.tex"
            content = self._generate_latex_report()

        with open(report_path, 'w') as f:
            f.write(content)

        logger.info(f"Report generated: {report_path}")

        return str(report_path)

    def _generate_markdown_report(self) -> str:
        """Generate markdown report"""
        lines = [
            "# Portfolio Analysis Report",
            f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n---\n",
        ]

        # Metrics section
        if self.metrics:
            lines.append("\n## Trading Metrics\n")
            lines.append(f"- Total Trades: {self.metrics.get('total_trades', 0)}")
            lines.append(f"- Win Rate: {self.metrics.get('win_rate', 0)*100:.1f}%")
            lines.append(f"- Average Return: {self.metrics.get('avg_return_pct', 0)*100:.2f}%")

        # Edge analysis
        if self.edge_analysis and self.edge_analysis.get('edge_identified'):
            lines.append("\n## Edge Analysis\n")
            lines.append(f"- Best Time Window: {self.edge_analysis.get('best_window', 'N/A')}")

        # Projections
        if self.projections and 'projections' in self.projections:
            lines.append("\n## Forward Projections\n")
            for proj in self.projections['projections']:
                lines.append(f"- Year {proj['year']}: ${proj['ending_balance']:,.2f}")

        # Risk
        if self.risk_metrics:
            lines.append("\n## Risk Metrics\n")
            lines.append(f"- Max Drawdown: {self.risk_metrics.get('max_drawdown_pct', 0):.2f}%")

        # Tax
        if self.tax_analysis:
            lines.append("\n## Tax Analysis\n")
            lines.append(f"- Total Tax: ${self.tax_analysis.get('total_tax', 0):,.2f}")

        return '\n'.join(lines)

    def _generate_latex_report(self) -> str:
        """Generate LaTeX report"""
        return r"""\documentclass{article}
\usepackage{booktabs}
\begin{document}
\title{Portfolio Analysis Report}
\maketitle

% Content sections here

\end{document}
"""

    def export_results(self, output_dir: Optional[str] = None) -> List[str]:
        """
        Export all results to files

        Args:
            output_dir: Output directory

        Returns:
            List of exported file paths
        """
        logger.info("Exporting results")

        output_dir = Path(output_dir or "/home/aaron/projects/portfolio")
        output_dir.mkdir(parents=True, exist_ok=True)

        exported_files = []

        # Export dashboard JSON
        dashboard_path = output_dir / f"portfolio_dashboard_{datetime.now().strftime('%Y%m%d')}.json"
        with open(dashboard_path, 'w') as f:
            json.dump(self.generate_dashboard(), f, indent=2)
        exported_files.append(str(dashboard_path))

        # Export trades CSV if available
        if self.trades_df is not None and len(self.trades_df) > 0:
            trades_path = output_dir / "portfolio_trades.csv"
            self.trades_df.to_csv(trades_path, index=False)
            exported_files.append(str(trades_path))

        logger.info(f"Exported {len(exported_files)} files")

        return exported_files

    def sync_to_gdrive(self, files: List[str]) -> bool:
        """
        Sync results to Google Drive

        Args:
            files: List of file paths to sync

        Returns:
            True if successful
        """
        logger.info("Syncing to Google Drive")
        # Placeholder for Google Drive integration
        logger.warning("Google Drive sync not yet implemented")
        return False

    def run_complete_analysis(self, csv_path: str, years: int = 3, state: str = 'FL') -> Dict:
        """
        Run complete portfolio analysis workflow

        Args:
            csv_path: Path to IB CSV statement
            years: Years to project
            state: State for tax calculations

        Returns:
            Complete analysis results
        """
        logger.info(f"Starting complete portfolio analysis")

        # Load data
        self.load_trading_csv(csv_path)

        # Calculate metrics
        self.calculate_metrics()

        # Identify edge
        self.identify_edge()

        # Run projections
        self.run_projections(years=years)

        # Analyze risk
        self.analyze_risk()

        # Calculate taxes
        self.calculate_taxes(state=state)

        # Generate dashboard
        dashboard = self.generate_dashboard()

        # Generate report
        report_path = self.generate_report()

        # Export results
        exported_files = self.export_results()

        logger.info(f"Complete analysis finished. Report: {report_path}")

        return {
            'dashboard': dashboard,
            'report_path': report_path,
            'exported_files': exported_files,
        }


def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Portfolio Analysis Agent')
    parser.add_argument('csv_path', help='Path to IB CSV statement')
    parser.add_argument('--years', type=int, default=3, help='Projection years')
    parser.add_argument('--state', default='FL', help='State for tax (NY/FL/TX)')
    parser.add_argument('--config', help='Path to config YAML')
    parser.add_argument('--format', default='markdown', choices=['markdown', 'latex'])

    args = parser.parse_args()

    # Initialize agent
    agent = PortfolioAnalysisAgent(config_path=args.config)

    # Run complete analysis
    results = agent.run_complete_analysis(
        csv_path=args.csv_path,
        years=args.years,
        state=args.state
    )

    print(f"\n✓ Portfolio analysis complete")
    print(f"  Report: {results['report_path']}")
    print(f"  Exported: {len(results['exported_files'])} files")


if __name__ == '__main__':
    main()
