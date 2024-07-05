
# break
# continue
# pass (Python)

for k in range(1, 5):
    for i in range(1, 3):
        for j in range(1, 4):
            # if i == 2:
            #     break
            print(i, ":", j)
        
# 중첩 반복문을 해석할 때는 하위 반복문에서 상위 반복문으로
# 해석하기

# break 동작 절차:
# 1) 위로 올라간다.
# 2) 첫 번째 만나는 반복을 종료한다.