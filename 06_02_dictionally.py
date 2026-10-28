# 딕셔너리
# 형식: {키: 값, 키: 값} - 키는 문자열
# - 리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)으로 찾는다

#sensors = {"모터온도": 78, "진동": 0.5}
#print(sensors)                             # {'모터온도': 78, '진동': 0.5}
#print(sensors["모터온도"])                 # 78
#print(type(sensors))                       # <class 'dict'>
# print(sensors["유량"])                   # keyError -> 없는 키를 조회시 에러

# 추가  / 수정  /  삭제
# 형식: 딕셔너리[키] = 값 (없는 키 - 추가 , 있는 키 - 수정)
# 형식: (삭제) del 딕셔너리[키]

#sensors = {"모터온도": 78, "진동": 0.5}
#sensors["펌프압력"] = 95
#sensors["모터온도"] = 80
#del sensors["진동"]
#print(sensors)                            # {'모터온도': 80, '펌프압력': 95}

# get / in 
# 형식: 딕셔너리.get(키, 기본값)      / 키 in 딕셔너리
#sensors = {"모터온도": 78, "진동": 0.5}
#print(sensors.get("유량"))                # None
#print(sensors.get("유량",0))              # 0
#print("모터온도" in sensors)              # True   (키만 포함 여부 확인 가능)
#print(80 in sensors)                      # False (값은 확인이 안된다)

#sensors = {"온도": 25, "습도": 60, "조도": 300}
#print(sensors["온도"])
#sensors["압력"] = 1013
#sensors["온도"] = 78
#print(sensors["온도"])
#print(sensors)
#print(sensors.get("소음", 0))
#print("습도" in sensors)

# keys / values / items / len
#sensors = {"모터온도": 78, "진동": 0.5}
#print(list(sensors.keys()))                # ['모터온도', '진동']
#print(list(sensors.values()))              # [78, 0.5]
#avg = sum(sensors.values()) / len(sensors)
#print(avg)                                 # 39.25

#for name, value in sensors.items():        # 모터온도 78
#    print(name, value)                     # 진동 0.5

# for k in sensors.keys()     
# for v in sensors.values()

# update - 여러 항목 한번에 갱신(키값이 있으면 수정, 없으면 추가해준다)
#d = {"온도": 78}
#d.update{"온도": 80 , "압력": 95}
#print(d)     

#sensors = {"온도": 70, "진동": 3.2 , "유량": 120}
#ew_d = {"온도": 75, "진동": 4.1}
#sensors.update(new_d)
#print(sensors)

#del sensors["유량"]
#print(sensors)
#print("센서 수:", len(sensors))

#sensors = {"온도":70 , "압력": 95, "유량": 65}
#avg = sum(sensors.values()) / len(sensors)
#print("평균:", round(avg, 1))

#max_name = max(sensors, key=sensors.get)
#max_value = sensors[max_name]
#for name, value in sensors.items():
#    if value > max_value:
#        max_name, max_value = name, value

#print("최댓값 센서:", max_name, max_value)

# zip : 센서명 - 값 매피하기
#names = ["온도", "진동", "압력"]
#values = [78, 0.5, 95]
#sensors = dict(zip(names, values))
#print(sensors)                       # {'온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리의 값에 리스트/ 딕셔너리 - 중첩 딕셔너리
#plant ={ 
#    "1번모터": {"온도": 78, "상태": "정상"},
#    "2번펌프": {"압력": 95, "상태": "경고"}
#    }

#print(plant["2번펌프"]["압력"])

#names = ["온도", "진동", "압력"]
#values = [78, 0.5, 95]
#sensors = dict(zip(names, values))
#print(sensor)
#for name, value in sensors.items():
#    print(name, value)

#values = {"온도": 78, "진동": 0.5, "압력": 95}
#limits = {"온도": 75, "진동": 1.0, "압력": 100}
#warning = []
#for name, value in values.items():
#    if value > limit[name]:
#        warning.append(name)

#print("경고 센서:", warning)

#plant = {
#    "1번펌프": {"온도":70, "압력":80, "상태": "정상"},
#    "2번펌프": {"온도":78, "압력":95, "상태": "경고"}
#}
#print(plant["2번펌프"]["압력"])
#for name, value in plant.items():
#    if value["상태"] == "경고":
#        print(name, "점검필요")

#rows = ["온도,78", "압력, 95", "진동, 0.5"]
#sensors = {}
#for row in rows:
#    name, value = row.split(",")
#    sensors[name] = float(value)
#print(sensors)

sensors = {"온도": 98, "압력": 110, "진동": 78.5}
limits = {"온도": 90, "압력": 100, "진동": 80}
avg = sum(sensors.values())/len(sensors)
print("평균:", avg)
danger = set()
for name , value in sensors.items():
    if value > limits[name]:
        danger.add(name)
print("위험 센서:", sorted(danger))

