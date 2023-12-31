# Data Extraction
In this stage, we want to develop a very simple script to download historical prices of stock tickers and store them locally.

## 1. Extract Pre-defined Stocks
- [session1/extract_stock_price.py](extract_stock_price.py)

The first script can download all the historical stock prices of Microsoft. You can execute it as follows:
```bash
python session1/extract_stock_price.py
```
You can edit the file and assign another value to the variable `stock_ticker` to download other stocks tickers. Go ahead and try it for 'AAPL' (Apple), 'META' (Facebook), and other stocks. The files will be saved in a folder named `data` in the root of our code repository.

The script fetches data in daily intervals, comprising the following columns:
  - **Date:** This represents the date for aggregated transactions in each row.
  - **Open, Close:** The 'Open' price is the first transaction of the interval, while 'Close' is the last. The closing price is often used to calculate different stock indicators. The difference between opening and closing prices is used to estimate the performance of a stock within an interval. A higher closing price than opening generally indicates positive performance, and vice 
  vers- a.
  - **High, Low:** They refer to the highest and lowest prices at which a stock has traded during the interval. These values are crucial for traders as they provide insight into the volatility and price range of the stock for that day.
  - **Volume:** It refers to the number of shares of a particular stock that are traded within the interval. Volume is an important indicator in technical analysis as it provides insight into the strength or weakness of price movements. For instance, a stock price moving up on high volume is typically viewed as a stronger, more relevant move than a price moving up on low volume, as it suggests a higher degree of investor interest and conviction in the price movement.

- [session1/extract_multiple_stocks.py](extract_multiple_stocks.py)

The second script downloads historical prices of my stock portfolio. It is defined in the code at line 8.
```python
tickers = ['MSFT', 'GOOG', 'AAPL', 'TSLA', 'AMZN', 'NFLX']
```
Go ahead and add some other stock tickers to the list and run the script.
```bash
python session1/extract_multiple_stocks.py
```
It will create and update several CSV files in the same `data` folder.

To keep your data files updated, you can run the script daily. You can open this files in Excel, and perform all kinds of analyses that we performed in session 0.

## 2. Extract Stocks in an ETF
- [session1/extract_stock_find.py](extract_stock_find.py)


  * **Data Management:** Set up a system to organize data so you can efficiently access this data and keep it up to date.
  * **Data Analysis**: Explore the power of Python and Excel in reading and analyzing our downloaded CSV files.
  * **Create a Personalized Stock Portfolio**: Learn to track a selected set of stock tickers, effectively creating and managing your first stock portfolio.
  * **Monitoring Stock Baskets**: Develop a new code to programmatically extract, analyze, and update ticker data for all mutual fund stocks or ETF stocks.
