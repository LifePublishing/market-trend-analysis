import json
import yfinance as yf

# 監視する銘柄リスト（例）
STOCKS = ["7203.T", "6758.T", "9984.T"]

stock_data = {}

for symbol in STOCKS:
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d")
    
    if not hist.empty:
        latest_price = hist["Close"].iloc[-1]
        prev_price = hist["Open"].iloc[0]
        change = ((latest_price - prev_price) / prev_price) * 100
        stock_data[symbol] = {"price": latest_price, "change": round(change, 2)}

with open("stock_trend.json", "w", encoding="utf-8") as file:
    json.dump(stock_data, file, ensure_ascii=False, indent=4)

print("✅ 株価データを 'stock_trend.json' に保存しました！")
