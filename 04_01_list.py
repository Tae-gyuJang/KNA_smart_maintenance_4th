# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

#temps = [25, 26, 24, 28, 27]        # 숫자 리스트
#machines = ["펌프", "모터", "압축기"]
#mixed = ["펌프", 87, True]          # 종류가 달라도 한 리스트에 담을 수 있다

#print(len(temps))

#temps = [25, 26, 24, 27, 26]
#print(temps)
#print(len(temps))
#results = []
#print(len(results))

#temps = [22, 24, 27, 25, 26, 23]
#print(temps[0])
#print(temps[2])
#print(temps[-1])

#line = [100, 120, 95, 130, 105, 122]
#first = line[0]
#last = line[-1]
#total = first + last
#print(total)
#mid = total / 2
#print(mid)

#temps = [22, 24, 27, 25, 26, 23, 29, 28, 30, 31]
#front = temps[0:3]
#print(front)
#back = temps[-3:]
#print(back)
#print(len(front))

#data = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
#first = data[0:6]
#print(first)
#second = data[6:12]
#print(second)
#print(len(first), len(second))

# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
#nums = [25, 26, 24, 28, 27]
#nums[2] = 99
#print(nums)
#print("모터" in machines)

# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
#data = [25, 26, 24]
#data.append(28)
#data.insert(1,99)
#data.extend([30],[31])
#print(data)

#temps = [25, 26, 240, 28, 27]
#print(240 in temps)
#i = temps.index(240)
#temps[i] = 24
#print(temps)
#print(240 in temps)

#temps = []
#temps.append(30)
#print(temps)
#temps.insert(0, 28)
#print(temps)
#more = [31, 32]
#temps.extend(more)
#print(temps) 

# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) /del 리스트[위치]
#d = [25, 26, 24, 28, 27]
#d.remove(24)
#print(d)                     # [25, 26, 28, 27]
#got = d.pop(1)
#print(got, d)                # 26 [25, 28, 27]
#del d[0]
#print(d)                     # [28, 27]

# 정렬 , 탐색 - sort, reverse / count, index
# 형식: 리스트.sort()  리스트.reverse()  리스트.count(값)  리스트.index(값)
#l = [27, 24, 30, 22, 26]
#l.sort()
#l.sort(reverse=True)
#l.reverse()
#print(l)

#r = ["정상", "이상", "정상", "정상", "이상"]
#print(r.count("정상"), r.index("이상"))           # 3 1

temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)
popped = temps.pop(1)
print("꺼낸값", popped)
del temps[0]
print(temps)

temps = [27, 24, 30, 22, 26, 24, 28]
temps.sort()
print(temps)
temps.reverse()
print(temps)
print(temps.count(24))
print(temps.index(24))

