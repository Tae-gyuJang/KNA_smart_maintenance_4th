# 실습 1
import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
df = pd.read_csv(F_SHOT)
#print(df.shape)

#cond = df["비스킷두께"] >= 16      
#print(cond.sum())                        

#picked = df[cond]
#print(len(picked))                        

#cond_lt = df["비스킷두께"] < 16
#print(cond_lt.sum())                      
#print(cond.sum() + cond_lt.sum())         
#print(len(df))                            
#print(df["비스킷두께"].isna().sum())  

# 실습 2

#c1 = df["비스킷두께"] >= 16
#c2 = df["사이클타임"] >= 25
#print((c1 & c2).sum())
#print((c1 | c2).sum())

#bad = df["품질등급"] == "불량"
#print((~bad).sum())

# 실습 3
#m1 = df["품질등급"].isin(["주의", "불량"])    
#print(m1.sum())                                    

#m2 = df["비스킷두께"].between(10, 16)
#print(m2.sum())                                    

#m3 = df["설비ID"].str.contains("A", na=False)     
#m4 = df["설비ID"] == "A라인1호기"
#print(m3.sum(), m4.sum())

# 실습 4

#top5 = df.sort_values("비스킷두께", ascending=False).head(5)
#print(top5)
#multi = df.sort_values(["품질등급", "사이클타임"],ascending=[True, False]).head(5)
#print(multi)
#print(df.head(5))

# 실습 5
cond = (df["품질등급"] != "양품") & (df["비스킷두께"] >= 16)
filtered = df[cond]
print("조건 통과:", len(filtered), "줄")

result = filtered.sort_values("비스킷두께", ascending=False)
print(result[["설비ID", "비스킷두께", "품질등급"]].head(5))

missing = df[(df["품질등급"] != "양품") & (df["비스킷두께"].isna())]
print("미포함 결측샷:", len(missing), "줄")
