# Variables store values — the label is on the left, the value on the right
ticker = "AAPL" # a string (text) — always in quotes
price = 189.50 # a float (decimal number)
shares = 10 # an integer (whole number)
is_gain = True # a boolean (True or False)
# You can print any variable
print(ticker) # prints: AAPL
print(price * shares) # prints: 1895.0

# Variables store values — the label is on the left, the value on the right
ticker = "MSFT" # a string (text) — always in quotes
price = 390.00 # a float (decimal number)
shares = 10 # an integer (whole number)
is_gain = True # a boolean (True or False)
# You can print any variable
print(ticker) # prints: MSFT
print(price * shares) # prints: 3900.0

# Variables store values — the label is on the left, the value on the right
ticker = "GOOGL" # a string (text) — always in quotes
price = 350.00 # a float (decimal number)
shares = 10 # an integer (whole number)
is_gain = True # a boolean (True or False)
# You can print any variable
print(ticker) # prints: GOOGL
print(price * shares) # prints: 3500.0

# Variables store values — the label is on the left, the value on the right
ticker = "NVDA" # a string (text) — always in quotes
price = 190.00 # a float (decimal number)
shares = 10 # an integer (whole number)
is_gain = True # a boolean (True or False)
# You can print any variable
print(ticker) # prints: NVDA
print(price * shares) # prints: 1900.0

# Variables store values — the label is on the left, the value on the right
ticker = "AMZN" # a string (text) — always in quotes
price = 230.00 # a float (decimal number)
shares = 10 # an integer (whole number)
is_gain = True # a boolean (True or False)
# You can print any variable
print(ticker) # prints: AMZN
print(price * shares) # prints: 2300.0

tickers = ["AAPL", "MSFT", "GOOGL", "JPM", "JNJ"]
# Access by position — counting starts at 0
print(tickers[0]) # prints: AAPL (first item)
print(tickers[-1]) # prints: JNJ (last item)
print(len(tickers)) # prints: 5 (number of items)
# Add and remove items
tickers.append("TSLA") # adds TSLA to the end
tickers.remove("JNJ") # removes JNJ

# A dictionary groups related data under named keys
stock = {
"ticker": "AAPL",
"price": 189.50,
"shares": 10,
"sector": "Technology",
}
# Access values by key name
print(stock["ticker"]) # prints: AAPL
print(stock["price"] * stock["shares"]) # prints: 1895.0
# Add a new key
stock["cost_basis"] = 150.00
stock["gain_loss"] = stock["price"] - stock["cost_basis"]

tickers = ["AAPL", "MSFT", "GOOGL", "JPM", "JNJ"]
# Loop through every ticker in the list
for ticker in tickers:
print(f"Processing: {ticker}") # f-string: {} inserts the variable
# Loop with an index (position number)
for i, ticker in enumerate(tickers):
print(f"{i+1}. {ticker}") # prints: 1. AAPL, 2. MSFT, etc.
# Build a new list using a loop
prices = [189.50, 415.20, 175.80, 220.30, 155.00]
portfolio_value = 0
for price in prices:
portfolio_value += price # += means "add to the running total"
print(f"Total: ${portfolio_value:.2f}")

# Define a function with def, then a name, then parameters in ()
def calculate_gain(cost_basis, current_price):
gain_loss = current_price - cost_basis
return gain_loss
# Call the function — pass in real values
result = calculate_gain(150.00, 189.50)
print(f"Gain: ${result:.2f}") # prints: Gain: $39.50
# A more complete version with percentage
def calculate_return_pct(cost_basis, current_price):
gain_loss = current_price - cost_basis
return_pct = (gain_loss / cost_basis) * 100
return gain_loss, return_pct # functions can return multiple values
gain, pct = calculate_return_pct(150.00, 189.50)
print(f"Gain: ${gain:.2f} ({pct:.1f}%)") # Gain: $39.50 (26.3%)
