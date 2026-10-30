# 함수 설계와 활용

# 기본값 인자는 인자 생략시 기본값을 사용한다
# 형식:
# def 함수(매개변수는 필수값, 선택은 기본값):

# 거의 항상 같은 값을 매번 적는 번거러움을 줄임, 필요할 때만 덮어쓴다
#def report(name, value, unit ="도"):
#    print(f'{name}: {value} {unit}')

#report("압축기1", 75.3)             # 압축기1: 75.3 도
#report("펌프1", 7.2, "bar")         # 펌프1: 7.2bar

#def check(value, limit = 90):
#    if value > limit:
#        return "경고"
#    return "정상"

#print(78, "→", check(78))
#print(95, "→", check(95))
#print(50, "→", check(50, 40))

# 지역변수와 범위(스코프)
# - 함수 안의 변수, 함수 바깥 변수를 읽을 수 있지만, 바깥에서는 한수 안 지역변수를 읽을 수 X
#def calc():
#    result = 10 + 5                  # 지역변수
#    return result                    # 밖에서 사용하려면 return으로 내보내야된다

#print(calc())

#x = 10
#def change():
#    x = 20                           # 함수 내부의 지역변수

#change()
#print(x)                             # 10 (함수 바깥의 x값 변경x)

# 실습 2
# 함수 선언
# 지역변수 생성
# 함수 밖에서 해당 지역변수 호출, 결과 확인

#def calc():
#    result = 30
#    print(result)

#calc()
#print(result)

# 함수 조합 (함수 설계: 입력/처리/출력)
def get_avg(values):
    return sum(values) /len(values)

def judge(avg, limit=85):
    if avg > limit:
        return "위험"
    else:
        return "정상"

temps = [76, 88, 91]
avg = get_avg(temps)
print(round(avg, 1), judge(avg))
