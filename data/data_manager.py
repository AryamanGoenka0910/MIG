# trading_framework/data/data_manager.py

import pandas as pd # type: ignore
import requests # type: ignore


class DataManager:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.polygon.io/v2/aggs/ticker"
        self.data = None

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
            
            def preprocess_data(df):
                df['date'] = pd.to_datetime(df['t'], unit='ms')
                df.set_index('date', inplace=True)
                df.sort_index(inplace=True)
                return df[['o', 'h', 'l', 'c', 'v']]  # Open, High, Low, Close, Volume
    
            self.data = preprocess_data(df)
            return self.data
        else:
            raise Exception(f"Error fetching data: {data.get('error', 'Unknown error')}")

    def save_to_csv(self, filename):
        if self.data is not None:
            self.data.to_csv(filename)
        else:
            print("Please load in a CSV file or fetch ticker data from Polygon")

    def load_from_csv(self, filename):
        self.data = pd.read_csv(filename, index_col='date', parse_dates=True)
        return self.data

    def normalize(self):
        if self.data is not None:
            self.data['norm'] = ((self.data['c'] - self.data['l']) / (self.data['h'] - self.data['l']))
            return self.data
        else:
            print("Please load in a CSV file or fetch ticker data from Polygon")
  