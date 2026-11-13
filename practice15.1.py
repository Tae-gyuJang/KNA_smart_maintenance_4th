import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
log = pd.read_csv(F_LOG)
# 실습 1

print(log.shape)
print(log.columns.tolist())

print(log.isna().sum())
print(log.isna().sum().sum())

print((log["사출압력"] == 0).sum())  
print((log["스크루속도"] == -999).sum())
print((log["배럴온도"] == 999).sum())