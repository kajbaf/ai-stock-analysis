# Data Extraction
Data Extraction is the very first step in any kind of data processing activity, including data engineering and analysis. It involves pulling data from various sources for further processing and computations. This process can be executed using multiple methods, including APIs or SDKs to access data programmatically, direct retrieval from databases or data files, and data entry, which can be either manual or automated. For example, using an API might involve pulling stock prices from a financial database, while automated data entry could include performing OCR on paper documents. Each method is chosen based on the data's nature and the desired analysis outcomes.

Here, we want to develop a very simple script to download historical prices of stock tickers and store them locally. Then we can manually analyze these data files or use programming techniques to automate our analysis.

## 1. Extract Stock Prices
### Extract data for a single stock
**Script: [session1/extract_stock_price.py](extract_stock_price.py)**

The first script can download all the historical stock prices of Microsoft. You can execute it as follows:
```bash
python session1/extract_stock_price.py
```
You can edit the file at line 8 and assign another value to the variable `stock_ticker` to download other stock tickers. Go ahead and try it for 'AAPL' (Apple), 'META' (Facebook), and other stocks. The script will save data as CSV files in a folder named `data` at the root of our project.

This script fetches data for daily periods, comprising of the following columns:
  - **Date**: This represents the date for aggregated transactions in each row.
  - **Open and Close**: The 'Open' price is the first transaction of the interval, while 'Close' is the last. The closing price is often used to calculate different stock indicators. The difference between opening and closing prices is used to estimate the performance of a stock within an interval, while a higher closing price than opening generally indicates positive performance, and vice versa.
  - **High and Low**: They refer to the highest and lowest prices at which a stock has traded during the interval. These values are crucial for traders as they provide insight into the volatility and price range of the stock for that day.
  - **Volume**: It refers to the number of shares of a particular stock that are traded within the interval. Volume is an important indicator in technical analysis as it provides insight into the strength or weakness of price movements. For instance, a stock price moving up on high volume is typically viewed as a stronger, more relevant move than a price moving up on low volume, as it suggests a higher degree of investor interest and conviction in the price movement.

You can edit script at line 11 and add some other arguments to the `yf.download` function call. Let's explore three arguments that can significantly enhance your queries:

1. **`start`**: This argument specifies the starting date for your data retrieval. You can input dates in the format 'YYYY-MM-DD'. If it is omitted, the function defaults to fetching data from 99 years ago.

2. **`end`**: This argument lets you define the end date for your data extraction, also in 'YYYY-MM-DD' format. Without this, the function pulls data up to the most recent trading day.

3. **`interval`**: This parameter controls the frequency of data points. Options include '1d' for daily, '1wk' for weekly, '1mo' for monthly, and others. The default is '1d', providing daily data. Here is the complete list of valid intervals:
   - '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'

For those eager to dive deeper, I recommend exploring the [yfinance wiki](https://github.com/ranaroussi/yfinance/wiki).

### Extract data for multiple stocks (portfolio)
**Script: [session1/extract_multiple_stocks.py](extract_multiple_stocks.py)**

The second script downloads the historical prices of my stock portfolio. It is defined in the code at line 8.
```python
tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA', 'AMZN', 'NFLX']
```
Go ahead and add some other stock tickers to the list and run the script.
```bash
python session1/extract_multiple_stocks.py
```
It will create and update several CSV files in the same `data` folder.

To keep your data files updated, you can run the script daily. You can open these files in Excel and perform all kinds of analyses that we performed in session 0.

## Analyze Data in MS Excel
In this exercise, we'll manually analyze downloaded stock data in Excel. Here I want to analyze the changes in the price of the 'NFLX' stock ticker (Netflix). After downloading the CSV file, which includes daily data like open, high, low, close, adjusted close prices, and transaction volume, we'll convert it into an Excel file for ease of use.

To visualize the data, we create a line chart by selecting the 'Date' and 'Close' columns and using the 'Insert Chart' from the 'Insert' tab. The initial view of the chart may appear compressed, so to focus on recent trends, right-click the Date axis and adjust the minimum value to '2023-01-01'. This adjustment highlights Netflix's substantial share price increase from the start of 2023, rising from below $300 to slightly under $500. For a more detailed view of price fluctuations, right-click the Y-axis (closing price axis) and set the range between $250 and $500. This offers a more distinct visualization of the stock's recent performance.
