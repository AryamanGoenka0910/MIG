# trading_framework/performance/performance_tracker.py

import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

class PerformanceTracker:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def calculate_metrics(self):
        returns = self.portfolio['returns']
        self.cumulative_returns = (1 + returns).cumprod() - 1
        self.annual_return = returns.mean() * 252
        self.annual_volatility = returns.std() * np.sqrt(252)
        self.sharpe_ratio = self.annual_return / self.annual_volatility

    def generate_report(self):
        print("Annual Return:", self.annual_return)
        print("Annual Volatility:", self.annual_volatility)
        print("Sharpe Ratio:", self.sharpe_ratio)

    def plot_performance(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.portfolio['total'], label='Portfolio Value')
        plt.title('Portfolio Performance')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.show()
