from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

DATA_PATH_MARKET = os.path.join("static", "market_trends.json")
DATA_PATH_STOCKS = os.path.join("static", "stock_data.json")

def load_data(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@app.route("/")
def home():
    market_trends = load_data(DATA_PATH_MARKET)
    stock_data = load_data(DATA_PATH_STOCKS)
    return render_template("index.html", market_trends=market_trends, stock_data=stock_data)

if __name__ == "__main__":
    app.run(debug=True)
