import yfinance as y
import pandas as pd

tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA', 'AMZN', 'NFLX']

data = y.download(
    tickers=tickers,
    interval='1d',
    group_by='ticker',
    threads=True
    )

data = data.T
downloaded_tickers = set(idx[0] for idx in data.index)

for ticker in downloaded_tickers:
    df = data.loc[ticker, :].T.sort_index().dropna()
    df.to_csv('data/' + ticker + '.csv', index=True)
    print(ticker, 'was saved sucessfully')