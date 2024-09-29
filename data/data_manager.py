# trading_framework/data/data_manager.py

import pandas as pd # type: ignore
import requests # type: ignore


class DataManager:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.polygon.io/v2/aggs/ticker"

    def fetch_data(self, ticker, start_date, end_date):
        url = f"{self.base_url}/{ticker}/range/1/day/{end_date}/{start_date}"
        params = {
            'adjusted': 'true',
            'sort': 'asc',
            'limit': 50000,
            'apiKey': self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        if 'results' in data:
            df = pd.DataFrame(data['results'])
            df = self.preprocess_data(df)
            return df
        else:
            raise Exception(f"Error fetching data: {data.get('error', 'Unknown error')}")

    def preprocess_data(self, df):
        df['date'] = pd.to_datetime(df['t'], unit='ms')
        df.set_index('date', inplace=True)
        df.sort_index(inplace=True)
        return df[['o', 'h', 'l', 'c', 'v']]  # Open, High, Low, Close, Volume


    def save_to_csv(self, df, filename):
        df.to_csv(filename)

    def load_from_csv(self, filename):
        df = pd.read_csv(filename, index_col='date', parse_dates=True)
        return df

    def normalize(self, df):
        df['norm'] = ((df['c'] - df['l']) / (df['h'] - df['l']))
        return df
    
    # def high_low(self):
    # #self.high, self.low = self.curr_data.loc[:, 'h'].max(), self.curr_data.loc[:, 'l'].min()
    #     return self.high, self.low
