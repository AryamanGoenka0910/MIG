# trading_framework/indicators/technical_indicators.py

import pandas as pd # type: ignore
import numpy as np # type: ignore
import talib # type: ignore

class TechnicalIndicators:
    @staticmethod
    def SMA(data, period=14):
        return talib.SMA(data['o'], timeperiod=period)

    @staticmethod
    def EMA(data, period=14):
        return talib.EMA(data['c'], timeperiod=period)

    @staticmethod
    def RSI(data, period=14):
        return talib.RSI(data['c'], timeperiod=period)

    @staticmethod
    def MACD(data):
        macd, macd_signal, macd_hist = talib.MACD(data['c'])
        return macd, macd_signal, macd_hist

    @staticmethod
    def BollingerBands(data, period=20):
        upper, middle, lower = talib.BBANDS(data['c'], timeperiod=period)
        return upper, middle, lower

    # Allow users to add custom indicators
    @staticmethod
    def custom_indicator(data, func, *args, **kwargs):
        return func(data, *args, **kwargs)
