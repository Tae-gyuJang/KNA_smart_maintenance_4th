# 문자열
# - "", '' 감싸서 표현

# 여러줄 문자열
# 형식: 삼중 따옴표 """ 적을 내용 .. """
#notice = """
#설비 점검 안내
#1. 전원 확인
#2. 센서 점검
#"""
#print(notice)

# 이스케이프 : \n 줄바꿈, \t 탭
#print("이름\t상태")
#print("첫줄\n둘째 줄")

notice = """
가동 점검표
1. 온도 확인
2. 압력 확인
"""
print(notice)
guide = "가동 점검표\n 1. 온도 확인\n 2. 압력 확인"
print(guide)

name = "PUMP_A_03"
status = "정상"
date = "2025-01-15"
print(name + "/" + status + "/" + date)

name = "PUMP_A_03"
status = "정상"
hours = 1200
card = "설비: " + name + "\n상태: " + status + "\n가동: " + str(hours) +"\n점검: " + date
date ="2025-01-05"
print(card)

