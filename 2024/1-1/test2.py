# 야구 게임 만들기

import random

# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성한다.
rand_list = []
count = 0
while count < 3:
    rand_num = random.randint(0, 9)
    # 중복값 검사
    for index in range(count):
        if rand_list[index] == rand_num:
            break
    else:
        rand_list.append(rand_num)
        count += 1
        
print(rand_list)

# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력한다.
count_trial = 1
count_strike_out = 0
while True:
    count_strike = 0
    count_ball = 0
    
    input_user = input(f"시도 {count_trial}: 입력한 숫자 - ").split()
    input_list = [ int(value) for value in input_user ]
    
    # 스트라이크, 볼 판정
    for i in range(3):
        for j in range(3):
            if rand_list[i] == input_list[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
    
    # 스트라이크 아웃
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
    
    print(f"{count_strike} Strike, {count_ball} Ball, {count_strike_out} Out")
    
    # 게임 패배 조건
    # 시도 횟수가 5번 이상일 경우
    if count_trial >= 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 초과)")
        print(f"정답: {rand_list}")
        break
    # 스트라이크 아웃 횟수가 2번 이상일 경우
    elif count_strike_out >= 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 초과)")
        print(f"정답: {rand_list}")
        break
    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    if count_strike == 3:
        print(f"게임 종료: 승리")
        print(f"정답: {rand_list}")
        break
    count_trial += 1