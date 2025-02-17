import json
import requests
from bs4 import BeautifulSoup

YAHOO_NEWS_RSS = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"

def get_news_data():
    response = requests.get(YAHOO_NEWS_RSS)
    response.encoding = response.apparent_encoding  # 自動検出
    soup = BeautifulSoup(response.text, "xml")

    news_list = []
    for item in soup.find_all("item"):
        title = item.title.text
        link = item.link.text
        published = item.pubDate.text
        category = item.find("category").text if item.find("category") else "その他"

        news_list.append({
            "category": category,
            "title": title,
            "link": link,
            "published": published
        })

    return news_list

def save_news_data(news_data):
    """ ニュースデータをUTF-8でJSONファイルに保存する """
    with open("news_data_raw.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_data = get_news_data()
    save_news_data(news_data)
    print(f"✅ {len(news_data)} 件のニュースを取得しました（news_data_raw.json）")
