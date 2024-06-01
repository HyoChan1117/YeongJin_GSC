# 숫자 맞추기 게임 확장 버전

import random

# 1부터 100까지의 정수 중 랜덤으로 하나 선택
random_int = random.randint(1, 100)

count = 1
num = 1

# 입력한 정수와 랜덤으로 받은 정수가 같으면 반복을 종료한다.
while True:
    input_int = int(input(f"기회 {num}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))
    
    if count == 10 or input_int == random_int or \
        input_int == 0:
        break
    
    elif input_int < random_int:
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")
        
    count += 1
    num += 1

# 10번의 시도를 했을 경우
if count == 10:
    # 입력한 정수와 랜덤 정수가 같지 않으면 해당 문구 출력
    if input_int != random_int:
        print(f"모든 기회를 사용하였습니다. 정답은 {random_int}입니다.")
    # 입력한 정수와 랜덤 정수가 같으면 해당 문구 출력
    elif input_int == random_int:
        print("정답입니다!")

# 경기 횟수를 무시하고 입력한 정수와 랜덤 정수가 같으면
# 해당 문구 출력
elif input_int == random_int:
    print("정답입니다!")
    