import json
import os
import time
from yahoo_fin.stock_info import get_day_gainers

OUTPUT_PATH = os.path.join("static", "stock_data.json")

def fetch_stock_data():
    """ 東証全銘柄の株価変動率を取得 """
    try:
        gainers = get_day_gainers()
        stock_changes = []
        
        for _, row in gainers.iterrows():
            stock_changes.append({
                "code": row["Symbol"],
                "name": row["Name"],
                "change_percent": row["% Change"]
            })

        return stock_changes
    except Exception as e:
        print(f"❌ 株価データ取得エラー: {e}")
        return []

def save_data(data):
    """ JSONデータを保存 """
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    print("🔄 株価データの取得開始")
    stock_data = fetch_stock_data()
    
    if stock_data:
        save_data(stock_data)
        print("✅ 株価データを更新しました")
    else:
        print("❌ 株価データの更新に失敗しました")

if __name__ == "__main__":
    main()
