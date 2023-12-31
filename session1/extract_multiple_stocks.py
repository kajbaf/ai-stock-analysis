"""
A script to download historical price data for a portfolio of stocks using Yahoo Finance API.
"""
# Import Yahoo Finance API
import yfinance as y

# Define your desired stock portfolio
tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA', 'AMZN', 'NFLX']

# Download the historical price data for a portfolio of stock tickers, on daily intervals and grouped by the ticker
# Enables threaded downloading for improved speed.
data = y.download(
    tickers=tickers,
    interval='1d',
    group_by='ticker',
    threads=True
    )

# Verifies set of successfully downloaded stocks
downloaded_tickers = set(col[0] for col in data.columns)

for stock_ticker in downloaded_tickers:
    # Separate data for a stock ticker and ensure data is sorted by date
    df = data.loc[:, stock_ticker].sort_index().dropna()
    # Save data as a CSV file
    file_path = 'data/' + stock_ticker + '.csv'
    df.to_csv(file_path, index=True)
    print(stock_ticker, 'was saved sucessfully at', file_path)

failed_tickers = set(tickers) - downloaded_tickers
if failed_tickers:
    print('Tickers ', failed_tickers, 'could not be downloaded.')