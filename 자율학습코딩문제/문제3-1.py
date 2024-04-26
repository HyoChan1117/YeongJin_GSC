# 사전 예약 시스템의 로직을 시뮬레이션하는 프로그램을 작성해야 한다.
# 이 시스템은 사용자가 특정 이벤트의 사전 예약을 진행할 때, 사용자의 입력에 따라 예약 가능
# 여부를 판단하고 그에 따른 결과를 출력한다.

# 사용자의 나이와 예약하려는 이벤트 코드, 예약을 원하는 날짜를 입력받는다.
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 만 18세 이상만 예약 가능
if 1 <= reservation_date <= 30 and event_code == "E1" :
    if age >= 18 :
        print("예약이 완료되었습니다!")
    else :
        print("나이 제한으로 인해 예약할 수 없습니다.")

# 모든 연령대가 예약 가능하지만, 날짜는 짝수일에만 예약 가능
elif 1 <= reservation_date <= 30 and event_code == "E2" :
    if reservation_date % 2 == 0 :
        print("예약이 완료되었습니다!")
    else :
        print("선택하신 날짜에는 예약할 수 없습니다.")

# 만 16세 이상만 예약할 수 있으며, 7의 배수인 날짜에만 예약 가능
elif 1 <= reservation_date <= 30 and event_code == "E3" :
    if age >= 16 and reservation_date % 7 == 0 :
        print("예약이 완료되었습니다!")
    else :
        print("선택하신 날짜에는 예약할 수 없습니다.")

# 잘못된 입력
else :
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    
    