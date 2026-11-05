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
