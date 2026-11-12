import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

# 빈도와 그룹 집계
# - 값별로 세기와 그룹별로 집계하기

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
print(df.shape, qc.shape)

# 1. 빈도
# - value_counts
# - pd.cut

#print(df["냉각기상태"].value_counts())
#print(df["밸브상태"].value_counts())

# 개수 -> 비율 : normalize
#counts = df["result"].value_counts()
#ratios = df["result"].value_counts(normalize=True)
#print(counts)
#print(ratios.round(3))
#print((ratios * 100).round(1))

# pd.cut
#band = pd.cut(df["온도"], bins=[0, 40, 50 , 200], labels=["낮음", "보통", "높음"], right=True)
#print(band.value_counts(sort=False))

# 그룹 집계
# - 분할 -> 적용 -> 결합 구조
# - groupby

#means = df.groupby("냉각기상태")["온도"].mean()
#print(means.round(2))

#print(df.groupby("냉각기상태")["온도"].max())

# 여러 키 그룹 코드
#keys = ["냉각기상태", "운전부하"]
#print(df.groupby(keys)["온도"].)

# crosstab
print(pd.crosstab(df["냉각기상태"], df["운전부하"]))