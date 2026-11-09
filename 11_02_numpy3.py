#import numpy as np

#F = 'data/11_hydraulic_cooler.csv'

#def col(c):
#    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# isnan - 결측값 위치 찾기
# - 결측값: 값이 빈 칸 -> 0이 아니라 값을 모름

#x = np.array([2.0, np.nan, 4.0])
#print(np.isnan(x))               # [False  True False] 
#print(np.isnan(x).sum())         # 1  (True 값이 한개라서 1)

# nanmean, nanstd - 결측값을 무시한 통계
#temp = np.array([70.1, np.nan, 71.2, 70.8])
#print(np.mean(temp))                # nan
#print(round(np.nanmean(temp), 2))   # 70.7

# nanmean, nanmax, nanmin

#import numpy as np
#vib = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=2)
#n_nan = np.isnan(vib).sum()
#ratio = n_nan / vib.size
#mean_ignore = np.nanmean(vib)
#print("결측 개수:", n_nan)
#print("결측 비율:", ratio)
#print("결측 제외 평균:", round(mean_ignore, 3))
#print("일반 평균:", vib.mean())

# 백분위수, 사분위수 - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25 , 50, 75 백분위수 -> 1사분위, 중앙값, 3사분위
# - 평균과 달리 극단적인 이상값에 휘둘리지 않음

#vib_s = np.array([2.0, 2.2, 2.5, 2.8, 2.8, 3.0, 6.5])
#print(np.round(float(np.percentile(vib_s, 25)), 2))       # 2.35
#print(np.round(float(np.percentile(vib_s, 75)), 2))       # 2.9

# 여러 자리 한번에
#print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))    # [2.35 2.8  2.9 ]

# quantile : 25 -> 0.25
#print(np.round(float(np.quantile(vib_s, 0.25)), 2))       # 2.35

# 사분위 기반 이상치 범위 - IQR

#q1, q3 = np.percentile(vib_s, [25, 75])             
#iqr = q3 - q1
#upper = q3 + 1.5 * iqr
#print(vib_s[vib_s > upper])                               # [6.5]

# 평균 / 표준편차로 정규화 - z-score
# - 부호의 의미 : 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요

#z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
#print(vib_s[np.abs(z) > 2])                               # [6.5]

#import numpy as np
#temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
#q1, q3 = np.nanpercentile(temp, [25, 75])
#iqr = q3 - q1
#upper = q3 + 1.5 * iqr
#print("상한:", round(upper, 1))
#outliers = temp[temp > upper]
#print("걸리는 값:", outliers)
#print("개수:", outliers.size)

#import numpy as np
#path = "data/11_hydraulic_cooler.csv"
#cyc = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=0)
#temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
#mean = np.nanmean(temp)
#std = np.nanstd(temp)
#z = (temp -mean) / std
#mask = np.abs(z) > 2
#print("이상 사이클:", cyc[mask])
#print("개수:", mask.sum())
#print("최대 z-score:", round(np.nanmax(np.abs(z)), 2))

#import numpy as np
#path = "data/11_hydraulic_cooler.csv"
#cyc = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=0)
#temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
#mean = np.nanmean(temp)
#std = np.nanstd(temp)
#upper = mean + 3 * std
#alarm = cyc[temp > upper]
#print("상한:", round(upper, 2))
#print("경보 사이클:", alarm)
#print("개수:", alarm.size)

# 센서 간 상관관계 - correcoef
# - 세기는 절댓값이 정함. +0.99와 -0.99는 세기가 똑같고 방향만 반대
# - 양수: 한쪽이 오르면 다른 한쪽도 오름 / 음수는 반대
# - 0에 가까움 -> 관계가 없는 상태

#import numpy as np
#temp = np.array([70, 72, 74, 76, 78])
#vib = np. array([2.0, 2.2, 2.5, 2.7, 3.0])
#print(round(float(np.corrcoef(temp,vib)[0, 1]), 3))             # 0.998

# 표 (행렬)
#print(np.round(np.corrcoef(temp, vib), 3))
#[[1.    0.998]
# [0.998 1.   ]]
# 온도-온도 , 온도-진동, 진동-온도, 진동-진동 네 조합을 모두 계산해 줌

# 2D 배열 axis별 통계 활용
# 행은 센서, 열은 시점인 행렬 axis로 방향을 정해 통계
# axis = 1 - 각 행을 옆으로 > 센서별 통계
# axis = 0 - 각 열을 아래로 > 시점별 통계

#data = np.array([[70., 72., 74.]], [[2.0, 2.2, 2.5]])
#print(np.round(np.mean(data, axis = 1), 2))
#print(np.round(np.mean(data, axis = 0), 2))

#import numpy as np
#path = "data/11_hydraulic_cooler.csv"
#temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
#ce = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=3)
#ok = ~np.isnan(temp) & ~np.isnan(ce)
#corr = np.corrcoef(temp[ok], ce[ok])
#print(corr)
#r = corr[0, 1]
#print("상관계수:", round(r,2))

#import numpy as np
#path = "data/11_hydraulic_cooler.csv"
#temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
#vib = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=2)
#ce = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=3)
#co = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=4)
#M = np.stack([temp, vib, ce, co])
#print("M.shape:", M.shape)
#mean = np.nanmean(M, axis=1)
#std = np.nanstd(M, axis=1)
#print("평균:", np.round(mean, 1))
#print("표준편차:", np.round(std, 1))

# 변화점 탐지
# - 누적 합으로 찾는 원리
# - 각 값에서 전체 평균을 빼면 평균보다 작은 값은 음수 , 큰 값은 양수
# - 해당 값들을 앞에서부터 누적하면 평균보다 낮은 구간에서는 계속 내려가고,
#   평균보다 높은 구간에서는 계속 올라감
# - 그래서 누적 곡선이 가장 낮아지는 자리가 내려가기를 멈추고 올라가기 시작한 자리

#import numpy as np
#v = np.array([2.0, 2.1, 2.0, 5.0, 5.2, 5.1])
#cs = np.cumsum(v - np.mean(v))
#print(np.argmin(cs))

#import numpy as np
#import pandas as pd

#df = pd.read_csv("data/11_hydraulic_cooler.csv")
#cycle = df.iloc[:, 0].to_numpy()
#temp = df.iloc[:, 1].to_numpy(dtype=float)
#mean_temp = np.nanmean(temp)
#cs = np.cumsum(temp - mean_temp)
#k = np.argmin(cs)
#print("최소:", cycle[k])

import numpy as np
import pandas as pd

df = pd.read_csv("data/11_hydraulic_cooler.csv")
cycle = df.iloc[:, 0].to_numpy()                  
temp = df.iloc[:, 1].to_numpy(dtype=float) 
eff = df.iloc[:, 2].to_numpy(dtype=float)
state = df.iloc[:, 3].to_numpy()
z_t = np.abs((temp - np.nanmean(temp)) / np.nanstd(temp))
z_e = np.abs((eff - np.nanmean(eff)) / np.nanstd(eff))
score = z_t + z_e

top3 = np.argsort(score)[::-1][:3]
print("최고 :", cycle[top3[0]], f'번 ({score[top3[0]]:.2f})')
print("상위 세 시점:", cycle[top3])
bad = cycle[state != "정상"]
print("상태 라벨 이상 구간:", bad.min(), "~", bad.max())
print("상위 3개가 라벨 구간에 포함하는가?", np.isin(cycle[top3], bad).all())
