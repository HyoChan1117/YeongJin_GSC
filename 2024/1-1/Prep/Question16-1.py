
import random

# 중복되지 않은 난수 값 3개 생성

count = 0
rand_list = []

while count < 3:
    rand_value = random.randint(0, 9)
    
    for index in range(count):
        if rand_list[index] == rand_value:
            break
    else:
        rand_list.append(rand_value)
        count += 1

print(f"생성된 난수값")

count_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    # 사용자로부터 정수 3개 입력
    input_values = input().split()
    input_list = [ int(value) for value in input_values ]

    # strike, ball 판별
    for i in range(3):
        for j in range(3):
            if rand_list[i] == input_list[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
                    
    # strike out 판별
    if count_strike == 0 and count_ball == 0 :
        count_strike_out += 1
        print(f"스트라이크 아웃: {count_strike_out}")

    # 게임 종료 조건
    # - strike 3개
    if count_strike >= 3:
        print(f"사용자 승리!")
        break
    
    # - strike out 2번 or 시도 횟수 5번 이상
    if count_strike_out >= 2 or count_trial >= 5:
        print(f"사용자 패배!")
        break
    
    count_trial += 1