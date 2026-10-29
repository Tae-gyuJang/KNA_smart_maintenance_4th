# 함수
# 함수의 기본 구조
# 형식:
# def 함수이름():
#    실행할 코드

#def greet():
#    print("점검을 시작합니다")
# 이렇게 하면 안된다
# 정의만으로는 실행 안됨 -> 호출해야 실행이 된다
# 호출: 함수 이름 적고 괄호를 붙이기
#greet()           # 점검을 시작합니다

#def greet():
#    print("점검을 시작합니다")
#greet()
#greet()

#def start_check():
#    print("점검을 시작합니다")
#    print("안전 장비를 확인하세요")
#    print("기록을 준비하세요")
#start_check()
#start_check()

# 실습 3
#def hello():
#    print("안녕하세요")   #이렇게만 하면 정의하는거라 NameError가 난다
#hello()
#hello()                  # 함수는 호출한 만큼만 ~ 2번이니까 안녕하세요 안녕하세요

# 실습 4
def line():
    print("=" * 10)

def check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")

line()
check()

line()
check()