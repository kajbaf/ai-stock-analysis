"""
A simple script to download historical prices of your desired stock using Yahoo Finance API.
"""
# Import Yahoo Finance API
import yfinance as y

# Define the desired stock ticker
stock_ticker = 'MSFT'

# Download the historical price data for the specified stock ticker, on daily intervals
dataframe = y.download(tickers=stock_ticker, interval='1d')

# Verify if the data for the specified stock ticker is retrieved
if not dataframe.empty:
    # Ensure data is sorted by date
    df = dataframe.sort_index()
    # Save data as a CSV file
    file_path = 'data/' + stock_ticker + '.csv'
    df.to_csv(file_path, index=True)
    print(stock_ticker, 'was saved sucessfully at', file_path)
else:
    print('Failed to download data for ', stock_ticker)