import requests
from bs4 import BeautifulSoup

def fetch_yahoo_finance_news():
    url = "https://news.yahoo.co.jp/categories/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []
    for item in soup.select(".newsFeed_item"):
        title = item.select_one(".newsFeed_item_title").text
        link = item.select_one("a")["href"]
        image = item.select_one("img")["src"] if item.select_one("img") else ""

        news_list.append({
            "title": title,
            "link": link,
            "image": image
        })

    return news_list
