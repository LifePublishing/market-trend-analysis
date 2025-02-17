import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_news_content(news_url):
    """ Selenium を使って JavaScript を実行し、記事の本文を取得する """
    
    # Chromeの設定
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモード（ブラウザ画面を表示しない）
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # ChromeDriverの起動
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(news_url)
        time.sleep(3)  # ページの読み込み待機

        # Yahooニュースの記事本文を取得
        article_body = driver.find_element(By.CLASS_NAME, "article_body")
        if article_body:
            return article_body.text

        return "本文なし"

    except Exception as e:
        return f"エラー: {str(e)}"

    finally:
        driver.quit()  # ブラウザを閉じる

def load_news_data():
    """ JSONファイルをUTF-8で読み込む """
    with open("news_data_raw.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_news_data(news_data):
    """ 記事の本文付きデータをUTF-8でJSONファイルに保存する """
    with open("news_data_fixed.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_data = load_news_data()

    for i, news in enumerate(news_data, start=1):
        print(f"[{i}/{len(news_data)}] {news['link']} から本文を取得中...")
        news["content"] = get_news_content(news["link"])

    save_news_data(news_data)
    print("✅ Yahooニュースの記事本文を取得しました！ → news_data_fixed.json に保存")
