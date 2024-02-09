# Question 2: Use Webscraping to Extract Tesla Revenue Data
# Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
htmlContent = response.content

# Save the HTML content to a file (optional)
with open("revenue_page.html", "wb") as file:
    file.write(htmlContent)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(htmlContent, "html.parser")

# Extract the title of the HTML page
title = soup.title
print(title)

# Find the table containing revenue data (hypothetical example)
revenue_table = soup.find('table', {'class': 'historical_data_table'})

# Check if the table is found before proceeding
if revenue_table:
    # Initialize lists to store data
    dates = []
    revenues = []

    # Extract data from the table rows
    for row in revenue_table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        date = cols[0].get_text(strip=True)
        revenue = cols[1].get_text(strip=True)

        dates.append(date)
        revenues.append(revenue)

    # Create a DataFrame from the extracted data
    revenue_data = {'Date': dates, 'Revenue': revenues}
    tesla_revenue = pd.DataFrame(revenue_data)

    # Display the last five rows using the tail function
    print(tesla_revenue.tail())
else:
    print("Table not found. Check HTML structure or class names.")

# Print the prettified HTML
# print(soup.prettify())
# Extract all paragraphs from the HTML
# paragraphs = soup.find_all('p')
# for para in paragraphs:
#     print(para.text)
