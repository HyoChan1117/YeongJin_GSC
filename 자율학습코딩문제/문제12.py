# 사용자로부터 가위, 바위, 보 중 하나를 입력 받고, 컴퓨터의 선택과 비교하여 승리, 패배,
# 또는 무승부를 결정하는 프로그램 작성

import random

# 난수를 생성하여 리스트에서 요소를 선택하는 방법

choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)

print(computer_choice)

my_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

if computer_choice == '가위':
    print("컴퓨터의 선택: 가위")
    if my_choice == '가위':
        print("결과: 무승부입니다!")
    elif my_choice == '바위':
        print("결과: 당신이 이겼습니다!")
    elif my_choice == '보':
        print("결과: 당신이 졌습니다!")
elif computer_choice == '바위':
    print("컴퓨터의 선택: 바위")
    if my_choice == '가위':
        print("결과: 당신이 졌습니다!")
    elif my_choice == '바위':
        print("결과: 무승부입니다!")
    elif my_choice == '보':
        print("결과: 당신이 이겼습니다!")
elif computer_choice == '보':
    print("컴퓨터의 선택: 보")
    if my_choice == '가위':
        print("결과: 당신이 이겼습니다!")
    elif my_choice == '바위':
        print("결과: 당신이 졌습니다!")
    elif my_choice == '보':
        print("결과: 무승부입니다!")
        
# 가위, 바위, 보를 입력하지 않았을 경우,
else:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
    