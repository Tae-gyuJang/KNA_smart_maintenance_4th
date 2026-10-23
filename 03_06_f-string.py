# f-string - 문자열 안에 변수열 바로 끼울 수 있는 기능
# 형식: f"~~~ {변수}~~~~"

#name = "홍길동"
#age = 25
#print(f'{name}님은 {age}살입니다')     #홍길동님은 25살입니다
# 숫자도 str 변환 없이 바로 들어감
#print(f'온도: {25.5}')                 #온도: 25.5
# 중괄호 안에 계산식 가능하다
#hours = 3
#print(f'{hours *60}분')                # 180분

# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 둘째 자리까지 (자동 반올림되서 값이 나올 것)
#value = 25.34567
#print(f'측정값: {value:.2f}')           # 측정값: 25.35
#print(f'측정값: {value:.1f}')           # 측정값: 25.3

#name = "PUMP_A"
#temperature = "87도"
#print(f'설비 {name},온도 {temperature}')

#score = 90
#score1 = 87
#score2 = 84
#print(f"평균 {(score + score1 + score2)/3}"")

#value = 87.456
#print(f"value: {value:.1f}")
#print(f"value: {value:.2f}")

raw = '  5 , sensor_2 , WARNING , 0.78912  '

number , sensor, status, value = raw.strip().split(' , ')
print(f"[센서{sensor}] 상태{status.lower()}, 측정값{float(value):.2f}")

#이 문제는 알아야 된다. strip은 공백제거 split은 구분

raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(',')
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
      