# 성적의 총합, 평균, 학생 수 출력 프로그램
# for 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균,
# 학생 수를 출력하는 프로그램 작성

score = [99, 29, 30, 40, 20, 60]

student_num = 6
sum = 0
avg = 0

for i in score:
    sum += i

avg = sum / student_num

print("학생 수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)