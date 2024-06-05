# 점수 분류 및 평균 계산
# 학생들의 점수 리스트가 주어졌을 때, 각 점수를 분류하고
# 분류된 점수들의 평균을 계산하는 프로그램 작성

# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

# 점수 리스트를 분류한다.
achieve1 = [ value for value in scores if value >= 90 ]
achieve2 = [ value for value in scores if 70 <= value < 90 ]
achieve3 = [ value for value in scores if 50 <= value < 70 ]
achieve4 = [ value for value in scores if value < 50 ]

# 90점 이상인 점수 리스트의 평균을 구하고 출력한다.
sum1 = 0
for score in achieve1:
    sum1 += score
    avg1 = sum1 / len(achieve1)
print(f"우수: {achieve1} 평균: {avg1}")

# 70점 이상 90점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum2 = 0
for score in achieve2:
    sum2 += score
    avg2 = sum2 / len(achieve2)
print(f"우수: {achieve2} 평균: {avg2}")

# 50점 이상 70점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum3 = 0
for score in achieve3:
    sum3 += score
    avg3 = sum3 / len(achieve3)
print(f"우수: {achieve3} 평균: {avg3}")

# 50점 미만인 점수 리스트의 평균을 구하고 출력한다.
sum4 = 0
for score in achieve4:
    sum4 += score
    avg4 = sum4 / len(achieve4)
print(f"우수: {achieve4} 평균: {avg4}")