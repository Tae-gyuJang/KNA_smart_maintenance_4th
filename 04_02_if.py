# 조건문
# if 기본 구조 - 콜론과 들여쓰기(코드 블록)
# 형식:
# if 조건식:
#   실행할 코드 (들여쓰기를 해야된다 한칸 뒤에~)

#temp = 85
#if temp > 80:                           # 콜론 : 콜론 시작 신호
#    print("온도 주의")                  # 들여쓰기 한 부분 -> 조건 참일 때만 실행 
#    print("점검 요망")                
#print("측정 종료")                      # 들여쓰기가 끝난부분 -> 조건과 무관하게 항상 실행

# else - 조건이 거짓일 때 사용
# 형식:
# if 조건문:
#    참일 때 코드
# else:
#    거짓일 때 코드

#score = 55
#if score >= 60:
#    print("합격")
#else:
#    print("불합격")

#age = int(input("나이를 입력하세요: "))
#if age >= 19:                               #나이를 입력하세요: 19 성인입니다
#     print("성인입니다")
#else:
#     print("미성년자입니다")  

# elif
# 형식:
# if ... elif ... else (위에서부터 검사, 처음 참인 곳만 실행)

#score = 82
#if score >= 90:
#    print("우수")
#elif score >= 70:
#    print("보통")
#else:
#    print("미흡")

#score = int(input("점수를 입력하세요:"))
#if score >= 90:
#    print("A")
#elif score >= 80:
#    print("B")
#elif score >= 70:
#    print("C")
#else:
#    print("F")

# 논리 연산자 and or not / 범위 조건
#temp = 45
#print(temp >= 20 and temp <= 60) #True

#if 20 <= temp <= 60:
#    print("정상 범위")

#temp = int(input("측정 온도를 입력하세요: "))
#if temp > 80:
#    print("위험")
#elif temp > 60:
#    print("주의")
#else:
#    print("정상")

#id = "admin"
#pw = "1234"

#user_id = input("아이디: ")
#user_pw = input("비밀번호: ")
#if user_id == id and user_pw == pw:
#    print(" 로그인 성공 ")
#else:
#    print(" 로그인 실패 ")

temp = int(input("온도: "))
vib = float(input("진동: "))
cur = int(input("전류: "))

if temp > 80 or vib > 4.0:
    print("위험: 즉시정지")
else:
    if cur > 60 and temp >70:
        print("주의: 부하 점검")
    elif vib > 2.5:
        print("주의: 진동 관찰")
    else:
        print("정상")
             