#실습 1

import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

#print(df.shape)
#print(df.columns.tolist())

#print(df["밸브상태"].value_counts())
#print(df["밸브상태"].value_counts(normalize=True).round(3))

#print(df["운전부하"].value_counts())
#print(df["운전부하"].value_counts(normalize=True).round(3))

#for col in ["밸브상태", "운전부하"]:
#    vc = df[col].value_counts()
#    print(col, "최대:", vc[vc == vc.max()].index.tolist())
#    print(col, "최소:", vc[vc == vc.min()].index.tolist())

# 실습 2

#print(qc.shape)
#print(qc.columns.tolist())
#print(qc["검사결과"].value_counts())

#ratio = qc["검사결과"].value_counts(normalize=True).round(3)
#print(ratio)  

#fail_pct = ratio["불합격"] * 100
#print(f"불합격은 전체의 약 {fail_pct:.0f}%")

# 실습 3

#print(df.columns.tolist())
#print(df["진동"].min(), df["진동"].max())

#df["진동구간"] = pd.cut(df["진동"], bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"])

#print(df["진동구간"].value_counts()) 
#print(df["진동구간"].isna().sum()) 

#vc = df["진동구간"].value_counts()
#print("최대:", vc[vc == vc.max()].index.tolist())  
#print("최소:", vc[vc == vc.min()].index.tolist())  

#df["진동구간2"] = pd.cut(df["진동"], bins=[0, 0.62, 0.7, 10], labels=["약함", "보통", "강함"])
#print(df["진동구간2"].value_counts())

# 실습 4

#print(df.columns.tolist()) 

#print(df["냉각기상태"].value_counts())             

#mean_t = df.groupby("냉각기상태")["온도"].mean().round(2)
#print(mean_t)                                      

#summary = df.groupby("냉각기상태")["온도"].agg(["mean", "max"]).round(2)
#print(summary)

#print(round(mean_t.max() - mean_t.min(), 2))

# 실습 5

print(df.columns.tolist())   

total = df["밸브상태"].value_counts()
print(total)                                       

fault = df[df["result"] == "고장"]
print(len(fault))

fault_cnt = fault["밸브상태"].value_counts()
print(fault_cnt)                                   

ratio = (fault_cnt / total).round(3)
print(ratio.sort_values(ascending=False))          
print("가장 높은 상태:", ratio.idxmax())