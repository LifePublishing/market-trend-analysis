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
fig, ax = plt.subplots(figsize=(7, 7))  # サイズを少し大きめに設定
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False
)

# フォント適用
for text in texts + autotexts:
    text.set_fontproperties(font_prop)
    text.set_fontsize(14)  # フォントサイズを大きめに設定

ax.set_title("市場テーマの注目度", fontproperties=font_prop, fontsize=16)

# 画像保存時にラベルが見切れないように調整
plt.subplots_adjust(left=0.3, right=0.7, top=0.9, bottom=0.1)  # 余白を広げる
plt.savefig("static/pie_chart.png", bbox_inches='tight', dpi=100, bbox_extra_artists=texts)

print("✅ 円グラフを 'static/pie_chart.png' に保存しました！")
