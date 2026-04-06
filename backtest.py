import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2019-01-01", end="2024-01-01")

data = data[['Close']]

print(data.head())

data['Close'].plot(title="AAPL Close Price")
plt.show()

data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

data[['Close', 'SMA_50', 'SMA_200']].plot(title="AAPL with Moving Averages")
plt.show()

data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
data['Signal'] = data['Signal'].shift(1)
data['Position'] = data['Signal'].diff()

#print(data[['Close', 'SMA_50', 'SMA_200', 'Signal', 'Position']].dropna().head(20))

data['Market_Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Market_Return'] * data['Signal']

data['Cumulative_Market'] = (1 + data['Market_Return']).cumprod()
data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod()

data[['Cumulative_Market', 'Cumulative_Strategy']].plot(
    title="Strategy vs Buy & Hold"
)
plt.show()

import numpy as np

sharpe = (data['Strategy_Return'].mean() / data['Strategy_Return'].std()) * np.sqrt(252)

rolling_max = data['Cumulative_Strategy'].cummax()
drawdown = (data['Cumulative_Strategy'] - rolling_max) / rolling_max
max_drawdown = drawdown.min()

win_rate = (data['Strategy_Return'] > 0).sum() / (data['Strategy_Return'] != 0).sum()

print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")
print(f"Win Rate: {win_rate:.2%}")