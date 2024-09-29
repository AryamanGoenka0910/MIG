## MIG Algo Building Framework

For use for members of MIG to research, develop, and backtest algorithmic trading strategies
CHECK example_main.py for example usage of framework
CHECK MIG-Docs: https://docs.michiganinvestmentgroup.com/ for usage of Conda Env

### Example use of Data Loading from Polygon

from MIG.data.data_manager import DataManager

API_KEY = "YOUR_API_KEY"
data_manager = DataManager(API_KEY)
start_date = "2022-01-01"
end_date = "2023-01-01"
ticker = "AAPL"

data = data_manager.fetch_data(ticker, start_date, end_date)
data_manager.save_to_csv(data, f"{ticker}_data.csv")
