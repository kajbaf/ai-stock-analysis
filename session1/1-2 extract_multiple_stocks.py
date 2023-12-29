import yfinance as y

tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA', 'AMZN', 'NFLX']

data = y.download(
    tickers=tickers,
    interval='1d',
    group_by='ticker',
    threads=True
    )

downloaded_tickers = set(col[0] for col in data.columns)

for ticker in downloaded_tickers:
    df = data.loc[:, ticker].sort_index().dropna()
    df.to_csv('data/' + ticker + '.csv', index=True)
    print(ticker, 'was saved sucessfully')
print('Tickers ', set(tickers) - downloaded_tickers, 'could not be downloaded.')