# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]    (첫 글자 = 0번)

#word = 'PYTHON'
#print(word[0], word[2], word[5])  # P T N
# 음수 인덱스: 뒤에서부터 -1, -2,...
#print(word[-1], word[-2])         # N O

# print(word[6])        # IndexError: string index out of range

#word ='SIGNAL'
#print(word[0], word[2], word[5])

#word ='SIGNAL'
#print(word[-1], word[-2])

# 슬라이싱  - 구간으로 잘라내기
# 형식: 문자열[시작:끝]   (시작은 포함 끝 제외)
#word = 'PYTHON'
#print(word[1:4])
# 생략 가능
# - 시작을 생략하면 처음부터 (0번부터)
# - 끝을 생략하면 끝까지
# - 둘 다 생략하면 전체
#print(word[:3])    # PYT
#print(word[3:])    # HON
#print(word[:])     # PYTHON
#print(word[-3:])   # HON
#print(word[:-1])   # PYTHO

#word = 'SIGNAL'
#print(word[:3])
#print(word[2:5])

#word = 'temp_sensor'
#print(word[:4])

#word = 'temp_sensor'
#print(word[5:])

#word = 'sensor_01'
#print(word[-2:])

# step 간격 주기
# 형식 : 문자열[시작:끝:간격]
#word = 'PYTHON'
#print(word[::2])      # PTO
#print(word[1::3])     # YO

#word = 'SIGNAL'
#print(word[::2])       # SGA

#print(word[::-1])      # LANGIS



