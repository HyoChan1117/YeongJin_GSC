# 구구단
# 2단 ~ 9단

for i in range(2, 10): # 5단과 7단은 제외
    if i != 5 and i != 7:
        for count in range(1, 10):
            mul = i * count
            print(f"{i} X {count} = {mul}")
        print("----------")