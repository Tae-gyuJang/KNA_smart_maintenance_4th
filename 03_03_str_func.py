# 문자열 연산과 검색
# - 문자열 연결하려면  (+), 반복하려면(*)

# len() - 글자 수를 알 수 있게 해준다
# 형식: len(문자열)
#print(len('PYTHON'))            #6 글자수
#print(len('AI 분석'))           #5 글자수 (공백도 글자수에 포함 AI 분석 사이 )
#print(len(''))                  #0 (빈 문자열)

# in / not in -  포함 / 불포함 여부 (결과 boool)
# 형식:  '찾을 것' 을 앞에 적고 in 문자열
#print('고장' in ' 설비 고장 발생')      #True
#print('정상' not in '고장 발생')        #True

# count
# 형식: 문자열에 .을 찍고 count('X') -> 값은 갯수가 나올 것
#print('banana' .count('a'))             # 3 ( a 가 banana 안에 3개가 있다)

# find
# 형식: 문자열. find('x') -> 처음 나오는 위치
#print('banana' .find('a'))              # 1 (0이 첫번째 b 1은 두번째 a)
#print('banana' .find('t'))              # -1 (못 찾을 경우) 

#phone = '01012345678'
#print(len(phone))

#msg = "설비 고장 발생"
#print('고장' in msg)
#print('정상' in msg)

#text = 'sensor-o1-temp'
#print(text.count('-'))

#text = 'temp_2024'
#print(text .find('_'))
#print(text .find('7'))

# index
# 주의할 점은 위치를 반환하지만 없으면 오류가 난다
#email = 'hong@company.com'
#at = email.index('@')
#print(at)                 # 4 ( 0 1 2 3 4 5번째인 4)
#print(email[:at])         #hong

# startswith /endswith
# 형식: 문자열.startswith('x') 반환값은 bool로 나올것이다
#print('EQP-001'.startswith('EQP'))     #True
#print('cmapss.csv'.endswith('csv'))    #True

text = "sensor_log.csv"
print(text.startswith('sensor'))
print(text.endswith('.csv'))

status = "WARNING"
print(status=="WARNING")
print(status=="warning")