# try-except-else-finally
# - else: 예외가 하나도 안 났을 때만 실행
# - finally: 성공/실패 상관없이 무조건 마지막 실행

#text = "62.5"
#try:
#    temp = float(text)
#except ValueError:
#    print("변환 실패")
#else:
#    print("변환 성공:", temp)
#finally:
#    print("종료")

#f = None
#try:
#    f = open("data/09_ict_inspection_15_261102_1.csv", "r", encoding="utf-8")
#    print("파일 열림, closed =", f.closed)
#    first = f.readline()
#    print("첫 줄:", first.strip())
#    num = int("abc")
#finally:
 #   if f is not None:
#        f.close()
#    print("finally 실행, closed =", f.closed if f else None)

#try:
#    f = open("data/09_ict_inspection_15_261102_1.csv", "r", encoding="utf-8")
#    first = f.readline()
#    print(first.strip())
#except FileNotFoundError:
#    print("파일이 존재하지 않습니다")
#finally:
#    f.close()

#print("파일이 안전하게 닫힘")

# 실습 2
#try:
#    with open("data/09_ict_inspection_dirty.csv", encoding="utf-8") as f:
#        rows = f.readlines()[1:]        # 슬라이싱 (헤더 빼려고)
#except FileNotFoundError:
#    rows = []

#total = 0.0
#skipped = 0
##for line in rows:
#    try:
#        total += float(line.split(",")[2])    # 측정값(2열)
#    except (ValueError, IndexError):
#        skipped += 1
#        continue

#print("합계:", round(total, 1), "/건너뜀:", skipped)    

try:
    with open("data/09_ict_inspection_15_261102_1.csv", encoding="utf-8") as f:
        rows = f.readlines()[1:]
except FileNotFoundError:
    rows = []

total, valid = 0.0, 0
for line in rows:
    try:
        value = float(line.split(",")[2])   
        total += value                       
        valid += 1                           
    except ValueError:
        pass                                 
    except IndexError:
        pass                                 

print(f"합계: {total:.2f} / 유효: {valid} / 제외: {len(rows) - valid}")
