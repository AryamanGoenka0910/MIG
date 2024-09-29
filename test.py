from data.data_manager import DataManager


ticker = "AAPL"
start_date = "2023-01-09"
end_date = "2023-02-10"

dm = DataManager("JHIRFNvJCdlnWV5Aya2kviwC6whO1pLi", ticker)
# df = dm.fetch_data(start_date, end_date)
dm.normalize()
print(dm.get_data())
