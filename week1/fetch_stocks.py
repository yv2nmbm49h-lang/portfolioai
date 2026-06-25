import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOGL", "JPM", "JNJ"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    price = stock.fast_info["lastPrice"]
    print(f"{ticker}: ${price:.2f}")

import yfinance as yf

portfolio = [
    {"ticker": "AAPL", "shares": 10, "cost_basis": 150.00},
    {"ticker": "MSFT", "shares": 5, "cost_basis": 380.00},
    {"ticker": "GOOGL", "shares": 8, "cost_basis": 160.00},
    {"ticker": "JPM", "shares": 15, "cost_basis": 200.00},
    {"ticker": "JNJ", "shares": 12, "cost_basis": 145.00},
]

total_cost = 0
total_value = 0

print(f"{'TICKER':<6} {'SHARES':>6} {'COST':>8} {'PRICE':>8} {'VALUE':>9} {'GAIN/LOSS':>10} {'RETURN':>8}")
print("-" * 70)

for holding in portfolio:
    stock = yf.Ticker(holding["ticker"])
    price = stock.fast_info["lastPrice"]

    shares = holding["shares"]
    cost_basis = holding["cost_basis"]

    cost = shares * cost_basis
    value = shares * price
    gain_loss = value - cost
    return_pct = (gain_loss / cost) * 100

    total_cost += cost
    total_value += value

    print(f"{holding['ticker']:<6} {shares:>6} {cost_basis:>8.2f} {price:>8.2f} {value:>9.2f} {gain_loss:>+10.2f} {return_pct:>7.1f}%")

print("-" * 70)
print(f"TOTAL Cost: ${total_cost:,.2f} | Value: ${total_value:,.2f} | Gain: ${total_value-total_cost:+,.2f}")

def annualized_return(total_return: float, years: float) -> float:
    """
    Calculate the annualized (CAGR) return from a total return over a period.

    Args:
        total_return: Total return as a decimal (e.g., 0.50 for 50%)
        years: Number of years the investment was held

    Returns:
        Annualized return as a decimal (e.g., 0.0915 for 9.15%)
    """
    if years <= 0:
        raise ValueError("Years must be greater than 0")
    if total_return <= -1:
        raise ValueError("Total return cannot be -100% or worse")

    return (1 + total_return) ** (1 / years) - 1


# --- Examples ---
if __name__ == "__main__":
    # Example 1: 50% total return over 4 years
    r = annualized_return(0.50, 4)
    print(f"50% over 4 years → {r:.2%} annualized")   # 10.67%

    # Example 2: Using start/end values directly
    def annualized_return_from_values(start: float, end: float, years: float) -> float:
        total = (end - start) / start
        return annualized_return(total, years)

    r2 = annualized_return_from_values(10_000, 18_500, 6)
    print(f"$10k → $18.5k over 6 years → {r2:.2%} annualized")  # 10.79%