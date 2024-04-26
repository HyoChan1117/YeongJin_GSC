# 사용자로부터 수학, 과학, 영어의 점수를 입력 받아, 평균 점수를 계산하고, 평균 점수를 사용하여
# 학점 등급을 결정하는 프로그램 작성

# 수학, 과학, 영어의 점수를 입력 받는다.
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

# 입력 받은 점수들을 바탕으로 평균 점수를 계산하는 함수를 정의한다.
def calculate(arg1, arg2, arg3):
    average_score = (arg1 + arg2 + arg3) / 3
    return average_score

# 평균 점수를 계산하는 함수를 호출하여 학점 등급을 결정하고 결과를 출력한다.
average_score = calculate(math_score, science_score, english_score)

if average_score >= 90:   # 평균 점수가 90점 이상
    print(f"평균 점수는 {average_score}점이고, 학점은 A입니다.")
elif 80 <= average_score < 90:   # 평균 점수가 80점 이상 90점 미만
    print(f"평균 점수는 {average_score}점이고, 학점은 B입니다.")
elif 70 <= average_score < 80:   # 평균 점수가 70점 이상 80점 미만
    print(f"평균 점수는 {average_score}점이고, 학점은 C입니다.")
elif 60 <= average_score < 70:   # 평균 점수가 60점 이상 70점 미만
    print(f"평균 점수는 {average_score}점이고, 학점은 D입니다.")
elif average_score < 60:   # 평균 점수가 60점 미만
    print(f"평균 점수는 {average_score}점이고, 학점은 F입니다.")