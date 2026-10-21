#  자료형

count = 3     # int 정수
temp = 25.5   # flot 실수
name = "센서A" # str 문자열

ok = True     # bool 불린형 - 참/거짓
no = False    

# type()  ->  자료형을 알려줌
print(type(25))        # <class 'int'>
print(type("센서A"))   # <class 'str'>
print(type(ok))        # <class 'bool'>

# 자료형마다 다른 동작
print(3 + 5)          # 8 (숫자 더하기 = 계산)
print("3" + "5")      # 35 (글자 더하기 = 이어 붙이기)

# 실습 1
count = 3
temp = 25.5
name = "센서A"
ok = True
no = False
print(3)
print(25.5)
print("센서A")
print(ok)
print(no)

print(type(3))
print(type(25))
print(type("센서A"))
print(type(ok))

print(type(100))   # <class 'int'>
print(type(100.0)) # <class 'float'>
print(type("100")) # <class 'str'>

print(3 + 5)
print("3" + "5")
print("35" + "46")

# 3>2 True
print(3>2)
print(5==5)
print(type(3>2))

count= 3
print(type(3)) # print(type(count))
temp= 3.0
print(type(3.0)) # print(type(temp))
name= "3"         
print(type("3")) # print(type(name))

device_temp= 25.5
check_count= 3
device_name= "센서A"
is_normal= True
print(type(device_temp))
print(type(check_count))
print(type(device_name))
print(type(is_normal))