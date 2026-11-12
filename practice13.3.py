# 실습 1
import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

#print("로그:", log.shape)
#print("대장:", master.shape)
#print("로그 칸:", list(log.columns))
#print("대장 칸:", list(master.columns))
#common = list(set(log.columns) & set(master.columns))
#print("공통 칸:", common)
#key = common[0]
#merged = log.merge(master, on=key, how="inner")
#print("합친 표:", merged.shape)
#print(merged.head(2))

# 실습 2

#key = list(set(log.columns) & set(master.columns))[0]
#inner = log.merge(master, on=key, how="inner")

#print("inner:", len(inner))
#left = log.merge(master, on=key, how="left")
#outer = log.merge(master, on=key, how="outer", indicator=True)

#print("left:", len(left))
#print("outer:", len(outer))
#print("차이:", len(left) - len(inner))

#new_cols = [c for c in master.columns if c != key]

#print(left[left[new_cols[0]].isna()][key].value_counts())   
#print(outer[outer["_merge"] == "right_only"][key])          
#print(outer["_merge"].value_counts())

# 실습 3

#print(log.shape)
#front = log.iloc[:100].reset_index(drop=True)
#back = log.iloc[100:].reset_index(drop=True)

#merged = pd.concat([front, back])
#print(merged.shape)

#print((merged.index == 0).sum())
#ignore_index=True
#merged2 = pd.concat([front, back], ignore_index=True)
#print(merged2.index[-1])

# 실습 4

print(log.columns.tolist())
print(master.columns.tolist())
merged = log.merge(master, on="설비ID", how="left")  
print(merged.shape)

has_line = merged[merged["라인"].notna()]
print(len(has_line))
bad = has_line[has_line["품질등급"] != "양품"]
print(len(bad))

cols = ["샷", "설비ID", "라인", "비스킷두께", "품질등급"]
print(bad.sort_values("비스킷두께", ascending=False)[cols].head(5))