import random

# 리스트 생성 : bar(참조변수)
bar = list()

for _ in range(0, 5):  # 0, 1, 2, 3, 4번 반복
    
    # random.randint(1, 100) -> 1이상 100이하의 정수 중 난수(임의의 수)를 한 개 선택
    bar.append(random.randint(1, 100))
    
print(bar)

# 예) [90, 50, 30, 100, 20]

print(bar[4])   # 4번째 위치에 있는 원소를 읽어 옴    20
print(bar[-1])   # 제일 마지막 원소를 읽어 옴     20    
print(bar[len(bar) - 1]) # bar함수의 길이를 len 함수를 사용해서 4번째 위치에 있는 원소를 읽어 옴     20
