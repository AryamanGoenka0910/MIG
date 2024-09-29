import requests
import pandas as pd
import matplotlib.pyplot as plt

"""
use MIG-Dev anacodna evn for this
"""

def fetch_stock_data(ticker, start_date, end_date, api_key):
    base_url = "https://api.polygon.io/v2/aggs/ticker"
    url = f"{base_url}/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

def plot_data():
    df = pd.DataFrame(stock_data)
    # Convert timestamp from milliseconds to date
    df['date'] = pd.to_datetime(df['t'], unit='ms')

    # Set the date as index
    df.set_index('date', inplace=True)

    print(df)
    # # Plotting the "Open" prices
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['o'], label='Open Price', marker='o')
    plt.title('Open Prices of Stock Over Time')
    plt.xlabel('Date')
    plt.ylabel('Open Price ($)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)  # Rotate date labels for better visibility
    plt.tight_layout()  # Adjust layout to make room for label
    plt.show()

# Example usage
api_key = "JHIRFNvJCdlnWV5Aya2kviwC6whO1pLi"
ticker = "AAPL"
start_date = "2023-01-09"
end_date = "2023-02-10"
#stock_data = fetch_stock_data(ticker, start_date, end_date, api_key)

stock_data = [{'v': 70790813.0, 'vw': 131.6292, 'o': 130.465, 'c': 130.15, 'h': 133.41, 'l': 129.89, 't': 1673240400000, 'n': 645365}, 
                    {'v': 63896155.0, 'vw': 129.822, 'o': 130.26, 'c': 130.73, 'h': 131.2636, 'l': 128.12, 't': 1673326800000, 'n': 554940}, 
                    {'v': 69458949.0, 'vw': 132.3081, 'o': 131.25, 'c': 133.49, 'h': 133.51, 'l': 130.46, 't': 1673413200000, 'n': 561278}, 
                    {'v': 71379648.0, 'vw': 133.171, 'o': 133.88, 'c': 133.41, 'h': 134.26, 'l': 131.44, 't': 1673499600000, 'n': 635331}, 
                    {'v': 57809719.0, 'vw': 133.6773, 'o': 132.03, 'c': 134.76, 'h': 134.92, 'l': 131.66, 't': 1673586000000, 'n': 537385}, 
                    {'v': 63612627.0, 'vw': 135.7587, 'o': 134.83, 'c': 135.94, 'h': 137.29, 'l': 134.13, 't': 1673931600000, 'n': 595831}, 
                    {'v': 69672800.0, 'vw': 136.3316, 'o': 136.815, 'c': 135.21, 'h': 138.61, 'l': 135.03, 't': 1674018000000, 'n': 578304}, 
                    {'v': 58280413.0, 'vw': 134.9653, 'o': 134.08, 'c': 135.27, 'h': 136.25, 'l': 133.77, 't': 1674104400000, 'n': 491674}, 
                    {'v': 80200655.0, 'vw': 136.3762, 'o': 135.28, 'c': 137.87, 'h': 138.02, 'l': 134.22, 't': 1674190800000, 'n': 552230}, 
                    {'v': 81760313.0, 'vw': 141.2116, 'o': 138.12, 'c': 141.11, 'h': 143.315, 'l': 137.9, 't': 1674450000000, 'n': 719288}, 
                    {'v': 66435142.0, 'vw': 142.0507, 'o': 140.305, 'c': 142.53, 'h': 143.16, 'l': 140.3, 't': 1674536400000, 'n': 498679}, 
                    {'v': 65799349.0, 'vw': 140.7526, 'o': 140.89, 'c': 141.86, 'h': 142.43, 'l': 138.81, 't': 1674622800000, 'n': 536505}, 
                    {'v': 54105068.0, 'vw': 143.3429, 'o': 143.17, 'c': 143.96, 'h': 144.25, 'l': 141.9, 't': 1674709200000, 'n': 472135}, 
                    {'v': 70547743.0, 'vw': 145.8365, 'o': 143.155, 'c': 145.93, 'h': 147.23, 'l': 143.08, 't': 1674795600000, 'n': 560022}, 
                    {'v': 64015274.0, 'vw': 143.6524, 'o': 144.955, 'c': 143, 'h': 145.55, 'l': 142.85, 't': 1675054800000, 'n': 551111}, 
                    {'v': 65874459.0, 'vw': 143.6473, 'o': 142.7, 'c': 144.29, 'h': 144.34, 'l': 142.28, 't': 1675141200000, 'n': 468170}, 
                    {'v': 77663426.0, 'vw': 143.8723, 'o': 143.97, 'c': 145.43, 'h': 146.61, 'l': 141.32, 't': 1675227600000, 'n': 693374}, 
                    {'v': 118338980.0, 'vw': 149.3764, 'o': 148.9, 'c': 150.82, 'h': 151.18, 'l': 148.17, 't': 1675314000000, 'n': 996203}, 
                    {'v': 154338835.0, 'vw': 154.2437, 'o': 148.03, 'c': 154.5, 'h': 157.38, 'l': 147.83, 't': 1675400400000, 'n': 1141350}, 
                    {'v': 69771906.0, 'vw': 152.0939, 'o': 152.575, 'c': 151.73, 'h': 153.1, 'l': 150.78, 't': 1675659600000, 'n': 583517}, 
                    {'v': 83322551.0, 'vw': 153.4202, 'o': 150.64, 'c': 154.65, 'h': 155.23, 'l': 150.64, 't': 1675746000000, 'n': 661767}, 
                    {'v': 63620079.0, 'vw': 152.3636, 'o': 153.88, 'c': 151.92, 'h': 154.58, 'l': 151.168, 't': 1675832400000, 'n': 524140}, 
                    {'v': 55994243.0, 'vw': 152.2769, 'o': 153.775, 'c': 150.87, 'h': 154.33, 'l': 150.42, 't': 1675918800000, 'n': 471973}, 
                    {'v': 57388108.0, 'vw': 150.4054, 'o': 149.46, 'c': 151.01, 'h': 151.3401, 'l': 149.22, 't': 1676005200000, 'n': 443405}]

#print(stock_data)
plot_data()
