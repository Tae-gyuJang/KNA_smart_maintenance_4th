import pandas as pd

F_SMALL = 'data/13_diecasting_small.csv'
F_SHOT = 'data/13_diecasting_shot.csv'

# 열 골라내기
# - 열 이름
df = pd.read_csv(F_SMALL)

#print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())

# 단일 열 선택
# - d["실린더압력"]
# -결과값은 dataframe으로 나온다
#print(df[["형체력", "실린더압력"]])

# 행 선택
# - 라벨과 위치 번호의 차이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번째인지, 항상 0부터

#sorted = df.sort_values("형체력", ascending=False)

#print("정렬 후 인덱스 앞 4개:", sorted.index[:4].tolist())
#print("정렬 후 iloc[0] 샷:", int(sorted.iloc[0]['샷']))
#print("정렬 후 loc[0] 샷:", int(sorted.loc[0, '샷']))

# 여러 행 선택
print(df.loc[0:4].shape)
print(df.iloc[0:4].shape)

# 행, 열 동시 선택
# df.loc[행, 열] - 열이름 사용 O / df.iloc[행, 열] - 열이름 사용X -> 숫자로 접근
print(df.loc[0:4, ['실린더압력', '형체력']].shape)
print(df.iloc[0:5, [2,6]].shape)

