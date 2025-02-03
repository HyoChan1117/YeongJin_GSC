# 사용자로부터 가위, 바위, 보 중 하나를 입력 받고, 컴퓨터가
# 선택한 값과 대결하여 승, 패, 무를 판단하고 결과를 출력
# 하는 프로그램 작성

import random

# 승패무를 초기화한다.
count_win, count_lose, count_draw = 0, 0, 0

# 가위, 바위, 보 게임 만들기
# 3판 2선승제에 따라 사용자가 2판을 이기거나 2판을 지는 경우
# 반복을 멈춘다.
while True:
    if count_win == 2 or count_lose == 2:
        if count_win == 2:
            print(f"전적: {count_win}승 {count_lose}패 {count_draw}무")
            print(f"최종 승자: 사용자")
        else:
            print(f"전적: {count_win}승 {count_lose}패 {count_draw}무")
            print(f"최종 승자: 컴퓨터")
        break
    # 가위, 바위, 보를 원소로 가지는 리스트를 생성한다.
    rsp = ["가위", "바위", "보"]

    # 컴퓨터가 낼 것을 생성한 리스트에서 랜덤으로 불러온다.
    input_computer = rsp[random.randint(0, 2)]

    # 사용자로부터 가위, 바위, 보 중 하나를 입력 받는다.
    input_user = input("가위, 바위, 보 중 하나를 입력하세요: ")

    # 컴퓨터의 경우를 출력한다.
    print(f"컴퓨터: {input_computer}")

    # 사용자와 컴퓨터가 무승부인 경우
    if input_user == input_computer:
        count_draw += 1
        print(f"무승부! 현재 전적: {count_win}승 {count_lose}패 {count_draw}무")

    # 사용자가 이길 경우
    elif input_user == "가위" and input_computer == "보" or\
        input_user == "바위" and input_computer == "가위" or\
        input_user == "보" and input_computer == "바위":
        count_win += 1
        print(f"승리! 현재 전적: {count_win}승 {count_lose}패 {count_draw}무")

    # 사용자가 질 경우
    else:
        count_lose += 1
        print(f"패배! 현재 전적: {count_win}승 {count_lose}패 {count_draw}무")