#!/usr/bin/env python3
"""
Trading Analysis Agent
Comprehensive trading performance analysis and edge identification
For Interactive Brokers CSV statements

Part of astoreyai/claude-skills trading-analysis skill
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict


@dataclass
class Trade:
    """Individual trade data"""
    symbol: str
    entry_date: str
    entry_price: float
    exit_date: str
    exit_price: float
    quantity: int
    commission: float
    realized_pnl: float
    holding_period_minutes: int
    return_pct: float
    category: str  # 'intraday' or 'swing'


class TradingAnalysisAgent:
    """Main trading analysis agent"""

    def __init__(self, csv_path: str):
        """Initialize with IB statement CSV"""
        self.csv_path = Path(csv_path)
        self.trades: List[Trade] = []
        self.account_info = {}
        self.capital = 0
        self.deposits = 0

    def parse_csv(self) -> bool:
        """Parse IB CSV statement"""
        try:
            with open(self.csv_path, 'r') as f:
                reader = csv.reader(f)
                section = None

                for row in reader:
                    if len(row) < 3:
                        continue

                    # Parse account info
                    if row[0] == 'Account Information' and row[1] == 'Data':
                        self.account_info[row[2]] = row[3]

                    # Parse trades
                    if row[0] == 'Trades' and row[1] == 'Data':
                        self._parse_trade_row(row)

                    # Parse deposits
                    if row[0] == 'Deposits & Withdrawals' and row[1] == 'Data':
                        self._parse_deposit_row(row)

                return True
        except Exception as e:
            print(f"Error parsing CSV: {e}")
            return False

    def _parse_trade_row(self, row: List) -> None:
        """Parse individual trade row"""
        if len(row) < 10:
            return
        if row[2] != 'Order' or row[3] != 'Stocks':
            return

        symbol = row[5]
        try:
            quantity = int(row[7])
            entry_price = float(row[8])
            # Parse more fields as needed
            # This is a simplified version
        except (ValueError, IndexError):
            pass

    def _parse_deposit_row(self, row: List) -> None:
        """Parse deposit/withdrawal"""
        try:
            amount = float(row[3])
            if amount > 0:
                self.deposits += amount
        except (ValueError, IndexError):
            pass

    def calculate_metrics(self) -> Dict:
        """Calculate all trading metrics"""
        if not self.trades:
            return {}

        metrics = {
            'total_trades': len(self.trades),
            'winning_trades': len([t for t in self.trades if t.realized_pnl > 0]),
            'losing_trades': len([t for t in self.trades if t.realized_pnl < 0]),
            'win_rate': 0,
            'total_gross_wins': 0,
            'total_gross_losses': 0,
            'profit_factor': 0,
            'avg_winner': 0,
            'avg_loser': 0,
            'largest_win': 0,
            'largest_loss': 0,
            'net_pnl': 0,
            'avg_holding_minutes': 0,
        }

        wins = [t for t in self.trades if t.realized_pnl > 0]
        losses = [t for t in self.trades if t.realized_pnl < 0]

        if wins:
            metrics['total_gross_wins'] = sum(t.realized_pnl for t in wins)
            metrics['avg_winner'] = metrics['total_gross_wins'] / len(wins)
            metrics['largest_win'] = max(t.realized_pnl for t in wins)

        if losses:
            metrics['total_gross_losses'] = sum(t.realized_pnl for t in losses)
            metrics['avg_loser'] = metrics['total_gross_losses'] / len(losses)
            metrics['largest_loss'] = min(t.realized_pnl for t in losses)

        if len(self.trades) > 0:
            metrics['win_rate'] = len(wins) / len(self.trades)

        if metrics['total_gross_losses'] != 0:
            metrics['profit_factor'] = metrics['total_gross_wins'] / abs(metrics['total_gross_losses'])

        metrics['net_pnl'] = metrics['total_gross_wins'] + metrics['total_gross_losses']

        if len(self.trades) > 0:
            metrics['avg_holding_minutes'] = sum(t.holding_period_minutes for t in self.trades) / len(self.trades)

        return metrics

    def analyze_edge(self) -> Dict:
        """Identify trading edges"""
        edge_analysis = {
            'intraday_trades': [],
            'swing_trades': [],
            'intraday_stats': {},
            'swing_stats': {},
            'symbol_stats': {},
            'time_analysis': {},
        }

        # Categorize trades
        intraday = [t for t in self.trades if t.category == 'intraday']
        swing = [t for t in self.trades if t.category == 'swing']

        edge_analysis['intraday_trades'] = intraday
        edge_analysis['swing_trades'] = swing

        # Calculate stats by category
        if intraday:
            edge_analysis['intraday_stats'] = {
                'count': len(intraday),
                'win_rate': len([t for t in intraday if t.realized_pnl > 0]) / len(intraday),
                'total_pnl': sum(t.realized_pnl for t in intraday),
                'avg_return': sum(t.return_pct for t in intraday) / len(intraday),
            }

        if swing:
            edge_analysis['swing_stats'] = {
                'count': len(swing),
                'win_rate': len([t for t in swing if t.realized_pnl > 0]) / len(swing),
                'total_pnl': sum(t.realized_pnl for t in swing),
                'avg_return': sum(t.return_pct for t in swing) / len(swing),
            }

        # Symbol stats
        symbols = {}
        for trade in self.trades:
            if trade.symbol not in symbols:
                symbols[trade.symbol] = {'count': 0, 'pnl': 0, 'returns': []}
            symbols[trade.symbol]['count'] += 1
            symbols[trade.symbol]['pnl'] += trade.realized_pnl
            symbols[trade.symbol]['returns'].append(trade.return_pct)

        for symbol, data in symbols.items():
            edge_analysis['symbol_stats'][symbol] = {
                'trades': data['count'],
                'total_pnl': data['pnl'],
                'avg_return': sum(data['returns']) / len(data['returns']),
            }

        return edge_analysis

    def generate_markdown_report(self) -> str:
        """Generate markdown analysis report"""
        metrics = self.calculate_metrics()
        edge = self.analyze_edge()

        report = f"""# Trading Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Account: {self.account_info.get('Account', 'Unknown')}

