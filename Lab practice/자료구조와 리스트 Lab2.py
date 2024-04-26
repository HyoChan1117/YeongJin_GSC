# 사용자로부터 정수의 개수 N을 입력 받는다.
# 입력 받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성한다.
# 생성된 랜덤 숫자들은 리스트에 저장된다.
# 사용자에게 리스트에서 원하는 원소의 인덱스를 입력 받는다.
# 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력한다.


# 유효값: 1 <= trial_num <= 100
# 유효범위 이외 값인 경우 에러메시지 출력 후 재입력

# 무한루프
while True:   # 유효값 
    # N 값 입력
    trail_num = int(input("N값을 입력하세요 (1-100): "))
    
    # 입력 받은 N 값이 유효범위
    if 1 <= trail_num <= 100:
        # 무한루프 탈출
        break   # 현재 반복을 부시는 것
    # 에러 메시지 출력
    print("에러: 1 이상 100 이하의 정수여야 합니다.")
import random

# 중복 값이 없는 정수를 저장할 List
made_list = []

# trail_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장
for trial_count in range(0, trail_num):

    # 중복 값 검사를 위해서
    while True:
        random_num = random.randint(1, 5)
    
        found_duplication = False
        
        for made_index in range(0, trial_count):
            # 중복값이 있으면
            if made_list[made_index] == random_num:
                found_duplication = True
                break

        if not found_duplication:
            made_list.append(random_num) 
            break

print(made_list)
    
while True:
    input_index = int(input("index : "))
    
    if 0 <= input_index < len(made_list):
        print("원소 값 : ", made_list[input_index])
        break
    
    print("out of index")
    