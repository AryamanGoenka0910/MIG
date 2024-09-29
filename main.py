from data.data_manager import DataManager
from strategies.example_strategy import MovingAverageStrategy
from backtester.backtester import Backtester
import matplotlib.pyplot as plt
import numpy as np
import talib as ta
from datetime import datetime, timedelta


from eval_algo import eval_actions


# Configuration
API_KEY = "JHIRFNvJCdlnWV5Aya2kviwC6whO1pLi"
TICKER = 'TSLA'
START_DATE = "2015-01-09"
END_DATE = "2023-02-10"

# api_key = "JHIRFNvJCdlnWV5Aya2kviwC6whO1pLi"
# ticker = "AAPL"
# start_date = "2023-01-09"
# end_date = "2023-02-10"
#stock_data = fetch_stock

# Fetch and prepare data
data_manager = DataManager(API_KEY)
start_date = datetime.today().date()  #start date is today
end_date = start_date - timedelta(days=365*2) #end date is how many days in the past I want to go, in this case 2years
prepared_data = data_manager.fetch_data(TICKER, start_date, end_date)

stock_close_data = prepared_data['c']
plt.plot(stock_close_data.index, stock_close_data.values)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices')
plt.legend()
plt.show()


open_prices = []
stock_open_data = prepared_data['o']
open_prices.append(stock_open_data.values)
open_prices = np.stack(open_prices)
trades = np.zeros_like(open_prices)

fast_sma = ta.SMA(open_prices[0], timeperiod=5)
slow_sma = ta.SMA(open_prices[0], timeperiod=40)

for day in range(1, len(open_prices[0])-1):
    
    # Buy: fast SMA crosses above slow SMA
    if fast_sma[day] > slow_sma[day] and fast_sma[day-1] <= slow_sma[day-1]:
        # we are trading the next day's open price
        trades[0][day+1] = 1
    
    # Sell/short: fast SMA crosses below slow SMA
    elif fast_sma[day] < slow_sma[day] and fast_sma[day-1] >= slow_sma[day-1]:
        # we are trading the next day's open price
        trades[0][day+1] = -1
    # else do nothing
    else:
        trades[0][day+1] = 0

print(trades)

portfolio_value, sharpe_ratio = eval_actions(trades, open_prices, cash=25000, verbose=True)
#print(f"\nPortfolio value: {portfolio_value}")
print(f"Sharpe ratio: {sharpe_ratio}")


plt.figure(figsize=(8, 6))

plt.plot(portfolio_value, label=f'{TICKER}')

plt.xlabel('Day')
plt.ylabel('Portoflio Value')
plt.title('Algorithm Performance')
plt.show()


# Create and run strategy
# strategy = MovingAverageStrategy(prepared_data)
# backtester = Backtester(strategy)
# results = backtester.backtest()

# # Output results
# print(results)
