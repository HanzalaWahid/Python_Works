import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")
# print(apple.info)
# print(apple_share_price_data.history(period="max",interval="3mo"))
# apple_share_price_data = apple.history(period = "max")
# print(apple_share_price_data.head(10))
# print(apple_share_price_data.tail(10))
# plt.show(apple_share_price_data.plot(x="Date", y="Open"))

#
# # with open('apple.json') as file:
# #     apple_info = json.load(file)
# #     # Print the type of data variable   
# #     #print("Type:", type(apple_info))
# # print(apple_info["name"])

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data for AAPL
apple = yf.Ticker("AAPL")
# apple_share_price_data = apple.history(period="max")
# apple_share_price_data = apple.dividends(p)

# Display the first 10 rows of the data
# print(apple_share_price_data.head(4))

# Plotting the data
# plt.plot(apple_share_price_data.index, apple_share_price_data['Open'], label='CLose price')
# print(apple_share_price_data.index)
# print(apple_share_price_data.head)
# plt.xlabel('Date')
# plt.ylabel('Stock Price (USD)')
# plt.title('AAPL Stock Price History')
# plt.legend()
# plt.show()
(apple.dividends.plot())
plt.show()
