import pandas as pd
import numpy as np
F = 'data/12_metro_compressor.csv'

#df = pd.read_csv(F)
#print(df.head())
#print(df.tail())
#print(df.head(3))
#print(df.tail(10))
#print(df.head().isna())

# 실습 2

FD = 'data/12_metro_digital.csv'
#df2 = pd.read_csv(FD)

#print(df2.shape)
#print(df2.columns.tolist())
#print(df2.dtypes)
#print(df2.head())

# 실습 3

#df = pd.read_csv('data/12_metro_compressor.csv')
#print(df.info())

# 실습 4

#print(df.describe())
#print(df.describe().loc[['mean', '50%']].T)
#s = df.describe().loc[['mean', '50%']].T
#s ['차이'] = (s['mean'] - s['50%']).abs()
#print(s.sort_values('차이', ascending=False))

#cur = df['모터전류'].values
#state = df['가동상태'].values

#print(round(cur[state == '가동'].mean(), 2))
#print(round(cur[state == '정지'].mean(), 2))

# 실습 5

#import pandas as pd
#import numpy as np

#comp = pd.read_csv(F)   
#dig  = pd.read_csv(FD)      
#print("압축기:", comp.shape)   
#print("디지털:", dig.shape)    
#print(comp.dtypes)   
#print(dig.dtypes)    
#print(comp.info())   
#print(dig.info())    

#for col in dig.columns:
#    vals, cnts = np.unique(dig[col].dropna(), return_counts=True)

#print(col, vals, cnts)

# 실습 6

df = pd.read_csv("data/12_metro_small.csv")
print(df.head())

print(df.shape)      
print(df.info())

missing = len(df) - df.count()
print(missing[missing > 0])   

desc = df.describe()
print(desc.loc[["mean", "50%"]])

gap = (desc.loc["mean"] - desc.loc["50%"]).abs()
print(gap.sort_values(ascending=False))   

col = gap.idxmax()
print(col, desc.loc["mean", col], desc.loc["50%", col])
