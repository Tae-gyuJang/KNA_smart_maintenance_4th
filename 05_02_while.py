# while - 조건이 참인 동안 반복을 해준다
# 형식 : 
# while 조건식 :  (조건이 거짓이 되는 순간 멈춤)
# for - '몇 번' 이 정해졌을 때, while은 '언제 끝날지 모르지만 조건으로 멈출 때' 사용하면 된다

#count = 1
#while count <= 3:
#    print(count)
#    count += 1                       # 1 2 3
# 주의) 무한루프를 막으려면 (1)언젠가 거짓이 될 조건, (2)반복문 안에서 조건을 갱신
# 처음부터 조건이 거짓이면 한 번도 실행되지 않는다.


#target = 7
#guess = 0

#while guess != target:
#    guess = int(input("숫자를 입력하세요: "))
#print("정답입니다! 반복 종료")

# break - 반복 도중에 완전히 멈추기
#for i in range(1,11):
   #if i == 5:
   #   print(i, "break")
   #   break             # 5를 만나면 반복 즉시 종료
   # print(i)            # 1 2 3 4 5break

#for i in range(1, 7):
#   if i % 2 == 0:
#      continue
#   print(i)               # 1 3 5

#found = False
#count_n = int(input("측정 횟수: "))

#for i in range(count_n):
#    value = int(input(f'{i + 1}번째 측정값: '))
#    if value > 80:
#        found = True
#        break
#if found:
#    print("발견")
#else:
#    print("없음")


