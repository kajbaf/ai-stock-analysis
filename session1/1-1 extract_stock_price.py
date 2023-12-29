"""
A simple script to download desired stock data from Yahoo Finance API.
"""
# Import Yahoo Finance API
import yfinance as y

# Define the desired stock ticker to get data from
stock_ticker = 'MSFT'

# Download the historical data for the specified stock ticker, on daily aggregation
dataframe = y.download(tickers=stock_ticker, interval='1d')

# Verify if the data for the specified stock ticker is retrieved
if not dataframe.empty:
    # Ensure data is sorted by date
    df = dataframe.sort_index()
    # Save data as a CSV file
    df.to_csv('data/' + stock_ticker + '.csv', index=True)
    print(stock_ticker, 'was saved sucessfully')
else:
    print('Failed to download data for ', stock_ticker)