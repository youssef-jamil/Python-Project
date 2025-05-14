# This Python code snippet is a web scraper that uses the `requests` library to make an HTTP request
# to a website and the `BeautifulSoup` library to parse the HTML content of the webpage. The code is
# specifically targeting the website "https://quotes.toscrape.com" to extract quotes and authors from
# the webpage.
import requests
from bs4 import BeautifulSoup

# ! web scraper to get and analyze the information from the website
# ! https://www.imdb.com/chart/top/?ref_=nv_mv_250
# ! and save the data in a csv file
# ! and a json file
# ! and a text file
# ! and a sqlite database
inFile = "out_put.txt"

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")
    with open(inFile, "w", encoding="utf-8") as file:
        for quote, author in zip(quotes, authors):
            file.write(f"{quote.text} - {author.text}\n")
