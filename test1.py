# 메뉴로 구성된 구구단과 삼각형 출력 프로그램
# 1. 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
# 2. 입력이 1~3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
# 3. 각 기능에 따른 추가 입력 요구와 에러 처리를 포함

import random

# 무한루프를 사용하여 메뉴 출력
while True:
    print("-------------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-------------------")
    menu_num = int(input("원하는 메뉴 번호를 입력하세요: "))
    
    # 구구단 출력
    if menu_num == 1:
        print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~9)")
        # 사용자로부터 출력할 구구단의 범위를 입력 받음
        # 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
        # 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
                
        while True:
            input_num1 = input().split("~")
            mul_num = [ int(value) for value in input_num1 ]
            if len(mul_num) == 1 and 2 <= mul_num[0] <= 9:
                for i in mul_num:
                    for j in range(1, 10):
                        print(f"{i} * {j} = {i * j}")
                break
                        
            elif len(mul_num) == 2 and 2 <= mul_num[0] <= 9 and 2 <= mul_num[1] <= 9:
                for i in range(mul_num[0], mul_num[1] + 1):
                    for j in range(1, 10):
                        print(f"{i} * {j} = {i * j}")
                    print()
                break
            else:
                print("2~9 사이의 값으로 입력하세요")


    # 랜덤값 삼각형 출력
    elif menu_num == 2:
        print("삼각형의 높이 줄 수를 입력하세요(2이상 3이하)")
        
        # 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음 -> 2 <= 높이 <= 3
        input_num2 = int(input())
        
        # 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
        list_num = [ int(value) for value in range(0, 10) ]
        
        # 사용자로부터 입력 받은 정수만큼 반복
        for i in range(input_num2):
            if i <= 3:
                print(" " * (2 - i), "*" * (i + 1))
            elif i <= 2:
                print(" " * (2 - i), "*" * (i + 1))
        
        # 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
        if input_num2 != 2 and input_num2 != 3:
            print("2 또는 3을 입력하세요")
    
    # 3번 종료를 선택했을 때 프로그램 종료
    elif menu_num == 3:
        print("프로그램을 종료합니다.")
        break