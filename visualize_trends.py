from flask import Flask, render_template, send_from_directory
import json

app = Flask(__name__)

@app.route("/")
def index():
    # 変動率ランキングのデータをロード
    with open("stock_trends.json", "r", encoding="utf-8") as f:
        stock_trends = json.load(f)

    return render_template("index.html", stock_trends=stock_trends)

if __name__ == "__main__":
    app.run(debug=True)
