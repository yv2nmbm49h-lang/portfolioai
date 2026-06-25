import yfinance as yf
# --- Block 1: Get a single stock object ---
aapl = yf.Ticker("AAPL")
# Current price (fast)
print(aapl.fast_info["lastPrice"])
# Company info dictionary — lots of fields
info = aapl.info
print(info["longName"]) # Apple Inc.
print(info["sector"]) # Technology
print(info["marketCap"]) # market cap in dollars
print(info["trailingPE"]) # price-to-earnings ratio
print(info["dividendYield"]) # dividend yield (if any)
# --- Block 2: Historical price data ---
history = aapl.history(period="1mo") # last 1 month of daily prices
print(history.head()) # show first 5 rows
print(history["Close"].tail(5)) # last 5 closing prices