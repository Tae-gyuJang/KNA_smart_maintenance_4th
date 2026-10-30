# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
# - 라이브러리: 위에 사항들을 통칭하는용어이다

# import 방식
# 형식 : import 모듈/ from 모듈 import 가능/
#import math                               # math 라는 모듈을 통째로 불러옴
#print(math.sqrt(16))                      # 4.0
#from math import sqrt, ceil               # 일부만 불러옴 -> 모듈명 없이 바로 사용 가능하다
#print(sqrt(16), ceil(4.2))
#import math as m
#print(m.sqrt(16))

#import math
#print(math.sqrt(16), math.ceil(4.2))
#from math import sqrt, ceil
#print(sqrt(16), ceil(4.2))
#import math as m
#print(m.sqrt(16), m.ceil(4.2))

# 표준 라이브러리 - math / random / datetime
# - 파이썬 설치 시 함께 깔리는 검증된 모듈들
#import random
#import datetime

#print(random.randint(1, 100))
#print(datetime.datetime.now())

#import random
#import math

#sensor = random.randint(1, 100)
#print("센서값:", sensor)
#root = math.sqrt(sensor)
#print("제곱근:", round(root, 2))

# //////////////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로
#   - 최상위부터 전체 주소를 의미한다
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소

#import os 
#print("현재 실행 위치(절대경로):", os.getcwd())  #현재 실행 위치(절대경로): C:\Users\user\Desktop\261019_python

# 폴더 유무 확인
#print(os.path.exists("data"))                   #True

# 폴더 목록 확인
#files = os.listdir("data")
#print(files)                                    # ['08_press_13_261029_3.csv']

# 폴더명 + 파일명 -> 경로
#path = os.path.join("data", "08_press.csv")

#import os
#folder = "data"
#print("현재 경로:", os.getcwd())
#files = os.listdir(folder)
#print("폴더 안 파일들")
#for name in files:
#    print(name)
#print(".csv 파일만")
#for name in files:
#    if name.endswith(".csv"):
#        print(name)

#import os
#path = os.path.join("data", "08_press_13_261029_3.csv")
#print("경로:", path)
#found= os.path.exists(path)
#print(found)
#if found:
#    print("파일 있음")
#else:
#    print("파일 없음")

#import os
#from datetime import datetime
#count = len(os.listdir("data"))
#now = datetime.now()
#print(f'파일 {count}개, 점검시작 {now}')

import os
folder = "data"
files = os.listdir(folder)
csv_files = []
for name in files:
    if name.endswith(".csv"):
        csv_files.append(name)

csv_paths = []
for name in csv_files:
    csv_paths.append(os.path.join(folder, name))

print("[csv]", csv_files)
