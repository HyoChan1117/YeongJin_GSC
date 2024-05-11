# 사용자로부터 가위, 바위, 보 중 하나를 입력 받고, 컴퓨터의 선택과 비교하여 승리, 패배,
# 또는 무승부를 결정하는 프로그램 작성

import random

# 가위, 바위, 보를 원소로 가지는 리스트를 생성한다.
rsp = ["가위", "바위", "보"]

# 생성된 리스트의 원소를 랜덤으로 선택하는 변수를 선언한다.
input_computer = rsp[random.randint(0, 2)]

# 사용자로부터 가위, 바위, 보 중 하나를 입력 받는다.
input_user = input("가위, 바위, 보 중 하나를 선택하세요: ")

# 랜덤으로 선택하는 변수를 출력한다.
print(f"컴퓨터의 선택: {input_computer}")

# 사용자와 컴퓨터가 무승부인 경우
if input_user == input_computer:
    print(f"결과: 무승부입니다!")

# 사용자가 승리하는 경우
elif input_user == "가위" and input_computer == "보" or\
    input_user == "바위" and input_computer == "가위" or\
    input_user == "보" and input_computer == "바위":
    print(f"결과: 당신이 이겼습니다!!")

# 사용자가 패배하는 경우
elif input_user == "가위" and input_computer == "바위" or\
    input_user == "바위" and input_computer == "보" or\
    input_user == "보" and input_computer == "가위":
    print(f"결과: 당신이 졌습니다!!")

# 사용자로부터 가위, 바위, 보 이외의 입력을 받은 경우
else:
    print(f"잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요.")