## Executive Summary

- **Total Trades**: {metrics['total_trades']}
- **Win Rate**: {metrics['win_rate']:.1%}
- **Net P&L**: ${metrics['net_pnl']:.2f}
- **Profit Factor**: {metrics['profit_factor']:.2f}
- **Avg Winner**: ${metrics['avg_winner']:.2f}
- **Avg Loser**: ${metrics['avg_loser']:.2f}
- **Avg Holding Period**: {metrics['avg_holding_minutes']:.0f} minutes

## Edge Analysis

### Intraday Trading
{self._format_edge_stats(edge['intraday_stats'])}

### Swing Trading
{self._format_edge_stats(edge['swing_stats'])}

### Symbol Performance
{self._format_symbol_stats(edge['symbol_stats'])}
"""
        return report

    def _format_edge_stats(self, stats: Dict) -> str:
        """Format edge statistics"""
        if not stats:
            return "No data"
        return f"""- Trades: {stats.get('count', 0)}
- Win Rate: {stats.get('win_rate', 0):.1%}
- Total P&L: ${stats.get('total_pnl', 0):.2f}
- Avg Return: {stats.get('avg_return', 0):.2f}%"""

    def _format_symbol_stats(self, stats: Dict) -> str:
        """Format symbol statistics"""
        if not stats:
            return "No data"

        output = ""
        for symbol, data in sorted(stats.items(), key=lambda x: x[1]['total_pnl'], reverse=True):
            output += f"""
- **{symbol}**: {data['trades']} trades, ${data['total_pnl']:.2f} P&L, {data['avg_return']:.2f}% avg return"""
        return output

    def export_csv(self, output_dir: Path) -> None:
        """Export analysis data to CSV"""
        # Trade summary
        with open(output_dir / 'trading_stats.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['symbol', 'entry_date', 'exit_date', 'return_pct', 'realized_pnl', 'holding_minutes'])
            writer.writeheader()
            for trade in self.trades:
                writer.writerow({
                    'symbol': trade.symbol,
                    'entry_date': trade.entry_date,
                    'exit_date': trade.exit_date,
                    'return_pct': f"{trade.return_pct:.2f}%",
                    'realized_pnl': f"${trade.realized_pnl:.2f}",
                    'holding_minutes': trade.holding_period_minutes,
                })


def main():
    """Main entry point"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python trading_analysis_agent.py <csv_path> [--output markdown|latex|csv]")
        sys.exit(1)

    csv_path = sys.argv[1]
    output_format = 'markdown'

    if '--output' in sys.argv:
        idx = sys.argv.index('--output')
        if idx + 1 < len(sys.argv):
            output_format = sys.argv[idx + 1]

    agent = TradingAnalysisAgent(csv_path)
    if agent.parse_csv():
        if output_format == 'markdown':
            report = agent.generate_markdown_report()
            print(report)
        else:
            print(f"Output format {output_format} not yet implemented")
    else:
        print(f"Failed to parse {csv_path}")
        sys.exit(1)


if __name__ == '__main__':
    main()
