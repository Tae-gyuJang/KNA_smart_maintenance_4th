# 셋 - 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
#logs =  ["S01","S02", "S01", "S03"]
#unique_logs = set(logs)
#print(unique_logs)          # {'S01', 'S03', 'S02'}  # 셋은 순서가 없어 인덱싱이 불가하다
#print(sorted(unique_logs))  # ['S01', 'S02', 'S03']

# add  - 값 추가
#alerts = {"S01","S02"}
#alerts.add("S03")
#print(alerts)               # {'S03', 'S01', 'S02'}  
#alerts.add("S02")           
#print(alerts)               # {'S03', 'S01', 'S02'}
#print("S02" in alerts)      # True

#sensor_ids = ["S02", "S01", "S03", "S01", "S02", "S03", "S01"]
#unique_ids = set(sensor_ids)
#print(sorted(unique_ids), "종류수:", len(unique_ids))

# 집합 연산 - union / intersection(공통)  / difference(차이)
#line_a = {"S01", "S02", "S03"}
#line_b = {"S03", "S04"}
#print(line_a.union(line_b))
#print(line_a.intersection(line_b))
#print(line_a.difference(line_b))

#line_a = {"S01", "S02" , "S03", "S05"}
#line_b = {"S03", "S04" , "S05"}
#print("전체:", line_a.union(line_b))
#print("공통:", line_a.intersection(line_b))
#print("A만:",line_a.difference(line_b))
#print("B만:",line_b.difference(line_a))

yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print("신규이상:", today.difference(yesterday))
print("지속이상:", today.intersection(yesterday))
