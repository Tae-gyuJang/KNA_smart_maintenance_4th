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

#status = '설비 정상 가동'
#print(status.replace('정상','점검'))

#name = 'PUMP A 03'
#print(name.split())

#name = 'a,b,c,d'
#print(name.split(','))
#print(name.split(',',1))

# join - 합치기 (리스트 -> 문자열)
# 형식: '구분자'.join(리스트)   구분자가 앞에 온다
#print('-'.join(['2025','01','15']))     #2025-01-15

# split + join
# - split : 문자열에서 리스트를 만들어주고
# - join : 리스트에서 문자열로 만들어주니까 split join 같이 쓸 수 있다
#raw = '사과, 배, 감'
#p = raw.split(',')
#print(p)                        #['사과', ' 배', ' 감']
#print('/'.join(p))              #사과/ 배/ 감               두개 다 공백 있는데 공백없애고 싶으면 strip이용
#print('/'.join([p[0].strip(), p[1].strip(), p[2].strip()]))  # 사과/배/감

print('-'.join(['2025','01','15']))

print('2025','1','15',sep='-')
print('2025','1','15',sep=',')

text = '2025/01/15'
parts = text.split('/')
print(parts)
print('-'.join(parts))

text = '1,NORMAL,25.3'
p = text.split(',')
print(p)
print(','.join([p[0].strip(), p[1].strip(), p[2].strip()]))
print((','.join([p[1].strip()])).lower())