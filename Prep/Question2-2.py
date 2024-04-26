# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램 작성

# 평균 점수를 계산하는 함수를 선언한다.
def calculate_average(math_score, science_score, english_score) :
    average = (math_score + science_score + english_score) / 3
    return average

# 사용자로부터 수학, 과학, 영어의 점수를 입력받는다.
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

average = calculate_average(math_score, science_score, english_score)
# 함수를 호출하여 평균 점수와 학점 등급이 나오는 결과를 출력한다.
if average >= 90 :
    print(f"평균 점수는 {average:.1f}점이고, 학점은 A입니다.")

elif 80 <= average < 90 :
    print(f"평균 점수는 {average:.1f}점이고, 학점은 B입니다.")

elif 70 <= average < 80 :
    print(f"평균 점수는 {average:.1f}점이고, 학점은 C입니다.")

elif 60 <= average < 70 :
    print(f"평균 점수는 {average:.1f}점이고, 학점은 D입니다.")

else :
    print(f"평균 점수는 {average:.1f}점이고, 학점은 F입니다.")

