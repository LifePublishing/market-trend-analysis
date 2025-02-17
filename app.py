from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stock_trends")
def stock_trends():
    data_path = os.path.join("static", "stock_trends.json")
    with open(data_path, "r", encoding="utf-8") as f:
        stock_data = json.load(f)

    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(debug=True)
