import pandas as pd
import numpy as np

F = 'data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'

df = pd.read_csv(F)

# 데이터 미리보기 및 구조 파악

# 1) 앞 부분 미리보기
# - df.head() > 위에서 5줄, 숫자 지정 가능
#print(df.head())

# 2) 윗 부분 미리보기
# - df.tail() > 밑에서 5줄, 숫자 지정 가능
#print(df.tail())

# 3) 행/열 의 크기
# - df.shape
#print(df.shape)                          # (행, 열)

# 4) 열 이름 목록
# - df.colums    ->  인덱스 형태로 출력
# - df.columns.tolist()     ->  목록으로 보기 좋게
#print(df.columns.tolist())
# ㄴ 여기서 나오는 값으로 특정 열의 데이터 값 추출

# 5) 행 번호표
# - df.index
#print(df.index)                                  # RangeIndex(start=0, stop=200, step=1)
# ㄴ 0부터 시작, 199까지 1 씩

# 6) 열별 자료형
# - df.dtypes
#print(df.dtypes)
#print("----------------------------------------")             # 구분선
#print(pd.read_csv(FD).dtypes)
#측정시각       str
#압축기      int64
#타워       int64
#저압스위치    int64
#dtype: object
#df2 = pd.read_csv(FD, dtype)

# 7) 전체 구조
# - df.info()
#print(df.info())
#<class 'pandas.DataFrame'>
#RangeIndex: 200 entries, 0 to 199                 -> 200행
#Data columns (total 7 columns):                   -> 7열
# #   Column  Non-Null Count  Dtype  
#---  ------  --------------  -----  
# 0   측정시각    200 non-null    str    
# 1   압축압력    200 non-null    float64
# 2   배출압력    200 non-null    float64
# 3   저장압력    200 non-null    float64
# 4   오일온도    199 non-null    float64
# 5   모터전류    200 non-null    float64
# 6   가동상태    200 non-null    str    
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB
# None

# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐

print(df.describe().round(2))

# 특정 조건에서의 통계 필요 시
state = df["가동상태"].values
cur = df["모터전류"].values
print(round(float(np.mean(cur[state == "가동"])), 2))

