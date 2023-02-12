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
for tr in soup.find_all("tr"):
    data = {}
    try:
        poster_column = tr.find("td", class_="posterColumn")
        title_column = tr.find("td", class_="titleColumn")
        rating_column = tr.find("td", class_="ratingColumn imdbRating")

        data["poster_src"] = poster_column.find("img").get("src")
        data["title"] = title_column.find("a").text.strip()
        data["imdb_rating"] = rating_column.find("strong").text

        contents.append(data)
    except AttributeError:
        pass


print(contents)
