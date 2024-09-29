# trading_framework/strategies/base_strategy.py

import pandas as pd # type: ignore

class BaseStrategy:
    def __init__(self, data):
        self.data = data
        self.signals = pd.DataFrame(index=data.index)
        self.positions = pd.DataFrame(index=data.index)

    def generate_signals(self):
        raise NotImplementedError("Should implement generate_signals()")

    def backtest_portfolio(self, initial_capital=100000.0):
        raise NotImplementedError("Should implement backtest_portfolio()")
