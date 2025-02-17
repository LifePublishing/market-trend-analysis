import json
import numpy as np
import spacy

# 日本語の形態素解析モデルをロード
nlp = spacy.load("ja_core_news_sm")

# 市場テーマの定義（送られたキーワードをそのまま適用）
MARKET_THEMES = {
    "AI・半導体": ["AI", "半導体", "NVIDIA", "TSMC", "人工知能"],
    "EV・電池": ["EV", "電気自動車", "リチウムイオン電池", "鉛蓄電池", "ニッケル水素電池", "ニッケルカドミウム電池", "全固体電池", "充電", "テスラ"],
    "宇宙・防衛": ["宇宙", "防衛", "ロケット", "人工衛星", "軍事"],
    "バイオ・医療": ["バイオ", "医療", "ワクチン", "創薬", "治療"],
    "脱炭素・エネルギー": ["脱炭素", "再生可能エネルギー", "水素", "風力", "太陽光"],
    "フィンテック・暗号資産": ["フィンテック", "暗号資産", "仮想通貨", "暗号通貨", "ブロックチェーン", "ビットコイン"],
    "不動産・建設": ["不動産", "建設", "マンション", "住宅", "地価"],
    "ゲーム・エンタメ": ["ゲーム", "エンタメ", "eスポーツ", "Nintendo", "PS5", "アニメ"],
    "中国関連": ["中国", "中国経済", "米中", "習近平", "上海"],
    "IPO・新興市場": ["IPO", "新興市場"]
}

# ニュースデータの読み込み
with open("news_data_raw.json", "r", encoding="utf-8") as file:
    news_data = json.load(file)

classified_news = []

for news in news_data:
    title = news["title"]
    doc = nlp(title)

    best_match = None
    best_score = -1

    # キーワードマッチング
    for theme, keywords in MARKET_THEMES.items():
        for keyword in keywords:
            if keyword in title:
                best_match = theme
                break  # 最初にマッチしたテーマを適用

    # ベクトル類似度分析
    if best_match is None:
        news_vector = doc.vector
        for theme, keywords in MARKET_THEMES.items():
            theme_vector = np.mean([nlp(keyword).vector for keyword in keywords], axis=0)
            similarity = np.dot(theme_vector, news_vector) / (np.linalg.norm(theme_vector) * np.linalg.norm(news_vector))
            if similarity > best_score:
                best_score = similarity
                best_match = theme

    news["theme"] = best_match if best_match else "その他"
    classified_news.append(news)

# 分類結果を保存
with open("news_data_classified.json", "w", encoding="utf-8") as file:
    json.dump(classified_news, file, ensure_ascii=False, indent=4)

print("✅ ニュース分類が完了しました！ → news_data_classified.json に保存")
