import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download Tesla stock data
data = yf.download("TSLA", start="2022-01-01", end="2024-01-01")

# Calculate daily returns
data['Returns'] = data['Close'].pct_change()

# Calculate moving averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Plot stock price and moving averages
plt.figure()
plt.plot(data['Close'], label='Closing Price')
plt.plot(data['MA50'], label='50-day MA')
plt.plot(data['MA200'], label='200-day MA')
plt.title("Tesla Stock Analysis")
plt.legend()
plt.show()

# Plot daily returns
plt.figure()
plt.plot(data['Returns'])
plt.title("Daily Returns")
plt.show()
