#Question 3: Use yfinance to Extract Stock Data
# Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch GameStop stock data
GameStock = yf.Ticker("GME")
GameStock_Data = GameStock.history(period="max")

# Display information about GameStop data, financials, and analyst price target
print(GameStock_Data.info())
print(GameStock_Data.head())


# Reset the index, save to a JSON file, and display the first five rows again
GameStock_Data.reset_index(inplace=True)
GameStock_Data.to_json('Game_stock_data.json', orient='records', lines=True)
print(GameStock_Data.head())

# Question 6: Plot GameStop Stock Graph

# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.
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

make_graph(GameStock_Data, "Game Stock Price Data")
