import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
log = pd.read_csv(F_LOG)
# 실습 1

#print(log.shape)
#print(log.columns.tolist())

#print(log.isna().sum())
#print(log.isna().sum().sum())

#print((log["사출압력"] == 0).sum())  
#print((log["스크루속도"] == -999).sum())
#print((log["배럴온도"] == 999).sum())

#실습 2

#proc = pd.read_csv(F_PROC)

#print(proc.shape)                          
#print(proc.head(3))

#proc.info()

#print(proc["최대사출속도"].describe())      
#print(proc["최대사출속도"].isna().sum())

# 실습 3

#base = pd.read_csv(F_LOG)
#print(base.columns.tolist())               
#print(base.isna().sum().sum())             

#step2 = pd.read_csv(F_LOG, na_values={"배럴온도": [999], "스크루속도": [-999],})
#print(step2.isna().sum().sum())            

#step3 = pd.read_csv(F_LOG, na_values={"배럴온도": [999] ,"스크루속도": [-999], "사출압력": [0],})

# 실습 4

#proc = pd.read_csv(F_PROC)    
#count = proc.isna().sum()

#pct = (count / len(proc) * 100).round(1)

#summary = pd.DataFrame({"결측수": count, "결측률(%)": pct})
#summary = summary[summary["결측수"] > 0].sort_values("결측수", ascending=False)

#print(len(summary))          
#print(summary)             

# 실습 5
#proc = pd.read_csv(F_PROC)    

#rate = (proc.isna().mean() * 100).round(1)
#print(rate.sort_values(ascending=False).head(3))

#row_na = proc.isna().sum(axis=1)
#print((row_na == 0).sum())      
#print((row_na > 0).sum())       

#heavy = proc[row_na >= 5]
#print(len(heavy))               
#print(heavy.shape)

# 실습 6

proc = pd.read_csv(F_PROC)    
print(proc.columns.tolist())  
cols = ["최대사출속도", "감압시간"]
print(proc[cols].isna().sum())                 
print(proc[cols].isna().head(10))

a = proc["최대사출속도"].isna()
b = proc["감압시간"].isna()
both = a & b
print(both.sum())                              
print(round(both.mean() * 100, 1))             

print(proc.loc[both, ["측정시각", "사출기"]].head())   
only_one = (a ^ b).sum()
none_missing = (~a & ~b).sum()
print(only_one)                                
print(none_missing)                            
print(both.sum() + only_one + none_missing)