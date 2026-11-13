import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)

# 결측 처리
# - 종류: NaN, None, NA, NaT
# ㄴ 표현은 달라도 isna()로 결측 여부 확인 가능

s = pd.Series([10, None, 20])
print(s.mean())                       # 15.0  (NaN 값이 있다고해서 계산이 멈춘다 X (10 + 20) / 2)
print(s + 1)                          # 11.0 , NaN , 21.0

