import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# 실습 1

#print(qc.columns.tolist())
#print(qc["검사결과"].value_counts())

#print(qc.groupby("검사결과")["온도"].agg(["mean", "std", "max"]).round(2))
#summary = qc.groupby("검사결과").agg(
#    평균온도=("온도", "mean"),
#    평균냉각효율=("냉각효율", "mean"),
#    측정수=("온도", "count"),
#).round(2)
#print(summary)
#print(summary.loc["불합격"] - summary.loc["합격"])

# 실습 2

#print(df.columns.tolist())
#d = df.copy()
#d["상태평균"] = d.groupby("냉각기상태")["온도"].transform("mean")

#d["편차"] = d["온도"] - d["상태평균"]
#print(d[["냉각기상태", "온도", "상태평균", "편차"]].head(3))

#idx = d["편차"].abs().idxmax()
#print(d.loc[idx, ["냉각기상태", "온도", "편차"]])

#pt = d.pivot_table(index="밸브상태", columns="운전부하",
#                   values="온도", aggfunc="mean", margins=True).round(2)
#print(pt)
#print(pt.shape)

# 실습 3
import numpy as np

#print(df.columns.tolist())
#print(df["온도"].corr(df["진동"]))

#print(df["온도"].corr(df["압력"]))
#print(df["온도"].corr(df["냉각효율"]))

#cols = ["온도", "진동", "압력", "냉각효율"]
#corr = df[cols].corr().round(3)
#print(corr)

#mask = np.triu(np.ones(corr.shape, dtype=bool), k=1)
#pairs = corr.where(mask).stack()
#print(pairs)

#print("가장 강한 짝:", pairs.abs().idxmax(), pairs[pairs.abs().idxmax()])   
#print("가장 약한 짝:", pairs.abs().idxmin(), pairs[pairs.abs().idxmin()]) 

#실습 4

#print(qc.columns.tolist())
#num = qc.select_dtypes(include="number")
#print(num.shape)                                   
#corr = num.corr()
#print(corr.shape)                                  

#mask = np.triu(np.ones(corr.shape, dtype=bool), k=1)
#pairs = corr.where(mask).stack(future_stack=True).dropna()
#pair_table = pairs.reset_index()
#pair_table.columns = ["지표1", "지표2", "상관"]
#pair_table["절대값"] = pair_table["상관"].abs()
#print(len(pair_table))                             

#print((pair_table["절대값"] >= 0.4).sum())          
#print((pair_table["절대값"] >= 0.95).sum())         

#top5 = (pair_table[pair_table["절대값"] >= 0.95]
#        .sort_values("절대값", ascending=False)
#        .head(5)[["지표1", "지표2", "상관"]])
#print(top5)

# 실습 5
print(df.columns.tolist())   
print(qc.columns.tolist())   
ref = qc   
print(ref["result"].duplicated().sum())          

m = df.merge(ref, on="result", how="left")
print(m.shape)                                       
print(m[["기준열1", "기준열2", "위험도", "점검주기"]].isna().sum()) 

m["온도구간"] = pd.cut(m["온도"], bins=[0, 40, 50, 200],
                       labels=["낮음", "보통", "높음"])
print(m["온도구간"].value_counts())                   

diag = m.groupby("result").agg(
    측정수=("온도", "count"),
    평균온도=("온도", "mean"),
    온도표준편차=("온도", "std"),
    평균냉각효율=("냉각효율", "mean"),
    위험도=("위험도", "first"),
    점검주기=("점검주기", "first"),
).round(2)
print(diag.shape)                                     
print(pd.crosstab(m["result"], m["온도구간"]))    
print(m["온도"].corr(m["냉각효율"]))                  
print(m["온도"].corr(m["진동"]))                      
diag = diag.sort_values(["위험도", "평균온도"], ascending=[False, False])
print(diag)                     