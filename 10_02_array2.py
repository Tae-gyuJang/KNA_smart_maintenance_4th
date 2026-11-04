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

import numpy as np
data = np.loadtxt("data/10_mct_tool.csv", delimiter="," ,skiprows=1)
table = data[:4, [4,3]]
print(table)
print("세 번째 시점:", table[2])
print("회전수 열:", table[:,0])
print("토크 열:", table[:, 1])