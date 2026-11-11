import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

# 조건 필터링과 정렬
df = pd.read_csv(F_SHOT)
print(df.shape)

# 배열에서 하던 것
arr = df["비스킷두께"].values
print("배열에서 조건 참 개수:", int((arr >= 16).sum()))

# 표에서 하는 것
print("표에서 조건 참 개수:", int((df["비스킷두께"] >= 16).sum()))

# 조건 -> boolean Series
#s = df["비스킷두께"] >= 16
#print(s.head(3).tolist())

#print(int((df["비스킷두께"] <16).sum()))
#print(int(df["비스킷두께"].isna().sum()))

# 복합 조건
#both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
#either = df[(df["비스킷두께"] >= 16 | (df["사이클타임"] >= 25))]
#print(len(both), len(either))

# 부정 조건 : ~
#print(len(df[~(df["품질등급"] == "불량")]))

# isin : 값이 포함되어 있는지
#print(len(df[df["품질등급"].isin(['주의', '불량'])]))             # 또는(|)을 사용하는것과 결과가 같다

# between : 사이를 의미(양쪽 경계 모두 포함)
#print(len(df[df["비스킷두께"].between(10, 16)]))

# 문자열 조건
# - 숫자 열에는 쓸 수가 없다
# - str.contains : 해당 문자열을 포함하는 값
#print(len(df[df["설비ID"].str.contains("A")]))                   # A라인 전체를 의미한다

# - str.split, str.replace, str.strip .. 
#print(df["설비ID"].head(1).tolist())
#print(df["설비ID"].str.split("-").head(1).tolist())

# 정렬, 복사본
# 정렬 - sort_values
# - 기본값은 작은 값부터인 오름차순
# - 한 열로 정렬해도 모든 열이 행 단위로 함께 이동한다
asc = df.sort_values("비스킷두께")
print(asc["비스킷두께"].head(3).tolist())

# 다중 키 정렬, 내림 차순
dec = df.sort_values("사이클타임", ascending = False)
print(dec["사이클타임"].head(3).tolist())

# 다중 키 정렬
two = df.sort_values(["품질등급", "비스킷두께"], ascending = [True, False])
print(two["샷"].head(3).tolist())

# copy
x = df[df["품질등급"] == "불량"].copy()
print(x.shape)
x["위험등급"] = "높음"
print(x.shape)
