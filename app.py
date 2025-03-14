from flask import Flask, render_template, jsonify
from fetch_news import fetch_yahoo_finance_news

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/news")
def get_news():
    news = fetch_yahoo_finance_news()
    return jsonify(news)

if __name__ == "__main__":
    app.run(debug=True)
