from data.data_manager import DataManager
from strategies.example_strategy import MovingAverageCrossStrategy
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Configuration
API_KEY = "JHIRFNvJCdlnWV5Aya2kviwC6whO1pLi"
TICKER = 'TSLA'
START_DATE = datetime.today().date()  #start date is today
END_DATE = START_DATE - timedelta(days=365*2) #end date is how many days in the past I want to go, in this case 2years

# Step 1: Data Management
data_manager = DataManager(API_KEY)
data = data_manager.fetch_data(TICKER, START_DATE, END_DATE)

print(data)

# Step 2: Strategy Development
strategy = MovingAverageCrossStrategy(data)
signals = strategy.generate_signals_without_delay()

print(signals)

signals['positions'].plot(title='Trading Strategy Signals', label='Positions')
plt.xlabel('Date')
plt.ylabel('Signal')
plt.legend()
plt.show()