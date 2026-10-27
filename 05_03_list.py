#temps = [28, 32, 25, 35, 29, 31]
##for t in temps:
#    if t >= 30:
#        print(f'고온: {t}')

#hours = [3, 8, 12, 6, 10, 4, 9]

#for h in hours:
#    if h >= 5 and h <= 10:
#        print(h)


# 최대, 최소
#temps = [25, 32, 28, 36, 27, 31]
#biggest = temps[0]
#for t in temps:
#    if t > biggest:
#        biggest = t
#print(biggest)          # 36

# 빈 리스트 채우기
#temps = [25, 32, 28, 36, 27, 31]
#doubled = []
#for t in temps:
#    doubled.append(t * 2)
#print(doubled)                # [50, 64, 56, 72, 54, 62]

#temps = [28, 32 , 25, 36, 29, 31]
#total = 0
#count = 0
#for t in temps:
#    if t > 30:
#        total += t
#        count += 1

#print(f'고온 평균: {total / count}')

#temps = [28, 32, 25, 35, 29, 31, 33]
#high = []

#for t in temps:
#    if t > 30:
#        high.append(t)

#print(high)
#print(f'개수{len(high)}')

#celsius = [25, 26, 24, 28, 27]
#fahrenheit = []

#celsius:
#    f = c * 1.8 + 32
#    fahrenheit.append(f)

#print(fahrenheit)

# 중첩 리스트 = 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
#rows = [["펌프", 25],["모터", 32],["압축기", 28]]
#for row in rows:
#    print(row[0], "온도", row[1])

temps = [26, 28, 35, 22, 36, 27, 32, 33, 31]
total = 0
high_temps = []
for t in temps:
    total += t
avg_all = total / len(temps)

for t in temps:
    if t > 30:
        high_temps.append(t)

high_sum = 0
for t in high_temps:
    high_sum += t
avg_high = high_sum / len(high_temps)

print("전체 평균:", avg_all)
print("고온 개수:", len(high_temps))
print("고온 평균:", avg_high)
