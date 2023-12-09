# Very Basic Data Engineering for Stock Market Pricess
In this course we will try to get market data programmatically.

Why?

Because financial market analysis requires a lot of time for processing huge amount of data for each type of financial contract (stock ticker). Going through different data sources and performing analysis again and again would be confusing and cumbersome. If we do it programmatically, we would be able to automate our practices, repeat them and improve them as we see fit.

## What We Need
* We need an installed Python interpreter.
  * We assume you have already installed Python.
  * If not, you can proceed to the [Python website](python.org) and download it.
  * In Mac OS and Linux you usually have an installed version of Python.
* Installing Python libraries. In each session, we will install only the required Python libraries for that session.
  * `yfinance`: It is a free Python library to access stock maerket data from yahoo Finance! It uses the free available Yahoo! APIs.
  * `pandas`: It is a free Python library for data processing, much like a very programmable MS Excel.

## What We Achieve
* We will download all the data in a folder `data`, and then we can perform all kind of analysis on them.
* We can intorduce our list of favorite stock market indices or tickers and update it at the beginning of our script, and run the script daily to receive more up-to-date data.
* We can open saved CSV files in data-analytic tools, or even Excel!