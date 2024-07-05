# 사용자로부터 출발 시간과 도착 시간, 그리고 이동 거리를 입력 받아,
# 평균 속도를 계산하는 프로그램 작성

# 출발 시간과 도착 시간, 그리고 이동 거리를 입력 받는다.
# 출발 시간을 시간과 분으로 나눠서 입력 받는다.
start_hour = int(input("출발 시 (시간)을 입력하세요: "))
start_minute = int(input("출발 시 (분)을 입력하세요: "))

# 도착 시간을 시간과 분으로 나눠서 입력 받는다.
department_hour = int(input("도착 시 (시간)을 입력하세요: "))
department_minute = int(input("도착 시 (분)을 입력하세요: "))

# 이동 거리를 입력 받는다.
move_distance = int(input("이동 거리(km)를 입력하세요: "))

# 총 이동시간은 분 단위로 환산하여 계산한 후 다시 시간으로 환산한 후 반환한다.
def calculate_to_minute(s_h, s_m, d_h, d_m) :
    all_move_minutes = (d_h * 60 + d_m) - (s_h * 60 + s_m)
    all_move_times = all_move_minutes / 60
    return all_move_times

# 함수를 호출하여 평균 속도를 계산하는 변수를 선언한다.
average_speed = move_distance / calculate_to_minute(start_hour, start_minute, department_hour, department_minute)

# 이동 거리, 출발 시간, 도착 시간, 평균 속도를 출력하고
print(f"이동 거리: {float(move_distance)}km")
print(f"출발 시간: {start_hour}시 {start_minute}분")
print(f"도착 시간: {department_hour}시 {department_minute}분")
# 속도 상태는 다음 조건을 따른다.
# 평균 속도가 60km/h 미만일 경우, 속도 상태를 "느림"으로 출력
if average_speed < 60 :
    print(f"평균 속도: {float(average_speed):.2f}km/h")
    print("속도 상태: 느림")
    
# 평균 속도가 90km/h 미만이면 속도 상태를 "보통"으로 출력
elif average_speed < 90 :
    print(f"평균 속도: {float(average_speed):.2f}km/h")
    print("속도 상태: 보통")

# 90km/h 이상이면 "빠름"으로 출력
elif average_speed >= 90 :
    print(f"평균 속도: {float(average_speed):.2f}km/h")
    print("속도 상태: 빠름")
