# trading_framework/backtester/backtester.py

import pandas as pd # type: ignore
import numpy as np # type: ignore

class Backtester:
    def __init__(self, data, signals, initial_capital=100000.0, shares_per_trade=100):
        """
        Initialize the Backtester with stock data and signals (buy/sell actions).
        data: DataFrame containing stock data with at least 'c' (close prices).
        signals: DataFrame containing signals and positions for the strategy.
        initial_capital: Starting cash amount for the portfolio.
        shares_per_trade: Number of shares to trade per signal.
        """
        self.data = data
        self.signals = signals
        self.initial_capital = initial_capital
        self.shares_per_trade = shares_per_trade 

    def backtest_portfolio(self):
        """
        Backtest the portfolio using the generated positions (not raw signals).
        Returns a DataFrame of portfolio metrics including total value, cash, and returns.
        """
        
        positions = pd.DataFrame(index=self.signals.index).fillna(0.0)  # Initialize positions DataFrame with the same index as signals
        positions['position'] = self.shares_per_trade * self.signals['positions']  # Each signal leads to a position change by a fixed number of shares

        portfolio = pd.DataFrame(index=self.signals.index) # Calculate portfolio holdings (value of the held stock) d
        portfolio['holdings'] = positions['position'] * self.data['c']

        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(portfolio)

        portfolio['posisition_diff'] = positions['position'].diff() # Calculate position changes (buys/sells)

        portfolio['cash'] = self.initial_capital
        portfolio['cash'].iloc[1:] = self.initial_capital - (portfolio['posisition_diff'] * self.data['c']).cumsum().iloc[1:] # Calculate remaining cash for all rows except the first one

        portfolio['total'] = portfolio['cash'] + portfolio['holdings'] # Total portfolio value is holdings + cash
        portfolio['returns'] = portfolio['total'].pct_change().fillna(0) # Portfolio returns, handling the first NaN row generated by pct_change

        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(portfolio)

        return portfolio
