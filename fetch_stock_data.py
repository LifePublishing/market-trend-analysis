import yfinance as yf
import json

# 監視する銘柄リスト（例）
stocks_list = [
    {"ticker": "7203.T", "name": "トヨタ"},
    {"ticker": "6758.T", "name": "ソニー"},
    {"ticker": "9984.T", "name": "ソフトバンクG"},
    {"ticker": "7267.T", "name": "ホンダ"},
    {"ticker": "8306.T", "name": "三菱UFJ"}
]

def fetch_stock_changes():
    stock_changes = []
    for stock in stocks_list:
        ticker = stock["ticker"]
        name = stock["name"]

        # 株価取得（直近の終値と過去の終値）
        try:
            data = yf.Ticker(ticker).history(period="5d")  # 直近5日間のデータ
            if len(data) < 2:
                continue  # 十分なデータがない場合スキップ

            latest_price = data["Close"].iloc[-1]  # 最新の終値
            past_price = data["Close"].iloc[0]     # 5日前の終値
            change_percent = round(((latest_price / past_price) - 1) * 100, 2)

            stock_changes.append({"name": name, "change": change_percent})

        except Exception as e:
            print(f"エラー: {name} のデータ取得失敗 -> {e}")

    # 変動率の降順に並べる
    stock_changes.sort(key=lambda x: x["change"], reverse=True)

    # JSONで保存
    with open("stock_data.json", "w", encoding="utf-8") as f:
        json.dump(stock_changes, f, ensure_ascii=False, indent=4)

    print("✅ 株価変動データを 'stock_data.json' に保存しました！")

if __name__ == "__main__":
    fetch_stock_changes()
