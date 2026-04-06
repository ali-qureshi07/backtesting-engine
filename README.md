# Backtesting Engine

A moving average crossover backtesting engine built in Python.

## Strategy
Buys when the 50-day simple moving average crosses above the 200-day 
simple moving average (golden cross), and exits when it crosses below 
(death cross). Uses a 1-day signal shift to prevent look-ahead bias.

## Results (AAPL 2019-2024)
- Sharpe Ratio: 0.91
- Max Drawdown: -31.43%
- Win Rate: 53.58%

## Libraries
Python, Pandas, NumPy, Matplotlib, yfinance