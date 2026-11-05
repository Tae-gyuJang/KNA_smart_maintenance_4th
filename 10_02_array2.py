#import numpy as np

# 인덱싱, 슬라이싱
#a = np.array([0, 1, 2, 3, 4])
#print(a[0], a[-1])                # 0 4
#print(a[1:4])                     # [1 2 3]
#print(a[::2])                     # [0 2 4]

#import numpy as np
#data = np.loadtxt("data/10_mct_tool.csv", delimiter=",", skiprows=1)
#rpm = data[:, 4]
#print("맨 앞:", rpm[0])
#print("맨 뒤:", rpm[-1])
#print("2~4번째:", rpm[1:4])
#print("하나 걸려:", rpm[::2])

#import numpy as np
#data = np.loadtxt("data/10_mct_tool.csv", delimiter="," ,skiprows=1)
#table = data[:4, [4,3]]
#print(table)
#print("세 번째 시점:", table[2])
#print("회전수 열:", table[:,0])
#print("토크 열:", table[:, 1])

# 배열 연산
#import numpy as np
#a = np.array([1,2,3])
#b = np.array([10,20,30])
#print(a + b)                      # [11 22 33]
# 같은 위치 값 끼리 계산 (반복문 필요X)
# 사칙연산 모두 같은 방식으로 계산

# 스칼라 연산
# - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# - 연산 숫자는 수학과 같아 곱하기 먼저
#print(a * 10 + 3)                           # [13 23 33]

# 보로드캐스팅
#table = np.array([[72, 2.4], [95, 6.8]])    
#print(table.shape)                          # (2, 2)
#base = np.array([70, 2.0])
#print(table - base)                         # [[ 2.   0.4] [25.   4.8]]
# 한 줄 짜리 기준값이 모든 행에 퍼져서 계산됨

#import numpy as np
#data = np.loadtxt("data/10_mct_tool.csv", delimiter = "," ,skiprows = 1)
#rpm = data[:10, 4]
#print("원본:", rpm)
#rpm_min = rpm.min()
#rpm_max = rpm.max()
#print("최소:", rpm_min, "최대:", rpm_max)
#shifted = rpm - rpm_min
#norm = shifted / (rpm_max - rpm_min)
#norm = np.round(norm, 2)
#print("정규화:", norm)
#print("0 개수:", np.sum(norm == 0), "1 개수:", np.sum(norm == 1))

# 비교 연산과 불리언 배열
#import numpy as np 
#vals = np.array([70, 95, 71, 88, 73])
#print(vals > 75)                           # [False  True False  True False]

# 불리언 인덱싱
# - 조건이 참/거짓인 배열을 만듦 -> 그 배열을 대괄호에 넣으면 참인 값만 남는다
#print(vals[vals > 75])                     # [95 88]

# np.where(조건, 참일 때 값, 거짓일 때 값)
#print(np.where(vals > 85, 1, 0))           # [0 1 0 1 0]

# 다중 조건
#print(vals[(vals > 70) & vals < 90])       # [70 95 71 88 73]

# 통계
# - 정상을 알아야 이상을 알 수 있다
# ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# - 평균, 최대/최소, 표준편차, 분산
# - NumPy 에서 함수 하나로 계산해준다

#import numpy as np
#s = np.array([70, 72, 71, 95, 73])
#print("합계:", s.sum())
#print("평균:", s.mean())
#print("중앙값:", np.median(s))
#print("최대:", s.max())
#print("최소:", s.min())

# 분산
#stable = np.array([70, 71, 70, 72, 71])
#unstable = np.array([60, 85, 65, 95, 70])
#print(round(stable.var(),1))                # 0.6
#print(round(unstable.var(),1))              # 170.0

# 표준편차
#print(round(stable.std(), 2))               # 0.75
#print(round(unstable.std(), 2))             # 13.04

# axis 개념 (행/열 방향)
#mat = np.array([70, 2.1], [72, 2.3])
#print(mat.mean(axis=0))                     # 열별 평균 (센서별)
#print(mat.mean(axis=1))                     # 행별 평균 (시점별)-> 지금은 큰 의미가 없다
#print(mat.mean())                           # 전체 평균 


#import numpy as np
#data = np.loadtxt("data/10_mct_tool.csv", delimiter="," ,skiprows=1)

#torque = data[:10, 3]
#print("토크:", torque)
#over = torque > 10
#print("참거짓:", over)
#count = np.sum(over)
#ratio = np.mean(over)
#print("개수:", count)
#print("비율:", ratio)

#import numpy as np
#data = np.loadtxt("data/10_mct_tool.csv", delimiter=",", skiprows=1)
#table = data[:,[4, 3]]
#print(table.shape)
#mean = table.mean(axis=0)
#std = table.std(axis=0)
#print("평균:", np.round(mean, 1))
#print("표준편차:", np.round(std, 1))

#import numpy as np
#rpm = np.array([4603, 4603, 58, 4603, 4603, 1216, 4603, 4603, 1217, 4603])
# 전류 데이터
#current = np.array([2, 2, 21, 2, 3,
#                    2, 2, 3, 2, 147])
#low_rpm = rpm < 2000
# 회전수 2000미만
#data = np.array([[4603, 2], [4603, 21]])
# 회전수 2000미만 또는 전류 25초과
#print(rpm[low_rpm])
#print(rpm[low_rpm], current[current > 25])
# 계수
#print(np.sum(low_rpm))
#print(np.sum((low_rpm) | (current > 25)))

# 비율 
#print(np.mean(low_rpm) * 100, "%")
# - low_rpm : True False 배열 -> True: 1 , False: 0
#print(np.mean((rpm < 200) | (current >25))* 100,"%")

# 파일에서 배열로 불러오기(np.loadtxt)

#import numpy as np
#rpm = np.loadtxt("data/10_mct_tool.csv",     
#                 delimiter= ",",             # 값을 나누는 기호
#                 skiprows=1 ,                # 첫 줄 (제목)은 건너뜀
#                 usecols=4)                  
#print(rpm)

#rpm_tq = np.loadtxt("data/10_mct_tool.csv",
#                    delimiter=",",
#                    skiprows=1,
#                    usecols=4)
#print(rpm_tq)

#import numpy as np
#rpm = np.loadtxt("data/10_mct_tool.csv",
#                 delimiter="," ,
#                 skiprows=1 ,
#                 usecols=4)
#mean = rpm.mean()
#std = rpm.std()
#rmin = rpm.min()
#rmax = rpm.max()
#print("평균:", round(mean, 1))
#print("표준편차:", round(std, 1))
#print("최소:", rmin)
#print("최대:", rmax)

#import numpy as np
#torque = np.loadtxt("data/10_mct_tool.csv",
#                    delimiter="," ,
#                    skiprows=1 ,
#                    usecols=5)
#selected = torque[torque > 10]
#print("골라낸 값:", selected)
#print("개수:", selected.size)
#print("선택 평균:", selected.mean())
#print("전체 평균:", torque.mean())
#print("차이:", selected.mean() - torque.mean())

import numpy as np
data = np.loadtxt("data/10_mct_tool.csv",
                  delimiter="," ,
                  skiprows=1 ,
                  usecols=(4, 5))
print("형태:", data.shape)
print("자료형:", data.dtype)
rpm = data[:, 0]
low = rpm[rpm < 2000]
print("이상 시점 값:", low)
print("이상 시점 개수:", low.size)
print("이상 평균:", round(low.mean() , 1))
print("전체 평균:", round(rpm.mean() , 1))