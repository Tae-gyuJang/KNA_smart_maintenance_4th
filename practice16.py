# 실습 1

import pandas as pd

df = pd.read_csv("data/16_diecasting.csv")
print(df.head())

#print(df.shape)     
#print(df.columns)

#df.info()

# 실습 2

#col = "실린더압력" 

#min_val = df[col].min()
#max_val = df[col].max()
#range_val = max_val - min_val

#print("최솟값:", min_val)
#print("최댓값:", max_val)
#print("범위:", range_val)

# 실습 3

#col = "사이클타임"

#sorted_df = df.sort_values(col, ascending=False)
#print(sorted_df.head(10))

#print(sorted_df.tail(5))

#def classify(x):
#    if 20 <= x <= 35:
#        return "정상"
#    else:
#        return "이상(설비잼 후보)"

#df["상태"] = df[col].apply(classify)

#print(df["상태"].value_counts())
#print(df[df["상태"] != "정상"].sort_values(col, ascending=False))

# 실습 4

#col = "사이클타임"

#mean_all = df[col].mean()
#median_all = df[col].median()
#print("전체 평균:", round(mean_all, 2))
#print("전체 중앙값:", round(median_all, 2))
#print("차이:", round(mean_all - median_all, 2))

#normal = df[df["상태"] == "정상"]

#mean_n = normal[col].mean()
#median_n = normal[col].median()
#print("정상 평균:", round(mean_n, 2))
#print("정상 중앙값:", round(median_n, 2))
#print("차이:", round(mean_n - median_n, 2))

# 실습 5

#col = "실린더압력"

#q1 = df[col].quantile(0.25)

#q2 = df[col].quantile(0.5)
#median = df[col].median()

#q3 = df[col].quantile(0.75)

#print("Q1:", q1)
#print("Q2:", q2)
#print("Q3:", q3)
#print("Q2 == 중앙값:", q2 == median)
#print("가운데 50% 범위(IQR):", q3 - q1)

#print(df[col].quantile([0.25, 0.5, 0.75]))

# 실습 6

#desc = df.describe()
#print(desc)

#summary = desc.T
#summary["중앙값"] = summary["50%"]
#summary["격차"] = summary["mean"] - summary["중앙값"]
#summary["격차비율(%)"] = (summary["격차"].abs() / summary["중앙값"].abs() * 100).round(1)

#result = summary[["mean", "중앙값", "격차", "격차비율(%)"]].sort_values(
#    "격차비율(%)", ascending=False
#)
#print(result)

# 실습 7

cols = ["실린더압력", "사이클타임", "비스킷두께"] 

q = df[cols].quantile([0.25, 0.5, 0.75])
print(q)

iqr = q.loc[0.75] - q.loc[0.25]
print(iqr)

print(iqr.sort_values())