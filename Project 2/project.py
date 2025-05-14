import requests
from bs4 import BeautifulSoup

inFile = "out_put.txt"

response = requests.get("http://books.toscrape.com")

soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    rate = book.find("p", class_="star-rating")["class"][1]
    availability = book.find("p", class_="instock availability").text.strip()
    print(
        f"Title: {title}, Price: {price}, Rating: {rate}, Availability: {availability}\n"
    )

    with open(inFile, "a", encoding="utf-8") as file:
        file.write(
            f"Title: {title}, Price: {price}, Rating: {rate}, Availability: {availability}\n"
        )
