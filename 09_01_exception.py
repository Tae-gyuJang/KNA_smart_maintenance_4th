# 각 종 예외 상황       
#temp = int("스물")   # ValueError: invalid literal for int() with base 10: '스물'
#result = 10 / 0      # ZeroDivisionError: division by zero
#print(undefined_var) # NameError: name 'undefined_var' is not defined


# try-except 구조 (위에 에러난 부분들 에러 안나게~)
#try:
#  temp = int("스물")
#except ValueError:
#  print("ValueError")

#try:
#  result = 10 / 0
#except ZeroDivisionError:
#  print("ZeroDivisionError")

#try:  
#  print(undefined_var)
#except NameError:
#  print("NameError")

#text = input("온도를 입력하세요: ")
#try:
#    temp =float(text)
#    print(f'현재온도: {temp}도')
#except ValueError:
#    print("숫자를 입력해 주세요.")
#print("프로그램은 계속 진행됩니다.")

# 여러 except
#row = "P-01,102".split(",")
#try:
#    code_no= int(row[3])
#except ValueError:
#    print("숫자 아님")
#except IndexError:
#    print("칸 부족")

text = input("측정값을 입력하세요:")
try:
    value = float(text)
    result = 100 / value
    print(f'100 / {value} = {result}')
except ValueError:
    print("숫자가 아닙니다. 숫자를 입력해 주세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다. 0이 아닌 값을 입력해 주세요.")

print("프로그램은 계속 진행됩니다.")