import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

# page has only one table
table = soup.find("table", class_="chart")

# cols: 'Rank & Title',	'IMDb Rating', 'Your Rating'

contents = []

for row in table.tbody.find_all("td"):
    cell = {}
    # cell{'posterColumn'}= = row
    print(row)
