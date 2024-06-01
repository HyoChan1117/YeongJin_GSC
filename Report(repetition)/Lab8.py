# 숫자 맞추기 게임
# while문과 break문을 사용하여 1부터 100 사이의 숫자를 맞추는 게임 작성
# 사용자가 숫자를 맞출 때까지 반복하고, 맞추면 반복을 종료
# 정답 숫자는 랜덤 함수를 이용하여 1에서 100 사이 임의 정수 선택

import random

# 1부터 100까지의 정수 중 랜덤으로 하나 선택
random_int = random.randint(1, 100)

# 입력한 정수와 랜덤 정수가 같을 때까지 반복한다.
while True:
    input_int = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    
    if input_int == random_int:
        print("정답입니다!")
        break
    
    elif input_int < random_int:
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")

        
        