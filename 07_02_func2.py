# 매개변수와 반환값

# 매개변수와 인자를 구분
# 형식:
# def 함수이름(매개변수):
# ....
# 호출
# 함수이름(인자)

#def check(name):                        #name = 매개변수
#    print(name + "점검을 시작합니다.")

#check("압축기1")                        # "압축기1" = 인자
#check("펌프1")
#check()   # TypeError: check() missing 1 required positional argument: 'name' 에러뜬다
#check("A", "B") #TypeError: check() takes 1 positional argument but 2 were given

#def report(name, temp):
#    print(name, temp, "도")

#report("모터", 78)
#report("펌프", 92)

#def show(name, value):
#    print(name, value)

#show(name="모터", value=78)
#show(value=78, name="모터")
#show("펌프", value=92)

# return
# - print: 사람이 확인할 수 있게 출력 / return : 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
#def add (a,b):
#    return a+b
#    print("실행 안됨")                # return을 만나면 즉시 함수 종료 -> 그 아래 코드는 실행 X

#total = add(3,4)
#print(total)

#def calc_avg(a, b):
#    return(a + b) / 2
#avg = calc_avg(80, 90)
#print(avg)
#print(avg +5)

# 여러 값 변환 / 언패킹
# - 쉼표로 여러 값을 return 하면 튜플로 묶여서 돌아옴 -> 언패킹 가능
#def min_max(values):
#    return min(values), max(values)

#print(min_max([75, 10, 100]))    # (10,100)
#low, high = min_max([75, 10, 100])
#print(low, high)

#def report(name, temp):
#     print(name, temp, "도")
#none = report("펌프", 10)
#print(none)

#def sensor_stats(values):
#    return min(values), max(values), sum(values) /len(values)

#data = [78, 85, 92]
#low, high, avg = sensor_stats(data)
#print(low, high, avg)
