
# 중복되지 않은 1~10사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# example)
# 3 7 4 : computer
# 2 3 4 : user
# result : 1 strike, 1 ball

import random

com_list = list()

count = 0

while count < 3:  # while문 안에 반복문이 들어감
    rand_value = random.randint(1, 10)
    found_duplicated_value = False  # 이 변수의 값이 True인지 False인지 확인해봐야 함
    
    for sub_count in range(count):  # 
        # 중복 값이 있을 경우
        if rand_value == com_list[sub_count]:
            found_duplicated_value = True  # 중복값이 있다고 마킹하는 것
            break
    
    # 중복 값이 없을 경우
    if not found_duplicated_value:
        com_list.append(rand_value)
        count += 1

# for count in range(3):  # 중복되지 않은 정수 3개를 뽑기
                        # 위해 for문 사용                      
    # while True:  # 
    #     # 1. 랜덤값 생성
    #     rand_value = random.randint(1, 10)
    #     # 2. 생성된 난수값이 리스트 내에 존재 여부 확인
    #     # 3-1 중복값 있음 : 1번 과정으로 돌아감
    #     # 3-2 중복값 없음 : 리스트에 값 추가
    #     if rand_value not in com_list:
    #         com_list.append(rand_value)
    #         break
    
print(com_list)