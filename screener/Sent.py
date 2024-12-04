from transformers import pipeline
import yfinance as yf
from goose3 import Goose
from requests import get
import pandas as pd

## Activate CONDA ENV MIG-Dev

def get_ticker_news_sentiment(ticker):
    """
    Returns a Pandas dataframe of the given ticker's most recent news article headlines,
    with the overal sentiment of each article.

    Args:
        ticker (string)

    Returns:
        pd.DataFrame: {'Date', 'Article title', Article sentiment'}
    """
    ticker_news = yf.Ticker(ticker)
    news_list = ticker_news.get_news()
    extractor = Goose()
    pipe = pipeline("text-classification", model="ProsusAI/finbert")

    data = []
    for dic in news_list:
        title = dic['title']
        response = get(dic['link'])
        article = extractor.extract(raw_html=response.content)
        text = article.cleaned_text
        date = article.publish_date
        if len(text) > 512:
            print("too long")
            data.append({'Ticker':f'{ticker}',
                         'Date':f'{date}',
                         'Article title':f'{title}',
                         'Article sentiment':'NaN too long'})
        else:
            results = pipe(text)
            print(results)
            data.append({'Ticker':f'{ticker}',
                         'Date':f'{date}',
                         'Article title':f'{title}',
                         'Article sentiment':results})
    df = pd.DataFrame(data)
    return df

def generate_csv(ticker):
    df = get_ticker_news_sentiment(ticker)
    df.to_csv(f'out/{ticker}.csv', index=False)
    return df

if __name__ == '__main__':
    undervalued = ['ZION','ISTR', 'BSRR']
    all_data = [] 
    for ticker in undervalued:
        df = generate_csv(ticker)
        all_data.append(df) 

    # Combine all DataFrames into one
    combined_df = pd.concat(all_data, ignore_index=True)

    print(combined_df)