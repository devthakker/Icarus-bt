import yfinance as yf

aapl= yf.Ticker("aapl")
print(aapl)

aapl_historical = aapl.history(start="2020-06-02", end="2021-06-07", interval="1d")
print(aapl_historical)

print(aapl_historical.columns)