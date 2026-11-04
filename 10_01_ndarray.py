import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 반복문을 돌아야 한다
#list = [70, 72, 71]
#print(list *2)                           # [70, 72, 71, 70, 72, 71]
#print([v * 2 for v in list])             # [140, 144, 142]

# 2)배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르다

#temp = np.array([70, 72, 71])
#print(temp)                              # [70 72 71]

#print(temp + 2)                          # [72 74 73]

# 튜플로 배열 만들기
#print(np.array((1,2,3)))                 # [1 2 3]

#import numpy as np
#celsius = np.array([0, 10, 20, 25, 30, 35])
#print("섭씨:", celsius)
#fahrenheit = celsius * 1.8 + 32
#print("화씨:", fahrenheit)

# 배열 생성
# np.arange(시작, 끝, 간격) : 연속 정수
# - 끝 값은 포함되지 않음
#print(np.arange(5))                       # [0 1 2 3 4]
#print(np.arange(0, 10, 2))                # [0 2 4 6 8]

# np.linspace(시작, 끝 , 개수) : 균등 분할
# - 끝값 포함
#print(np.linspace(0, 1, 5))               # [0.   0.25 0.5  0.75 1.  ] 
#print(np.linspace(0, 10, 5))              # [ 0.   2.5  5.   7.5 10. ]

#import numpy as np
#start = 0
#stop = 70
#current = np.linspace(start, stop , 8)
#print("전류:", current)
#print("간격:", np.diff(current))
#print("70 포함 여부:", 70 in current)

#import numpy as np
#start = 0
#stop = 40
#step = 5
#index = np.arange(start, stop, step)
#print("순번:", index)
#print("40 포함 여부:", 40 in index)

# 배열 속성
# - ndim, shape, size, dtype
# - 속서은 괄호를 붙이지 않고 사용하면 된다

#a = np.array([1, 2, 3])
#b = np.array([[1,2,3], [4,5,6]])

#print("dim:",a.ndim, b.ndim)           # dim: 1 2
#print("shape:",a.shape, b.shape)       # shape: (3,) (2, 3)
#print("size:",a.size, b.size)          # size: 3 6

#import numpy as np
#sensor = np.array([[20,10], [22,20], [25,30], [27,40]])
#print("차원:", sensor.ndim)
#print("형태:", sensor.shape)
#print("개수:", sensor.size)
#rows, cols = sensor.shape
#print("줄x칸 == 개수:", rows * cols == sensor.size)

#import numpy as np
#current = np.array([12.3, 18.69, 25.5, 30.99])
#print("자료형:", current.dtype)
##current_int = current.astype(int)
#print("원본:", current)
#print("정수:", current_int)

# reshape() 로 형태 바꾸기
#c = np.arange(12)
#print(c.reshape(3,4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# flatten() -> 1차원을 만든다
#b3 = np.array([[1, 2, 3], [4, 5, 6]])
#print(b3.flatten())                   #[1 2 3 4 5 6]

#import numpy as np
#cycle = np.array([5.2, 5.1, 5.4, 5.3, 5.0, 5.2,
#                  5.5, 5.3, 5.1, 5.2, 5.4, 5.3])
#rows, cols = 3, 4
#table = cycle.reshape(rows, cols)
#print("원본 개수:", cycle.size)
#print(table)
#print("변환 후 개수:", table.size)
#print("개수 동일:", cycle.size == table.size)

import numpy as np
flat = np.array([20.5, 10, 1200, 22.0,
                  20, 1500, 25.3, 30, 
                  1800, 27.8, 40, 2100])
table = flat.reshape(4, 3)
print(table)
restored = table.flatten()
print(restored)
print("처음과 동일:", np.array_equal(flat, restored))