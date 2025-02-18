import requests
import json
import os
import time

# デバッグ用ログ出力
def log(message):
    print(f"🔍 {message}")

log("✅ スクリプト開始")

# データ取得対象のURL（適宜変更）
DATA_URL = "https://example.com/api/market-trends"  # ここを実際のURLに変更

# JSONファイルの保存パス
OUTPUT_PATH = os.path.join("static", "market_trends.json")

# データ取得の試行回数
RETRY_COUNT = 3

# ヘッダー情報（必要なら変更）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_market_data():
    """ 市場トレンドデータを取得 """
    for attempt in range(RETRY_COUNT):
        try:
            log(f"🟡 データ取得試行 {attempt + 1} 回目")
            response = requests.get(DATA_URL, headers=HEADERS, timeout=10)

            if response.status_code == 200:
                log("✅ データ取得成功！")
                return response.json()  # JSONデータを取得
            else:
                log(f"⚠️ データ取得失敗 (HTTP {response.status_code})")
        
        except requests.exceptions.RequestException as e:
            log(f"❌ リクエストエラー: {e}")

        time.sleep(3)  # 少し待機してリトライ

    return None  # すべての試行で失敗した場合

def save_data(data):
    """ JSONデータを保存 """
    try:
        log("🔄 データを整形して保存")
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        log(f"✅ データを {OUTPUT_PATH} に保存しました")
    except Exception as e:
        log(f"❌ データ保存に失敗: {e}")

def main():
    """ メイン処理 """
    log("🔄 市場トレンドデータ取得処理を開始")

    data = fetch_market_data()
    
    if data:
        save_data(data)
    else:
        log("❌ データ取得に失敗しました")

if __name__ == "__main__":
    main()
