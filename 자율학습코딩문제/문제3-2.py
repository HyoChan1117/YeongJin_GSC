# 사용자로부터 주당 수업 시간, 결석한 총 시간, 지각 횟수를 입력 받아서 출석 점수를
# 출력하는 프로그램 작성

# 출석 점수를 계산하는 함수를 정의한다.
def calculate_attendance_score(arg1, arg2, arg3):
    absence_hours = arg2 + (arg3 // 3)
    total_hours = arg1 * 15
    attendance_score = 20 - (20 * absence_hours / total_hours)
    return attendance_score

# 주당 수업 시간, 결석한 총 시간, 지각 횟수를 입력 받는다.
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

# 출석 점수를 계산하는 함수를 호출한다.
attendance_score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

# 결석 시간이 총 수업 시간의 1/4를 초과하는 경우, "F (학점 미부여)"를 출력한다.
if absence_hours + (tardy_count // 3) > hours_per_week * 15 * 0.25 :
    print(f"당신의 출석 점수는 F (학점 미부여)점입니다.")


# 그 외의 경우에는 출석 점수를 출력한다.
else :
    print(f"당신의 출석 점수는 {float(attendance_score)}점 입니다.")
