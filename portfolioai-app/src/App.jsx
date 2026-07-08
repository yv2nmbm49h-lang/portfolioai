import { useState } from 'react'
import './App.css'

function App() {
  const [ticker, setTicker] = useState('AAPL')

  const portfolio = [
    { ticker: 'AAPL', price: 189.50, change: 2.3 },
    { ticker: 'MSFT', price: 415.20, change: -0.8 },
    { ticker: 'GOOGL', price: 175.80, change: 1.1 },
  ]

  return (
    <div className="app">

      {/* Navigation Bar */}
      <nav className="navbar">
        <h1>PortfolioAI</h1>
      </nav>

      <main className="dashboard">

        {/* Summary Card */}
        <div className="summary-card">
          <h2>Portfolio Summary</h2>
          <p>
            Total Holdings: <strong>{portfolio.length}</strong>
          </p>
        </div>

        <h2>Stock Holdings</h2>

        {/* Stock Table */}
        <table className="stock-table">
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Price</th>
              <th>Change</th>
            </tr>
          </thead>

          <tbody>
            {portfolio.map(stock => (
              <tr key={stock.ticker}>
                <td>{stock.ticker}</td>
                <td>${stock.price}</td>

                <td className={stock.change > 0 ? "positive" : "negative"}>
                  {stock.change > 0 ? "▲" : "▼"} {stock.change}%
                </td>
              </tr>
            ))}
          </tbody>
        </table>


        <button onClick={() => setTicker('MSFT')}>
          Switch Selected Stock to MSFT
        </button>

        <p>
          Selected Stock: <strong>{ticker}</strong>
        </p>

      </main>

    </div>
  )
}

export default App