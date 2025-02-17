import matplotlib.pyplot as plt
import json
import os
from matplotlib import font_manager

# フォントの設定
font_path = "C:/Windows/Fonts/NotoSansJP-VariableFont_wght.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

# JSONデータの読み込み
data_path = os.path.join("static", "market_trends.json")
with open(data_path, "r", encoding="utf-8") as f:
    market_data = json.load(f)

labels = [item["theme"] for item in market_data]
sizes = [item["count"] for item in market_data]

# 円グラフの作成
fig, ax = plt.subplots(figsize=(7, 7))  # サイズを大きめに設定
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False
)

# フォント適用
for text in texts + autotexts:
    text.set_fontproperties(font_prop)
    text.set_fontsize(12)  # フォントサイズを調整

ax.set_title("市場テーマの注目度", fontproperties=font_prop, fontsize=16)

# レイアウト調整（見切れ防止）
plt.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.2)

# 画像保存
plt.savefig("static/pie_chart.png", bbox_inches='tight', dpi=100)

print("✅ 円グラフを 'static/pie_chart.png' に保存しました！")
