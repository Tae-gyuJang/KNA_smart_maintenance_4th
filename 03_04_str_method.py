# 메서드 - 점(.) 문법
# 형식: 문자열.메서드이름()  중요한점은 ()괄호를 붙여야 실행이 된다
#word = 'python'
#print(word.upper())     # PYTHON
#print(word.count('p'))  # 1
#print(word)             # python  원본 값 그대로구나.

#print('NORMAL'.lower())  # normal 이것또한 upper 처럼 ()괄호를 꼭 붙여야된다
# upper() : 모두 대문자 / lower() : 모두 소문자

#print('python is'.capitalize())     # Python is
#print('hong gil'.title())           # Hong Gil

#word = 'ready'
#print(word.upper())

#status = "WARNING"
#print(status.lower())

#name = " kim chul soo"
#print(name.title())

#status = 'Fault'
#status1 = 'FAULT'
#print(status==status1)
#print(status.lower() == status1.lower())

# 확인하는 메서드 : is*** 메서드는 참/거짓을 반환해준다
#print('ABC'.isupper(), 'abc'.islower())  # True True
# 공백 정리 - strip
# 형식: .strip() = 앞 뒤 공백 제거

#raw = '정상'
#print('['+ raw +']')                 # [정상]
#print('[' + raw.strip() + ']')       # [정상]

# .lstrip() -> 왼쪽 공백을 제거 / .rstrip() -> 오른쪽 공백을 제거
# 주의할 점은 strip은 '앞 과 뒤' 공백만 제거할 수 있고 , 가운데 공백은 제거 할 수 없다.
# strip() 으로 특정한 문자를 제거할 때 -> strip('문자')
#S = '###정상###'
#print(S.strip("#"))                   # 정상

#print('ABC'.isupper(), 'abc'.islower(), 'Abc'.islower())

#text = 'Sensor_LOG.CSV'
#print(text.lower().startswith('sensor'))
#print(text.lower().endswith('.csv'))

#status = ' 가동중 '
#status = status.strip()
#print('[' + status + ']')

#status = ' 대기 '
#status = status.lstrip()
#print('[' + status + ']')
#status = ' 대기 '
#status = status.rstrip()
#print('[' + status + ']')

#S = '***경고***'
#print(S.strip("*"))

# 체이닝 - 메서드를 이어 붙어주는 작업
# 형식: 문자열.strip().lower() -> 왼쪽부터 차례로 적용이된다
#clean = "  NORMAL  ".strip().lower()
#print(clean)                      # normal

clean = "  WARNING  ".strip().lower()
print(clean)

text = '  경보  '
print(text.strip())
print('[' + text + ']')
text = text.strip()
print('[' + text + ']')
