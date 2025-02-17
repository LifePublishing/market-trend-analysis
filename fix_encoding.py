import json

# 元のJSONファイルを読み込む
with open("news_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 文字化けを修正（ここでは特に変更せず、データをそのまま使う）
fixed_data = data

# 修正後のデータをUTF-8（BOM付き）で保存
with open("news_data_fixed.json", "w", encoding="utf-8-sig") as f:
    json.dump(fixed_data, f, indent=4, ensure_ascii=False)

print("✅ 修正済みデータを news_data_fixed.json に保存しました！")
