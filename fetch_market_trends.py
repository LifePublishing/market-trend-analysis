import json
from collections import defaultdict

# 市場テーマのリスト
market_themes = [
    "AI・半導体", "EV・電池", "宇宙・防衛", "バイオ・医療",
    "脱炭素・エネルギー", "フィンテック・暗号資産", "不動産・建設",
    "ゲーム・エンタメ", "中国関連", "IPO・新興市場"
]

theme_counts = defaultdict(int)

try:
    with open("news_data_classified.json", "r", encoding="utf-8") as file:
        news_data = json.load(file)
except FileNotFoundError:
    print("❌ 'news_data_classified.json' が見つかりません。")
    exit()
except json.JSONDecodeError:
    print("❌ 'news_data_classified.json' の形式が不正です。")
    exit()

for article in news_data:
    theme = article.get("theme", "その他").strip()
    if theme in market_themes:
        theme_counts[theme] += 1

with open("market_trends.json", "w", encoding="utf-8") as file:
    json.dump(theme_counts, file, ensure_ascii=False, indent=4)

print("✅ 市場テーマのデータを 'market_trends.json' に保存しました！")
