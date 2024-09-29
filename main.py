from data.data_manager import DataManager
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
open_prices = np.stack(prepared_data['o'])
trades = np.zeros_like(open_prices)

fast_sma = ta.SMA(prepared_data['o'], timeperiod=5)
slow_sma = ta.SMA(prepared_data['o'], timeperiod=40)

prepared_data = prepared_data.copy()  # Ensure you're modifying a copy
prepared_data['trades'] = 0

# Loop through each day to determine buy/sell signals using .iloc for positional indexing
for day in range(1, len(prepared_data) - 1):
    
    # Buy: fast SMA crosses above slow SMA
    if fast_sma.iloc[day] > slow_sma.iloc[day] and fast_sma.iloc[day - 1] <= slow_sma.iloc[day - 1]:
        prepared_data.iloc[day + 1, prepared_data.columns.get_loc('trades')] = 1
    
    # Sell/short: fast SMA crosses below slow SMA
    elif fast_sma.iloc[day] < slow_sma.iloc[day] and fast_sma.iloc[day - 1] >= slow_sma.iloc[day - 1]:
        prepared_data.iloc[day + 1, prepared_data.columns.get_loc('trades')] = -1
    
    # Else do nothing
    else:
        prepared_data.iloc[day + 1, prepared_data.columns.get_loc('trades')] = 0

# Now print the 'trades' column
print(prepared_data['trades'])

input2 = []
input2.append(open_prices)

#portfolio_value, sharpe_ratio = eval_actions(input, input2, cash=25000, verbose=True)
#print(f"\nPortfolio value: {portfolio_value}")
#print(f"Sharpe ratio: {sharpe_ratio}")


# plt.figure(figsize=(8, 6))

# plt.plot(portfolio_value, label=f'{TICKER}')

# plt.xlabel('Day')
# plt.ylabel('Portoflio Value')
# plt.title('Algorithm Performance')
# plt.show()


# Create and run strategy
# strategy = MovingAverageStrategy(prepared_data)
# backtester = Backtester(strategy)
# results = backtester.backtest()

# # Output results
# print(results)
