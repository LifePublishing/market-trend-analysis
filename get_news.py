import feedparser
import pandas as pd

# Yahoo!ニュースのRSSフィードURL
RSS_FEEDS = {
    "経済": "https://news.yahoo.co.jp/rss/categories/business.xml",
    "IT": "https://news.yahoo.co.jp/rss/categories/it.xml",
    "国際": "https://news.yahoo.co.jp/rss/categories/world.xml",
    "科学": "https://news.yahoo.co.jp/rss/categories/science.xml"
}

# 市場テーマのキーワード（修正後）
MARKET_THEMES = [
    "AI", "半導体", "フィンテック", "暗号資産", "仮想通貨", "暗号通貨",
    "EV", "電気自動車", "リチウムイオン電池", "鉛蓄電池", "ニッケル水素電池", "ニッケルカドミウム電池", "全固体電池",
    "宇宙", "防衛", "不動産", "建設", "ゲーム", "エンタメ", "バイオ", "医療",
    "中国", "脱炭素", "エネルギー", "IPO", "新興市場", "市場", "金融", "物価", "インフレ", "円安", "円高", "金利"
]

def fetch_news():
    news_list = []
    
    for category, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            published = entry.published

            # 市場テーマのキーワードがタイトルに含まれるかチェック
            for theme in MARKET_THEMES:
                if theme in title:
                    news_list.append({"title": title, "link": link, "published": published, "theme": theme})
                    break  # 1つのニュースを1つのテーマに分類

    # 結果をCSVファイルに保存
    df = pd.DataFrame(news_list)
    df.to_csv("static/news_data.csv", index=False, encoding="utf-8-sig")
    print("✅ ニュースデータ取得完了: static/news_data.csv")

if __name__ == "__main__":
    fetch_news()
