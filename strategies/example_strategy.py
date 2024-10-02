# trading_framework/strategies/moving_average_strategy.py

import numpy as np # type: ignore

from strategies.base_strategy import BaseStrategy
from indicators.technical_indicators import TechnicalIndicators

class MovingAverageCrossStrategy(BaseStrategy):
    def __init__(self, data, short_window=5, long_window=40, delay=True):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window
        self.delay = delay

    def set_delay(self, delay):
        self.delay = delay

    def generate_signals(self):
        """
        This method overrides the abstract method from BaseStrategy.
        It decides which signal generation method to call based on the delay flag.
        """
        if self.delay:
            return self.generate_signals_with_delay()
        else:
            return self.generate_signals_without_delay()

    ##uses mavgs to trade on trading day with signals
    def generate_signals_without_delay(self):
        # 1. Calculate short-term and long-term moving averages
        self.data['fast_mavg'] = TechnicalIndicators.SMA(self.data, self.short_window)
        self.data['slow_mvag'] = TechnicalIndicators.SMA(self.data, self.long_window)
        
        # 2. Initialize the 'signal' column with 0 (no signal initially)
        self.data = self.data.copy()
        self.data['signal'] = 0.0
        
        # 3. Set signals based on moving average crossover
        self.data['signal'][self.short_window:] = np.where(
            self.data['fast_mavg'][self.short_window:] > self.data['slow_mvag'][self.short_window:], 1.0, 0.0
        )
        
        # 4. Calculate 'positions' by taking the difference of the signal to track transitions
        self.data['positions'] = self.data['signal'].diff().fillna(0)  # Replace NaN with 0 to avoid any NaN issues

        return self.data
    
    #uses mavgs to trade on next trading day based on previous day signal
    def generate_signals_with_delay(self):
        self.data['fast_mavg'] = TechnicalIndicators.SMA(self.data, self.short_window)
        self.data['slow_mvag'] = TechnicalIndicators.SMA(self.data, self.long_window)

        self.data = self.data.copy()
        self.data['positions'] = 0.0

        for day in range(1, len(self.data) - 1):
            if self.data['fast_mavg'][day] > self.data['slow_mvag'][day] and self.data['fast_mavg'][day - 1] <= self.data['slow_mvag'][day - 1]:
                self.data.iloc[day + 1, self.data.columns.get_loc('positions')] = 1
    
            # Sell/short: fast SMA crosses below slow SMA
            elif self.data['fast_mavg'][day] < self.data['slow_mvag'][day] and self.data['fast_mavg'][day - 1] >= self.data['slow_mvag'][day - 1]:
                self.data.iloc[day + 1, self.data.columns.get_loc('positions')] = -1
            
            # Else do nothing
            else:
                self.data.iloc[day + 1, self.data.columns.get_loc('positions')] = 0
        
        return self.data