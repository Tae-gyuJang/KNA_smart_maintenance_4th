# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형식 : +, - , *, /, // (몫), %(나머지), **(거듭제곱)

# 우선순위
# - 곱셈, 나누셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식: score += 10 <-> score = score + 10
score = 100
score += 10
print(score)
# -=, *= , /=

# 문자열 연산
# +, * 가능
print("안녕" + "하세요")   # 안녕하세요 -> 이어붙이기
print("-" * 4)          # ---- -> 반복
# 주의) 자료형이 같은 것 끼리 연산 할 수 있다

a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 81
b = 93
c = 87
print(( a + b + c)/3)
side = 7
print(side ** 2)
print(3 * 4 * 5)

# 비교 연산자
# 형식: == (같다) != (다르다) < > <= >=
print(5 == 5) # True
print("정상" == "정상") #True
print("A" == "a") #False

# 논리 연산자
# - and: 모두 참이어야 함, or: 하나만 참이어도 참 , not: 반대
print(True and False)   # False
print(True or False)    # 
print()

