# 범위 내의 난수 리스트 생성

import random

# 사용자로부터 Start, End, N의 세 값을 입력 받는다.
print("난수를 생성할 범위와 개수를 입력하세요.")
while True:
    input_start = int(input("Start (0 이상의 정수): "))
    if input_start >= 0:
        break
    else:
        print("Start는 0 이상의 정수여야 합니다.")
    
while True:
    input_end = int(input("End (Start보다 큰 정수): "))
    if input_end > input_start:
        break
    else:
        print("End는 Start(1)보다 커야 합니다.")
        
while True:
    input_num = int(input("N (생성할 난수의 개수): "))
    if 1 <= input_num <= 2:
        break
    else:
        print("N은 1부터 2 사이의 정수여야 합니다.")
        
              
# 입력 받은 Start, End, N을 바탕으로 중복되지 않은 N개의 난수를 생성한다.
# 중복되지 않은 N개의 난수를 저장하기 위한 리스트
bingo_board = []

count = 0
while True:
    rand_num = random.randint(input_start, input_end)
    for index in range(count):
        if bingo_board[index] == rand_num:
            break
    else:
        bingo_board.append(rand_num)
        count += 1

    if count == input_num:
        print(f"생성된 난수 리스트: {bingo_board}")
        break