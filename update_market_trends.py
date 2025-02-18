import requests
import json
import os
import feedparser
from collections import Counter
import MeCab

# YahooニュースのRSSフィードURL
RSS_FEEDS = {
    "AI・半導体": "https://news.yahoo.co.jp/rss/categories/it.xml",
    "EV・電池": "https://news.yahoo.co.jp/rss/categories/economy.xml",
    "宇宙・防衛": "https://news.yahoo.co.jp/rss/categories/science.xml",
    "バイオ・医療": "https://news.yahoo.co.jp/rss/categories/health.xml",
    "脱炭素・エネルギー": "https://news.yahoo.co.jp/rss/categories/local.xml",
    "フィンテック・暗号資産": "https://news.yahoo.co.jp/rss/categories/business.xml",
    "不動産・建設": "https://news.yahoo.co.jp/rss/categories/domestic.xml",
    "ゲーム・エンタメ": "https://news.yahoo.co.jp/rss/categories/entertainment.xml",
    "中国関連": "https://news.yahoo.co.jp/rss/categories/world.xml",
    "IPO・新興市場": "https://news.yahoo.co.jp/rss/categories/stock.xml",
}

OUTPUT_PATH = os.path.join("static", "market_trends.json")

def parse_news_feed(url):
    """ RSSフィードを取得して、ニュースのタイトルをリストに格納 """
    feed = feedparser.parse(url)
    return [entry["title"] for entry in feed.entries]

def classify_news(news_list, theme):
    """ MeCabを使用して形態素解析し、テーマごとに分類 """
    mecab = MeCab.Tagger()
    classified_count = 0
    for news in news_list:
        parsed_text = mecab.parse(news)
        if theme in parsed_text:
            classified_count += 1
    return classified_count

def get_market_trends():
    """ 市場テーマごとのニュース記事数を集計 """
    theme_counts = {}
    
    for theme, url in RSS_FEEDS.items():
        news_list = parse_news_feed(url)
        theme_counts[theme] = classify_news(news_list, theme)

    # 総件数で正規化（割合にする）
    total_articles = sum(theme_counts.values())
    if total_articles > 0:
        theme_ratios = {theme: round((count / total_articles) * 100, 1) for theme, count in theme_counts.items()}
    else:
        theme_ratios = {theme: 0 for theme in RSS_FEEDS.keys()}
    
    return theme_ratios

def save_data(data):
    """ JSONデータを保存 """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    market_trends = get_market_trends()
    save_data(market_trends)
    print("✅ 市場テーマのデータ更新完了")

if __name__ == "__main__":
    main()
