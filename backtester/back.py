from collections import defaultdict
import numpy as np # type: ignore
from pathlib import Path
import argparse

class Back:
    def __init__(self, verbose=True) -> None:
        self.verbose = verbose

    def calc_sharpe_ratio(portfolio_values):
        #Return Annualized Sharpe Ratio

        daily_returns = np.diff(portfolio_values) / portfolio_values[:-1]
        risk_free_rate = 0
        average_daily_return = np.mean(daily_returns)
        volatility = np.std(daily_returns)

        #252 Trading days in a year
        sharpe_ratio = np.sqrt(252) * (average_daily_return - risk_free_rate) / volatility
        
        return sharpe_ratio
    
    def run_backtest(actions, prices, cash=25000):
        cash = cash