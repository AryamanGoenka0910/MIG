import pandas as pd # type: ignore

class Backtester:
    def __init__(self, strategy):
        self.strategy = strategy

    def backtest(self):
        self.strategy.generate_signals()
        initial_capital = float(100000.0)
        positions = pd.DataFrame(index=self.strategy.data.index).fillna(0.0)
        portfolio = positions.multiply(self.strategy.data['c'], axis=0)
        pos_diff = positions.diff()

        portfolio['holdings'] = (positions.multiply(self.strategy.data['c'], axis=0)).sum(axis=1)
        portfolio['cash'] = initial_capital - (pos_diff.multiply(self.strategy.data['c'], axis=0)).sum(axis=1).cumsum()   
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()
        return portfolio
