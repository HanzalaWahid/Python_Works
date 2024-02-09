# Question 4: Use Webscraping to Extract GME Revenue Data
# Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the page to load (you might need to adjust the sleep time)
import time
time.sleep(5)

# Extract HTML content after the page has loaded
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the table containing revenue data
revenue_table = soup.find('table', {'class': 'historical_data_table'})

# Extract data from the table
if revenue_table:
    data = []
    for row in revenue_table.find_all('tr')[1:]:
        cols = row.find_all('td')
        date = cols[0].get_text(strip=True)
        revenue = cols[1].get_text(strip=True)
        data.append([date, revenue])

    # Create a DataFrame
    GameStock_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])

    # Display the last five rows
    print(GameStock_revenue.tail())
else:
    print("Table not found. Check HTML structure or class names.")
