# replace - 바꾸기 / 지우기
# 형식: 문자열.replace('바꿀 것', '새 것')
# - 모두 바꾸기, 결과는 저장이 필요하다

#print('정 상 가 동'.replace(' ',''))   #공백을 없애주고 공백없는 것을 집어넣는다 # 정상가동
#print('010-1234-5678'.replace('-',''))                                        # 01012345678
#print('3,000'.replace(',',''))                                                # 3000
# 체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 변경

# split - 구분자로 나누기 (결과 값은 리스트)
# 형식 - 문자열.split('구분자')  (구분자 생략 = 공백 기준)
#print('A1 A2 A3'.split())                                     # ['A1', 'A2', 'A3']
#print('사과,배,감'.split(','))                                # ['사과', '배' , '감']

status = '설비 정상 가동'
print(status.replace('정상','점검'))

name = 'PUMP A 03'
print(name.split())

name = 'a,b,c,d'
print(name.split(','))
print(name.split(',',1))