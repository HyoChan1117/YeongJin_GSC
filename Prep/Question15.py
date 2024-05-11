# 사용자로부터 가위, 바위, 보 중 하나를 입력받고 컴퓨터가
# 선택한 값과 대결하여 승, 패, 무를 판단하고 결과를 출력
# 하는 프로그램 작성

import random

# 가위, 바위, 보를 원소로 가지는 리스트를 하나 생성한다.
r_p_s = ["가위", "바위", "보"]

# 초기값을 설정한다.
win = 0
loss = 0
draw = 0

# 가위바위보가 끝날 때까지 무한루프를 돌린다.
while True:
    # 2선승제 조건을 만족하기 위해 2번 이기거나 2번 지는 경우 반복을 멈춘다.
    if win == 2 or loss == 2:
        break
    
    # 사용자로부터 가위, 바위, 보 중 하나를 입력 받는다.
    user = input("가위, 바위, 보 중 하나를 입력하세요: ")
    # 컴퓨터는 가위, 바위, 보 중 하나를 랜덤으로 가져오도록 한다.
    computer = random.choice(r_p_s)
    
    # 사용자가 승리했을 경우
    if (computer == "가위" and user == "바위") or (computer == "바위" and user == "보") or (computer == "보" and user == "가위"):
        win += 1
        print(f"컴퓨터: {computer}")
        print(f"승리! 현재 전적: {win}승 {loss}패 {draw}무")
    
    # 사용자와 컴퓨터가 무승부 했을 경우
    elif computer == user:
        draw += 1
        print(f"컴퓨터: {computer}")
        print(f"무승부! 현재 전적: {win}승 {loss}패 {draw}무")
    
    # 사용자가 패배했을 경우
    elif (computer == "가위" and user == "보") or (computer == "바위" and user == "가위") or (computer == "보" and user == "바위"):
        loss += 1
        print(f"컴퓨터: {computer}")
        print(f"패배! 현재 전적: {win}승 {loss}패 {draw}무")
    
    # 가위, 바위, 보 이외에 다른 문자열을 입력한 경우
    else:
        print("가위, 바위, 보 중에서 선택하세요.")

# 2선승제에 따라 승리를 2번 하거나 패배를 2번 했을 경우(= 가위바위보가 종료 되었을 때)
if win == 2 or loss == 2:
    print(f"전적: {win}승 {loss}패 {draw}무")
    # 승리가 패배보다 많은 경우
    if win > loss:
        print("최종 승자: 사용자")
    # 패배가 승리보다 많은 경우
    else:
        print("최종 승자: 컴퓨터")
    
