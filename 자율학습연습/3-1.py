# 사용자로부터 나이, 예약하려는 이벤트 코드, 예약을 원하는 날짜를 입력 받아, 예약 가능 여부를
# 판단하고 그에 따른 결과를 출력하는 프로그램 작성

# 사용자의 나이, 예약하려는 이벤트 코드, 예약을 원하는 날짜를 입력 받는다.
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 입력 받은 이벤트 코드에 따라 다음과 같은 규칙이 적용된다.(조건문 사용)
# 각 조건에 따라 다른 결과를 출력한다.
# 예약 날짜가 1 이상 30 이하인 숫자
if 1 <= reservation_date <= 30:
    # E1 : 만 18세 이상만 예약 가능
    if event_code == "E1":
        if age >= 18:
            print("예약이 완료되었습니다!")
        else:
            print("나이 제한으로 인해 예약할 수 없습니다.")

    # E2 : 모든 연령대가 예약 가능하지만, 날짜는 짝수일에만 예약 가능
    elif event_code == "E2":
        if reservation_date % 2 == 0:
            print("예약이 완료되었습니다!")
        else:
            print("선택하신 날짜에는 예약할 수 없습니다.")

    # E3 : 만 16세 이상만 예약 가능하며, 7의 배수인 날짜에만 예약 가능
    elif event_code == "E3":
        if age >= 16 and reservation_date % 7 == 0:
            print("예약이 완료되었습니다!")
        elif age < 16:
            print("나이 제한으로 인해 예약할 수 없습니다.")
        elif reservation_date % 7 != 0:
            print("선택하신 날짜에는 예약할 수 없습니다.")

    # 이외의 이벤트 코드를 입력 받은 경우, "잘못된 입력입니다. 프로그램을 종료합니다."
    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")

# 예약 날짜가 1 이상 30 이하가 아닌 경우
else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")