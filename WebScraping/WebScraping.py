from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page
# url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Fetch the HTML content of the page
page = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find the second table on the page (index 1, as tables are zero-indexed)
table = soup.find_all('table')[1]

# Extract column headers (th elements) from the table
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

# Create an empty DataFrame with columns from the extracted titles
df = pd.DataFrame(columns=world_table_titles)

# Extract row data (td elements) from the table
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    # Append the row data to the DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv(r'D:\DA\Python\US_Companies.csv', index=False)
