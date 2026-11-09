# Pandas
import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - Series : 하나의 열들
# - DataFrame : Series가 모여서 합쳐진 것, 표 구조 (df)

# 앞 단원 방식 -> 숫자 열만 골라야 함
# Pandas 방식 -> 글자 열까지 그대로, 열은 이름으로

df = pd.read_csv(F)
#print("데이터 크기:", df.shape)    # 데이터 크기: (200, 7)

#print(df.head())
#                   측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
#0  2020-02-27 06:38:47  9.30 -0.02  9.30  51.3  6.04   가동
#1  2020-02-27 07:28:21  8.55 -0.02  8.55  56.8  0.04   정지
#2  2020-02-27 08:17:54  8.67 -0.02  8.67  55.7  0.03   정지
#3  2020-02-27 09:07:27  9.76 -0.02  9.76   NaN  3.81   가동
#4  2020-02-27 09:57:01  8.49 -0.02  8.49  55.3  0.04   정지

#print("열 이름:", df.columns.tolist())
# 열 이름: ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

#print(df.dtypes)
#측정시각        str
#압축압력    float64
#배출압력    float64
#저장압력    float64
#오일온도    float64
#모터전류    float64
#가동상태        str
#dtype: object

state = df["가동상태"].values
print("가동상태 종류 계수:", np.unique(state, return_counts=True))

cur = df["모터전류"].values
print("모터전류 평균 %.2f / 가운데 값 %.2f" % (np.mean(cur), np.median(cur)))

s = df["오일온도"]
print(s.head(3))

# Pandas = 열 이름
new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
print(new.shape)

# 행 수를 제한하는 설정
print(pd.read_csv(F, nrows=10).shape)

# read_csv 옵션
# - usecols, nrows, encoding, sep(구분자)

# 값을 나누는 기호를 알려줘서 나눠줘야함
b = pd.read_csv(F5, sep=";", encoding="utf-8")
