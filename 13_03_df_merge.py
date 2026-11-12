import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

#print(log.shape)
#print(master.shape)

#three = log.head(3)[["샷", "설비ID", "비스킷두께"]]
#print(three.to_string(index=False))

#print(three.merge(master, on="설비ID").to_string(index=False))

# merge 기본사용법
# - on : 두 표를 잇는 키 열
# - 행은 예측불가, 열 수는 예측 가능

# - how: 어느 쪽을 다 남길 것인가
#   - (기본) how='inner'
#   - how = 'left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
#   - how = 'outer' : 양쪽을 다 남긴다

#m_inner = log.merge(master, on="설비ID")
#m_left = log.merge(master, on="설비ID", how="left")
#m_outer = log.merge(master, on="설비ID", how="outer")

#print(m_inner.shape, m_left.shape, m_outer.shape)              

# 합치기 전후 점검 코드

#print(len(log))
#print(len(master), master["설비ID"].nunique())

#m_left = log.merge(master, on="설비ID", how="left")
#print(len(m_left))
#print(int(m_left["라인"].isna().sum()))

#unmatched = m_left[m_left["라인"].isna()]
#print(unmatched["설비ID"].head(1).tolist(), len(unmatched))

# merge 는 옆으로 칸을 이어 붙이고, concat은 아래로 줄을 쌓는다
# concat은 키 열이 필요 없고, 칸 이름만 맞으면 된다

# pd.concat

# ex) 설비 로그를 1차, 2차로 나눠 받은 경우
part1 = log.iloc[:100].reset_index(drop=True)
part2 = log.iloc[100:].reset_index(drop=True)
print(part1.shape, part2.shape)

stacked = pd.concat([part1, part2])
print(stacked.shape)
print(stacked.index[-3:].tolist())
print(len(stacked.loc[[0]]))

# - 번호를 다시 매기기 -> ignore_index
renumbered = pd.concat([part1, part2], ignore_index=True)
print(int(renumbered.index[-1]))

# - 칸이(열이) 다른 표를 붙이면 -> 빈 칸이 생긴다
#   붙이기 전에 두 표의 columns 비교
#   -> set(표1.columns) - set(표2.columns)
