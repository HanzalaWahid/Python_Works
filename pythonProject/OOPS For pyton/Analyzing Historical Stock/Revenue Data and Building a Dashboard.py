# Question 1: Use yfinance to Extract Stock Data
# Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch Tesla stock data
Tesla_stock = yf.Ticker("TSLA")
Tesla_data = Tesla_stock.history(period="max")

# Display information about Tesla data and the first five rows
print(Tesla_data.info())
print(Tesla_data.head())

# Reset the index, save to a JSON file, and display the first five rows again
Tesla_data.reset_index(inplace=True)
Tesla_data.to_json('tesla_stock_data.json', orient='records', lines=True)
print(Tesla_data.head())


# Question 5: Plot Tesla Stock Graph
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.
# Upload a screenshot of your results.

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data['Close'], label="Closing price", color="blue")
    plt.title(title)  # Use the provided title parameter
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

make_graph(Tesla_data, "Tesla Stock Price Data")


