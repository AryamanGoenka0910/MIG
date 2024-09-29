import numpy as np
from strategies.base_strategy import BaseStrategy

class MovingAverageStrategy(BaseStrategy):
    def __init__(self, data, short_window=40, long_window=100):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        self.data['short_mavg'] = self.data['c'].rolling(window=self.short_window, min_periods=1, center=False).mean()
        self.data['long_mavg'] = self.data['c'].rolling(window=self.long_window, min_periods=1, center=False).mean()
        self.data['signal'] = np.where(self.data['short_mavg'] > self.data['long_mavg'], 1.0, 0.0)
        self.data['positions'] = self.data['signal'].diff()
