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

import numpy as np
temp = np.genfromtxt("data/11_hydraulic_cooler.csv", delimiter=",", skip_header=1, usecols=1)
q1, q3 = np.nanpercentile(temp, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print(f'Q1={q1:.2f} Q3={q3:.2f} IQR={iqr:.2f}')
print("상한:", round(upper, 1))
outliers = temp[temp > upper]
print("걸리는 값:", outliers)
print("개수:", outliers.size)
