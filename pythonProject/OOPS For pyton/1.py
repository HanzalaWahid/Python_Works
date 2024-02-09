import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")
apple_share_price_data = apple.history(period="max")
print(apple.info)
print(apple_share_price_data.head(10))
print(apple_share_price_data.tail(10))
plt.plot(apple_share_price_data.index, apple_share_price_data['Open'], label='Open price')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.title('AAPL Stock Price History')
plt.legend()
plt.show()
print(apple.dividends)
apple.dividends.plot()
plt.title('AAPL Dividend History')
plt.show()
