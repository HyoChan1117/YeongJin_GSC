# 구구단
# 2단 ~ 9단

for i in range(2, 10): # 5단과 7단은 제외
    
    if i == 5 or i == 7:
        continue
    
    for count in range(1, 10):
        mul = i * count
        print(f"{i} X {count} = {mul}")
    print("----------")
    
# continue는 break와 유사
# continue를 만나면 이번 회차에서는 실행X, 하지만 반복을
# 계속해서 함
# break를 만나면 반복문이 끝남