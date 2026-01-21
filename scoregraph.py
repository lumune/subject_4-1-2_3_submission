import pandas as pd
import matplotlib.pyplot as plt

# 日本語フォント設定（←これが超重要）
plt.rcParams["font.family"] = "Hiragino Sans"

# 1. CSV を読み込む
df = pd.read_csv("課題3.csv")  # 文字化けする場合は encoding="utf-8-sig" などに変更

# 2. 列名を指定（あなたの CSV に合わせて変更）
dept_col = "所属"   # 所属を表す列名
score_col = "スコア" # スコアを表す列名
if dept_col not in df.columns or score_col not in df.columns:
    raise ValueError(f"CSV に '{dept_col}' または '{score_col}' がありません")

# 3. 所属ごとに最高スコア・最低スコアを集計
agg_scores = df.groupby(dept_col)[score_col].agg(["max", "min"]).reset_index()

# 4. 棒グラフ：所属ごとの最高・最低スコア
plt.figure(figsize=(10, 5))
bar_width = 0.4
index = range(len(agg_scores))
plt.bar([i - bar_width/2 for i in index], agg_scores["max"],
        width=bar_width, color="royalblue", label="最高点")
plt.bar([i + bar_width/2 for i in index], agg_scores["min"],
        width=bar_width, color="tomato", label="最低点")
plt.xticks(index, agg_scores[dept_col], rotation=45, ha="right")
plt.ylabel("スコア")
plt.title("所属ごとの最高スコア・最低スコア")
plt.legend()   # ← 凡例
plt.tight_layout()
plt.savefig("scores_by_dept.png", dpi=150)
plt.close()

# 5. 円グラフ：所属ごとの参加者数
counts = df[dept_col].value_counts().reset_index()
counts.columns = [dept_col, "count"]
plt.figure(figsize=(6, 6))
plt.pie(counts["count"],
        labels=counts[dept_col],
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False)
plt.title("所属ごとの参加者数")
plt.tight_layout()
plt.savefig("participants_pie.png", dpi=150)
plt.close()

# 6. ヒストグラム：全参加者のスコア分布
bins = [70, 75, 80, 85, 90, 95, 100]
plt.figure(figsize=(8, 4))
plt.hist(df[score_col], bins=bins, color="seagreen", edgecolor="white")
plt.xlabel("スコア")
plt.ylabel("人数")
plt.title("スコア分布（全参加者）")
plt.tight_layout()
plt.savefig("score_histogram.png", dpi=150)
plt.close()

print("棒グラフ: scores_by_dept.png を保存しました")
print("円グラフ: participants_pie.png を保存しました")
print("ヒストグラム: score_histogram.png を保存しました")