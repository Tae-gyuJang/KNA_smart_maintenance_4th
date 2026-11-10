# 실습1

import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

#df = pd.read_csv(F)
#print(df.shape)
#print(df.head())
#print(df.isna().sum())

# 실습 2

#df3 = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
#print(df3.shape)
#df20 = pd.read_csv(F, nrows=20)
#print(df20.shape)

# 실습 3

F2 = 'data/12_metro_compressor_semicolon.csv'
#df_bad = pd.read_csv(F2)
#print(df_bad.shape)
#print(df_bad.head(3))
#df_ok = pd.read_csv(F2, sep=",", encoding="utf-8")
#print(df_ok.shape)
#print(df_ok.columns.tolist())

# 실습 4
df = pd.read_csv(F2, sep=";", encoding="utf-8",usecols=["측정시각", "오일온도", "모터전류"],  
    nrows=50,)
print(df.shape)
print(df.head())