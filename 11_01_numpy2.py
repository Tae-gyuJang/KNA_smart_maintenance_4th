#import numpy as np

#F = 'data/11_diecasting_series.csv'

#ct = np.genfromtxt(F, delimiter="," , skip_header=1, usecols=1)
#print(ct.shape, ct.dtype)                               # (50,) float64

#def col(c):
#    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 자리 찾기
# fancy indexing

#vib = np.array([2.1, 2.3, 2.0, 5.8])                     
#pick = np.array([0, 3])
#print(vib[pick])                                         # [2.1 5.8]


# 정렬과 정렬 순서
# - sort, argsort : 원래 자리 번호 돌려줌

#print(np.sort(vib))                                      # [2.  2.1 2.3 5.8]
#print(np.argsort(vib))                                   # [2 0 1 3]

#import numpy as np
#shot = np.loadtxt("data/11_diecasting_series.csv", delimiter="," ,skiprows=1, usecols=0)
#ct = np.loadtxt("data/11_diecasting_series.csv", delimiter="," ,skiprows=1, usecols=1)
#i = np.argmax(ct)
#shot_number = shot[i]
#cycle_time = ct[i]
#print("인덱스:", i)
#print("샷 번호:", shot_number)
#print("사이클타임:", cycle_time, "초")
#print("최댓값과 일치:", cycle_time == ct.max())

# diff
#vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
#change = np.diff(vib)
#print(np.round(change,1))
#print(np.argmax(change))

#import numpy as np
#cyc = np.loadtxt("data/11_diecasting_series.csv", delimiter=",", skiprows=1, usecols=0)
#ct = np.loadtxt("data/11_diecasting_series.csv", delimiter=",", skiprows=1, usecols=1)
#diff = np.diff(ct)
#change = np.abs(diff)
#j = np.argmax(change)
#print("구간 위치 j:", j)
#print(f'{cyc[j]}번과 {cyc[j+1]}번 사이에서 {change[j]}초만큼 변함')

# clip - 보정
#import numpy as np
#pres = np.array([4.5, 9999.0, 4.6, -1.0])
#fixed = np.clip(pres, 0, 10)
#print(fixed)                              # [ 4.5 10.   4.6  0. ] 개수는 변하지 않는다

# cumsum - 누적 합
#defects = np.array([0, 1, 0, 2, 3, 5])
#print(np.cumsum(defects))

# np.where
#vib = np.array([2.1, 3.5, 2.0, 6.2])
#label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))          # 5 이상: 2, 3이상: 1, 나머지는 0
#print(label)

# unique - 중복된것을 정리
# -return_counts 옵션: 각 종류의 개수 확인
#status = np.array * ([0, 0, 1, 0, 2, 1, 0])
#kinds, counts = np.unique(status, return_counts=True)
#print(kinds)
#print(counts)

#import numpy as np
#cyl = np.loadtxt("data/11_diecasting_series.csv", delimiter="," ,skiprows=1 , usecols=2)
#print("원래 평균:", round(cyl.mean(), 1))
#cyl[0] = 9999
#print("보정 전 평균:", round(cyl.mean(), 1))
#fixed = np.clip(cyl, 100, 300)
#print("보정 후 평균:", round(fixed.mean(), 1))

#import numpy as np
#ct = np.loadtxt("data/11_diecasting_series.csv", delimiter="," ,skiprows=1 , usecols=1)
#state = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))
#count = np.bincount(state)
#print("개수(정상, 경고 , 잼):", count)
#ratio = count / ct.size
#print("비율:", ratio)
#print("경고 이상 비율:", (count[1] + count[2]) / ct.size)

# any, all - 조건 충족 여부 판정
# - any: 하나라도 만족하면 True
# - all: 모두 만족해야 True

#import numpy as np
#vib = np.array([2.1, 3.5 , 2.0, 7.2])
#print(np.any(vib > 5))
#print(np.all(vib < 10))

# concatenate, stack - 배열 합치기
#am = np.array([2.0, 2.1, 2.2])
#pm = np.array([2.3, 2.4, 2.5])
#print(np.concatenate([am, pm]))
#print(np.stack([am, pm]))

#import numpy as np
#path = "data/11_diecasting_series.csv"
#ct = np.loadtxt(path, delimiter=",", skiprows=1, usecols=1)
#cyl = np.loadtxt(path, delimiter=",",skiprows=1, usecols=2)
#cast = np.loadtxt(path, delimiter=",", skiprows=1, usecols=3)
#clamp = np.loadtxt(path, delimiter=",", skiprows=1, usecols=4)
#M = np.stack([ct, cyl, cast, clamp])
#print("전체:", M.shape)
#recent = M[:, -10:]
#print("최근 구간:", recent.shape)

import numpy as np
path = "data/11_diecasting_series.csv"
cyc = np.loadtxt(path, delimiter=",",skiprows=1, usecols=0)
ct = np.loadtxt(path, delimiter=",",skiprows=1, usecols=1)
cyl = np.loadtxt(path, delimiter=",",skiprows=1, usecols=2)

i = np.argmax(ct)
print(f'최대: {cyc[i]:.0f}번 {ct[i]}')
j = np.argmax(np.abs(np.diff(ct)))
print(f'급변: {cyc[j]:.0f}->{cyc[j+1]:.0f}')
warn = (ct >= 50) | (cyl < 150)
print("경고 비율:", np.mean(warn))
top3 = np.argsort(ct)[::-1][:3]
print("상위 세 시점:", cyc[top3])
