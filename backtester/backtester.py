# trading_framework/backtester/backtester.py

import pandas as pd

class Backtester:
    def __init__(self, data, signals, initial_capital=100000.0):
        self.data = data
        self.signals = signals
        self.initial_capital = initial_capital

    def backtest_portfolio(self):
        positions = pd.DataFrame(index=self.signals.index).fillna(0.0)
        positions['position'] = 100 * self.signals['signal']  # Example: 100 shares

        portfolio = positions.multiply(self.data['c'], axis=0)
        pos_diff = positions.diff()

        portfolio['holdings'] = positions.multiply(self.data['c'], axis=0).sum(axis=1)
        portfolio['cash'] = self.initial_capital - (pos_diff.multiply(self.data['c'], axis=0)).sum(axis=1).cumsum()
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()

        return portfolio
