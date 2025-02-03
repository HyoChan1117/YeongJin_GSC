# 2차원은 가로부터 생각하고 그 다음 세로를 생각함

for i in range(4):  # 세로축이 4번 반복
    for j in range(3):  # 가로축이 3번 반복 -> 결과 : "***"
        print("*", end= "")
    
    if i != 3:    
        print("")