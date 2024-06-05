# 학생 점수 분석 및 등급 분포 시각화
# 여러분은 학생들의 점수 데이터를 분석하고, 점수에 따른
# 등급 분포를 텍스트 기반의 그래프로 시각화하는 프로그램 작성

# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 점수 리스트를 분류한다.
achieve1 = [ value for value in scores if value >= 90 ]
achieve2 = [ value for value in scores if 80 <= value < 90 ]
achieve3 = [ value for value in scores if 70 <= value < 80 ]
achieve4 = [ value for value in scores if 60 <= value < 70 ]
achieve5 = [ value for value in scores if value < 60 ]

print("등급 분포 및 평균 점수:")

# 90점 이상인 점수 리스트의 평균을 구하고 출력한다.
sum1 = 0
for score in achieve1:
    sum1 += score
    avg1 = sum1 / len(achieve1)
print(f"A 등급: 평균 점수 = {avg1:.2f}")
print(f"{len(achieve1) * "*"} ({len(achieve1)}명)")

# 80점 이상 90점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum2 = 0
for score in achieve2:
    sum2 += score
    avg2 = sum2 / len(achieve2)
print(f"B 등급: 평균 점수 = {avg2:.2f}")
print(f"{len(achieve2) * "*"} ({len(achieve2)}명)")

# 70점 이상 80점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum3 = 0
for score in achieve3:
    sum3 += score
    avg3 = sum3 / len(achieve3)
print(f"C 등급: 평균 점수 = {avg3:.2f}")
print(f"{len(achieve3) * "*"} ({len(achieve3)}명)")

# 60점 이상 70점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum4 = 0
for score in achieve4:
    sum4 += score
    avg4 = sum4 / len(achieve4)
print(f"D 등급: 평균 점수 = {avg4:.2f}")
print(f"{len(achieve4) * "*"} ({len(achieve4)}명)")

# 60점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum5 = 0
for score in achieve5:
    sum5 += score
    avg5 = sum5 / len(achieve5)
print(f"F 등급: 평균 점수 = {avg5:.2f}")
print(f"{len(achieve5) * "*"} ({len(achieve5)}명)")